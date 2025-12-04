import pandas as pd
from typing import Optional
import logging


class LeitorCSV:
    def __init__(self, csv_file, logger: Optional[logging.Logger] = None):
        self.logger = logger or logging.getLogger(__name__)
        self.csv_file = csv_file

    def ler(self):
        self.logger.debug("Lendo arquivo CSV...")
        df = pd.read_csv(self.csv_file)
        lista_cpfs = df['cpfs'].astype(str).tolist()
        lista_cpfs = sorted(set(lista_cpfs))
        return lista_cpfs
