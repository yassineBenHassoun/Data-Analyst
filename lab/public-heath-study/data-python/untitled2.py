#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:10:57 2020

@author: yassine
"""

import pandas as pd
import numpy as np


# Import des données des bilans alimentaires
veg = pd.read_csv("/Users/yassine/Desktop/data-python/fr_vegetaux.csv")
ani = pd.read_csv("/Users/yassine/Desktop/data-python/fr_animaux.csv")

cac = veg['Produit'].sum()


# Ajout de la variable origin
ani["Origine"] = "animale"
veg["Origine"] = "vegetale"
# On regroupe veg et ani en un unique dataframe, via une union
temp = ani.append(veg)
# Suppression de ani et veg
del ani, veg
# Transformation de temp en table pivot
data = temp.pivot_table(index=["Zone","Produit","Origine"],
                        columns = ["Élément"], values=["Valeur"], aggfunc=sum)
data.columns = ['Aliments pour animaux', 'Autres Utilisations', 'Disponibilité alimentaire (Kcal/personne/jour)',
                'Disponibilité alimentaire en quantité (kg/personne/an)',
                'Disponibilité de matière grasse en quantité (g/personne/jour)',
                'Disponibilité de protéines en quantité (g/personne/jour)', 'Disponibilité intérieure',
                'Exportations - Quantité', 'Importations - Quantité', 'Nourriture', 'Pertes', 'Production',
                'Semences', 'Traitement', 'Variation de stock']
dispo_alimentaire = data.reset_index()
dispo_alimentaire.head()




