

def get_map_names():
    return ['level 1']


# pylint: disable=line-too-long
# This map will be removed and it weill be kept in the database
# it is easier to visualize if it isn't broken down
def get_map(name: str = '123'):
    if name:
        return [
        '                                                                                                               ',
        '                                             -     --                                                          -',
        '                                       --                                                                       -',
        '                                   -                       -                                                    -',
        '                              -                                                                                 -',
        '                         -      ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤  ¤¤          ¤¤¤¤              ¤¤¤¤     ---         -',
        '----------------------------------------------------------------------------------------------------------------'
        ]
    return None
