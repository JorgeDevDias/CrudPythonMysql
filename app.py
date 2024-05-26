#pip install mysql-connector-python 

import mysql.connector 

 
 
 

conexao = mysql.connector.connect( 

 host='bancotestevix.mysql.uhserver.com', 

                           user='devvix', 

                           passwd='devdias1@', 

                           database='bancotestevix' 

) 

 
 

cursor = conexao.cursor() 

cursor.execute('SELECT * FROM bdqm') 

resultados = cursor.fetchall() 

for resultado in resultados: 

  print(resultado) 

cursor.close() 

conexao.close() 