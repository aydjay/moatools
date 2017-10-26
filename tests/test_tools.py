from src import tools
import unittest


class test_tools(unittest.TestCase):

    def test_zKillProcessing(self):

        tool = tools.Tools()
        result = tool.ShowNames("Efraya\nGen Eve")
        self.assertTrue(result)

    if __name__ == '__main__':
        unittest.main()
