
/*
Les 10 pays ayant le plus haut ratio disponibilité alimentaire/habitant en termes de protéines (en kg) par habitant, puis en termes de kcal par habitant.
*/

SELECT
    pays,
    sum(dispo_prot) AS dispo_prot_g_per_jour
FROM dispo_alim
WHERE annee=2013
GROUP BY pays
ORDER BY dispo_prot_g_per_jour DESC
LIMIT 10

SELECT
    pays,
    annee,
    sum(dispo_alim_kcal_p_j) as dispo_alim_kcal_p_jour
FROM dispo_alim
GROUP BY pays, annee
ORDER BY dispo_alim_kcal_p_jour DESC
LIMIT 10


/*
Pour l'année 2013, les 10 pays ayant le plus faible ratio disponibilité alimentaire/habitant en termes de protéines (en kg) par habitant.
*/

SELECT
    pays,
    sum(dispo_prot) AS dispo_prot_g_per_jour
FROM dispo_alim
WHERE annee=2013
GROUP BY pays
ORDER BY dispo_prot_g_per_jour ASC
LIMIT 10

/*
La quantité totale (en kg) de produits perdus par pays en 2013.
*/


SELECT sum(pertes) * 1000
FROM `equilibre_prod`
WHERE equilibre_prod.annee = 2013


/*
Les 10 pays pour lesquels la proportion de personnes sous-alimentées est la plus forte
*/

SELECT
    pays,
    AVG(nb_personnes / population * 1000) AS prop_p_ss_alim
FROM population
    NATURAL JOIN sous_nutrition
GROUP BY pays
ORDER BY prop_p_ss_alim DESC
LIMIT 10


/*
Les 10 produits pour lesquels le ratio Autres utilisations/Disponibilité intérieure est le plus élevé.
*/

SELECT
    produit,
    AVG(autres_utilisations / dispo_int) AS ratio_autres_utilisations_dispo_int
FROM equilibre_prod
GROUP BY produit
ORDER BY ratio_autres_utilisations_dispo_int DESC
LIMIT 10


/*

definition des Z premier produit de la liste
    - Alcool, non Comestible : essentiecelement des produits ménager et sert a la fabrication de pièces google.com
    - Huile de Palme : 50 millions de tonnes produites par an on l'utilise dans le nutella mais aussi comme bio carburant elle devient illegal dans certain pays pour cause le déforestation wikipedia.comme
*/
