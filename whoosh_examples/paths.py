# -*- coding: utf-8 -*-

from pathlib_mate import Path

dir_here = Path.dir_here(__file__)
dir_project_root = dir_here.parent
dir_whoosh_index = Path(dir_project_root, ".whoosh_index")
dir_whoosh_index.mkdir_if_not_exists()
