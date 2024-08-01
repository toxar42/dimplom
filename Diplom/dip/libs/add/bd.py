import pymysql

try:
    connection = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='12345678',database='auto',cursorclass=pymysql.cursors.DictCursor)
    print('Successfully')
except Exception as ex:
    print(ex)
# Функция для запроса создания
def insert(table, columns, values):
    with connection.cursor() as cursor:
        # Формирование строки запроса с заполнителями
        placeholders = ', '.join(['%s'] * len(values))
        insert_query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor.execute(insert_query, values)
        connection.commit()
# Функция для запроса чтения
def read(table):
    with connection.cursor() as cursor:
        insert_query = f'SELECT * FROM `{table}`'
        cursor.execute(insert_query)
        return cursor.fetchall()
# Функция для запроса удаления
def delete(table,name_id,id):
    with connection.cursor() as cursor:
        insert_query = f'DELETE FROM `{table}` WHERE {name_id}={id}'
        cursor.execute(insert_query)
        connection.commit()
# Функция для запроса обновления
def update(table, column, value,name_id, id):
    with connection.cursor() as cursor:
        insert_query = f"UPDATE `{table}` SET {column}='{value}' WHERE {name_id}={id}"
        cursor.execute(insert_query)
        connection.commit()