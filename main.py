from PySimpleGUI import PySimpleGUI as sg
from Pessoa import Pessoa

pessoa = Pessoa()
sg.theme('Dark Green 5')

layout = [
    [sg.Text(5*'\t'),sg.Text('BEM VINDO AO SISTEMA DE CADASTRO!', font='Courier 15', text_color='White Smoke')],
    [sg.Text('\n\n')],
    [sg.Text('Listar Contatos:'),sg.Button('listar contatos', button_color='Green')],
    [sg.Text('\n\n\n\n')],
    [sg.Button('Fechar', button_color='Gray')],
]


janela = sg.Window('Sistema de Cadastro', layout,size=(1000,700))

while True:
    eventos, valores = janela.read()
    if eventos in ('4 quit', sg.WIN_CLOSED,'Fechar'):
        break
    elif eventos == 'listar contatos':
        data = pessoa.todosUsuarios()
        sg.popup_scrolled(data, title="Lista de usuários no sistema!")


    janela.Refresh()

janela.close()
