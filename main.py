import mysql.connector
import tabulate

connection = mysql.connector.connect(user='root',
                                     password='admin',
                                     host='127.0.0.1',
                                     database='database')
cursor = connection.cursor()




def insert():
    name = input('Name: \n')
    job = input('Job: \n')
    salary = input('Salary: \n')
    cursor.execute(f"INSERT INTO employees (name, salary, job) VALUES ('{name}', {salary}, '{job}')")

    connection.commit()

def delete():
    id = int(input('Id: '))
    cursor.execute(f"DELETE FROM employees WHERE `id`={id}")
    connection.commit()


def select():
    id= int(input('Введи id: '))
    cursor.execute(f"SELECT * FROM employees WHERE `id`={id}")

    response = cursor.fetchall()
    print(tabulate.tabulate(response, headers=["id","name","job","salary"], tablefmt="pretty"))


def selectAll():
    cursor.execute(f"SELECT * FROM employees")

    response = cursor.fetchall()
    dict=[]
    for row in response:
        dict.append([row[0],row[1],row[2],row[3]])

    print(tabulate.tabulate(dict, headers=["id","name","job","salary"], tablefmt="pretty"))



while True:
    print("\nHello, this is DBMS system. What do you want yo do?")
    choice = input("1. Create\n2. Select one\n3. Select all\n4. Delete\n5. Exit\n:")

    match choice:
        case '1':
            insert()
        case '2':
            select()
        case '3':
            selectAll()
        case '4':
            delete()
        case '5':
            break



connection.close()