from citation.csl_constants import (
    ARTICLE,
    ARTICLE_JOURNAL,
    ARTICLE_MAGAZINE,
    ARTICLE_NEWSPAPER,
    BROADCAST,
    CHAPTER,
    ENTRY_DICTIONARY,
    ENTRY_ENCYCLOPEDIA,
    GRAPHIC,
    LEGAL_CASE,
    LEGISLATION,
    MOTION_PICTURE,
    PAPER_CONFERENCE,
    PERSONAL_COMMUNICATION,
    POST,
    POST_WEBLOG,
    SONG,
    SPEECH,
)

ARTWORK = "ARTWORK"
AUDIO_RECORDING = "AUDIO_RECORDING"
BILL = "BILL"
BLOG_POST = "BLOG_POST"
BOOK = "BOOK"
BOOK_SECTION = "BOOK_SECTION"
CASE = "CASE"
CONFERENCE_PAPER = "CONFERENCE_PAPER"
DICTIONARY_ENTRY = "DICTIONARY_ENTRY"
DOCUMENT = "DOCUMENT"
EMAIL = "EMAIL"
ENCYCLOPEDIA_ARTICLE = "ENCYCLOPEDIA_ARTICLE"
FILM = "FILM"
FORUM_POST = "FORUM_POST"
HEARING = "HEARING"
INSTANT_MESSAGE = "INSTANT_MESSAGE"
INTERVIEW = "INTERVIEW"
JOURNAL_ARTICLE = "JOURNAL_ARTICLE"
LETTER = "LETTER"
MAGAZINE_ARTICLE = "MAGAZINE_ARTICLE"
MANUSCRIPT = "MANUSCRIPT"
MAP = "MAP"
NEWSPAPER_ARTICLE = "NEWSPAPER_ARTICLE"
PATENT = "PATENT"
PODCAST = "PODCAST"
PREPRINT = "PREPRINT"
PRESENTATION = "PRESENTATION"
RADIO_BROADCAST = "RADIO_BROADCAST"
REPORT = "REPORT"
SOFTWARE = "SOFTWARE"
STATUTE = "STATUTE"
THESIS = "THESIS"
TV_BROADCAST = "TV_BROADCAST"
VIDEO_RECORDING = "VIDEO_RECORDING"
WEBPAGE = "WEBPAGE"

ZOTERO_TO_CSL_MAPPING = {
    ARTWORK: GRAPHIC,
    AUDIO_RECORDING: SONG,
    BILL: BILL,
    BLOG_POST: POST_WEBLOG,
    BOOK: BOOK,
    BOOK_SECTION: CHAPTER,
    CASE: LEGAL_CASE,
    CONFERENCE_PAPER: PAPER_CONFERENCE,
    DICTIONARY_ENTRY: ENTRY_DICTIONARY,
    DOCUMENT: DOCUMENT,
    EMAIL: PERSONAL_COMMUNICATION,
    ENCYCLOPEDIA_ARTICLE: ENTRY_ENCYCLOPEDIA,
    FILM: MOTION_PICTURE,
    FORUM_POST: POST,
    HEARING: HEARING,
    INSTANT_MESSAGE: PERSONAL_COMMUNICATION,
    INTERVIEW: INTERVIEW,
    JOURNAL_ARTICLE: ARTICLE_JOURNAL,
    LETTER: PERSONAL_COMMUNICATION,
    MAGAZINE_ARTICLE: ARTICLE_MAGAZINE,
    MANUSCRIPT: MANUSCRIPT,
    MAP: MAP,
    NEWSPAPER_ARTICLE: ARTICLE_NEWSPAPER,
    PATENT: PATENT,
    PODCAST: BROADCAST,
    PREPRINT: ARTICLE,
    PRESENTATION: SPEECH,
    RADIO_BROADCAST: BROADCAST,
    REPORT: REPORT,
    SOFTWARE: SOFTWARE,
    STATUTE: LEGISLATION,
    THESIS: THESIS,
    TV_BROADCAST: BROADCAST,
    VIDEO_RECORDING: MOTION_PICTURE,
    WEBPAGE: WEBPAGE,
}

