#Questão 4 de 4 (AULA 6)


#-----------Início das Variáveis Globais ---------
lista_funcionario = []
id_funcionario = 0
#-----------Fim das Variáveis Globais ------------


#-------------------Início da função cadastrar_funcionario(id)-----------------#
def cadastrar_funcionario(id):
  print('-----------------MENU CADASTRAR FUNCIONÁRIO-----------')
  print(f'Codigo do funcionario: {id_funcionario}')
  nome = input('Digite o NOME do funcionário: ') 
  setor = input('Digite o SETOR do funcionário: ')
  salario = float(input('Digite o SALÁRIO do funcionário (R$): '))
  dicionario_funcionario = {'id': id,
                            'nome': nome,
                            'setor': setor,
                            'salario ': salario} #Armazena os dados inseridos pelo usuário.
  lista_funcionario.append(dicionario_funcionario.copy()) #Move o dicionário para a lista_funcionario.
    
  
#-------------------Fim da função cadastrar_funcionario(id)-------------------#




#-------------------Início da função consultar_funcionários()-----------------#
def consultar_funcionario():
    while True:
      opcao_consultar = input('---------------------MENU CONSULTAR FUNCIONÁRIO---------------\n' +
                           '\n Escolha a opção desejada:  \n' +
                           '1 - Consultar todos os funcionários \n' +
                           '2 - Consultar Funcionários por ID  \n' +
                           '3 - Consultar funcionários por SETOR \n' +
                           '4 - Retornar \n' +
                           '>>')
      if opcao_consultar == '1':
          print('Você escolheu opção consultar TODOS os funcionários')
          for funcionario in lista_funcionario: #Variavel para varrer a lista de funcionários, "funcionário" vai varrer toda a lista_funcionario.
            print('-----------------------------------------------------------')
            for key, value in funcionario.items(): #Acessa cada "chave valor", varre todos os conjuntos chave e valor do dicionário_funcionario.
                print('{}: {}'.format(key,value)) #comando de saída de cada "chave valor".
          print('-------------------------------------------------------------')
      elif opcao_consultar == '2':
        print('Você escolheu opção consultar funcionários por ID')
        valor_desejado = int(input('Entre com o ID do funcionário: '))
        for funcionario in lista_funcionario:
            if funcionario['id'] == valor_desejado: #O valor do campo ID desse dicionário é igual o valor desejado.
              print('-----------------------------------------------------------')
              for key, value in funcionario.items():  #Acessa cada "chave valor", varre todos os conjuntos chave e valor do dicionário_funcionario.
                print('{}: {}'.format(key, value))  #comando de saída de cada "chave valor".
      elif opcao_consultar == '3':
        print('Você escolheu opção consultar funcionários por SETOR')
        valor_desejado = (input('Entre com o SETOR do funcionário: '))
        for funcionario in lista_funcionario:
            if funcionario['setor'] == valor_desejado:  # o valor do campo ID desse dicionario é igual o valor desejado.
              print('-----------------------------------------------------------')
              for key, value in funcionario.items():  # Acessa cada "chave valor", varre todos os conjuntos chave e valor do dicionário_funcionario.
                print('{}: {}'.format(key, value))  # comando de saída de cada "chave valor".
            print('-----------------------------------------------------------')
      elif opcao_consultar == '4':
        return  # Sai da função consultar_funcionario e volta para o MAIN.
      else:
        print(' !!!! OPÇÃO INVÁLIDA, tente novamente!!')
      continue #retorna ao inicio do menu / laço.




#------------------Fim da função consultar_funcionários()----------------------#




#-------------------Início da função remover_funcionario()---------------------#
def remover_funcionario():
  print('----------------MENU REMOVER FUNCIONÁRIO-------------')
  valor_desejado = int(input('Entre com o ID do funcionário que deseja remover: ')) 
  for funcionario in lista_funcionario:
    if funcionario['id'] == valor_desejado:
      lista_funcionario.remove(funcionario)
      print('FUNCIONÁRIO REMOVIDO!')
#--------------------Fim da função remover_funcionario()-----------------------#




#-----------------------------Início do Main-----------------------------------#
print('Bem vindo ao Controle de Funcionários da Nataly Rossini ')
print('******************************************************* ')
while True:
    opcao_desejada = input('-------------------------MENU PRINCIPAL----------------\n' +
                           '\n Escolha a opção desejada:  \n' +
                           '1 - Cadastrar Funcionário  \n' +
                           '2 - Consultar Funcionário(s) \n' +
                           '3 - Remover Funcionário  \n' +
                           '4 - Sair \n' +
                           '>>')
    if opcao_desejada == '1':
      id_funcionario = id_funcionario + 1 #Acumulador para gerar números novos.
      cadastrar_funcionario(id_funcionario) #Toda vez que foi solicitada, irá incluir o valor de id.
    elif opcao_desejada == '2':
      consultar_funcionario()
    elif opcao_desejada == '3':
        remover_funcionario()
    elif opcao_desejada == '4':
      break #encerra o laço principal e o programa acaba.
    else:
      print(' !!!! OPÇÃO INVÁLIDA, tente novamente!!')
      continue #Retorna ao início do menu / laço.


#-----------------------------Fim do Main-----------------------------------#
