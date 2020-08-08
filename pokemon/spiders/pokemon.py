import scrapy
import json

class PokeonSpyder(scrapy.Spider):
    name = 'pokemon'

    def start_requests(self):
        # gerador de urls, pode colocar uma lista de url
        yield scrapy.Request(url= 'https://pokemondb.net/pokedex/national', callback=self.parse)

    def parse(self, response):     

        arr = []
        for card in response.css('span.infocard-lg-data'):

            # EXTAINDO DADOS DA PAG
            id = card.css('small::text').extract_first() 
            #o extract_first retorna a primeira aparição de um elemento na pag 
            name = card.css('.ent-name::text').extract_first()
            url_datais = f"{'https://pokemondb.net/pokedex/' + name.lower()}"
            types = [typex for typex in card.css('a::text').extract()] #o extract retorna uma lista 
            print(f'Dados do {name} gravados no arquivo json')

            arr.append({
                'id':id,
                'name': name,
                'types': types,
                'datais': url_datais
            })

        with open('data/pokemons.json', 'w') as f:
            #gravando os dados em um json com identação
            json.dump(arr, f, indent=4)
            
            
