# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:50:14 2020

@author: Syamanthaka
"""
import pandas as pd
import plotly.figure_factory as ff
#import plotly.graph_objs as go
#from plotly.subplots import make_subplots

df = pd.read_excel('Skills.xlsx', sheet_name='Career')
#print(df.head())
## Value for total count of studies

#################################################################################################
#
#s, 
career_tl = ff.create_gantt(df,index_col='Finish', colors=['#333F44', '#93e4c1'], title="Career Timeline",
                      bar_width=0.2, showgrid_x=True, showgrid_y=True)

## Pie chart for distribution of countries
#def generate_country_pie():
#   country_labels = df['Country'].unique()
#   country_vals = df['Country'].value_counts()
#   
#   country_pie = go.Figure(data=[go.Pie(labels=country_labels, values=country_vals)])
#   return(country_pie)
#country_pie = generate_country_pie()
#
#Plotly.plot('graph', [{
#  type: 'bar',
#  y: [0,0,0],
#  x: [1,2,1],
#  orientation: 'h',
#  base: [0,2,5]
#}, {
#  type: 'bar',
#  y: [1,1,1],
#  x: [2,1,2],
#  orientation: 'h',
#  base: [0,3,5]
#}])
