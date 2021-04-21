from ebird.api import get_taxonomy
from tokens import get_creds


def get_bird_names():
    creds = get_creds()
    taxonomy = get_taxonomy(str(creds))
    prev_name = ''
    bird_list = []

    for bird in taxonomy:
        try:
            name = bird['familyComName']
            try:
                name = name.split(' ')[-1]
            except:
                pass
            try:
                name = name.split('-')[-1]
            except:
                pass
            try:
                name = name.split(',')[-1]
            except:
                pass
            if name[-1] == 's':
                name = name[:-1]
            if prev_name != name:
                prev_name = name
                bird_list.append(name)
        except:
            pass
    return bird_list
