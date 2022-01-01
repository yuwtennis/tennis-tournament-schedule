
import sys
from importlib import import_module
from tournaments.utils.args import *
from tournaments.config import *

def main(club):

    if club not in MODULES:
        raise(ModuleNotFoundError())

    # Load base class
    c = getattr(import_module(MODULES[club]['module']), MODULES[club]['class'])

    # Instantiate
    t = c()

    res = t.run()

    # Display
    t.display(res)

    # Notify
    t.notify_to_console(res)

if __name__ == "__main__":

    args = parse_args()
    main(args.tennis_club)
