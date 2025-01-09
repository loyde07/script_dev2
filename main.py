import argparse
from inventory_handler import InventoryHandler
from data_consolidator import DataConsolidator


def import_csv(data_path):
    """
    Importe les fichiers CSV depuis un dossier spécifié et les enregistre dans un fichier consolidé.
    """
    try:
        # Consolider les fichiers CSV
        consolidated_data = DataConsolidator.import_csv_files(data_path)
        print(f"Fichiers CSV importés depuis le dossier: {data_path}")
        print(consolidated_data)  # Afficher les données consolidées

        # Enregistrer les données consolidées dans un fichier CSV
        consolidated_data.to_csv(InventoryHandler.DATA_FILE, index=False)
        print(f"Les données consolidées ont été enregistrées dans {InventoryHandler.DATA_FILE}")

    except Exception as e:
        print(f"Erreur lors de l'importation des fichiers CSV : {e}")


def search_product(search_term):
    """
    Recherche un produit ou une catégorie dans l'inventaire consolidé.
    """
    try:
        # Utilisez 'search_by_product' au lieu de 'search_product'
        results = InventoryHandler.search_by_product(search_term)
        if results.empty:
            print("Aucun résultat trouvé.")
        else:
            print("Résultats de la recherche :")
            print(results)
    except Exception as e:
        print(f"Erreur lors de la recherche : {e}")


def generate_report(report_type, threshold=None):
    """
    Génère un rapport 

    """
    try:
        if report_type == "category":
            # Appeler la méthode generate_report pour obtenir un rapport par catégorie
            report = InventoryHandler.generate_report("category")
            print("Rapport par catégorie généré avec succès.")
            print(report)  # Afficher le rapport par catégorie

        elif report_type == "low_stock":
            if threshold is None:
                print("Le seuil de stock doit être spécifié pour un rapport sur les stocks faibles.")
            else:
                report = InventoryHandler.generate_report("low_stock", threshold=threshold)
                print("Rapport des produits avec stock faible généré avec succès.")
                print(report)  # Afficher le rapport des produits avec stock faible

        else:
            print("Type de rapport non valide.")

    except Exception as e:
        print(f"Erreur lors de la génération du rapport : {e}")


def interactive_shell():
    """
    Boucle interactive pour exécuter les commandes en continu

    """
    print("Bienvenue dans le shell interactif du système de gestion d'inventaire.")
    print("Tapez 'help' pour afficher les commandes disponibles. Tapez 'exit' pour quitter.\n")

    while True:
        command = input("inventaire> ").strip().split()

        if not command:
            continue

        action = command[0].lower()

        if action == "exit":
            print("Au revoir !")
            break
        elif action == "help":
            print("\nCommandes disponibles :")
            print("  import <data_path>        Importer les fichiers CSV depuis un dossier spécifié")
            print("  search <search_term>      Rechercher un produit ou une catégorie")
            print("  report category           Générer un rapport par catégorie")
            print("  report low_stock <seuil>  Générer un rapport des produits avec un stock faible")
            print("  exit                      Quitter le programme\n")
        elif action == "import" and len(command) == 2:
            import_csv(command[1])
        elif action == "search" and len(command) >= 2:
            search_term = " ".join(command[1:])
            search_product(search_term)
        elif action == "report" and len(command) >= 2:
            report_type = command[1]
            threshold = int(command[2]) if len(command) == 3 and command[1] == "low_stock" else None
            generate_report(report_type, threshold)
        else:
            print("Commande invalide. Tapez 'help' pour voir les commandes disponibles.")


def parse_args():
    """
    Analyse les arguments passés en ligne de commande pour tester les fonctionnalités du programme.
    """
    parser = argparse.ArgumentParser(description="Outil de gestion des stocks.")

    # Ajouter les options de la ligne de commande
    parser.add_argument('--import_data', metavar='data_path', type=str, help="Importer des fichiers CSV depuis un dossier spécifié.")
    parser.add_argument('--search', metavar='search_term', type=str, help="Rechercher un produit ou une catégorie.")
    parser.add_argument('--report', choices=['category', 'low_stock'], help="Générer un rapport résumé des catégories ou des produits en faible stock.")
    parser.add_argument('--low_stock_threshold', metavar='threshold', type=int, help="Seuil de stock faible pour le rapport.")

    return parser.parse_args()


def main():
    args = parse_args()

    if args.import_data:
        print(f"Importation des fichiers CSV depuis le dossier : {args.import_data}")
        import_csv(args.import_data)
    elif args.search:
        print(f"Recherche du produit : {args.search}")
        search_product(args.search)
    elif args.report:
        print(f"Génération du rapport : {args.report}")
        threshold = args.low_stock_threshold if args.report == "low_stock" else None
        generate_report(args.report, threshold)
    else:
        print("Aucune option valide fournie. Lancement de l'interface interactive...")
        # Si aucun argument n'est fourni, lance la CLI interactive
        interactive_shell()


if __name__ == "__main__":
    main()
