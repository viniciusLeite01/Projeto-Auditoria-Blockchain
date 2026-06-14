import subprocess
from datetime import datetime
import os

RELATORIOS = "auditoria/relatorios"


def gerar_relatorio():

    os.makedirs(RELATORIOS, exist_ok=True)

    nome = datetime.now().strftime(
        "auditoria_%Y%m%d_%H%M%S.txt"
    )

    caminho = os.path.join(
        RELATORIOS,
        nome
    )

    comandos = {
        "USUARIOS CONECTADOS": "who",
        "HISTORICO DE LOGIN": "last",
        "PORTAS E SERVICOS": "ss -tulpn",
        "INTERFACES DE REDE": "ip a"
    }

    with open(caminho, "w") as rel:

        rel.write(
            "RELATORIO DE AUDITORIA\n"
        )

        rel.write(
            f"Gerado em: {datetime.now()}\n\n"
        )

        for titulo, cmd in comandos.items():

            rel.write(
                f"\n{'='*50}\n"
            )

            rel.write(
                f"{titulo}\n"
            )

            rel.write(
                f"{'='*50}\n"
            )

            resultado = subprocess.getoutput(cmd)

            rel.write(resultado)

            rel.write("\n")

    return caminho
