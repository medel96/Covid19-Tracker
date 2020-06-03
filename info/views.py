
import json
import requests
from django.shortcuts import render
import pandas as pd
import os
import folium
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import chart_studio
username='medel'
api_key='uiMAmfBFm6jx09RmTttE'
chart_studio.tools.set_credentials_file(username=username , api_key=api_key)
import chart_studio.plotly as py
import chart_studio.tools as tls
from .	import views
from django.http import HttpResponse,JsonResponse
from .api import Country,World


def information(request):
    return render(request, 'info/information.html')



def country(request):


            MA_data = pd.read_csv('https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/MA-times_series.csv')
            by_cities = pd.read_csv('https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/cities.csv')
            by_regions = pd.read_csv('https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/regions.csv')
            by_provinces = pd.read_csv(r'./provinces.csv', encoding ='UTF-8',sep=';')

            MA_data.columns = ['Dates','Confirmed','Recovered','Deaths']
            by_cities.columns = ['City','Region','Confirmed','Deaths','Recovered']
            by_regions.columns = ['Region','Total Cases','Confirmed','Deaths','Recovered']
            by_provinces.columns = ['FID_1','provinces','Confirmed','Latitude','Longitude']

            Latitudes = [35.3174,33.3260,33.7560,34.0980,32.4843,33.1010,31.8310,31.3860,29.7453,28.3870,26.7270,22.8170]
            Longitudes = [-5.4657,-2.4220,-4.8450,-6.3280,-6.3199,-7.8060,-8.3170,-5.5470,-8.1436,-10.0910,-11.6610,-14.3610]
            by_regions['Latitude'] = Latitudes
            by_regions['Longitude'] = Longitudes

            Lati = [30.41,31.36,35.24,28.68,22.58,31.96,32.33,33.61,34.92,33.26,26.22,33.05,33.6,35.17,31.55,30.22,34.98,33.69,33.24,32.05,31.94,31.46,26.62,35.66,34.02,32.11,32.5,28.99,34.23,33.53,30.36,34.3,34.27,33.82,32.94,32.88,27.17,35.18,35.69,33.45,33.88,31.61,32.7,33.7,34.09,35.17,33.38,30.93,34.8,23.75,34.7,33.99,32.24,32.29,34.06,33.83,33.92,33,32.66,29.38,34.23,34.26,35.79,28.44,34.53,34.41,27.93,30.52,29.76,34.22,35.58,31.52,29.69,32.24,30.32]
            Longi = [-9.577,-7.947,-3.935,-9.349,-14.42,-6.57,-6.368,-7.123,-2.325,-7.589,-14.4,-3.989,-7.63,-5.269,-8.767,-9.37,-3.393,-5.366,-8.51,-7.4,-4.423,-9.749,-11.78,-5.514,-4.979,-1.224,-6.688,-10.07,-3.349,-5.105,-9.552,-2.18,-6.538,-6.068,-5.666,-6.915,-13.09,-6.152,-5.325,-7.514,-5.507,-7.95,-4.733,-7.39,-5.178,-2.924,-7.559,-6.915,-5.57,-15.92,-1.903,-6.87,-7.947,-9.231,-6.788,-4.83,-6.91,-7.616,-8.426,-10.16,-5.71,-5.922,-5.903,-11.1,-4.646,-2.893,-12.9,-8.861,-7.969,-4.014,-5.349,-5.503,-9.704,-8.527,-5.826]
            by_provinces['Latitude'] = Lati
            by_provinces['Longitude'] = Longi

            cols = by_regions.select_dtypes(include=[np.object]).columns
            by_regions[cols] = by_regions[cols].apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))

            total_confirmed = MA_data['Confirmed'].max()
            total_recovered = MA_data['Recovered'].max()
            total_deaths = MA_data['Deaths'].max()
            active_cases = total_confirmed - ( total_recovered + total_deaths )
            mortality = (total_deaths / total_confirmed)*100
            mortality_rate = round(mortality,2)
            recovery = (total_recovered / total_confirmed)*100
            recovery_rate = round(recovery,2)


    # moroccan region map

            regions_coord = by_regions[['Region','Latitude','Longitude']].copy()

            map = folium.Map(location=[30, -7], zoom_start=5,tiles='OpenStreetMap')
            ma_region = os.path.join('morocco_region.json')
            provinces = os.path.join('morocco_province.json')
            reg = folium.Choropleth(
                geo_data=ma_region,
                name='Regions',
                data=by_regions,
                columns=['Region', 'Confirmed'],
                fill_color='Reds',
                fill_opacity=0.2
            ).add_to(map)
            folium.TileLayer(
                            tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                            attr = 'Esri',
                            name = 'Esri Satellite',
                            overlay = False,
                            control = True
                           ).add_to(map)
            folium.TileLayer(location=[30, -7], zoom_start=5,tiles='stamentoner', attr = 'stamentoner').add_to(map)
            m = folium.Choropleth(
                geo_data=provinces,
                name='Provinces',
                data=by_provinces,
                columns=['FID_1', 'Confirmed'],
                key_on='feature.properties.FID_1',
                fill_color='YlGn',
                fill_opacity=0.7,
                line_opacity=0.2,
                legend_name='Confirmed Cases by provinces'
            ).add_to(map)
            folium.LayerControl('topleft', collapsed=False).add_to(map)

            for lat, lon, value, name in zip(by_regions['Latitude'], by_regions['Longitude'], by_regions['Confirmed'], by_regions['Region']):
                    folium.CircleMarker([lat, lon], radius=value*0.04, popup = ('<strong>State</strong>: ' + str(name).capitalize() + '<br>''<strong>Total Cases</strong>: ' + str(value) + '<br>'),color='red',fill_color='red',fill_opacity=0.3 ).add_to(reg)

            for lat, lon, value, name in zip(by_provinces['Latitude'], by_provinces['Longitude'], by_provinces['Confirmed'], by_provinces['provinces']):
                    folium.CircleMarker([lat, lon], radius=2, tooltip = ('<strong>State</strong>: ' + str(name).capitalize() + '<br>''<strong>Total Cases</strong>: ' + str(value) + '<br>'),color='red',fill_color='red',fill_opacity=0.01 ).add_to(m)

            iframe = map._repr_html_();



            country = Country("Morocco")
            context = { "country" : country, "iframe":iframe, "mortality_rate":mortality_rate, "recovery_rate":recovery_rate, "active_cases":active_cases

            }
            return render(request,'info/country.html' ,context)



