from django.shortcuts import render

# Create your views here.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import os
import csv
import requests
plt.rcParams['figure.figsize'] = 10, 12
import warnings
warnings.filterwarnings('ignore')
import chart_studio
username='medel'
api_key='uiMAmfBFm6jx09RmTttE'
chart_studio.tools.set_credentials_file(username=username , api_key=api_key)
import chart_studio.plotly as py
import chart_studio.tools as tls
from .api import Country,World
from .	import views


def moroccan_plots(request):

        MA_data = pd.read_csv('https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/MA-times_series.csv')
        by_cities = pd.read_csv('https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/cities.csv')
        by_regions = pd.read_csv('https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/regions.csv')


        MA_data.columns = ['Dates','Confirmed','Recovered','Deaths']
        by_cities.columns = ['City','Region','Confirmed','Deaths','Recovered']
        by_regions.columns = ['Region','Total Cases','Confirmed','Deaths','Recovered']

        Latitudes = [35.3174,33.3260,33.7560,34.0980,32.4843,33.1010,31.8310,31.3860,29.7453,28.3870,26.7270,22.8170]
        Longitudes = [-5.4657,-2.4220,-4.8450,-6.3280,-6.3199,-7.8060,-8.3170,-5.5470,-8.1436,-10.0910,-11.6610,-14.3610]
        by_regions['Latitude'] = Latitudes
        by_regions['Longitude'] = Longitudes

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

        currently_infected = MA_data['Confirmed']-(MA_data['Recovered'] + MA_data['Deaths'])

# Daily New Cases in Morocco
        new_confirmed_cases = [0]
        new_recovered_cases = [0]
        new_death_cases = [0]

        for i,r in MA_data[['Confirmed','Recovered','Deaths']].iterrows():
            if i > 0:
                new_confirmed_cases.append(r['Confirmed'] - MA_data['Confirmed'][i-1])
                new_recovered_cases.append(r['Recovered'] - MA_data['Recovered'][i-1])
                new_death_cases.append(r['Deaths'] - MA_data['Deaths'][i-1])
        new_cases_df = pd.DataFrame({'Dates':MA_data['Dates'],'new_confirmed':new_confirmed_cases,'new_recovered':new_recovered_cases,'new_deaths':new_death_cases})
        df_long=pd.melt(new_cases_df, id_vars=['Dates'], value_vars=['new_confirmed','new_deaths','new_recovered'])
        fig1 = px.line(df_long, x='Dates', y='value', color='variable')
        fig1.update_layout(xaxis_title='Days',
                           yaxis_title='New Cases')
        fig1 = py.plot(fig1 , filename='Daily New Cases in Morocco', auto_open=False)

# Active Cases in Morocco (Number of Infected people)
        fig2 = go.Figure(data=go.Scatter(x=MA_data['Dates'],y=currently_infected.values,mode='lines+markers'))
        fig2.update_layout( xaxis_title='Days',
                           yaxis_title='New Cases')

        fig2 = py.plot(fig2 , filename='Active Cases in Morocco (Number of Infected people)', auto_open=False)

# Covid19 Cases in Moroccan Regions
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(
            y=by_regions['Region'],
            x=by_regions['Confirmed'],
            name='Confirmed',
            orientation='h',
            marker=dict(
                color='rgba(222, 25, 27, 0.6)',
                line=dict(color='rgba(222, 25, 27, 0.6)', width=3)
            )
        ))
        fig3.add_trace(go.Bar(
            y=by_regions['Region'],
            x=by_regions['Recovered'],
            name='Recovered',
            orientation='h',
            marker=dict(
                color='rgba(80, 180, 50, 0.6)',
                line=dict(color='rgba(80, 180, 50, 0.6)', width=3)
            )
        ))

        fig3.update_layout(barmode='stack',
                           xaxis_title='Cases',
                           yaxis_title='Regions')
        fig3 = py.plot(fig3 , filename='Covid19 Cases in Moroccan Regions', auto_open=False)

# Confirmed cases

        fig4 = px.bar(MA_data,x="Dates",y="Confirmed",color="Confirmed",orientation="v",
                     height=400,title="Confirmed",
                     color_discrete_sequence=px.colors.cyclical.IceFire)
        fig4 = py.plot(fig4 , filename='Confirmed cases', auto_open=False)

# Recovered Cases
        fig5 = px.bar(MA_data,x="Dates",y="Recovered",color="Recovered",orientation="v",
                     height=400,title="Recovered",
                     color_discrete_sequence=px.colors.sequential.Plasma)
        fig5 = py.plot(fig5 , filename='Recovered Cases', auto_open=False)

# Deaths Cases
        fig6 = px.bar(MA_data,x="Dates",y="Deaths",color="Deaths",orientation="v",
                     height=400,title="Deaths",
                     color_discrete_sequence=px.colors.cyclical.mrybm)
        fig6 = py.plot(fig6 , filename='Deaths Cases', auto_open=False)

        country = Country("Morocco")
        context = { "country" : country, "mortality_rate":mortality_rate, "recovery_rate":recovery_rate, "active_cases":active_cases, "fig1" : fig1, "fig2" : fig2, "fig3" : fig3, "fig4" : fig4, "fig5" : fig5, "fig6" : fig6}

        return render(request,'info/moroccan_plots.html' ,context)






def world_plots(request):


    death_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')

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

    # total number of confirmed, death and recovered cases
    confirmed_total = int(country_df['confirmed'].sum())
    deaths_total = int(country_df['deaths'].sum())
    recovered_total = int(country_df['recovered'].sum())
    active_total = int(country_df['active'].sum())
    mortality_rate = round(((deaths_total/confirmed_total)*100), 2)
    recovery_rate = round(((recovered_total/confirmed_total)*100), 2)
    country_count = int(country_df['country'].count())

    sorted_country_df = country_df.sort_values('confirmed', ascending= False)

# 20 Worst hit countries
    fig1 = px.scatter(sorted_country_df.head(20), x="country", y="confirmed", size="confirmed", color="country",
               hover_name="country", size_max=60)
    fig1.update_layout(
                    xaxis_title="Countries",
                    yaxis_title="Confirmed Cases",
                    width = 700
                    )
    fig1 = py.plot(fig1 , filename='20 Worst hit countries', auto_open=False)

# Top 10 worst affected countries (confirmed cases)

    fig2 =px.bar(
                    sorted_country_df.head(10),
                    x = "country",
                    y = "confirmed",
                    color_discrete_sequence=["pink"],
                    height=500,
                    width=800
                )
    fig2 = py.plot(fig2 , filename='Top 10 worst affected countries (confirmed cases)', auto_open=False)

# Top 10 worst affected countries (deaths)

    fig3 = px.bar(
                sorted_country_df.head(10),
                x = "country",
                y = "deaths",
                color_discrete_sequence=["pink"],
                height=500,
                width=800
                )
    fig3 = py.plot(fig3 , filename='Top 10 worst affected countries (deaths)', auto_open=False)

# Top 10 worst affected countries (recovered)
    fig4 = px.bar(
                sorted_country_df.head(10),
                x = "country",
                y = "recovered",
                color_discrete_sequence=["pink"],
                height=500,
                width=800
                )

    fig4 = py.plot(fig4 , filename='Top 10 worst affected countries (recovered)', auto_open=False)

    context = { "fig1" : fig1, "fig2" : fig2, "fig3" : fig3, "fig4" : fig4, "country_count":country_count, "confirmed_total":confirmed_total, "deaths_total":deaths_total, "recovered_total":recovered_total, "mortality_rate":mortality_rate, "recovery_rate":recovery_rate}

    return render(request,'info/world_plots.html', context)
