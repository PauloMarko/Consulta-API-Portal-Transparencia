import pandas as pd
import os


class GravadorCSV:
    def __init__(self, dados):
        self.dados = dados

    def gravar(self, csv_saida):
        if isinstance(self.dados, dict):
            registro = [self.dados]
        else:
            registro = self.dados

        df = pd.DataFrame(registro)
        arquivo_existe = os.path.exists(csv_saida)
        if arquivo_existe:
            df.to_csv(csv_saida, index=False, header=False, encoding="utf-8", mode="a")
        else:
            df.to_csv(csv_saida, index=False, encoding="utf-8", mode="w")