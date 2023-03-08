import PySimpleGUI as sg
import mysql.connector

class TelaPython:
    def __init__(self):
        # Conexão com o banco de dados
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="felpy_sistem"
        )
        self.cursor = self.conn.cursor()

        # Layout da janela de login
        layout_login = [
            [sg.Text('Login:', size=(5, 1), background_color='black', text_color='gold'), sg.Input(key='usuario', font=('Arial', 12), background_color='white', text_color='black')],
            [sg.Text('Senha:', size=(5, 1), background_color='black', text_color='gold'), sg.Input(key='senha', password_char='*', font=('Arial', 12), background_color='white', text_color='black')],
            [sg.Button('Login', button_color=('black', 'gold'), font=('Arial', 12)), sg.Button('Cadastrar', button_color=('black', 'gold'), font=('Arial', 12))]
        ]
        self.janela_login = sg.Window('Felpy_sistem', background_color='black').layout(layout_login)

    def criar_usuario(self):
        # Layout da janela de criar usuário
        layout_criar = [
            [sg.Text('Nome:', size=(5, 1), background_color='black', text_color='gold'), sg.Input(key='Nome', font=('Arial', 12), background_color='white', text_color='black')],
            [sg.Text('Idade:', size=(5, 1), background_color='black', text_color='gold'), sg.Input(key='Idade', font=('Arial', 12), background_color='white', text_color='black')],
            [sg.Text('Email:', size=(5, 1), background_color='black', text_color='gold'), sg.Input(key='Email', font=('Arial', 12), background_color='white', text_color='black')],
            [sg.Text('Login:', size=(5, 1), background_color='black', text_color='gold'), sg.Input(key='usuario', font=('Arial', 12), background_color='white', text_color='black')],
            [sg.Text('Senha:', size=(5, 1), background_color='black', text_color='gold'), sg.Input(key='senha', password_char='*', font=('Arial', 12), background_color='white', text_color='black')],
            [sg.Button('Criar', button_color=('black', 'gold'), font=('Arial', 12))]
        ]

        janela_criar = sg.Window('Criar Usuário', background_color='black').layout(layout_criar)
        button, values = janela_criar.Read()

        if values['Nome'] and values['Idade'] and values['Email'] and values['usuario'] and values['senha']:


            # Verificar se o nome foi preenchido corretamente
            try:
                str(values['Nome'])
            except ValueError:
                sg.Popup('O nome precisa ser preenchido somente com caracteres')

            # Verificar se a idade é um número
            try:
                int(values['Idade'])
            except ValueError:
                sg.Popup('A idade precisa ser um número')


            # Verificar se o email é válido
            if '@' not in values['Email']:
                sg.Popup('E-mail inválido')

            # Inserção de dados na tabela pessoas
            query = "INSERT INTO pessoas (Nome, Idade, Email, usuario, senha) VALUES (%s, %s, %s, %s, %s)"
            data = (values['Nome'], values['Idade'], values['Email'], values['usuario'], values['senha'])
            self.cursor.execute(query, data)
            self.conn.commit()
            sg.Popup('Login criado com sucesso')
            janela_criar.Close()


    def iniciar(self):
        while True:
            button, values = self.janela_login.Read()
            if button == sg.WIN_CLOSED:
                break

            if button == 'Login':
                query = "SELECT * FROM pessoas WHERE usuario=%s AND senha=%s"
                data = (values['usuario'], values['senha'])

                if not values['usuario'] or not values['senha']:
                    sg.Popup('Você deve inserir LOGIN e SENHA!')
                    continue

                self.cursor.execute(query, data)
                result = self.cursor.fetchone()

                if result:
                    sg.Popup('Login realizado com sucesso')
                    self.janela_login.Close()
                    break
                else:
                    sg.Popup('login ou senha inválidos')

            elif button == 'Cadastrar':
                self.criar_usuario()



tela = TelaPython()
tela.iniciar()
