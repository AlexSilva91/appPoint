from logging_config import logging
from firebase_config import db  # Importa a configuração do Firebase
from models.usuario import Usuario
from models.ponto import Ponto
from models.banco__de_horas import BancoDeHoras
from services.usuario_service import UsuarioService
from services.ponto_service import PontoService
from services.banco_de_horas_service import BancoDeHorasService

def exibir_usuarios(usuarios):
    print("\n--- Lista de Usuários ---")
    for usuario in usuarios:
        dados = usuario.to_dict()
        print(f"ID: {usuario.id}")
        print(f"Nome: {dados.get('nome', 'N/A')}")
        print(f"Email: {dados.get('email', 'N/A')}")
        print(f"Cargo: {dados.get('cargo', 'N/A')}")
        print(f"Modalidade: {dados.get('modalidade', 'N/A')}")
        print(f"Horário de Entrada: {dados.get('horario_entrada', 'N/A')}")
        print(f"Horário de Saída: {dados.get('horario_saida', 'N/A')}")
        print(f"Administrador: {dados.get('administrador', 'N/A')}")
        print(f"Status: {dados.get('status', 'N/A')}\n")

def exibir_pontos(pontos):
    print("\n--- Lista de Pontos ---")
    for ponto in pontos:
        dados = ponto.to_dict()
        print(f"ID: {ponto.id}")
        print(f"Data: {dados.get('data', 'N/A')}")
        print(f"Entrada: {dados.get('entrada', 'N/A')}")
        print(f"Saída para Almoço: {dados.get('saida_almoco', 'N/A')}")
        print(f"Volta do Almoço: {dados.get('volta_almoco', 'N/A')}")
        print(f"Saída: {dados.get('saida', 'N/A')}\n")

def exibir_banco_de_horas(banco_de_horas):
    print("\n--- Banco de Horas ---")
    if banco_de_horas:
        print(f"Total de Horas: {banco_de_horas.get('total_horas', 'N/A')}")
        print(f"Horas Extras: {banco_de_horas.get('horas_extras', 'N/A')}\n")
    else:
        print("Banco de horas não encontrado.\n")

if __name__ == '__main__':
    # --- Testar Funções do Administrador ---
    
    # Simulando um usuário administrador
    admin = True

    # Cadastrar um novo usuário
    novo_usuario = Usuario('usuarioID1', 'Maria', 'maria@example.com', 'Designer', False, '6x1', '08:00', '18:00')
    UsuarioService.cadastrar_usuario(novo_usuario, admin)

    # Listar todos os usuários
    usuarios_ref = db.collection('usuarios')

    # Editar um usuário existente
    novo_usuario.nome = 'Maria Silva'
    UsuarioService.editar_usuario(novo_usuario, admin)

    # --- Testar Funções do Usuário Comum ---
    
    # Simulando um usuário comum
    admin = False

    # Cadastrar um usuário comum
    usuario_comum = Usuario('usuarioID2', 'João', 'joao@example.com', 'Desenvolvedor', False, '6x1', '08:00', '18:00')
    UsuarioService.cadastrar_usuario(usuario_comum, True)  # Cadastrado por um administrador

    # Listar todos os usuários
    usuarios = usuarios_ref.stream()
    exibir_usuarios(usuarios)

    # Registrando ponto para um usuário comum
    ponto = Ponto('pontoID2', 'usuarioID2', '2025-03-03', '08:00', '12:00', '14:00', '20:00')
    ponto2 = Ponto('pontoID3', 'usuarioID2', '2025-03-03', '08:00', '12:00', '14:00', '20:00')
    PontoService.bater_ponto(ponto)
    PontoService.bater_ponto(ponto2)

    # Listar pontos batidos pelo usuário comum
    pontos_ref = db.collection('pontos').where('usuarioID', '==', 'usuarioID2')
    pontos = pontos_ref.stream()
    exibir_pontos(pontos)

    # Visualizar banco de horas do usuário comum
    banco_de_horas_ref = db.collection('banco_de_horas').document('usuarioID2')

    # Calcular banco de horas total e atualizar
    PontoService.calcular_banco_de_horas_total('usuarioID2')

    # Visualizar banco de horas atualizado do usuário comum
    banco_de_horas_doc = banco_de_horas_ref.get()
    exibir_banco_de_horas(banco_de_horas_doc.to_dict())

    # Tentar listar usuários (deve falhar)
    UsuarioService.listar_usuarios(admin)
