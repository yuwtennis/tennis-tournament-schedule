
import sys
from importlib import import_module
from pkgs.utils.args import *
from pkgs.config import *

def main(club):

    #try:
    if club not in MODULES:
        raise(ModuleNotFoundError())

    # Load base class
    c = getattr(import_module(MODULES[club]['module']), MODULES[club]['class'])

    t = c()

    t.display()

    #except:
    #    print('Something is wrong error: {}'.format(sys.exc_info()[0]))

if __name__ == "__main__":

    args = parse_args()
    main(args.tennis_club)