CSL_TO_ZOTERO_MAPPING = {value: key for key, value in ZOTERO_TO_CSL_MAPPING.items()}

CITATION_TYPE_CHOICES = (
    (ARTWORK, ARTWORK),
    (AUDIO_RECORDING, AUDIO_RECORDING),
    (BILL, BILL),
    (BLOG_POST, BLOG_POST),
    (BOOK, BOOK),
    (BOOK_SECTION, BOOK_SECTION),
    (CASE, CASE),
    (CONFERENCE_PAPER, CONFERENCE_PAPER),
    (DICTIONARY_ENTRY, DICTIONARY_ENTRY),
    (DOCUMENT, DOCUMENT),
    (EMAIL, EMAIL),
    (ENCYCLOPEDIA_ARTICLE, ENCYCLOPEDIA_ARTICLE),
    (FILM, FILM),
    (FORUM_POST, FORUM_POST),
    (HEARING, HEARING),
    (INSTANT_MESSAGE, INSTANT_MESSAGE),
    (INTERVIEW, INTERVIEW),
    (JOURNAL_ARTICLE, JOURNAL_ARTICLE),
    (LETTER, LETTER),
    (MAGAZINE_ARTICLE, MAGAZINE_ARTICLE),
    (MANUSCRIPT, MANUSCRIPT),
    (MAP, MAP),
    (NEWSPAPER_ARTICLE, NEWSPAPER_ARTICLE),
    (PATENT, PATENT),
    (PODCAST, PODCAST),
    (PREPRINT, PREPRINT),
    (PRESENTATION, PRESENTATION),
    (RADIO_BROADCAST, RADIO_BROADCAST),
    (REPORT, REPORT),
    (SOFTWARE, SOFTWARE),
    (STATUTE, STATUTE),
    (THESIS, THESIS),
    (TV_BROADCAST, TV_BROADCAST),
    (VIDEO_RECORDING, VIDEO_RECORDING),
    (WEBPAGE, WEBPAGE),
)


CREATOR_TYPES = {
    # "annotation": [],
    ARTWORK: ["artist", "contributor"],
    # ATTACHMENT: [],
    AUDIO_RECORDING: ["performer", "contributor", "composer", "words_by"],
    BILL: ["sponsor", "cosponsor", "contributor"],
    BLOG_POST: ["author", "commenter", "contributor"],
    BOOK: ["author", "contributor", "editor", "translator", "series_editor"],
    BOOK_SECTION: [
        "author",
        "contributor",
        "editor",
        "book_author",
        "translator",
        "series_editor",
    ],
    CASE: ["author", "counsel", "contributor"],
    SOFTWARE: ["programmer", "contributor"],
    CONFERENCE_PAPER: [
        "author",
        "contributor",
        "editor",
        "translator",
        "series_editor",
    ],
    DICTIONARY_ENTRY: [
        "author",
        "contributor",
        "editor",
        "translator",
        "series_editor",
    ],
    DOCUMENT: ["author", "contributor", "editor", "translator", "reviewed_author"],
    EMAIL: ["author", "contributor", "recipient"],
    ENCYCLOPEDIA_ARTICLE: [
        "author",
        "contributor",
        "editor",
        "translator",
        "series_editor",
    ],
    FILM: ["director", "contributor", "scriptwriter", "producer"],
    FORUM_POST: ["author", "contributor"],
    HEARING: ["contributor"],
    INSTANT_MESSAGE: ["author", "contributor", "recipient"],
    INTERVIEW: ["interviewee", "contributor", "interviewer", "translator"],
    JOURNAL_ARTICLE: [
        "author",
        "contributor",
        "editor",
        "translator",
        "reviewed_author",
    ],
    LETTER: ["author", "contributor", "recipient"],
    MAGAZINE_ARTICLE: ["author", "contributor", "translator", "reviewed_author"],
    MANUSCRIPT: ["author", "contributor", "translator"],
    MAP: ["cartographer", "contributor", "series_editor"],
    NEWSPAPER_ARTICLE: ["author", "contributor", "translator", "reviewed_author"],
    # NOTE: [],
    PATENT: ["inventor", "attorney_agent", "contributor"],
    PODCAST: ["podcaster", "contributor", "guest"],
    PREPRINT: ["author", "contributor", "editor", "translator", "reviewed_author"],
    PRESENTATION: ["presenter", "contributor"],
    RADIO_BROADCAST: [
        "director",
        "scriptwriter",
        "producer",
        "cast_member",
        "contributor",
        "guest",
    ],
    REPORT: ["author", "contributor", "translator", "series_editor"],
    STATUTE: ["author", "contributor"],
    THESIS: ["author", "contributor"],
    TV_BROADCAST: [
        "director",
        "scriptwriter",
        "producer",
        "cast_member",
        "contributor",
        "guest",
    ],
    VIDEO_RECORDING: [
        "director",
        "scriptwriter",
        "producer",
        "cast_member",
        "contributor",
    ],
    WEBPAGE: ["author", "contributor", "translator"],
}


