import sqlite3
conexao=sqlite3.connect('DesafioWMC')
cursor=conexao.cursor()
#exercicio 1
#cursor.execute('CREATE TABLE alunos( id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')
#exercicio 2

#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Isabella Ibagon", 18, "Física")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Carolina Pardo", 19, "Ciência de Dados")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Jimena Martinez", 20, "Zootecnia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Viviana Alba", 18, "Medicina")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Ingrid Triana", 18, "Economia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "Olivia Silva", 22, "Artes visuais")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(7, "Diana Dias", 28, "Ciências Contábeis")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(8, "Sandra Tarazona", 21, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(9, "Rodrigo Rodrigues", 30, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(10, "Andres Andrade", 23, "Engenharia")')


#exercicio 3
#selecionar todos os registros 
#Dados_a=cursor.execute('SELECT * FROM  alunos')
#for aluno in Dados_a:
#    print(aluno)
#selecionar o nome e a idade dos alunos com mais de 20
#Dados_b=cursor.execute('SELECT nome,idade FROM  alunos WHERE idade>20')
#for aluno in Dados_b:
#    print(aluno)
#selecionar os alunos do curso engenharia  em ordem alfabetica
#Dados_c=cursor.execute('SELECT * FROM  alunos WHERE curso="Engenharia" ORDER BY nome')
#for aluno in Dados_c:
#    print(aluno)
#Contar o número total de alunos na tabela
#cursor.execute('SELECT COUNT(*) FROM  alunos')
#total = cursor.fetchone()[0]
#print(total)

#Exercicio 4
#Atualize a idade de um aluno
#cursor.execute('UPDATE alunos SET idade=18 WHERE nome="Rodrigo Rodrigues"')
#Remova um aluno pelo seu ID
cursor.execute('DELETE FROM alunos where id=4')

conexao.commit()

conexao.close
