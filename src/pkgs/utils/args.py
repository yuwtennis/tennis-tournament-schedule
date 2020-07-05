
import argparse

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('--tennis_club', default='南市川テニスガーデン')

    return parser.parse_args()
