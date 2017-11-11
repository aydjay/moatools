import sys
from src.tools import Tools


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.


if __name__ == "__main__":
    # bin.names.ShowNames("Efraya\r\nGen Eve")

    with open("/home/d347hm4n/Downloads/11 11 CTA.txt", "r") as myfile:
        data = myfile.readlines()

        tool = Tools()
        tool.GetNamesFromZkillLinks(data)
