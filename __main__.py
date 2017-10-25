import sys
from src.tools import Tools


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
        # How the fuck do I call the function in the names class?


    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.


if __name__ == "__main__":
    #bin.names.ShowNames("Efraya\r\nGen Eve")
    mail = '''https://zkillboard.com/kill/65514053/
https://zkillboard.com/kill/65516727/
https://zkillboard.com/kill/65519032/
https://zkillboard.com/kill/65514648/
https://zkillboard.com/kill/65519651/
https://zkillboard.com/kill/65520490/
https://zkillboard.com/kill/65520480/
https://zkillboard.com/kill/65520723/
https://zkillboard.com/kill/65520543/
https://zkillboard.com/kill/65519788/
https://zkillboard.com/kill/65520208/
https://zkillboard.com/kill/65519332/
https://zkillboard.com/kill/65520380/
https://zkillboard.com/kill/65519948/
https://zkillboard.com/kill/65520597/
https://zkillboard.com/kill/65520548/
https://zkillboard.com/kill/65520693/
https://zkillboard.com/kill/65520693/
https://zkillboard.com/kill/65519271/
https://zkillboard.com/kill/65519474/
https://zkillboard.com/kill/65521141/
https://zkillboard.com/kill/65519115/
https://zkillboard.com/kill/65519114/
https://zkillboard.com/kill/65519113/
https://zkillboard.com/kill/65516621/
https://zkillboard.com/kill/65517782/
https://zkillboard.com/kill/65519001/
https://zkillboard.com/kill/65518205/
https://zkillboard.com/kill/65517380/
'''
    tool = Tools();
    tool.GetNamesFromZkillLinks(mail)
