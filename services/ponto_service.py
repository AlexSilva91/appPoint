from logging_config import logging
from firebase_config import db
from models.ponto import Ponto

class PontoService:
    @staticmethod
    def bater_ponto(ponto):
        try:
            db.collection('pontos').document(ponto.ponto_id).set({
                'usuarioID': ponto.usuario_id,
                'data': ponto.data,
                'entrada': ponto.entrada,
                'saida_almoco': ponto.saida_almoco,
                'volta_almoco': ponto.volta_almoco,
                'saida': ponto.saida
            })
            PontoService.atualizar_banco_de_horas(ponto)
            logging.info(f"Ponto {ponto.ponto_id} registrado com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao registrar ponto: {e}")

    @staticmethod
    def listar_pontos(usuario_id):
        try:
            pontos_ref = db.collection('pontos').where('usuarioID', '==', usuario_id)
            docs = pontos_ref.stream()

            for doc in docs:
                print(f'{doc.id} => {doc.to_dict()}')
            logging.info("Pontos listados com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao listar pontos: {e}")

    @staticmethod
    def atualizar_banco_de_horas(ponto):
        try:
            usuario_ref = db.collection('usuarios').document(ponto.usuario_id)
            usuario_doc = usuario_ref.get()
            if usuario_doc.exists:
                usuario_data = usuario_doc.to_dict()
                modalidade = usuario_data['modalidade']

                entrada = int(ponto.entrada.split(':')[0])
                saida = int(ponto.saida.split(':')[0])
                saida_almoco = int(ponto.saida_almoco.split(':')[0])
                volta_almoco = int(ponto.volta_almoco.split(':')[0])

                horas_manha = saida_almoco - entrada
                horas_tarde = saida - volta_almoco
                horas_trabalhadas = horas_manha + horas_tarde

                horas_extras = 0
                if modalidade == '12x36':
                    horas_extras = horas_trabalhadas - 12
                elif modalidade == '6x1':
                    horas_extras = horas_trabalhadas - 8

                banco_de_horas_ref = db.collection('banco_de_horas').document(ponto.usuario_id)
                banco_de_horas_doc = banco_de_horas_ref.get()
                if banco_de_horas_doc.exists:
                    banco_de_horas_data = banco_de_horas_doc.to_dict()
                    banco_de_horas_data['total_horas'] += horas_extras
                    banco_de_horas_data['horas_extras'] += max(horas_extras, 0)
                else:
                    banco_de_horas_data = {
                        'total_horas': horas_extras,
                        'horas_extras': max(horas_extras, 0)
                    }

                banco_de_horas_ref.set(banco_de_horas_data)
                logging.info(f"Banco de horas de {ponto.usuario_id} atualizado com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao atualizar banco de horas: {e}")

    @staticmethod
    def calcular_banco_de_horas_total(usuario_id):
        try:
            pontos_ref = db.collection('pontos').where('usuarioID', '==', usuario_id)
            pontos = pontos_ref.stream()

            total_horas = 0
            horas_extras = 0

            for ponto in pontos:
                dados = ponto.to_dict()
                entrada = int(dados['entrada'].split(':')[0])
                saida = int(dados['saida'].split(':')[0])
                saida_almoco = int(dados['saida_almoco'].split(':')[0])
                volta_almoco = int(dados['volta_almoco'].split(':')[0])

                horas_manha = saida_almoco - entrada
                horas_tarde = saida - volta_almoco
                horas_trabalhadas = horas_manha + horas_tarde

                usuario_ref = db.collection('usuarios').document(usuario_id)
                usuario_doc = usuario_ref.get()
                if usuario_doc.exists:
                    usuario_data = usuario_doc.to_dict()
                    modalidade = usuario_data['modalidade']

                    if modalidade == '12x36':
                        horas_extras_ponto = horas_trabalhadas - 12
                    elif modalidade == '6x1':
                        horas_extras_ponto = horas_trabalhadas - 8

                    total_horas += horas_extras_ponto
                    horas_extras += max(horas_extras_ponto, 0)

            banco_de_horas_ref = db.collection('banco_de_horas').document(usuario_id)
            banco_de_horas_data = {
                'total_horas': total_horas,
                'horas_extras': horas_extras
            }
            banco_de_horas_ref.set(banco_de_horas_data)

            logging.info(f"Banco de horas total de {usuario_id} atualizado com sucesso.")
            print(f"Banco de horas total de {usuario_id} atualizado com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao calcular banco de horas total: {e}")
