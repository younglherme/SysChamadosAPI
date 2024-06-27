import PySimpleGUI as sg
import requests

# URL da API
API_URL = 'http://localhost:5000'  # Substitua pelo URL real da sua API

# Função para exibir a tela de cadastro
def tela_cadastro():
    layout_cadastro = [
        [sg.Text('Nome')],
        [sg.Input(key='-NOME-')],
        [sg.Text('Email')],
        [sg.Input(key='-EMAIL-')],
        [sg.Text('Telefone')],
        [sg.Input(key='-TELEFONE-')],
        [sg.Text('CPF')],
        [sg.Input(key='-CPF-')],
        [sg.Text('RG')],
        [sg.Input(key='-RG-')],
        [sg.Button('Salvar'), sg.Button('Cancelar')]
    ]

    janela_cadastro = sg.Window('Cadastro', layout_cadastro)

    while True:
        event, values = janela_cadastro.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
        elif event == 'Salvar':
            # Coleta dos dados de cadastro
            nome = values['-NOME-']
            email = values['-EMAIL-']
            telefone = values['-TELEFONE-']
            cpf = values['-CPF-']
            rg = values['-RG-']
            
            # Dados para enviar à API
            dados_cadastro = {
                'nome': nome,
                'email': email,
                'telefone': telefone,
                'cpf': cpf,
                'rg': rg
            }

            # Chamada à API para cadastro
            response = requests.post(f'{API_URL}/cadastro', json=dados_cadastro)
            
            if response.status_code == 200:
                sg.popup('Cadastro realizado com sucesso!')
                break
            else:
                sg.popup('Erro no cadastro. Tente novamente.')

    janela_cadastro.close()

# Layout da janela de login
layout_login = [
    [sg.Text('Login')],
    [sg.Input(key='-LOGIN-')],
    [sg.Text('Senha')],
    [sg.Input(key='-SENHA-', password_char='*')],
    [sg.Button('Entrar'), sg.Button('Cadastro')]
]

# Criação da janela de login
window_login = sg.Window('Tela de Login', layout_login)

# Loop de eventos da janela de login
while True:
    event, values = window_login.read()
    if event == sg.WINDOW_CLOSED:  # Fechar a janela
        break
    elif event == 'Entrar':
        # Coleta dos dados de login
        login = values['-LOGIN-']
        senha = values['-SENHA-']
        
        # Dados para enviar à API
        dados_login = {
            'login': login,
            'senha': senha
        }

        # Chamada à API para autenticação
        response = requests.post(f'{API_URL}/login', json=dados_login)
        
        if response.status_code == 200:
            sg.popup('Login realizado com sucesso!')
            # Aqui você pode adicionar lógica adicional para quando o login for bem-sucedido
        else:
            sg.popup('Erro no login. Verifique suas credenciais e tente novamente.')
    elif event == 'Cadastro':
        window_login.hide()  # Esconder a janela de login
        tela_cadastro()
        window_login.un_hide()  # Mostrar novamente a janela de login

# Fechar a janela de login
window_login.close()
