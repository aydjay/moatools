import sys
import bin.names

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
        # How the fuck do I call the function in the names class?


    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.


if __name__ == "__main__":
    bin.names.ShowNames("Efraya\r\nGen Eve")
