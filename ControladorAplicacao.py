import os
import logging
from dotenv import load_dotenv
from ConsultaAPI import ConsultaAPI
from LeitorCSV import LeitorCSV
from GravadorCSV import GravadorCSV
from ValidarDados import ValidarDados


class ControladorAplicacao:
    def __init__(self, chave_api, csv_entrada, csv_saida):
        if os.path.exists(csv_saida):
            os.remove(csv_saida)

        self.chave_api = chave_api
        self.csv_entrada = csv_entrada
        self.csv_saida = csv_saida

        leitor = LeitorCSV(self.csv_entrada)
        self.cpfs = leitor.ler()

        # Para iniciar o logging
        self.log()

    def executar(self):
        for cpf in self.cpfs:
            consulta = ConsultaAPI(self.chave_api, cpf)
            dados = consulta.consultar()
            pessoa = ValidarDados(**dados)
            dados_validos = pessoa.dict()
            gravador = GravadorCSV(dados_validos)
            gravador.gravar(self.csv_saida)

    def log(self):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%d-%b-%y %H:%M:%S',
            filename='logfile.log',
        )

    @staticmethod
    def chaveApi():
        if os.path.exists('.env'):
            try:
                load_dotenv()
                chave = os.getenv('CHAVE_API_DADOS')
                if chave:
                    return chave
            except Exception:
                logging.warning("[Aviso] Chave API não foi encontrada nas variáveis de ambiente ('.env').")

        while True:
            chave_input = input("Insira a chave API do Portal da Transparência: ")
            if chave_input:
                return chave_input
            print("[Aviso] A chave não pode ser vazia. Tente novamente.")
            break
