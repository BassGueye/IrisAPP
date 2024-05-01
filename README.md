# IrisAPP
# Projet de Modélisation du Fichier iris.csv
Ce projet vise à effectuer une modélisation prédictive sur le jeu de données iris.csv en utilisant des techniques d'apprentissage automatique.

1. Summary
Le fichier iris.csv contient des mesures de différentes parties des fleurs de trois espèces d'iris : iris setosa, iris versicolor et iris virginica. L'objectif est de prédire l'espèce d'iris en fonction de ces mesures.

2. Import Libraries
Les bibliothèques Python nécessaires pour ce projet sont :

Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Et on a utilisé streamlit pour modeliser une application qui predit l'espece d'une plante en fonction de la modele 

3. Load & Understand Data
Le jeu de données est chargé à l'aide de Pandas pour l'analyse exploratoire et la modélisation. Des informations sur les types de données, les valeurs manquantes et les statistiques résumées sont examinées pour comprendre la structure des données.

4. Exploratory Data Analysis
L'analyse exploratoire comprend l'examen des variables catégorielles (espèces d'iris) et des variables numériques (mesures des fleurs). Des visualisations telles que des histogrammes, des diagrammes à barres et des matrices de corrélation sont utilisées pour explorer les données.

4.1 Categorical Variables
Les espèces d'iris sont examinées pour comprendre la répartition des classes dans le jeu de données.

4.2 Numerical Variables
Les mesures des fleurs sont analysées pour comprendre leurs distributions et leurs relations potentielles avec les espèces d'iris.

5. Data Transformation
Les données sont transformées si nécessaire pour les préparer à la modélisation. Cela peut inclure la normalisation, la gestion des valeurs manquantes, l'encodage des variables catégorielles, etc.

6. Model Building
Différents modèles d'apprentissage automatique sont construits à l'aide de Scikit-learn, tels que des classificateurs de régression logistique, des arbres de décision, des méthodes ensemblistes, etc. Les modèles sont entraînés, évalués à l'aide de mesures de performance appropriées et optimisés si nécessaire.

7. Conclusion
Les performances des modèles sont résumées et comparées. Des conclusions sont tirées sur les modèles les plus performants et leurs capacités de généralisation à de nouvelles données. Des recommandations peuvent être fournies pour des travaux futurs ou des améliorations de modèle.

