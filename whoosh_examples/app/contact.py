# -*- coding: utf-8 -*-

"""
MacOS Contact app full text search
"""

from whoosh.fields import (
    SchemaClass,
    ID, TEXT, KEYWORD, NUMERIC, STORED, NGRAM, DATETIME, BOOLEAN,
)
from whoosh_examples.paths import dir_whoosh_index
from whoosh_examples.helpers import get_index

class Contact(SchemaClass):
    id = ID()
    firstname = NGRAM(minsize=2, maxsize=10, stored=True)
    lastname = NGRAM(minsize=2, maxsize=10, stored=True)
    firstname_phonetic = NGRAM(minsize=2, maxsize=10, stored=True)
    lastname_phonetic = NGRAM(minsize=2, maxsize=10, stored=True)
    birth_date = DATETIME(stored=True)

