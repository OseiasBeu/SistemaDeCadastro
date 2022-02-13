from PySimpleGUI import PySimpleGUI as sg
from Pessoa import Pessoa

pessoa = Pessoa()
sg.theme('Dark Green 5')

layout = [
    [sg.Text(5*'\t'),sg.Text('BEM VINDO AO SISTEMA DE CADASTRO!', font='Courier 15', text_color='White Smoke')],

    [sg.Text('\n\n')],
    [sg.Text('EXIBIR CONTATOS')],
    [sg.Text('Listar Contatos:'),sg.Button('listar contatos', button_color='Green')],
    [sg.Text('\n')],
    [sg.Text('Busca por Nome:'),sg.Input(key='nome',size=(20,0)),sg.Button('buscar por nome', button_color='Green')],
    [sg.Text('Busca por ID:'),sg.Input(key='id',size=(20,0)),sg.Button('buscar por id', button_color='Green')],

    [sg.Text('\n\n')],
    [sg.Text('INSERIR CONTATOS')],
    [sg.Text('Inserir Contato:')],
    [sg.Text('Nome:'),sg.Input(key='nome_in',size=(20,0))],
    [sg.Text('Email:'),sg.Input(key='email_in',size=(20,0))],
    [sg.Button('Inserir', button_color='Green')],
    [sg.Text('\n')],
    [sg.Text("Inserir em lote"), sg.Input(key='procurar arquivo'), sg.FileBrowse(),sg.Button('Inserir Lote', button_color='Green')],

    [sg.Text('\n\n')],
    [sg.Text('REMOVER CONTATOS')],
    [sg.Text('Remover por Nome:'),sg.Input(key='nome_rem',size=(20,0)),sg.Button('remover por nome', button_color='Red')],
    [sg.Text('Remover por ID:'),sg.Input(key='id_rem',size=(20,0)),sg.Button('remover por id', button_color='Red')],

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

    elif eventos == 'buscar por nome':
        data = pessoa.buscaPessoaPorNome(valores['nome'])
        janela['nome'].update('')
        if len(data)  == 0:
            sg.Popup('Registro não encontrado!')
        else:
            sg.Popup(data)

    elif eventos == 'buscar por id':
        data = pessoa.buscaPessoaPorId(valores['id'])
        janela['id'].update('')
        if len(data)  == 0:
            sg.Popup('Registro não encontrado!')
        else:
            sg.Popup(data)
    elif eventos == 'Inserir':
        data = pessoa.inserirPessoa(valores['nome_in'],valores['email_in'])
        janela['nome_in'].update('')
        janela['email_in'].update('')
        sg.Popup('Registro Inserido com sucesso!')
    elif eventos == 'Inserir Lote':
        caminho = valores['procurar arquivo']
        data= pessoa.inserirLote(caminho)
        janela['procurar arquivo'].update('')
        sg.Popup('Registros Inseridos com sucesso!')
    elif eventos == 'remover por nome':
        # print(valores['nome_rem'])
        data = pessoa.removeUsuarioPorNome(valores['nome_rem'])
        janela['nome_rem'].update('')
        sg.Popup('Registros Apagado com Sucesso!')
    elif eventos == 'remover por id':
        # print(valores['id_rem'])
        data = pessoa.removeUsuarioPorNome(valores['id_rem'])
        janela['id_rem'].update('')
        sg.Popup('Registros Apagado com Sucesso!')




    janela.Refresh()

janela.close()
