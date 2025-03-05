import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import sys
import os

# Adicionar o diretório `appPoint` ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Ajustar o caminho para os serviços
from services.usuario_service import UsuarioService
from services.ponto_service import PontoService
from services.banco_de_horas_service import BancoDeHorasService

class LoginScreen(Screen):
    pass

class UserScreen(Screen):
    pass

class AdminScreen(Screen):
    pass

class RegistrarPontoScreen(Screen):
    pass

class VisualizarPontosScreen(Screen):
    pass

class VisualizarBancoHorasScreen(Screen):
    pass

class CadastrarUsuarioScreen(Screen):
    pass

class EditarUsuarioScreen(Screen):
    pass

class RemoverUsuarioScreen(Screen):
    pass

class VisualizarTodosUsuariosScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    
    def build(self):
        print("Construindo a aplicação...")  # Mensagem de depuração
        self.load_kv('login_screen.kv')
        self.load_kv('user_screen.kv')
        self.load_kv('admin_screen.kv')
        self.load_kv('registrar_ponto_screen.kv')
        self.load_kv('visualizar_pontos_screen.kv')
        self.load_kv('visualizar_banco_horas_screen.kv')
        self.load_kv('cadastrar_usuario_screen.kv')
        self.load_kv('editar_usuario_screen.kv')
        self.load_kv('remover_usuario_screen.kv')
        self.load_kv('visualizar_todos_usuarios_screen.kv')
        
        self.screen_manager = MyScreenManager()
        self.screen_manager.add_widget(LoginScreen(name='login'))
        self.screen_manager.add_widget(UserScreen(name='user_screen'))
        self.screen_manager.add_widget(AdminScreen(name='admin_screen'))
        self.screen_manager.add_widget(RegistrarPontoScreen(name='registrar_ponto'))
        self.screen_manager.add_widget(VisualizarPontosScreen(name='visualizar_pontos'))
        self.screen_manager.add_widget(VisualizarBancoHorasScreen(name='visualizar_banco_horas'))
        self.screen_manager.add_widget(CadastrarUsuarioScreen(name='cadastrar_usuario'))
        self.screen_manager.add_widget(EditarUsuarioScreen(name='editar_usuario'))
        self.screen_manager.add_widget(RemoverUsuarioScreen(name='remover_usuario'))
        self.screen_manager.add_widget(VisualizarTodosUsuariosScreen(name='visualizar_todos_usuarios'))

        return self.screen_manager

    def login(self, email, password):
        print(f"Login: {email}, {password}")  # Mensagem de depuração
        # Verifique as credenciais e redirecione para a tela correta
        if email == 'admin@example.com':
            self.screen_manager.current = 'admin_screen'
        else:
            self.screen_manager.current = 'user_screen'

    def registrar_ponto(self):
        print("Registrando ponto...")  # Mensagem de depuração
        pass

    def visualizar_pontos(self):
        print("Visualizando pontos...")  # Mensagem de depuração
        pass

    def visualizar_banco_de_horas(self):
        print("Visualizando banco de horas...")  # Mensagem de depuração
        pass

    def cadastrar_usuario(self):
        print("Cadastrando usuário...")  # Mensagem de depuração
        pass

    def editar_usuario(self):
        print("Editando usuário...")  # Mensagem de depuração
        pass

    def remover_usuario(self):
        print("Removendo usuário...")  # Mensagem de depuração
        pass

    def visualizar_todos_usuarios(self):
        print("Visualizando todos os usuários...")  # Mensagem de depuração
        pass

    def logout(self):
        print("Saindo...")  # Mensagem de depuração
        self.screen_manager.current = 'login'

if __name__ == '__main__':
    MyApp().run()
