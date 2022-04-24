# -*- coding: utf-8 -*-

import shutil
from pathlib_mate import Path
from whoosh.index import open_dir, create_in, exists_in, FileIndex
from whoosh.fields import Schema


def get_index(
    path: Path,
    schema: Schema,
    reset=True,
) -> FileIndex:
    if reset:
        try:
            shutil.rmtree(path.abspath)
        except:
            pass
    path.mkdir_if_not_exists()
    if exists_in(path.abspath):
        return open_dir(path.abspath)
    else:
        return create_in(dirname=path.abspath, schema=schema)
