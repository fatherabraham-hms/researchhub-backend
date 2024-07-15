from user.views import PersonaWebhookView
from user.models import User, UserVerification
from django.test import TestCase, override_settings

import os


class PersonaWebhookViewTests(TestCase):

    webhook_secret = "wbhsec_researchhub"

    def setUp(self):
        self.webhook_approved_body = self.read_test_file(
            "persona_webhook_approved.json"
        )
        self.webhook_declined_body = self.read_test_file(
            "persona_webhook_declined.json"
        )

    def read_test_file(self, filename):
        file_path = os.path.join(os.path.dirname(__file__), "test_files", filename)
        with open(file_path, "r") as file:
            return file.read()

    @override_settings(PERSONA_WEBHOOK_SECRET=webhook_secret)
    def test_post_webhook_without_signature(self):
        response = self.client.post(
            "/webhooks/persona/",
            self.webhook_approved_body,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message": "Unauthorized"})

    @override_settings(PERSONA_WEBHOOK_SECRET=webhook_secret)
    def test_post_webhook_with_invalid_signature(self):
        body = self.webhook_approved_body
        response = self.client.post(
            "/webhooks/persona/",
            body,
            content_type="application/json",
            headers={
                "Persona-Signature": "t=1720448965,v1=aaabbb2356a65fd3a1734457430a1a2fe0c566349e0d472c45cb9281a7d3b68d"
            },
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message": "Unauthorized"})

    def test_post_webhook_with_invalid_format(self):
        body = self.webhook_approved_body
        response = self.client.post(
            "/webhooks/persona/",
            body,
            content_type="application/json",
            headers={"Persona-Signature": "INVALID_FORMAT"},
        )

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"message": "Failed to process webhook"})

    def test_create_digest(self):
        # arrange
        body = "abc123"
        t = "1720713905"

        # act
        digest = PersonaWebhookView.create_digest(self.webhook_secret, t, body)

        # assert
        self.assertEqual(
            digest, "0fd4586aa5cb67c098a920ed55906fb2669a2bb21c6ed2de58e4f5cfb79814c7"
        )

    @override_settings(PERSONA_WEBHOOK_SECRET=webhook_secret)
    def test_post_webhook(self):
        # arrange
        user = User.objects.create(first_name="firstName1", last_name="lastName1")

        # replace the reference-id placeholder in the body with the Id of the
        # created user and recomputes the digest:
        body = self.webhook_approved_body.replace(
            '"reference-id": "$REFERENCE_ID"', f'"reference-id": "{user.id}"'
        )
        digest = PersonaWebhookView.create_digest(
            self.webhook_secret, "1720448965", body
        )

        # act
        response = self.client.post(
            "/webhooks/persona/",
            body,
            content_type="application/json",
            headers={"Persona-Signature": f"t=1720448965,v1={digest}"},
        )

        user_verification = UserVerification.objects.get(user=user)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Webhook successfully processed"})
        self.assertEqual(user_verification.status, UserVerification.Status.APPROVED)
        self.assertEqual(user_verification.is_verified, True)

    @override_settings(PERSONA_WEBHOOK_SECRET=webhook_secret)
    def test_post_webhook_declined_status(self):
        # arrange
        user = User.objects.create(first_name="firstName1", last_name="lastName1")

        # replace the reference-id placeholder in the body with the Id of the
        # created user and recomputes the digest:
        body = self.webhook_declined_body.replace(
            '"reference-id": "$REFERENCE_ID"', f'"reference-id": "{user.id}"'
        )
        digest = PersonaWebhookView.create_digest(
            self.webhook_secret, "1720448965", body
        )

        # act
        response = self.client.post(
            "/webhooks/persona/",
            body,
            content_type="application/json",
            headers={"Persona-Signature": f"t=1720448965,v1={digest}"},
        )

        user_verification = UserVerification.objects.get(user=user)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Webhook successfully processed"})
        self.assertEqual(user_verification.status, UserVerification.Status.DECLINED)
        self.assertEqual(user_verification.is_verified, False)
