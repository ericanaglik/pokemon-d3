import json

with open('pokemon.json') as mon_file, open('pokedex.json') as dex_file, \
    open('output.json', 'w') as outfile:
    mon_list = json.loads(mon_file.read())
    dex_list = json.loads(dex_file.read())

    out_list = []
    for pokemon, pokedex in zip(mon_list, dex_list):
        pokedex['base']['Weight'] = pokemon['weight']
        pokedex['base']['Height'] = pokemon['height']
        out_list.append(pokedex)
    
    json.dump(out_list, outfile)