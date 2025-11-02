import mysql.connector

try:
    conexion=mysql.connector.connect(
        port=3307,
        host='localhost',
        user='root',
        password='',
        database='bd_notas',
    )
    cursor=conexion.cursor(buffered=True)
except:
     print(f"Error en la conexión. Por favor, verifique ...")    
