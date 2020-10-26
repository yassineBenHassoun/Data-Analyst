#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:20:43 2020

@author: yassine
"""

import pandas as pd
import numpy as np


vegetauxCsv = pd.read_csv("/Users/yassine/Desktop/data-python/fr_vegetaux.csv")
dateV = vegetauxCsv.loc[vegetauxCsv['Année'] == 2013]
r = dateV[dateV['Unité'] == 'Kcal/personne/jour']
perDayV = r[r['Élément'] == 'Disponibilité alimentaire (Kcal/personne/jour)']

populationCsvToArray = pd.read_csv("/Users/yassine/Desktop/data-python/fr_population.csv", sep=',')
populationBydate = populationCsvToArray.loc[populationCsvToArray['Année'] == 2013]
filtered_df = populationBydate[(populationBydate['Code zone'] != 96) & (populationBydate['Code zone'] != 41) & (populationBydate['Code zone'] != 128) & (populationBydate['Code zone'] != 214)]
populationRemoveDuplicateByCountries =  filtered_df.drop_duplicates(subset='Code zone', keep="last")
populationRemoveDuplicateByCountries.rename(columns={'Zone':'Pays'}, inplace=True)
dropPop = populationRemoveDuplicateByCountries.drop(['Élément','Code Produit','Symbole','Domaine','Code Domaine','Code Élément','Code année','Description du Symbole'], axis=1)
dropPop['Population'] = dropPop['Valeur'] * 1000





countries = dropPop
vegetaux = perDayV.drop(['Année','Code Produit','Symbole','Domaine','Code Domaine','Code Élément','Code année','Description du Symbole'], axis=1)




print(vegetaux.columns)