import sqlite3

connector = sqlite3.connect('analytics.db')
cursor = connector.cursor()
cursor.execute("""CREATE TABLE vendas (Id Interger Primary key,
               valor_venda NUM NOT NULL,
               cliente_id Interger NOT NULL,
               foreign key (cliente_id) references clientes (id))""")
cursor.execute("INSERT INTO vendas VALUES (1, 15.60, 1)")
connector.commit()

cursor.execute("""SELECT * FROM vendas AS v 
               join clientes AS c ON v.clientes_id = c.id""")
vendas = cursor.fetchall()
print(vendas)

connector.close()
