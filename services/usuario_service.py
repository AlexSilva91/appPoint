from logging_config import logging
from firebase_config import db
from models.usuario import Usuario

class UsuarioService:
    @staticmethod
    def cadastrar_usuario(usuario, admin):
        if not admin:
            logging.error("Permissão negada: Apenas administradores podem cadastrar usuários.")
            return
        try:
            db.collection('usuarios').document(usuario.usuario_id).set({
                'nome': usuario.nome,
                'email': usuario.email,
                'cargo': usuario.cargo,
                'administrador': usuario.administrador,
                'modalidade': usuario.modalidade,
                'horario_entrada': usuario.horario_entrada,
                'horario_saida': usuario.horario_saida,
                'status': 'ativo'
            })
            logging.info(f"Usuário {usuario.usuario_id} cadastrado com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao cadastrar usuário: {e}")

    @staticmethod
    def listar_usuarios(admin):
        if not admin:
            logging.error("Permissão negada: Apenas administradores podem listar usuários.")
            return
        try:
            usuarios_ref = db.collection('usuarios')
            docs = usuarios_ref.stream()

            for doc in docs:
                print(f'{doc.id} => {doc.to_dict()}')
            logging.info("Usuários listados com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao listar usuários: {e}")

    @staticmethod
    def editar_usuario(usuario, admin):
        if not admin:
            logging.error("Permissão negada: Apenas administradores podem editar usuários.")
            return
        try:
            db.collection('usuarios').document(usuario.usuario_id).update({
                'nome': usuario.nome,
                'email': usuario.email,
                'cargo': usuario.cargo,
                'administrador': usuario.administrador,
                'modalidade': usuario.modalidade,
                'horario_entrada': usuario.horario_entrada,
                'horario_saida': usuario.horario_saida,
                'status': 'ativo'
            })
            logging.info(f"Usuário {usuario.usuario_id} editado com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao editar usuário: {e}")

    @staticmethod
    def remover_usuario(usuario_id, admin):
        if not admin:
            logging.error("Permissão negada: Apenas administradores podem remover usuários.")
            return
        try:
            db.collection('usuarios').document(usuario_id).delete()
            logging.info(f"Usuário {usuario_id} removido com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao remover usuário: {e}")
