
import numpy as np
import pandas as pd
import streamlit as st
import pickle

## Load all the instances that are required

with open('model.pkl','rb') as file:
    model = pickle.load(file)

with open('scaler.pkl','rb') as file:
    scaler = pickle.load(file)

with open('pca.pkl','rb') as file:
    pca = pickle.load(file)

def prediction(input_data):
    scaled_data = scaler.transform(input_data)
    pca_data = pca.transform(scaled_data)
    pred = model.predict(pca_data)[0]

    if pred==0:
        return 'Developed'
    elif pred==1:
        retun 'Developing'
    else:
        return 'Under Developed'

def main():
    st.title('HELP International Foundation')
    st.subheader('This application helps to classify the country on the basis of Socio-Economic and health factors')
    cld_mor = st.text_input('Enter Child Mortality Rate')
    life_exp = st.text_input('Enter Average Life Expectancy')
    tol_fer = st.text_input('Enter Total Fertility Rate')
    health = st.text_input('Enter the GDP spent on health')
    export = st.text_input('Enter the GDP spent on Exports')
    impor = st.text_input('Enter the GDP spent on Imports')
    gdp = st.text_input('Enter GDP per population')
    income = st.text_input('Enter the Income per person')
    infl = st.text_input('Enter the Inflation Rate')

    imp_list= [[cld_mor, export, health, impor, income, infl, life_exp, tol_fer, gdp]]

    if st.button('Perdict'):
        reponse = prediction(inp_list)
        st.success(reponce)

if __name__ == '__main__':
    main()
