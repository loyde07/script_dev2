
## Utilisation du programme 

### Prérequis 

Avant de pouvoir utiliser ce programme, il faut s'assurer d'avoir installé la bibliothéque suivante : 

`pandas`  : pour la manipulation des données. 

Celle ci peut etre installer via la commande suivante  : 

```bash
pip install pandas
```

### Utilisation du programme 

**Importer des fichiers CSV et les consolider**

Vous pouvez importer tous les fichiers CSV depuis un dossier donné et les consolider en un seul fichier consolidated_inventory.csv. 
Ceci est possible, en executant la commande suivante :

```bash
python main.py import_data /chemin/vers/le/dossier
```

### Recherche de produits

Pour rechercher un produit ou une catégorie, utilisez cette commande afin que ceux-ci s'affiche dans le terminal :

```bash
python main.py search "nom_du_produit"
```
### Générer un rapport

Vous pouvez générer deux types de rapports :

**Rapport par catégorie** :

```bash
python main.py --report "category"
```
Rapport des produits en faible stock :

```bash
python main.py report low_stock "seuil"
```
"seuil" est un nombre et il représente le seuil de stock à partir duquel les produits seront considérés en faible stock.

