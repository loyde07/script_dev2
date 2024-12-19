import pandas as pd
import os


class InventoryHandler:
    DATA_FILE = "data/consolidated_data.csv"

    @staticmethod
    def load_data():
        """
        Charge les données depuis le fichier CSV consolidé.

        Returns:
            pandas.DataFrame: Un DataFrame contenant les données du fichier CSV.

        Raises:
            FileNotFoundError: Si le fichier "data/consolidated_data.csv" n'existe pas.
        """
        if not os.path.exists(InventoryHandler.DATA_FILE):
            raise FileNotFoundError("Fichier consolidé introuvable. Importez d'abord les données.")
        return pd.read_csv(InventoryHandler.DATA_FILE)

    @staticmethod
    def search_by_product(product_name):
        """
        Recherche un produit dans l'inventaire consolidé.

        Args:
            product_name (str): Le nom du produit à rechercher.

        Returns:
            pandas.DataFrame: Un DataFrame contenant les lignes qui correspondent au produit recherché.

        Raises:
            FileNotFoundError: Si le fichier "data/consolidated_data.csv" n'existe pas.
        """
        df = InventoryHandler.load_data()
        results = df[df['product'].str.contains(product_name, case=False, na=False)]
        return results

    @staticmethod
    def generate_report(report_type, threshold=None):
        """
        Génère un rapport basé sur le type spécifié (par catégorie ou sur les stocks faibles).

        Args:
            report_type (str): Le type de rapport à générer, soit "category" pour un rapport par catégorie,
                                soit "low_stock" pour un rapport sur les produits avec un stock faible.
            threshold (int, optional): Le seuil de stock pour générer un rapport des stocks faibles. Utilisé uniquement pour
                                       "low_stock". Par défaut à None.

        Returns:
            str: Un rapport sous forme de chaîne de caractères.

        Raises:
            FileNotFoundError: Si le fichier "data/consolidated_data.csv" n'existe pas.
        """
        df = InventoryHandler.load_data()

        if report_type == "category":
            # Générer un rapport par catégorie avec les quantités
            report = df.groupby("category").agg({"quantity": "sum"}).reset_index()
            report_str = report.to_string(index=False)  # Convertir le DataFrame en une chaîne
            return report_str  # Retourner le rapport sous forme de texte

        elif report_type == "low_stock":
            if threshold is None:
                return "Le seuil de stock doit être spécifié pour un rapport sur les stocks faibles."
            else:
                low_stock_report = df[df["quantity"] < threshold]
                return low_stock_report.to_string(index=False)

        else:
            return "Type de rapport non valide."