def world(request):

    death_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')
    df_table = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_time.csv",parse_dates=['Last_Update'])


    # data cleaning

    # renaming the df column names to lowercase
    country_df.columns = map(str.lower, country_df.columns)
    confirmed_df.columns = map(str.lower, confirmed_df.columns)
    death_df.columns = map(str.lower, death_df.columns)
    recovered_df.columns = map(str.lower, recovered_df.columns)

    # changing province/state to state and country/region to country
    confirmed_df = confirmed_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
    recovered_df = confirmed_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
    death_df = death_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
    country_df = country_df.rename(columns={'country_region': 'country'})
    confirmed_df['state'] = confirmed_df['state'].replace(np.nan, '')

    # total number of confirmed, death and recovered cases
    confirmed_total = int(country_df['confirmed'].sum())
    deaths_total = int(country_df['deaths'].sum())
    recovered_total = int(country_df['recovered'].sum())
    active_total = int(country_df['active'].sum())
    mortality_rate = round(((deaths_total/confirmed_total)*100), 2)
    recovery_rate = round(((recovered_total/confirmed_total)*100), 2)
    country_count = int(confirmed_df['country'].count())
# world map
    world_map = folium.Map(location=[11,0], tiles="OpenStreetMap", zoom_start=2, max_zoom = 6, min_zoom = 2)
    for i in range(0,len(confirmed_df)):
        folium.Circle(
            location=[confirmed_df.iloc[i]['lat'], confirmed_df.iloc[i]['long']],
            fill=True,
            radius=(int((np.log(confirmed_df.iloc[i,-1]+1.00001)))+0.2)*50000,
            color='grey',
            fill_color='indigo',
            tooltip = "<div style='margin: 0; background-color: white; color: white;'>"+
                        "<h4 style='color: Black;text-align:center;font-weight: bold'>"+str(confirmed_df.iloc[i]['country']) + "<br>" +str(confirmed_df.iloc[i]['state']) + "</h4>"
                        "<hr style='margin:10px;color: white;'>"+
                        "<ul style='color: Black;list-style-type:circle;align-item:left;padding-left:20px;padding-right:20px'>"+
                            "<li>Confirmed: "+str(confirmed_df.iloc[i,-1])+"</li>"+
                            "<li>Deaths:   "+str(death_df.iloc[i,-1])+"</li>"+
                            "<li>Death Rate: "+ str(np.round(death_df.iloc[i,-1]/(confirmed_df.iloc[i,-1]+1.00001)*100,2))+ "</li>"+
                        "</ul></div>",
            ).add_to(world_map)
        iframe = world_map._repr_html_()

#map by Dates

    df_data = df_table.groupby(['Last_Update', 'Country_Region'])['Confirmed', 'Deaths'].max().reset_index().fillna(0)
    df_data["Last_Update"] = pd.to_datetime( df_data["Last_Update"]).dt.strftime('%m/%d/%Y')

    fig = px.scatter_geo(df_data, locations="Country_Region", locationmode='country names',
                         color=np.power(df_data["Confirmed"],0.3)-2 , size= np.power(df_data["Confirmed"]+1,0.3)-1, hover_name="Country_Region",
                         hover_data=["Confirmed"],
                         range_color= [0, max(np.power(df_data["Confirmed"],0.3))],
                         animation_frame="Last_Update",
                         color_continuous_scale=px.colors.sequential.Plasma
                        )
    fig.update_geos(
    visible=True, resolution=50,
    showcountries=True, countrycolor="#000000"
    )
    fig.update_coloraxes(colorscale="hot")
    fig.update(layout_coloraxis_showscale=False)
    fig = py.plot(fig , filename='COVID-19: Progression of spread', auto_open=False)

#Chart

    w = pd.read_csv('https://coronavirus.politologue.com/data/coronavirus/coronacsv.aspx?format=csv&t=global', header=3,sep=';',index_col=None)
    f = w.drop([0])
    listp = []
    listp.append(f)
    k = listp[0]
    dates = k['Date']
    confirmed = k['Infections']
    deaths = k['Deces']
    recovered = k['Guerisons']

    world = World()
    context = { "world" : world, "iframe":iframe, "country_count":country_count, "confirmed_total":confirmed_total, "deaths_total":deaths_total, "recovered_total":recovered_total, "mortality_rate":mortality_rate, "recovery_rate":recovery_rate , 'dates':dates, 'confirmed':confirmed, 'deaths':deaths, 'recovered':recovered
    }
    return render(request,'info/world.html' ,context)
