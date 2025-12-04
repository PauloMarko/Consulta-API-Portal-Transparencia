import pandas as pd
import os
import logging

from typing import Optional


class GravadorCSV:
    def __init__(self, dados, logger: Optional[logging.Logger] = None):
        self.dados = dados
        self.logger = logger or logging.getLogger(__name__)

    def gravar(self, csv_saida):
        registro = [self.dados] if isinstance(self.dados, dict) else self.dados
        df = pd.DataFrame(registro)
        arquivo_existe = os.path.exists(csv_saida)
        if arquivo_existe:
            self.logger.debug(
                f"Reescrevendo {csv_saida}"
            )
            df.to_csv(csv_saida, index=False, header=False, encoding="utf-8", mode="a")
        else:
            self.logger.debug(
                f"Criando o arquivo de saída... {csv_saida}"
            )
            df.to_csv(csv_saida, index=False, encoding="utf-8", mode="w")
            self.logger.info(
                f"O arquivo {csv_saida} criado com sucesso."
            )
