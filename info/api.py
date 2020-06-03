import json
import requests
#import schedule
#import time
from dateutil import parser
import datetime
import pytz
import itertools



class World():
    def __init__(self):
        self.data = fetch()
        self.timeline = timeline(self.data)
        self.all_countries = self.data['all_countries']
        if 'is_in_progress' in self.timeline[0] and self.timeline[0]['new_deaths'] == 0:
            self.today =dict(itertools.islice(self.timeline[1].items(), 5,8))
        else:
            self.today = dict(itertools.islice(self.timeline[1].items(), 6,9))
        self.increment =increment(self.timeline)





class Country():
    def __init__(self,name=None,alpha=None):


        if alpha != None:
            self.data = fetch_with_alpha(alpha)
            self.code = alpha.upper()
            self.name = name_tr(self.code)

        if alpha == None and name != "":
            self.name = name
            self.code = alpha_2(self.name)
            self.data = fetch(self.name)


        self.coordinates = self.data['coordinates']
        self.flag = f"https://www.countryflags.io/{self.code}/flat/64.png"
        self.population = self.data['population']
        self.last_update = date_convert(self.data['updated_at'])
        self.total = total(self.data)
        self.today = today(self.data)
#        if 'is_in_progress' in self.timeline and
#        self.deaths_percent = round(100/(self.info['timeline'][1]['deaths'] / (self.info['timeline'][0]['deaths'] - self.info['timeline'][1]['deaths'])),1)
#        self.recovered_percent = round(100/(self.info['timeline'][1]['recovered'] / (self.info['timeline'][0]['recovered'] - self.info['timeline'][1]['recovered'])),1)
#        self.confirmed_percent = round(100/(self.info['timeline'][1]['confirmed'] / (self.info['timeline'][0]['confirmed'] - self.info['timeline'][1]['confirmed'])),1)
        self.rates = rates(self.data)
        self.timeline = timeline(self.data)
        if 'is_in_progress' in self.timeline[0] and self.timeline[0]['new_deaths'] == 0:
            self.today.update({'recovered' : self.timeline[1]['new_recovered']})
            self.today.update({'confirmed' : self.timeline[1]['new_confirmed']})
            self.today.update({'deaths' : self.timeline[1]['new_deaths']})
        else:
            self.today.update({'recovered' : self.timeline[0]['new_recovered']})
            self.today.update({'confirmed' : self.timeline[0]['new_confirmed']})
            self.today.update({'deaths' : self.timeline[0]['new_deaths']})

        self.increment =increment(self.timeline)




def increment(timeline):
    increment = {'confirmed':0,'deaths':0,'recovered':0}

    try:
        if 'is_in_progress' in timeline[0] and timeline[0]['new_deaths'] == 0:
            increment.update({'confirmed':round(100/(timeline[2]['confirmed'] / (timeline[1]['confirmed'] - timeline[2]['confirmed'])),1),
                                'deaths':round(100/(timeline[2]['deaths'] / (timeline[1]['deaths'] - timeline[2]['deaths'])),1),
                                'recovered':round(100/(timeline[2]['recovered'] / (timeline[1]['recovered'] - timeline[2]['recovered'])),1)
                                })
        else:
            increment.update({'confirmed':round(100/(timeline[1]['confirmed'] / (timeline[0]['confirmed'] - timeline[1]['confirmed'])),1),
                                'deaths':round(100/(timeline[1]['deaths'] / (timeline[0]['deaths'] - timeline[1]['deaths'])),1),
                                'recovered':round(100/(timeline[1]['recovered'] / (timeline[0]['recovered'] - timeline[1]['recovered'])),1)
                                })
        return increment
    except:
        return False





#Generate alpha-2 code
def alpha_2(country_name):
        '''
        NOTE: Capitalize the first letter of countries beginning with "D" (for example: Spain, Iran).
        You can also type other countries in lowercase.
        the api we are requesting keeps the country data according to alpha-2 code (e.g. Turkey = TR).
        The country's Turkish names and alpha-2 codes are kept in the dictionary type in the country's .json file
        The alpha-2 code value for the country you wrote in this function returns.

        '''
        with open('nations.json' ,encoding="utf8") as f:
            data = json.load(f)
        for alpha_code,name in data.items():
            if name.lower() == country_name.lower():
                code = alpha_code
                return code
        if country_name[0] == "i" or country_name[0] == "I" :
            raise NameError(f'{country_name} type the first letter of your country as => {"İ"+country_name[1:]}')
        else:
            raise NameError(f'{country_name} no alpha-2 code found corresponding to')







#Date format
def date_convert(date):
    return parser.isoparse(date).astimezone(pytz.timezone("Europe/Paris"))


#Fetch Data
def fetch(*args):
    if len(args) == 0:
        response = {}
        timeline = requests.get(f'https://corona-api.com/timeline').json()
        response['timeline'] = timeline['data']
        all_countries = requests.get(f'https://corona-api.com/countries').json()
        all_countries = all_countries['data']
        confirmed_countries=[]
        for i in all_countries:
            if i['latest_data']['confirmed'] !=0:
                confirmed_countries.append(i)
        confirmed_countries = sorted(confirmed_countries,key=lambda i:i['latest_data']['confirmed'],reverse=True)

        response['all_countries'] = confirmed_countries
        return response

    else:
        country_list = []
        for arg in args:
            code = alpha_2(arg)
            response = requests.get(f'https://corona-api.com/countries/{code}').json()
            response = response['data']
            country_list.append(response)
        if len(country_list) <= 1:
            return country_list[0]
        else:
            return country_list

    raise NameError(f'{code} no data found for country with code')




# fetch with alpha2 code
def fetch_with_alpha(alpha_code):
    data = requests.get(f'https://corona-api.com/countries/{alpha_code}').json()
    data = data['data']
    return data



def name_tr(alpha_code):
    try:
        with open('nations.json' ,encoding="utf8") as f:
            data = json.load(f)
        for code,country_name in data.items():
            if code.upper() == alpha_code.upper():
                name = country_name
                return name
    except:
        print("Error")




# Fetch total data
def total(country_data):
    return dict(itertools.islice(country_data['latest_data'].items(), 4)) #slicing



#Fetch todays(latest) data
def today(country_data):
    return country_data['today']





#Fetch rates
def rates(country_data):

    return country_data['latest_data']['calculated']



# Convert string to datetime object, then format to Africa/Casablanca

#locale.setlocale(locale.LC_ALL, "Turkish")
# data.strftime("%a, %d %b %Y %H:%M:%S")  --> for localization (9 Nisan 2020)

def tr_date(date):
#    datetime.strptime(date, '%d/%B/%Y %H:%M:%S')
    pass




# Cleaned timeline(date convert,sort etc.)
def timeline(country_data):

    timeline = country_data['timeline']
    #convert date
    try:
        for day in timeline:
            day['date']= date_convert(day['date'])
            day['updated_at'] = date_convert(day['updated_at'])
    except Exception as e:
        raise e

    return timeline






#dictionary sorting
#import operator


#liste = []
#dic = {}
#for i in data:
#    if i['latest_data']['calculated']['recovery_rate'] is not None:
#
#        dic['name'] = i['name']
#        dic['rate'] = i['latest_data']['calculated']['recovery_rate']
#        liste.append(dic.copy())
##
#



#todo list
#world ve country için özet bilgi döndüren method yazılacak..
