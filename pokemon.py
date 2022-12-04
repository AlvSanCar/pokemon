import re
from textwrap import indent
from unicodedata import name
import requests
import json

url_api = "https://pokeapi.co/api/v2/pokemon?limit=3"
url_pokemon = "https://pokeapi.co/api/v2/pokemon/"
pokemons = []
pokemon = {}
def get_stats_pokemon (pokemon_stats):
    for stat in pokemon_stats:
        pokemon[stat['stat']['name']] = stat['base_stat']
    
def get_info_pokemon(name_pokemon):
    res_info_pokemon = requests.get(url_pokemon+name_pokemon)
    data_pokemon = res_info_pokemon.json()
    stats = data_pokemon['stats']
    pokemon['id'] = str(data_pokemon['id'])
    pokemon['name'] = data_pokemon['name']
    get_stats_pokemon(stats)
    if(res_info_pokemon.status_code != 200):
        print("Error: Not Pokemon Info")
        exit()
    return pokemon
   
    


def get_all_pokemon(url_api):
    
    res_all_pokemon = requests.get(url_api)
    if(res_all_pokemon.status_code != 200):
        print("Error: Not API Server")
        exit()
    data_all_pokemon = res_all_pokemon.json()['results']
    for data_pokemon in data_all_pokemon:
        pepe = json.dumps(get_info_pokemon(data_pokemon['name']))
        pokemons.append(pepe)
     

    



if __name__ == '__main__':
    get_all_pokemon(url_api)
    print(pokemons)


'''


def get_all_pokemon_data(pokemon=''):

    url_pokemon = url_api + pokemon

    response = requests.get(url_pokemon)

    if (response.status_code  != 200):  
        print ("Error")
        exit()
    name = response.json()['name']
    id = response.json()['id']
    stats = response.json()['stats']
    moves = response.json()['moves']
    with open('pokemon_moves.json','w') as file:
        json.dump(moves,file,indent=4)
    file.close()
    with open('pokemon_stats.json','w') as file:
        json.dump(stats,file,indent=4)
    file.close()
    print("..............")



if __name__ =='__main__':
    pokemon = input ("Introduce un pokemon")
    get_all_pokemon_data(pokemon)

    '''