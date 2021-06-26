from itertools import islice
from os import linesep
from shutil import get_terminal_size
from subprocess import check_call
from unittest import TestCase

from ....coq.clients.tags.parser import parse
from ....coq.consts import TAGS_DIR, TOP_LEVEL


class Parser(TestCase):
    def test_1(self) -> None:
        tag = TAGS_DIR / "TAG"
        TAGS_DIR.mkdir(parents=True, exist_ok=True)
        if not tag.exists():
            check_call(("etags", "--recurse", "-o", str(tag)), cwd=TOP_LEVEL)

        spec = tag.read_text()
        parsed = tuple(parse(spec, raise_err=True))

        cols, _ = get_terminal_size()
        sep = linesep + "-" * cols + linesep
        print(*islice(parsed, 10), sep=sep)

