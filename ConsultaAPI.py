import requests


class ConsultaAPI:
    def __init__(self, chave_api, cpf):
        self.__url = "https://api.portaldatransparencia.gov.br/api-de-dados/pessoa-fisica"
        self.__chave_api = chave_api
        self.cpf = str(cpf)

    def consultar(self):
        if not isinstance(self.cpf, str):
            raise TypeError("O valor CPF tem que ser string")
        if not self.__chave_api:
            raise ValueError("Não há chave de API.")

        header = {
            "chave-api-dados": self.__chave_api
        }

        consulta = f"{self.__url}?cpf={self.cpf}"
        resposta = requests.get(consulta, headers=header, timeout=5)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            raise ConnectionError(f"A conexão falhou: {resposta.status_code}")