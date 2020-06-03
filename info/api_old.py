import json
import requests
# import schedule
import time



class Country():
    def __init__(self,name):

        self.name = name
        self.status = False
        self.code = ""
        self.info = self.search()['data']
        self.endpoint = 'https://corona-api.com/countries/'
        self.coordinates = self.info['coordinates']

        self.flag = f"https://www.countryflags.io/{self.code}/flat/64.png"
        self.population = self.info['population']
        self.last_update = self.info['updated_at']
        self.total_deaths = self.info['latest_data']['deaths']
        self.total_confirmed = self.info['latest_data']['confirmed']
        self.total_recovered = self.info['latest_data']['recovered']
        self.total_critical = self.info['latest_data']['critical']
        self.today_deaths = self.info['today']['deaths']
        self.today_confirmed = self.info['today']['confirmed']
        self.today_recovered = self.info['timeline'][0]['new_recovered']
        self.deaths_percent = round(100/(self.info['timeline'][1]['deaths'] / (self.info['timeline'][0]['deaths'] - self.info['timeline'][1]['deaths'])),1)
        self.recovered_percent = round(100/(self.info['timeline'][1]['recovered'] / (self.info['timeline'][0]['recovered'] - self.info['timeline'][1]['recovered'])),1)
        self.confirmed_percent = round(100/(self.info['timeline'][1]['confirmed'] / (self.info['timeline'][0]['confirmed'] - self.info['timeline'][1]['confirmed'])),1)
        self.death_rate = self.info['latest_data']['calculated']['death_rate']
        self.recovery_rate = self.info['latest_data']['calculated']['recovery_rate']
        self.cases_per_million_population = self.info['latest_data']['calculated']['cases_per_million_population']
        self.timeline = {"dates":[] , "confirmed":[], "deaths" : [], "recovered": [], "active":[]}
        self.get_timeline()




    def fetch(self):
        if self.code != "":
            country = requests.get(f'https://corona-api.com/countries/{self.code}').json()
            return country
        else:
            print("Error")


    def search(self):
        with open('nations.json' ,encoding="utf8") as f:
            data = json.load(f)
        for code, country_name in data.items():
            if country_name.lower() == self.name.lower():
                self.code = code
                self.status = True
                return self.fetch()

        return False


    def get_timeline(self):
        for i in range(len(self.info['timeline'])):
            self.timeline["dates"].append(self.info['timeline'][i]["date"])
            self.timeline["confirmed"].append(self.info['timeline'][i]["confirmed"])
            self.timeline["deaths"].append(self.info['timeline'][i]["deaths"])
            self.timeline["recovered"].append(self.info['timeline'][i]["recovered"])
            self.timeline["active"].append(self.info['timeline'][i]["active"])



class World():

    def __init__(self):
        self.endpoint = 'https://corona-api.com/countries'
        self.info = []

        self.fetch()

    def fetch(self):
        data = requests.get(self.endpoint).json()
        self.data = data['data']
