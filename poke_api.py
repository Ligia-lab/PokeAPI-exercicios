import requests
import pandas as pd
import sqlite3


class PokemonExtract:
    
    def __init__(self, api_url):
        self.api_url = api_url
        
        # dados basicos
        self.names = []
        self.urls = []
        self.ids = []
        self.results = []
        
        #dados detalhados
        self.heights = []
        self.weights = []
        self.types_list = []
        self.abilities_list = []
        
            
    def get_data(self):
        print(f'Fazendo requisição para: {self.api_url}')
        response = requests.get(self.api_url)
        if response.status_code == 200:
            self.results = response.json().get('results', [])
            print(f'Dados recebidos. Total de {len(self.results)} Pokémon identificados.')
        else:
            raise Exception(f'Falha ao acessar dados: {response.status_code}')
        

    def process_data(self):
        for pokemon in self.results:
            name = pokemon['name']
            url = pokemon['url']
            id = int(url.strip('/').split('/')[-1])
            
            self.names.append(name)
            self.urls.append(url)
            self.ids.append(id)


    def get_pokemon_details(self):
        for url in self.urls:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                
                self.heights.append(data['height'])
                self.weights.append(data['weight'])
                
                types = []
                for t in data['types']:
                    type_name = t['type']['name']
                    types.append(type_name)
                    
                self.types_list.append(types)
                
            else:
                print(f'Erro ao acessar {url}')
                self.heights.append(None)
                self.weights.append(None)
                self.types_list.append([])  
                  
                 
    def get_abilities(self):
        for url in self.urls:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                
                abilities = []
                for a in data['abilities']:
                    ability_name = a['ability']['name']
                    abilities.append(ability_name)
                    
                self.abilities_list.append(abilities)
            else:
                self.abilities_list.append([])
                          

    def get_type_waeknesses(self):
        print('Coletando fraquezas por tipo...')
        
        response = requests.get('https://pokeapi.co/api/v2/type/')  
        if response.status_code != 200:
            raise Exception('Erro ao buscar tipos')
        
        all_types = response.json().get('results', [])
        type_weaknesses = {}
        
        for tipo in all_types:
            type_name = tipo['name']
            type_url = tipo['url']
            
            r = requests.get(type_url)
            if r.status_code != 200:
                continue
            
            data = r.json()
            weaknesses = []
            
            for item in data['damage_relations']['double_damage_from']:
                weaknesses.append(item['name'])
                
        df = self.to_df()
        
        types_converted = []
        for t in df['types']:
            if isinstance(t, str):
                types_converted.append(t.split(', '))
            else:
                types_converted.append(t)
                
        df['types'] = types_converted
        
        weaknesses_list = []
        for types in df['types']:
            if isinstance(types, list) and len(types) > 0:
                primary_type = types[0]
                weaknesses = type_weaknesses.get(primary_type, [])
                weaknesses_list.append(', '.join(weaknesses))
            else:
                weaknesses_list.append('')
                
        df['weaknesses'] = weaknesses_list
        self._final_df = df
        
        print('coluna de fraqueza adicionada')


    def to_df(self):
        if hasattr(self, '_final_df'):
            return self._final_df
        
        df = pd.DataFrame({
            'id': self.ids,
            'name': self.names,
            'url': self.urls,
            'height': self.heights,
            'weight': self.weights,
            'types': self.types_list,
            'abilities': self.abilities_list
        })
        
        return df
    
    
    def save_to_sqlite(self, db_path='pokemon.db', table_name='pokemon'):
        print('fazendo a leitura dos dados')
        conn = sqlite3.connect(db_path)
        
        df = self.to_df()
        
        type_str = []
        abilities_str = []
        
        for t in df['types']:
            if isinstance(t, list):
                type_str.append(', '.join(t))
            else:
                type_str.append('')
                
        for a in df['abilities']:
            if isinstance(a, list):
                abilities_str.append(', '.join(a))
            else:
                abilities_str.append('')
                
        df['types'] = type_str
        df['abilities'] = abilities_str
       
        
        # df['types'] = df['types'].apply(lambda x: ', '.join(x) if isinstance(x, list) else '')
        # df['abilities'] = df['abilities'].apply(lambda x: ', '.join(x) if isinstance(x, list) else '')
        
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        print('Dados salvos na tabela')


    