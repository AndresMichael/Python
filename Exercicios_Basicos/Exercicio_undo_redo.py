"""
SOLUÇÃO DO Michael
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""


def show_op():
    print()
    print('Tarefas:')
    print(faz_lista)
    print()


def add_faca(faca, faz_lista):
    faz_lista.append(faca)


def faca_redo(faz_lista, desfaz_lista):
    if not desfaz_lista:
        print('Nada a Refazer')
        return
    k = desfaz_lista.pop()
    faz_lista.append(k)


def faca_undo(faz_lista, desfaz_lista):
    if not faz_lista:
        print('nada a desfazer ')
        return
    k = faz_lista.pop()
    desfaz_lista.append(k)


op = True
faz_lista = []
desfaz_lista = []

while op:
    faca = input('###################################################################################'
                 '\ndigite uma tarefa, desfazer(undo), refazer(redo),mostrar(ls) e sair: ')
    if faca == 'sair':
        op = False
    elif faca == 'mostrar' or faca == 'ls':
        show_op()
        continue
    elif faca == 'desfazer' or faca == 'undo':
        faca_undo(faz_lista, desfaz_lista)
        continue
    elif faca == 'refazer' or faca == 'redo':
        faca_redo(faz_lista, desfaz_lista)
        continue

    add_faca(faca, faz_lista)
