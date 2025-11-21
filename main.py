from ControladorAplicacao import ControladorAplicacao

if __name__ == "__main__":
    api_key = ControladorAplicacao.chaveApi()
    app = ControladorAplicacao(api_key, "cpfs.csv", "dados-cpfs.csv")
    app.executar()