CITATION_TYPE_FIELDS = {
    JOURNAL_ARTICLE: [
        "title",
        "abstract",
        "container-title",
        "volume",
        "issue",
        "page",
        "collection-title",
        "collection-title",
        "journalAbbreviation",
        "language",
        "DOI",
        "ISSN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    ARTWORK: [
        "title",
        "abstract",
        "medium",
        "dimensions",
        "language",
        "title-short",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "URL",
        "license",
    ],
    AUDIO_RECORDING: [
        "title",
        "abstract",
        "medium",
        "collection-title",
        "volume",
        "number-of-volumes",
        "publisher-place",
        "publisher",
        "dimensions",
        "language",
        "ISBN",
        "title-short",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "URL",
        "license",
    ],
    BILL: [
        "title",
        "abstract",
        "number",
        "container-title",
        "volume",
        "section",
        "page",
        "authority",
        "chapter-number",
        "references",
        "language",
        "URL",
        "title-short",
        "license",
    ],
    BLOG_POST: [
        "title",
        "abstract",
        "container-title",
        "genre",
        "URL",
        "language",
        "title-short",
        "license",
    ],
    BOOK: [
        "title",
        "abstract",
        "collection-title",
        "collection-number",
        "volume",
        "number-of-volumes",
        "edition",
        "publisher-place",
        "publisher",
        "number-of-pages",
        "language",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    BOOK_SECTION: [
        "title",
        "abstract",
        "container-title",
        "collection-title",
        "collection-number",
        "volume",
        "number-of-volumes",
        "edition",
        "publisher-place",
        "publisher",
        "page",
        "language",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    CASE: [
        "title",
        "abstract",
        "authority",
        "number",
        "container-title",
        "volume",
        "page",
        "references",
        "language",
        "title-short",
        "URL",
        "license",
    ],
    SOFTWARE: [
        "title",
        "abstract",
        "collection-title",
        "version",
        "medium",
        "publisher-place",
        "publisher",
        "genre",
        "ISBN",
        "title-short",
        "URL",
        "license",
        "archive",
        "archive_location",
        "source",
        "call-number",
    ],
    CONFERENCE_PAPER: [
        "title",
        "abstract",
        "container-title",
        "event-title",
        "publisher-place",
        "publisher",
        "volume",
        "page",
        "collection-title",
        "language",
        "DOI",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    DICTIONARY_ENTRY: [
        "title",
        "abstract",
        "container-title",
        "collection-title",
        "collection-number",
        "volume",
        "number-of-volumes",
        "edition",
        "publisher-place",
        "publisher",
        "page",
        "language",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    DOCUMENT: [
        "title",
        "abstract",
        "publisher",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    EMAIL: ["title", "abstract", "title-short", "URL", "language", "license"],
    ENCYCLOPEDIA_ARTICLE: [
        "title",
        "abstract",
        "container-title",
        "collection-title",
        "collection-number",
        "volume",
        "number-of-volumes",
        "edition",
        "publisher-place",
        "publisher",
        "page",
        "ISBN",
        "title-short",
        "URL",
        "language",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    FILM: [
        "title",
        "abstract",
        "publisher",
        "genre",
        "medium",
        "dimensions",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    FORUM_POST: [
        "title",
        "abstract",
        "container-title",
        "genre",
        "language",
        "title-short",
        "URL",
        "license",
    ],
    HEARING: [
        "title",
        "abstract",
        "section",
        "publisher-place",
        "publisher",
        "number-of-volumes",
        "number",
        "page",
        "authority",
        "chapter-number",
        "references",
        "language",
        "title-short",
        "URL",
        "license",
    ],
    INSTANT_MESSAGE: [
        "title",
        "abstract",
        "language",
        "title-short",
        "URL",
        "license",
    ],
    INTERVIEW: [
        "title",
        "abstract",
        "medium",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    LETTER: [
        "title",
        "abstract",
        "genre",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    MAGAZINE_ARTICLE: [
        "title",
        "abstract",
        "container-title",
        "volume",
        "issue",
        "page",
        "language",
        "ISSN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    MANUSCRIPT: [
        "title",
        "abstract",
        "genre",
        "publisher-place",
        "number-of-pages",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    MAP: [
        "title",
        "abstract",
        "genre",
        "scale",
        "collection-title",
        "edition",
        "publisher-place",
        "publisher",
        "language",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    NEWSPAPER_ARTICLE: [
        "title",
        "abstract",
        "container-title",
        "publisher-place",
        "edition",
        "section",
        "page",
        "language",
        "title-short",
        "ISSN",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    PATENT: [
        "title",
        "abstract",
        "publisher-place",
        "authority",
        "number",
        "page",
        "call-number",
        "issue",
        "references",
        "status",
        "language",
        "title-short",
        "URL",
        "license",
    ],
    PODCAST: [
        "title",
        "abstract",
        "collection-title",
        "number",
        "medium",
        "dimensions",
        "URL",
        "language",
        "title-short",
        "license",
    ],
    PREPRINT: [
        "title",
        "abstract",
        "genre",
        "publisher",
        "number",
        "publisher-place",
        "collection-title",
        "collection-number",
        "DOI",
        "URL",
        "archive",
        "archive_location",
        "title-short",
        "language",
        "source",
        "call-number",
        "license",
    ],
    PRESENTATION: [
        "title",
        "abstract",
        "genre",
        "publisher-place",
        "event-title",
        "URL",
        "language",
        "title-short",
        "license",
    ],
    RADIO_BROADCAST: [
        "title",
        "abstract",
        "container-title",
        "number",
        "medium",
        "publisher-place",
        "publisher",
        "dimensions",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    REPORT: [
        "title",
        "abstract",
        "number",
        "genre",
        "collection-title",
        "publisher-place",
        "publisher",
        "page",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    STATUTE: [
        "title",
        "abstract",
        "container-title",
        "volume",
        "number",
        "page",
        "section",
        "chapter-number",
        "references",
        "language",
        "title-short",
        "URL",
        "license",
    ],
    THESIS: [
        "title",
        "abstract",
        "genre",
        "publisher",
        "publisher-place",
        "number-of-pages",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    TV_BROADCAST: [
        "title",
        "abstract",
        "container-title",
        "number",
        "medium",
        "publisher-place",
        "publisher",
        "dimensions",
        "language",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    VIDEO_RECORDING: [
        "title",
        "abstract",
        "medium",
        "collection-title",
        "volume",
        "number-of-volumes",
        "publisher-place",
        "publisher",
        "dimensions",
        "language",
        "ISBN",
        "title-short",
        "URL",
        "archive",
        "archive_location",
        "source",
        "call-number",
        "license",
    ],
    WEBPAGE: [
        "title",
        "abstract",
        "container-title",
        "genre",
        "title-short",
        "URL",
        "language",
        "license",
    ],
}
