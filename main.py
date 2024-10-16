tarefas = []

while True:
    print("\n")
    print("Bem vindo a lista de tarefa: ")
    print("1 - para inserir tarefa.")
    print("2 - para sair.")

    opcao = input("Digite o numero da opção desejada: ")

    match opcao:
        case "1":
            nova_tarefa = input("Informe a tarefa: ").capitalize()
            tarefas.append(nova_tarefa)
            print("\n")
            print("Esses sãos as tarefas que voce digitou:")
            for tarefa in tarefas:
                print(f"- {tarefa}.")
        case "2":
            break
        case _: 
            print('Opção inválida.')