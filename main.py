import toml
from ConsultaAPI import ConsultaAPI
from LeitorCSV import LeitorCSV
from GravadorCSV import GravadorCSV


if __name__ == "__main__":
    api_key = toml.load("api_key.toml")["chave_api_dados"]
    leitor = LeitorCSV("cpfs.csv")
    cpfs = leitor.ler()
    print(cpfs)
    for cpf in cpfs:
        consulta = ConsultaAPI(api_key, cpf)
        gravador = GravadorCSV(consulta)
        gravador.gravar()
