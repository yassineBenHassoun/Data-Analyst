#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:58:14 2020

@author: yassine
"""

YEAR = 2013 


data["food_feed_kcal"] = data[["Food","Feed"]].sum(axis=1) * 1000000 * data["ratio_kcal/kg"]
data["food_feed_kgprot"] = data[["Food","Feed"]].sum(axis=1) * 1000000 * data["protein_%"] * .01

# Selection des produits vegetaux
vegetal = data[data["origin"] == "vegetal"]

# Calcul de la dispo. alim., nouritura animale et pertes par année
q_kcal = vegetal.groupby("year")["food_feed_kcal"].sum()
q_kgprot = vegetal.groupby("year")["food_feed_kgprot"].sum()
quantity = pd.DataFrame({"kcal": q_kcal, "kgprot": q_kgprot})

population = quantity.loc[YEAR, "kcal"] / 365 / NB_KCAL_PER_CAPITA_PER_DAY
print("Population potentiellement nourrie par la disponibilité alimentaire, la nouriture animale et les pertes de produits végétaux (en termes calorifiques) : {} Miliards, \nsoit {}% de la population mondiale.".format(round(population/1000000000,2), round(100*population/total_pop[YEAR])))
population = quantity.loc[YEAR, "kgprot"] / 365 / KG_PROT_PER_CAPITA_PER_DAY
print("Population potentiellement nourrie par la disponibilité alimentaire, la nouriture animale et les pertes de produits végétaux (en termes de protéines) : {} Miliards, \nsoit {}% de la population mondiale.".format(round(population/1000000000,2), round(100*population/total_pop[YEAR])))


print("- " * 20)


# Calcul de la dispo. alim. par année
q_kcal = data.groupby("year")["food_supply_kcal"].sum()
q_kgprot = data.groupby("year")["food_supply_kgprotein"].sum()
quantity = pd.DataFrame({"kcal": q_kcal, "kgprot": q_kgprot})

population = quantity.loc[YEAR, "kcal"] / 365 / NB_KCAL_PER_CAPITA_PER_DAY
print("Population potentiellement nourrie par la disponibilité alimentaire mondiale (en termes calorifiques) : {} Miliards, \nsoit {}% de la population mondiale.".format(round(population/1000000000,2), round(100*population/total_pop[YEAR])))
population = quantity.loc[YEAR, "kgprot"] / 365 / KG_PROT_PER_CAPITA_PER_DAY
print("Population potentiellement nourrie par la disponibilité alimentaire mondiale (en termes de protéines) : {} Miliards, \nsoit {}% de la population mondiale.".format(round(population/1000000000,2), round(100*population/total_pop[YEAR])))