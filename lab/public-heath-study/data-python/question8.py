#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:05:30 2020

@author: yassine
"""

import pandas as pd
import numpy as np


SousAlimentation = pd.read_csv("/Users/yassine/Desktop/data-python/fr_sousalimentation.csv")
SousAlimentation['Valeur'].dropna(axis=0)
SousAlimentation.dropna(subset = ["Valeur"], inplace=True)
SousAlimentation['Valeur'] = SousAlimentation['Valeur'].str.replace('<', '')
SousAlimentation['Valeur'] = SousAlimentation['Valeur'].astype(float)
SousAlimentation['MoyenneValeur/perY'] = SousAlimentation['Valeur'] / 36

v1 = SousAlimentation.loc[SousAlimentation['Code année'] != 20142016]
v2 = v1.loc[v1['Code année'] != 20152017 ]
v3 = v2.loc[v2['Code année'] != 20162018 ]

traitementDataSousAlimentation = v3.drop(['Élément','Code Domaine','Domaine','Symbole','Domaine','Code Domaine','Code Élément','Code année','Description du Symbole','Note'], axis=1)


lostWorldFood = traitementDataSousAlimentation['MoyenneValeur/perY'].sum()
NbpersonSousalimentation = lostWorldFood * 1000000

vegetauxCsv = pd.read_csv("/Users/yassine/Desktop/data-python/fr_vegetaux.csv")
dateV = vegetauxCsv.loc[vegetauxCsv['Année'] == 2013]
rcpVegetaux = dateV.drop(['Année','Code Produit','Symbole','Domaine','Code Domaine','Code Élément','Code année','Description du Symbole'], axis=1)
rcpVegetaux[rcpVegetaux['Élément'] == 'Disponibilité alimentaire (Kcal/personne/jour)']
rgVegetaux = rcpVegetaux.loc[rcpVegetaux['Valeur'] !=  0]
vegetauxTotal = rgVegetaux['Valeur'].sum()



populationCsvToArray = pd.read_csv("/Users/yassine/Desktop/data-python/fr_population.csv", sep=',')
populationBydate = populationCsvToArray.loc[populationCsvToArray['Année'] == 2013]
filtered_df = populationBydate[(populationBydate['Code zone'] != 96) & (populationBydate['Code zone'] != 41) & (populationBydate['Code zone'] != 128) & (populationBydate['Code zone'] != 214)]
populationRemoveDuplicateByCountries =  filtered_df.drop_duplicates(subset='Code zone', keep="last")
populationRemoveDuplicateByCountries.rename(columns={'Zone':'Pays'}, inplace=True)
dropPop = populationRemoveDuplicateByCountries.drop(['Élément','Code Produit','Symbole','Domaine','Code Domaine','Code Élément','Code année','Description du Symbole'], axis=1)
dropPop['Population'] = dropPop['Valeur'] * 1000
countries = dropPop

sumPopulation = countries['Population'].sum()


##reponsse
vegetauxPerPopulation = vegetauxTotal / sumPopulation

