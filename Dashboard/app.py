import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
from babel.numbers import format_currency
sns.set(style='white')
import streamlit as st
 
with st.sidebar:
    
    st.text('Berikan Nilai Terhadap Project Ini')
    
    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=10, value=(0,10)
    )
    st.write('Values:', values)
#Load Data
day_df = pd.read_csv("day.csv")
hour_df= pd.read_csv("hour.csv")

#DataFrame
data = {
  "col1" : day_df['registered'],
  "col2" : day_df["casual"]
}

st.title('Selamat Datang di Dashboard Rental Bike')
st.header('Bagian analisis data statistik descriptif')
st.markdown('Tools untuk analisis adalah describe dan head')

st.write(day_df.describe(), day_df.head())
st.write(hour_df.describe(), hour_df.head())

st.header('Line chart untuk data stochastics')
st.line_chart(data)
st.header('Area chart untuk data stochastics')
st.area_chart(data)
st.header('Bar chart untuk data stochastics')
st.bar_chart(data)

#BoxPlot day_df
st.header('Boxplot untuk data day_df')
fig, ax = plt.subplots(figsize=(15, 10))  # You can adjust the size as needed
sns.boxplot(day_df, ax=ax)
st.pyplot(fig)
#BoxPlot hour_df
st.header('Boxplot untuk data hour_df')
fig2, ax = plt.subplots(figsize=(15, 10))  # You can adjust the size as needed
sns.boxplot(hour_df, ax=ax)
st.pyplot(fig2)




