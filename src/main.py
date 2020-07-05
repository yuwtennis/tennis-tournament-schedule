
import sys
from importlib import import_module
from config import *

def main(club):

    try:
        if club not in MODULES:
            raise(ModuleNotFoundError())

        # Load class
        c = getattr(import_module(MODULE[club]['module'],
            MODULES[club]['class'])

    except:
        print('Something is wrong error: {}'.format(sys.exc_info()[0]))

if __name__ == "__main__":

    main(args.tennis_club)
