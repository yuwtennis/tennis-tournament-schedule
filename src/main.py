
import sys
from importlib import import_module
from pkgs.utils.args import *
from pkgs.config import *

def main(club):

    if club not in MODULES:
        raise(ModuleNotFoundError())

    # Load base class
    c = getattr(import_module(MODULES[club]['module']), MODULES[club]['class'])

    # Instantiate
    t = c()

    # Notify
    t.nofity_to_console()

if __name__ == "__main__":

    args = parse_args()
    main(args.tennis_club)
