import sqlite3
conn = sqlite3.connect("user.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS user(name TEXT, phone INTEGER, age INTEGER)""")
conn.commit
name = 'shohrux'
phone = 3221
age = 18

# cur.execute(f"""INSERT INTO user VALUES ('{name}', '{phone}', '{age}') """)
# conn.commit()
# cur.execute(f"""SELECT * FROM user WHERE age = 18""")
# user = cur.fetchone()
# print(user[1])



def update_user(name, phone, age):
    cur.execute(f"""SELECT * FROM  user WHERE name = {name} """)
    user = cur.fetchone()
    old_name = user[0]
    old_phone = user[1]
    old_age = user[2]
    if name == "None":
        name = old_name
    if phone == 'None':
        phone = old_phone
    if age == 'None':
        age = old_age

    cur.execute(
        f"""UPDATE user SET name = '{name}, phone = '{phone}', age = '{age}' """)
    conn.commit()

def select_user(name):
    cur.execute(f"""SELECT * FROM user WHERE name = {name}""")
    user = cur.fetchone()
    print(user)


num = 12
str_num = str(num)
print(str_num[-1])
