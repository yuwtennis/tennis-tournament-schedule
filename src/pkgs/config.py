import os

YAML_FILE = os.path.join( os.getcwd(), 'pkgs/tournaments.yaml')

TENNIS_CLUB_1 = '南市川テニスガーデン'

MODULES = {
    '南市川テニスガーデン': {
        'class': 'MinamiIchikawaTennisGarden',
        'module': 'pkgs.minami_ichikawa_tennis_garden'
     }
}
