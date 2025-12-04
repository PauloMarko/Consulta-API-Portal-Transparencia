import logging
import os

from dotenv import load_dotenv
from typing import Optional

from ConsultaAPI import ConsultaAPI
from GravadorCSV import GravadorCSV
from LeitorCSV import LeitorCSV
from ValidarDados import ValidarDados


class ControladorAplicacao:
    def __init__(self, chave_api, csv_entrada, csv_saida, logger: Optional[logging.Logger] = None):
        self.logger = logger or logging.getLogger(__name__)
        self.chave_api = chave_api
        self.csv_entrada = csv_entrada
        self.csv_saida = csv_saida

    def executar(self) -> None:
        leitor = LeitorCSV(self.csv_entrada)
        self.cpfs = leitor.ler()
        for cpf in self.cpfs:
            consulta = ConsultaAPI(self.chave_api, cpf)
            dados = consulta.consultar()
            pessoa = ValidarDados(**dados)
            dados_validos= pessoa.dict()
            gravador = GravadorCSV(dados_validos)
            gravador.gravar(self.csv_saida)

    @staticmethod
    def chaveApi():
        logger = logging.getLogger(__name__)
        if os.path.exists(".env"):
            try:
                load_dotenv()
                chave = os.getenv("CHAVE_API_DADOS")
                if chave:
                    logger.info(
                        "Chave API encontrada nas variáveis de ambiente ('.env')"
                    )
                    return chave
            except Exception as e:
                logger.warning(
                    f"[Aviso] Chave API não foi encontrada nas variáveis de ambiente ('.env'): {e}"
                )

        while True:
            chave_input = input("Insira a chave API do Portal da Transparência: ")
            if chave_input:
                return chave_input
            print("[Aviso] A chave não pode ser vazia. Tente novamente.")
            break
