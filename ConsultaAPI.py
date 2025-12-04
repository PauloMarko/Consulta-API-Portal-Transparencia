import requests
import logging
from typing import Optional

class ConsultaAPI:
    def __init__(self, chave_api, cpf, logger: Optional[logging.Logger] = None):
        self.logger = logger or logging.getLogger(__name__)
        self.__url = "https://api.portaldatransparencia.gov.br/api-de-dados/pessoa-fisica"
        self.__chave_api = chave_api
        self.cpf = str(cpf)

    def consultar(self):
        if not self.__chave_api:
            self.logger.error("Não há chave de API.")
            raise ValueError("Não há chave de API.")

        header = {
            "chave-api-dados": self.__chave_api
        }

        consulta = f"{self.__url}?cpf={self.cpf}"
        resposta = requests.get(consulta, headers=header, timeout=5)
        if resposta.status_code == 200:
            self.logger.info("Consulta realizada com sucesso!")
            return resposta.json()
        else:
            self.logger.error(f"Falha de conexão: {resposta.status_code}")
            raise ConnectionError(f"Falha de conexão: {resposta.status_code}")
