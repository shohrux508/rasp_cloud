postCategories = {'Science': ['physics', 'astronomy', 'philosophy'], 'IT Technologies': ['artificial intelligence', 'robotics'], 'Psychology': ['brain and universe', 'coaching']}

key = 'Science'
values = postCategories[key]



list = [i for i in range(1, 10)]



import sqlite3
import json

# Создаем соединение с базой данных SQLite
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Создаем таблицу для хранения списка значений
cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, list TEXT)''')

# Пример списка значений для сохранения
my_list = [1, 2, 3, 4, 5]
values_json = json.dumps(my_list)
cursor.execute(f"INSERT INTO my_table VALUES('{3}', '{values_json}')")
conn.commit()
cursor.execute("SELECT list FROM my_table")
row = cursor.fetchone()
retrieved_values = json.loads(row[0])

print(retrieved_values[1]) 
conn.close()

