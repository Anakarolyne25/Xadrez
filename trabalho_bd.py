import mysql.connector
def conectar():
  conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nathalina",
    database="xadrez"
  )
  return conexao


def cadastro_jogadores():
  conexao = conectar()
  nome = input ('Digite o nome do Jogador:')
  meucursor = conexao.cursor ()
  sql = "INSERT INTO Jogadores (nome) Values (%s)"
  valor= (nome,)

  meucursor . execute (sql, valor)
  print(meucursor.rowcount, "arquivo(s) inseridos")
  conexao.commit()
  meucursor.close()
  conexao.close()


def listar_jogadores():
  conexao = conectar()
  print(conexao)
  
  meucursor = conexao.cursor()
  sql= "SELECT * FROM Jogadores"
  meucursor.execute(sql)

  myresult = meucursor.fetchall()
    
  print('{:^10} | {:^10}'.format('Id', 'Nome'))
  for id, nome in myresult:
    print('{:^10} | {:^10}'.format(id, nome))
  meucursor.close()
  conexao.close()


def listar_partidas():
    conexao = conectar()
    print(conexao)
  
    meucursor = conexao.cursor()
    sql= "SELECT * FROM partidas"
    meucursor.execute(sql)

    myresult = meucursor.fetchall()
    
    print('{:^10} | {:^10} | {:^10}'.format('Id', 'nome', 'data'))
    for id, nome, data in myresult:
      print('{:^10} | {:^10} | {:^10}'.format(id, nome, str(data)))

    meucursor.close()
    conexao.close()


def alterar_jogadores():
  conexao = conectar()
  listar_jogadores()
  nome = input('digite o nome do novo jogador: ')
  id = int(input('Qual o id que você deseja modificar? '))

  meucursor = conexao.cursor()

  sql = "UPDATE jogadores SET nome = %s WHERE id = %s"
  valor = (nome, id)
    
  meucursor.execute(sql, valor) 
  conexao.commit() 
    
  print(meucursor.rowcount, "detalhes inseridos") 
  meucursor.close() 
  conexao.close()


def alterar_partidas():
  listar_partidas()
  conexao = conectar()
  
  id = int(input('Qual o id que você deseja modificar? '))
  data = input('digite a nova data da partida: ')

  meucursor = conexao.cursor()

  sql = "UPDATE partidas SET id = %s WHERE data = %s"
  valor = (id, data)
    
  meucursor.execute(sql, valor) 
  conexao.commit() 
    
  print(meucursor.rowcount, "Partida Alterada!") 
  meucursor.close() 
  conexao.close()


def apagar_jogadores():
    listar_jogadores()
    id = int(input('Selecione o id do jogador que deseja apagar: '))
    print("\n O jogador com o id  {} foi apagado!\n".format(id))
    
    conexao = conectar()

    meucursor = conexao.cursor()

    sql = "DELETE FROM jogadores WHERE id = %s"
    valor = (id,)

    meucursor.execute(sql,valor)

    conexao.commit()

    print(meucursor.rowcount, "Jogador deletado!")
    meucursor.close()
    conexao.close()
    

def inserir_resultados():
  
  conexao = conectar()

  id = input ('Digite o id da partida:')
  resultado = input ('Digite o tipo de resultado da partida:')
  meucursor = conexao.cursor ()
  sql = "INSERT INTO Resultados (id_partida, Tipo_resultado) Values (%s, %s)"
  valor = (id, resultado)

  meucursor.execute(sql, valor)
  conexao.commit()
  print(meucursor.rowcount, "Resultado(s) inseridos")

  meucursor.close()
  conexao.close()


def apagar_partidas():
  conexao = conectar()
  listar_partidas()
  id = int(input('Selecione o id da partida que deseja apagar: '))
  print("\n A partida com o id  {} foi apagada!\n".format(id))
    
    
  sql = "DELETE FROM partidas WHERE id = %s"
  valor = (id,)
  meucursor = conexao.cursor ()

  meucursor . execute (sql, valor)
  print(meucursor.rowcount, "Partida deletada!")
  conexao.commit()
  meucursor.close()
  conexao.close()


   
def  cadastrar_em_uma_partida():  
  conexao = conectar()
  partida = input ('Digite o id da partida que deseja se cadastrar:')
  j1 = input ('Digite o id do jogador 1:')
  j2 = input ('Digite o id do jogador 2:')
  meucursor = conexao.cursor ()
  sql = "INSERT INTO Partidas_tem_jogadores (id_partida, id_jogador1, id_jogador2) values (%s, %s, %s)"
  valor = (partida, j1, j2)

  meucursor.execute(sql, valor)

  print(meucursor.rowcount, "Cadastrado na partida!")
  conexao.commit()
  meucursor.close()
  conexao.close()


def  cadastrar_uma_partida():
  conexao = conectar()
  nome = input ('Digite o nome de uma partida:')
  data = input ('Digite a data da partida:')
  meucursor = conexao.cursor ()
  sql = "INSERT INTO Partidas (nome, data) Values (%s, %s)"
  valor = (nome, data)

  meucursor.execute(sql, valor)
  conexao.commit()

  print(meucursor.rowcount, "Partida(s) inserida!")
  conexao.commit()
  meucursor.close()

def  listar_resultados():
  conexao = conectar()

  meucursor = conexao.cursor()
  sql= """SELECT j.nome, j2.nome, p.nome, data, Tipo_resultado FROM  Partidas P 
Join Resultados R on r.Id_partida=p.id
join partidas_tem_jogadores PJ on pj.id_partida=p.id
join Jogadores J on id_Jogador1=j.id
join jogadores J2 on id_jogador2=j2.id;"""
  meucursor.execute(sql)

  myresult = meucursor.fetchall()
    
  print('{:^12} | {:^10} | {:^10} | {:^10} | {:^10}'.format('jogador1', 'jogador2', 'nome_partida','data','tipo_resultado'))
  for jogador1, jogador2, nome_partida,data,tipo_resultado in myresult:
    print('{:^12} | {:^10} | {:^10} | {:^10}| {:^10}'.format(jogador1, jogador2, nome_partida,str(data),tipo_resultado))

  meucursor.close()
  conexao.close()
  

while True:    
    opcoes = input("\n================\n     Menu\n================\n1-Cadastrar novo Jogador\n2-Listar Jogadores\n3-Alterar um jogador\n4-Apagar Id jogador\n5-Cadastrar um jogador em uma Partida\n6-Cadastrar uma nova partida\n7-Listar_Resultados\n8-Alterar_Partidas\n9-Listar_Partidas\n10-Apagar_Partida\n11-Inserir_resultados\n12-Sair\n")

    if opcoes =='1':
        cadastro_jogadores()
    elif opcoes =='2':
        listar_jogadores()
    elif opcoes =='3':
        alterar_jogadores()
    elif opcoes =='4':
        apagar_jogadores()
    elif opcoes =='5':
        cadastrar_em_uma_partida()
    elif opcoes =='6':
        cadastrar_uma_partida()
    elif opcoes =='7':
        listar_resultados()
    elif opcoes =='8':
        alterar_partidas()
    elif opcoes =='9':
        listar_partidas()       
    elif opcoes =='10':
        apagar_partidas()
    elif opcoes =='11':
       inserir_resultados()
    elif opcoes =='12':
        print('Saindo...')
        break
    else:
        print("\nErro!!")


