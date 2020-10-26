#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:19:04 2020

@author: yassine
"""

import pandas as pd
import numpy as np



#Q1
pop=pd.read_csv("/Users/yassine/Desktop/data-python/fr_population.csv")
pop=pop[['Zone','Valeur','Code zone']]
pop['Valeur']=pop['Valeur']*1000
pop=pop.rename(columns={"Valeur":"population", "Zone":"pays", "Code zone":"zone"})
pop['population'].sum()
pop.duplicated()
pop.drop_duplicates(subset=['pays'], keep= False)
pop=pop.loc[pop['pays']!= 'Chine',:]
pop.shape
pop['population'].sum()


#q2

# Import des données des bilans alimentaires 
veg = pd.read_csv("/Users/yassine/Desktop/data-python/fr_vegetaux.csv")
ani = pd.read_csv("/Users/yassine/Desktop/data-python/fr_animaux.csv")
ani["Origine"] = "animale"
veg["Origine"] = "vegetale"
temp = ani.append(veg)
del ani, veg

data = temp.pivot_table(index=["Zone","Produit","Origine"],
                        columns = ["Élément"], values=["Valeur"], aggfunc=sum)


data.columns = ['Aliments pour animaux', 'Autres Utilisations', 'Disponibilité alimentaire (Kcal/personne/jour)', 
                'Disponibilité alimentaire en quantité (kg/personne/an)', 
                'Disponibilité de matière grasse en quantité (g/personne/jour)', 
                'Disponibilité de protéines en quantité (g/personne/jour)', 'Disponibilité intérieure', 
                'Exportations - Quantité', 'Importations - Quantité', 'Nourriture', 'Pertes', 'Production', 
                'Semences', 'Traitement', 'Variation de stock']


dispo_alimentaire = data.reset_index()


listecolonne = ['Aliments pour animaux', 'Autres Utilisations', 'Disponibilité intérieure', 
                'Exportations - Quantité', 'Importations - Quantité', 'Nourriture', 'Pertes', 'Production', 
                'Semences', 'Traitement', 'Variation de stock']


for colonne in listecolonne :
    dispo_alimentaire[colonne] = dispo_alimentaire[colonne] * 1000000
    
    
dispo_alimentaire=dispo_alimentaire.rename(columns={"Zone":"pays"})
dispo_alimentaire=dispo_alimentaire.merge(pop,on="pays")
dispo_alimentaire.head()
dispo_alimentaire['Dispokcal']= dispo_alimentaire ['Disponibilité alimentaire (Kcal/personne/jour)']*dispo_alimentaire['population']*365
dispo_alimentaire['Dispoperproteine']=dispo_alimentaire ['Disponibilité de protéines en quantité (g/personne/jour)']*dispo_alimentaire['population']*365/1000
 


#Q4

dispo_alimentaire['Ratioenergiepoid']=dispo_alimentaire['Dispokcal']/ dispo_alimentaire ['Nourriture']
dispo_alimentaire['Ratioperproteine']=dispo_alimentaire['Dispoperproteine']/ dispo_alimentaire ['Nourriture']
dispo_alimentaire.head()
dispo_alimentaire = dispo_alimentaire.replace([np.inf, -np.inf],np.nan)
ratio =dispo_alimentaire.groupby ('Produit').mean()
ratio =ratio.reset_index()
ratio.head()
ratio =ratio[['Produit', 'Ratioenergiepoid', 'Ratioperproteine']]
ratio.loc[ratio['Produit'] == 'Oeufs',:]
ratio =ratio[['Produit', 'Ratioenergiepoid', 'Ratioperproteine']]
ratio.loc[ratio['Produit'] == 'Avoine',:]


#Q5

#ratioBySSort = ratio.sort_values (by = 'Ratioenergiepoid', ascending = False)



#q6


dfvegetaux = dispo_alimentaire.loc[dispo_alimentaire['Origine'] == 'vegetale',:]
df = dfvegetaux.dropna()
df['dom_sup_kcal'] = df['Disponibilité intérieure'] * df['Ratioenergiepoid']
df['dom_sup_kgprot'] = df['Disponibilité intérieure'] * df['Ratioperproteine']



#Q7

MOYWorldKCAL = 2500
KG_PROT_PER_CAPITA_PER_DAY = 62 * .9 * .001
sumDomSupKgProt = df['dom_sup_kgprot'].sum()
sumDomSupKcal = df['dom_sup_kcal'].sum()
responseD7A = sumDomSupKcal/ 365 / MOYWorldKCAL
response7APourcent = responseD7A * 100 / pop['population'].sum()
responseD7B  = sumDomSupKgProt / 365 / KG_PROT_PER_CAPITA_PER_DAY
responseD7BPourcent  = responseD7B * 100 / pop['population'].sum() 

#Q8


    

