from logging_config import logging
from firebase_config import db
from models.banco__de_horas import BancoDeHoras

class BancoDeHorasService:
    @staticmethod
    def definir_banco_de_horas(banco_de_horas):
        try:
            db.collection('banco_de_horas').document(banco_de_horas.usuario_id).set({
                'total_horas': banco_de_horas.total_horas,
                'horas_extras': banco_de_horas.horas_extras
            })
            logging.info(f"Banco de horas de {banco_de_horas.usuario_id} definido com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao definir banco de horas: {e}")

    @staticmethod
    def visualizar_banco_de_horas(usuario_id):
        try:
            doc_ref = db.collection('banco_de_horas').document(usuario_id)
            doc = doc_ref.get()
            if doc.exists:
                print(doc.to_dict())
                logging.info(f"Banco de horas de {usuario_id} visualizado com sucesso.")
            else:
                print('Banco de horas não encontrado.')
                logging.warning(f"Banco de horas de {usuario_id} não encontrado.")
        except Exception as e:
            logging.error(f"Erro ao visualizar banco de horas: {e}")
