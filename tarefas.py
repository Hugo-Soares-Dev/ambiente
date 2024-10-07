
def add_tarefa(tarefas):
    descricao = input('descreva a terfa: ').strip().upper()
    prioridade = input('digite a prioridade: ')
    categoria = input('qual categoria: ')
    status = 'pendente'
    tarefa = {
        'descricao': descricao,
        'prioridade': prioridade, 
        'categoria': categoria,
        'status': status 
     }
    tarefas.append(tarefa)
    print('tarefa adicionada!')

def marcar (tarefas, descricao):
    for tarefa in tarefas:
        if tarefa['descricao'] == descricao:
          tarefa['status'] = 'concluido'
          print(f'a terefa {descricao} foi concluida')
          return
    print('tarefa nao encontrada')
      

def lista_tarefas(tarefas):
    if not tarefas:
        print('lista de tarefas vazia')
        return
    for tarefa in tarefas:
        print(f"tarefa: \033[7;33m{tarefa['descricao']}\033[m\nprioridade: {tarefa['prioridade']}\ncategoria: {tarefa['categoria']}\nstatus: {tarefa['status']}\n{'=='*20}")

def remover_tarefa(tarefas):
    descricao = input('qua a descriçao da tarefa? ').strip().upper()
    for tarefa in tarefas:
        if tarefa['descricao'] == descricao:
            tarefas.remove(tarefa)
            print('tarefa removida com sucesso!')
            return
    print('tarefa nao encontrada')            

def menu():
    print('[1] para ver lista de tarefas\n[2] para adicionar uma nova terefa\n[3] para remover uma tarefa\n[4] para filtrar por prioridade\n[5] para filtrar por categoria\n[6] para marcar uma tarefa como concluida\n[7] para sair')
    return input('escolha uma opçao: ')

def prioridades(tarefas, filtro, valor):
    filtradas = [tarefa for tarefa in tarefas if tarefa[filtro] == valor]
    if not filtradas:
        print('nenhuma tarefa com essa prioridade encontrada ')
        return
    for tarefa in filtradas:
     print(f"tarefa: \033[7;33m{tarefa['descricao']}\033[m\nprioridade: {tarefa['prioridade']}\ncategoria: {tarefa['categoria']}\nstatus: {tarefa['status']}\n{'=='*20}")

tarefas = []

while True:
    resposta = menu()
    match resposta:
        case '1':
            lista_tarefas(tarefas)
        case '2':
            add_tarefa(tarefas)
        case '3':
            remover_tarefa(tarefas)
        case '4':
            prioridade = input('qual prioridade? (baixa, media ou atlta): ') 
            prioridades(tarefas, 'prioridade', prioridade)  
        case '5':
            categoria = input('deseja filtrar por qual categoria? ')
            prioridades(tarefas, 'categoria', categoria)
        case '6':
            descricao = input('qual tarefa gostaria de comcluir? ').strip().upper()
            marcar(tarefas, descricao)
        case '7':
            break    
        case _:
            print('opçao invalida!')
                    

