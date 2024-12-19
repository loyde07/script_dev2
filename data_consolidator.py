class DataConsolidator:
    @staticmethod
    def import_csv_files(data_path):
        """
        Importe tous les fichiers CSV depuis un dossier spécifié et les fusionne en un seul DataFrame.

        Args:
            data_path (str): Le chemin vers le dossier contenant les fichiers CSV à importer.

        Returns:
            pandas.DataFrame: Un DataFrame contenant les données consolidées de tous les fichiers CSV.

        Raises:
            FileNotFoundError: Si le dossier spécifié n'existe pas.
            ValueError: Si aucun fichier CSV n'a été trouvé dans le dossier.
            Exception: Si une erreur se produit lors de la lecture d'un fichier CSV.
        """
        import os
        import pandas as pd

        # Initialiser une liste pour stocker les DataFrames
        all_data = []

        # Vérifier si le dossier existe
        if not os.path.isdir(data_path):
            raise FileNotFoundError(f"Le dossier {data_path} n'existe pas.")

        # Parcourir les fichiers CSV dans le dossier
        for filename in os.listdir(data_path):
            if filename.endswith(".csv"):
                file_path = os.path.join(data_path, filename)
                try:
                    # Lire le fichier CSV dans un DataFrame
                    df = pd.read_csv(file_path)
                    all_data.append(df)
                except Exception as e:
                    print(f"Erreur lors de l'importation du fichier {filename}: {e}")

        # Fusionner tous les DataFrames en un seul
        if all_data:
            consolidated_data = pd.concat(all_data, ignore_index=True)
            return consolidated_data
        else:
            raise ValueError("Aucun fichier CSV n'a été trouvé dans le dossier.")
