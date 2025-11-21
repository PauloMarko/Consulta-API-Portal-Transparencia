import pandas as pd


class LeitorCSV:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def ler(self):
        df = pd.read_csv(self.csv_file)
        lista_cpfs = df['cpfs'].astype(str).tolist()
        lista_cpfs = sorted(set(lista_cpfs))
        return lista_cpfs
