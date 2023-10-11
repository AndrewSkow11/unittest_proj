from utils.dicts import get_val
import unittest

class TestDict(unittest.TestCase):
    def test_get_val(self):
        self.assertEqual(get_val({"vcs": "mercurial"}, 'vcs'),'mercurial')
        self.assertEqual(get_val({"vcs": "mercurial"}, 'vcs', 'git'),'mercurial')
        self.assertEqual(get_val({}, 'vcs', 'git'),'git')
        self.assertEqual(get_val({}, 'vcs', 'bazaar'), 'bazaar')




