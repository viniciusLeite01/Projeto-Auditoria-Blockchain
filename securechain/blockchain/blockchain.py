import hashlib
import json
import os
from datetime import datetime

ARQUIVO_CHAIN = "blockchain/chain.json"


class Blockchain:

    def __init__(self):
        self.chain = []
        self.carregar()

        if len(self.chain) == 0:
            self.criar_bloco_genesis()

    def calcular_hash(self, bloco):
        conteudo = json.dumps(bloco, sort_keys=True)
        return hashlib.sha256(conteudo.encode()).hexdigest()

    def criar_bloco_genesis(self):

        bloco = {
            "id": 0,
            "timestamp": datetime.now().isoformat(),
            "evento": "Genesis Block",
            "hash_anterior": "0"
        }

        bloco["hash_atual"] = self.calcular_hash(bloco)

        self.chain.append(bloco)
        self.salvar()

    def adicionar_bloco(self, evento):

        ultimo = self.chain[-1]

        bloco = {
            "id": len(self.chain),
            "timestamp": datetime.now().isoformat(),
            "evento": evento,
            "hash_anterior": ultimo["hash_atual"]
        }

        bloco["hash_atual"] = self.calcular_hash(bloco)

        self.chain.append(bloco)

        self.salvar()

    def salvar(self):

        with open(ARQUIVO_CHAIN, "w") as arquivo:
            json.dump(self.chain, arquivo, indent=4)

    def carregar(self):

        if os.path.exists(ARQUIVO_CHAIN):

            with open(ARQUIVO_CHAIN, "r") as arquivo:
                self.chain = json.load(arquivo)

    def validar(self):

       if len(self.chain) <= 1:
           return True, "Blockchain válida"

       for i in range(1, len(self.chain)):

           atual = self.chain[i]
           anterior = self.chain[i - 1]

           hash_calculado = self.calcular_hash({
               "id": atual["id"],
               "timestamp": atual["timestamp"],
               "evento": atual["evento"],
               "hash_anterior": atual["hash_anterior"]
           })

           if hash_calculado != atual["hash_atual"]:

               return (
                   False,
                   f"Bloco {atual['id']} adulterado (hash inválido)"
               )

           if atual["hash_anterior"] != anterior["hash_atual"]:

               return (
                   False,
                   f"Bloco {atual['id']} com quebra de encadeamento"
               )

       return True, "Blockchain íntegra"
