from pydantic import BaseModel
from typing import Optional


class ValidarDados(BaseModel):
    cpf: str
    nome: str
    nis: Optional[str] = None

    favorecidoDespesas: bool = False
    servidor: bool = False
    beneficiarioDiarias: bool = False
    permissionario: bool = False
    contratado: bool = False
    sancionadoCEIS: bool = False
    sancionadoCNEP: bool = False
    sancionadoCEAF: bool = False
    portadorCPDC: bool = False
    portadorCPGF: bool = False
    favorecidoBolsaFamilia: bool = False
    favorecidoPeti: bool = False
    favorecidoSafra: bool = False
    favorecidoSeguroDefeso: bool = False
    favorecidoBpc: bool = False
    favorecidoTransferencias: bool = False
    favorecidoCPCC: bool = False
    favorecidoCPDC: bool = False
    favorecidoCPGF: bool = False
    participanteLicitacao: bool = False
    servidorInativo: bool = False
    pensionistaOuRepresentanteLegal: bool = False
    instituidorPensao: bool = False
    auxilioEmergencial: bool = False
    favorecidoAuxilioBrasil: bool = False
    favorecidoNovoBolsaFamilia: bool = False
    favorecidoAuxilioReconstrucao: bool = False
