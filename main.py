import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('happy.csv')
columm = df.columns.tolist()
print(columm)
#print(dict(columm))
# colum_dict = list(columm)
# # print(colum_dict)

col1 = st.header("In Search for Hapiness")

for index, column in df.iterrows():
    print(column)

#print(df.head())
col2 = st.selectbox(label="Select Data for the x axis", options=columm)

col3 = st.selectbox(label="Select data for Axis", options=columm, placeholder= "Choose an option")

col4 = st.subheader(f"{col2} and {col3}")
d = df[col2]

t = df[col3]
figure = px.scatter(x=d, y=t, labels={"x": col2.capitalize(), "y": col3.capitalize()})

col5 = st.plotly_chart(figure)
