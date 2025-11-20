import pandas as pd
import json
import os


class GravadorCSV:
    def __init__(self, dados_json):
        self.dados = dados_json

    def gravar(self):
        data = json.loads(self.dados)
        df = pd.DataFrame(data)
        print(df)

        df.to_csv('output.csv', index=False, encoding="utf-8")
        return None
