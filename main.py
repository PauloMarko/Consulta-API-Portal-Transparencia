import logging
import time
from ControladorAplicacao import ControladorAplicacao


def log_init():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        filename="logfile.log",
    )
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)

if __name__ == "__main__":
    log_init()
    api_key = ControladorAplicacao.chaveApi()
    app = ControladorAplicacao(api_key, f"cpfs.csv", f"dados.csv")
    start_time = time.perf_counter()
    app.executar()
    logger = logging.getLogger(__name__)
    logger.info("Programa finalizado com sucesso!")
