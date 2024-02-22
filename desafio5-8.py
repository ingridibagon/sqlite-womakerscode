import sqlite3
conexao=sqlite3.connect('DesafioWMC')
cursor=conexao.cursor()
#exercicio 5
# cursor.execute('CREATE TABLE clientes( id INT NOT NULL PRIMARY KEY, nome VARCHAR(100), idade INT, saldo NUMERIC)')


# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Isabella Ibagon", 18, 100)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Ana Pardo", 50, 5000)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Maria Silva", 42, 3100)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Thiago Mattos", 28, 1500)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Rosa Dias", 37, 1200)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(6, "Luana Campos", 35, 1300)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(7, "Marta Mora", 24, 1100)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(8, "Andrea Zica", 22, 1500)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(9, "Roberto Andrade", 25, 2100)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(10, "Fernanda Regaldo", 19, 1000)')




#exercicio 6

#selecionar o nome e a idade dos alunos com mais de 20
# Dados_a=cursor.execute('SELECT nome,idade FROM  clientes WHERE idade>30')
# for cliente in Dados_a:
#     print(cliente)

#saldo medio dos clientes
#cursor.execute('SELECT AVG(saldo) FROM  clientes')
# media = cursor.fetchone()[0]
# print(media)

#cliente com maior saldo
# dados_c=cursor.execute('SELECT * FROM clientes WHERE saldo=(SELECT MAX(saldo) FROM  clientes)')
# for cliente in dados_c:
#     print(cliente)

#cliente com saldo >100
# dados_d=cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo>1000')
# for dado in dados_d:
#      print(dado[0])




#Exercicio 7
#Atualize o saldo de um cliente
#cursor.execute('UPDATE clientes SET saldo=10000 WHERE nome="Ana Pardo"')
#Remova um aluno pelo seu ID
#cursor.execute('DELETE FROM clientes where id=4')

#Exercicio 8
#criar a tabela compras
#cursor.execute('CREATE TABLE compras( id INT NOT NULL PRIMARY KEY, cliente_id INT NOT NULL, produto VARCHAR(100), valor NUMERIC, FOREIGN KEY (cliente_id) REFERENCES clientes (id) )')

#inserir dados
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 1, "Caderno", 20)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 1, "Lapis", 5)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(3, 1, "Borracha", 5)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(4, 1, "Caneta Marca Texto", 30)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(5, 2, "Caderno", 20)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(6, 2, "Lapis", 5)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(7, 2, "Caixa Lapis de cor", 25)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(8, 3, "Lapis", 5)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(9, 3, "Caixa Lapis de cor", 25)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(10, 9, "Caixa Lapis de cor", 25)')

#cliente , producto e valor de cada compra
# dados_d=cursor.execute('SELECT nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id=compras.cliente_id')
# for dado in dados_d:
#      print(dado)


conexao.commit()

conexao.close
