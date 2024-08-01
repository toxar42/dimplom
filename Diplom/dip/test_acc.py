import pytest
import pymysql
# from libs.comps.signupscreen import login,password
from dip.libs.comps.loginscreen import connection as bd

def test_connection():
    """Проверяет успешное подключение к базе данных."""
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='12345678',
            database='auto',
            cursorclass=pymysql.cursors.DictCursor
        )
        connection.close()
    except Exception as ex:
        pytest.fail(f"Ошибка подключения к базе данных: {ex}")

def read(table, connection):  # Добавляем connection как аргумент
    with connection.cursor() as cursor:
        insert_query = f'SELECT * FROM {table}'
        cursor.execute(insert_query)
        return cursor.fetchall()

def test_read_data(mocker):
    """Тестирует чтение данных из таблицы."""

    # Мокируем соединение с базой данных
    mock_connection = mocker.MagicMock()
    mock_cursor = mocker.MagicMock()
    mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

    # Мокируем результат выполнения запроса
    mock_cursor.fetchall.return_value = [
        {'id': 1, 'name': 'Test'},
        {'id': 2, 'name': 'Data'}
    ]

    # Вызываем функцию read с моками
    result = read('test_table', mock_connection)

    # Проверяем результаты
    assert mock_cursor.execute.called_once_with('SELECT * FROM test_table')
    assert result == [
        {'id': 1, 'name': 'Test'},
        {'id': 2, 'name': 'Data'}
    ]

def test_create_data():
    pass

def test_update_data():
    pass

def test_delete_data():
    pass