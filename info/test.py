import json
import requests
import schedule




class Covid():

    def __init__(self,name,url):
        self.name = name
        self.url = url
        self.endpoint = f'https://corona-api.com/'



    def convert(self):
        try:
            with open('nations.json' ,encoding="utf8") as f:
                data = json.load(f)
            for code, country_name in data.items():
                if country_name.lower() == self.name.lower():
                    return code
        except Exception:
            print("api function did not work properly...")


    def fetch(self):
        try:
            response = requests.get(self.url)
            if response.status == "200":
                response = response.json()
                return response
            else:
                print('Failed to capture data..')
        except Exception:
            print('fetch function did not work properly')



class World(Covid):
    endpoint = f'https://corona-api.com/'
    timeline = "12"





class Country(Covid):
    def __init__(self,name):
        self.name = name


        #  to-do
