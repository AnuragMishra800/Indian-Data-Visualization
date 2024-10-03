import streamlit as st 
import numpy as np
import pandas as pd
import plotly.express as px  

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv') 

list_of_states = list(df['State'].unique()) 
list_of_states.insert(0, 'Overall India')

st.sidebar.title('Indian Data Visulization')

selected_state = st.sidebar.selectbox('Select State', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secendary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:

    st.text('Size Represents Primary Parameter')
    st.text('Color Represents Secondary Parameter')

    if selected_state == 'Overall India':
        # plotting for india 
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size=primary, color=secondary, zoom=3, mapbox_style="carto-positron", size_max=35, height=500, width=1200, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)  
    else:
        # plotting for state 
        state_df = df[df['State'] == selected_state]
        
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary, zoom=5, mapbox_style="carto-positron", size_max=35, height=500, width=1200, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)