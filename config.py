import firebase_admin
from firebase_admin import credentials, firestore

# Carregue as credenciais do Firebase
cred = credentials.Certificate("/home/alex/projetos_python/appPointAuth/apppoint-e5c3e-firebase-adminsdk-fbsvc-7d97b2803f.json")

# Inicialize o app do Firebase
firebase_admin.initialize_app(cred)

# Obtenha a instância do Firestore
db = firestore.client()

# Função para adicionar um usuário
def adicionar_usuario(usuario_id, nome, email):
    doc_ref = db.collection('usuarios').document(usuario_id)
    doc_ref.set({
        'nome': nome,
        'email': email
    })
    print(f'Usuário {nome} adicionado com sucesso.')

# Função para ler os usuários
def ler_usuarios():
    usuarios_ref = db.collection('usuarios')
    docs = usuarios_ref.stream()

    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

# Função para atualizar o email de um usuário
def atualizar_email(usuario_id, novo_email):
    doc_ref = db.collection('usuarios').document(usuario_id)
    doc_ref.update({'email': novo_email})
    print(f'Email do usuário {usuario_id} atualizado para {novo_email}.')

# Função para excluir um usuário
def excluir_usuario(usuario_id):
    doc_ref = db.collection('usuarios').document(usuario_id)
    doc_ref.delete()
    print(f'Usuário {usuario_id} excluído com sucesso.')

# Exemplo de uso das funções
if __name__ == '__main__':
    # Adicionar um usuário
    adicionar_usuario('usuarioID1', 'João', 'joao@example.com')

    # Ler todos os usuários
    ler_usuarios()

    # Atualizar o email de um usuário
    atualizar_email('usuarioID1', 'novoemail@example.com')

    # Excluir um usuário
    #excluir_usuario('usuarioID1')
