# -*- coding: utf-8 -*-

"""
MacOS Contact app full text search
"""

from rich import print as rprint
from datetime import datetime

from pathlib_mate import Path
from whoosh.fields import (
    SchemaClass,
    ID, TEXT, KEYWORD, NUMERIC, STORED, NGRAM, DATETIME, BOOLEAN,
)
from whoosh.query import And, Or, Term, NumericRange, DateRange
from whoosh.searching import Hit

from whoosh_examples.paths import dir_whoosh_index
from whoosh_examples.helpers import get_index


class Contact(SchemaClass):
    id = ID()
    firstname = KEYWORD(lowercase=True, stored=True)
    lastname = KEYWORD(lowercase=True, stored=True)
    firstname_phonetic = KEYWORD(lowercase=True, stored=True)
    lastname_phonetic = KEYWORD(lowercase=True, stored=True)
    fullname_ngram = NGRAM(minsize=2, maxsize=10, stored=True)
    birth_day = DATETIME(stored=True)


p_index = Path(dir_whoosh_index, "contact")

documents = [
    dict(
        id="1",
        firstname="Anthony",
        lastname="Zhao",
        firstname_phonetic="jianguo, jg",
        lastname_phonetic="zhao",
        fullname_ngram="Anthony Zhao, Jianguo Zhao, JianguoZhao, ZhaoJianguo, zjg, jgz",
        birth_day=datetime(1974, 8, 13),
    )
]

def insert_documents():
    writer = index.writer()
    for document in documents:
        writer.add_document(**document)
    writer.commit()


def search_documents():
    q = And([
        Term("fullname_ngram", "jia"),
        Term("fullname_ngram", "guo"),
    ])
    with index.searcher() as s:
        results = s.search(q)
        hit: Hit
        for hit in results:
            print(hit.highlights("fullname_ngram"))
            # rprint(hit.fields())
            # rprint(hit)

index = get_index(p_index, Contact(), reset=True)
insert_documents()
search_documents()