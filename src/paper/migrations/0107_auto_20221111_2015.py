# Generated by Django 2.2 on 2022-11-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0106_paper_oa_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='abstract_src',
            field=models.FileField(blank=True, default=None, help_text='\n            Abstract_src is different field than abstract field.\n            Abstract is legacy text field where as abstract_src field is a src field that is \n            intended to be used along with different types of text editors from the frontend.\n        ', max_length=512, null=True, upload_to='uploads/paper_abstract_src/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='paper',
            name='abstract_src_type',
            field=models.CharField(choices=[('CK_EDITOR', 'CK_EDITOR'), ('DRAFT_JS', 'DRAFT_JS'), ('TEXT_FIOELD', 'TEXT_FIOELD')], default='TEXT_FIOELD', help_text='Indicates which text editor was used for abstract section.', max_length=32, null=True),
        ),
    ]
