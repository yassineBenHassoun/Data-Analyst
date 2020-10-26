#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:35:05 2020

@author: yassine
"""

vegetauxCsv = pd.read_csv("/Users/yassine/Desktop/data-python/fr_vegetaux.csv")
dateV = vegetauxCsv.loc[vegetauxCsv['Année'] == 2013]
rcpVegetaux = dateV.drop(['Année','Code Produit','Symbole','Domaine','Code Domaine','Code Élément','Code année','Description du Symbole'], axis=1)
vegeKCAL = rcpVegetaux[rcpVegetaux['Élément'] == 'Disponibilité alimentaire (Kcal/personne/jour)']
vegeKCAL = vegeKCAL.loc[rcpVegetaux['Valeur'] !=  0]
vegetauxKCAL = vegeKCAL['Valeur'].sum()
vegetauxKCALPerYear = vegetauxKCAL * 365



populationCsvToArray = pd.read_csv("/Users/yassine/Desktop/data-python/fr_population.csv", sep=',')
populationBydate = populationCsvToArray.loc[populationCsvToArray['Année'] == 2013]
filtered_df = populationBydate[(populationBydate['Code zone'] != 96) & (populationBydate['Code zone'] != 41) & (populationBydate['Code zone'] != 128) & (populationBydate['Code zone'] != 214)]
populationRemoveDuplicateByCountries =  filtered_df.drop_duplicates(subset='Code zone', keep="last")
populationRemoveDuplicateByCountries.rename(columns={'Zone':'Pays'}, inplace=True)
dropPop = populationRemoveDuplicateByCountries.drop(['Élément','Code Produit','Symbole','Domaine','Code Domaine','Code Élément','Code année','Description du Symbole'], axis=1)
dropPop['Population'] = dropPop['Valeur'] * 1000
countries = dropPop



sumPopulation = countries['Population'].sum() 
nbPersonneVegetauxKCAL = vegetauxKCALPerYear / 2000

pourcentKcalVegetaux = 100 * (nbPersonneVegetaux / sumPopulation)


vegeProtein = rcpVegetaux[rcpVegetaux['Élément'] == 'Disponibilité de protéines en quantité (g/personne/jour)']
vegeProteinSumPerY = vegeProtein['Valeur'].sum() / 365
nbVegeProtein = vegeProteinSumPerY / 54

pourcentGProteinVegetaux = 100 * (nbVegeProtein / sumPopulation)


pop = vegetauxKCALPerYear / 365 / 2500


KG_PROT_PER_CAPITA_PER_DAY = 62 * 0.2 * .001


