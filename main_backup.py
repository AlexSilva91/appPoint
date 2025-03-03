from logging_config import logging
from models.usuario import Usuario
from models.ponto import Ponto
from models.banco__de_horas import BancoDeHoras
from services.usuario_service import UsuarioService
from services.ponto_service import PontoService
from services.banco_de_horas_service import BancoDeHorasService

if __name__ == '__main__':
    # --- Testar Funções do Administrador ---
    
    # Simulando um usuário administrador
    admin = True

    # Cadastrar um novo usuário
    novo_usuario = Usuario('usuarioID2', 'Maria', 'maria@example.com', 'Designer', False, '6x1', '08:00', '18:00')
    UsuarioService.cadastrar_usuario(novo_usuario, admin)

    # Listar todos os usuários
    UsuarioService.listar_usuarios(admin)

    # Editar um usuário existente
    novo_usuario.nome = 'Maria Silva'
    UsuarioService.editar_usuario(novo_usuario, admin)

    # Listar todos os usuários novamente para verificar a edição
    UsuarioService.listar_usuarios(admin)

    # Remover um usuário
    UsuarioService.remover_usuario('usuarioID2', admin)

    # Listar todos os usuários novamente para verificar a remoção
    UsuarioService.listar_usuarios(admin)

    # --- Testar Funções do Usuário Comum ---
    
    # Simulando um usuário comum
    admin = False

    # Registrando ponto para um usuário comum
    ponto = Ponto('pontoID2', 'usuarioID1', '2025-03-03', '08:00', '12:00', '14:00', '20:00')
    PontoService.bater_ponto(ponto)

    # Listar pontos batidos pelo usuário comum
    PontoService.listar_pontos('usuarioID1')

    # Visualizar banco de horas do usuário comum
    BancoDeHorasService.visualizar_banco_de_horas('usuarioID1')

    # Tentar listar usuários (deve falhar)
    UsuarioService.listar_usuarios(admin)
