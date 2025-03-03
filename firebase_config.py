import firebase_admin
from firebase_admin import credentials, firestore

# Carregue as credenciais do Firebasecred = credentials.Certificate("caminho/para/seu/arquivo-de-credenciais.json")
cred = credentials.Certificate("/home/alex/projetos_python/appPointAuth/apppoint-e5c3e-firebase-adminsdk-fbsvc-7d97b2803f.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
