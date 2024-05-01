#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Créer une application Streamlit
def main():
    def predict_species(species):
        prediction=model.predict(species.reshape(1,-1))[0]
        
        #Associer la valeur predite a la classe correspondante
        if prediction==0:
            return 'setosa'
        elif prediction==1:
            return 'versicolor'
        else:
            return 'virginica'
    # Afficher un titre
    st.title('Prédiction des varietes de Iris')
        
    # Chargement du modèle
    model = joblib.load('C:\\Users\\hp\\Desktop\\L3 CS\\Machine Learning-Model_Iris.pkl')

    # Obtenir les données du client
    Sepal_Length = st.number_input('Longueur Sepale',min_value=0.0, max_value=10.0, value=3.5)
    Sepal_Width = st.number_input('Largeur Sepale',min_value=0.0, max_value=10.0, value=4.0)
    Petal_Length = st.number_input('Longueur Petale',min_value=0.0, max_value=10.0, value=3.5)
    Petal_Width = st.number_input('Largeur Petale',min_value=0.0, max_value=10.0, value=4.0)

    # Collecte des caracteristiques dans un tableau 
    species = np.array([Sepal_Length,Sepal_Width,Petal_Length,Petal_Width])

    # Utiliser le modèle pour prédire la probabilité 
    predict = predict_species(species)

    # Afficher la prédiction
    if st.button("Predict"):
        st.success(f'Especes predis: {predict}')
        

if __name__ == '__main__':
     main()


