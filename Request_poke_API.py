import pandas as pd
from poke_api import PokemonExtract
import sqlite3


url = 'https://pokeapi.co/api/v2/pokemon?limit=50'

extração = PokemonExtract(api_url=url)
extração.get_data()
extração.process_data()
extração.get_pokemon_details()
extração.get_abilities()
extração.get_type_waeknesses()

df = extração.to_df()
print(df[['name', 'types', 'weaknesses']].head())


extração.save_to_sqlite()

conn = sqlite3.connect('pokemon.db')
result = pd.read_sql_query('SELECT * FROM pokemon WHERE weight > 500', conn)
print(result)


