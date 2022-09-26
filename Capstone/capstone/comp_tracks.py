from collections import UserDict, UserList
import dbm
import sqlite3
from tkinter import Menu
import bcrypt

connection = sqlite3.connect('Competency_Tracking_Tool.db')
cursor = connection.cursor()

def man_menu():
    user_input = input()
    print("***Manager Menu***\n       Welcome!      \n\n~~  *** Options *** ~~\n[1]View all Users\n[2]Search\n[3]Create User\n[4]Add User\n[5]User Assessments\n[6]Competencey Report\n[7]Add New Competencey\n[8]New Assessment\n[9]User Results\n[10]Edit User\n[11]Edit Comptency\n[12]Edit Assessment\n[13]Edit Result\n[14]Delete Result")

    if user_input == '1':
    view_user()
    elif user_input == '2':
    search_user()
    elif user_input == '3':
    create_us()
    elif user_input == '4':
    add_user()
    elif user_input == '5':
    assess_user()
    elif user_input == '6':
    competency_report()
    elif user_input == '7':
    new_competency()
    elif user_input == '8':
    new_assessment()
    elif user_input == '9':
    results()
    elif user_input == '10':
    edit_user()
    elif user_input == '11':
    edit_comptency()
    elif user_input == '12':
    edit_assessment()
    elif user_input == '13':
    edit_result()
    elif user_input == '14':
    delete_result()


with open("comp_tracks.txt", "r")as infile:
     queries = infile.read()
     # cursor.executescript(queries)
     connection.commit()


is_logged_in = False

while True:
    if (is_logged_in == True):
        if (user.type == manager):
            show man_menu
        else:
            show us_menu
        else:
            email = input("Enter email: ")
            password = input("Enter password: ")

            encrypted_password = bcrypt(password)
            email, password_from_db = cursor.execute("SELECT email, password FROM email, password FROM user WHERE email = ?", email)
            if (encrypted_password == password_from_db):
                is_logged_in = True

def view_user():
    rows = cursor.execute("SELECT * FROM users").fetchall()

    print(f'{"User_ID:<10"}{"Name":<25}{"Address":<30}{"City":<10}{"State":<10}{"Zip":<10}{"Phone":<20}{"email"}')
    print(f"{'-----':<10}{'----':<25}{'--------':<30}{'----':<10}{'-----':<10}{'---':<10}{'-----':<20}{'-----'}")

    for row in rows:
        user_id, name, street_address, city, state, postal_code, email = row
        user_id = user_id if user_id != None else " "
        name = name if name != None else " "
        street_address = street_address if street_address != None else " "
        city = city if city != None else " "
        state = state if state != None else " "
        postal_code = postal_code if postal_code != None else " "
        phone = phone if phone != None else " "
        email = email if email != None else " "
        print(f'{user_id:<10}||{name:<25}||{street_address:<30}||{city:<10}||{state:<10}||{postal_code:<10}||{phone:<20}||{email}')

def search_user():
    entry = input('Enter Name to search: ')
    name = f'%{entry}%'
    rows = cursor.execute("SELECT * FROM Users WHERE name Like ?", (name,)).fetchall()

def create_us():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    password = input("Create password: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip = input("Enter zip code: ")
    date_created("Enter date taken in YYYY-MM-DD format: ")
    hire_date("Enter date taken in YYYY-MM-DD format: ")
    values = (first_name, last_name, email, phone, password, address, city, state, zip)
    insert_sql = "INSERT INTO People(first_name, last_name, email, phone, password, address, city, state, zip, date_created, hire_date) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
    cursor.execute(insert_sql, values)
    connection.commit()
    print("User created")

def date_created():
    manager_id = input("Enter Manager ID: ")
    manager_id = int(manager_id)
    user_id = input("Enter user ID: ")
    user_id = int(user_id)
    start_date = input("Enter start date in YYYY-MM-DD format: ")
    values = (start_date)
    insert_sql = "INSERT INTO Report(user_id, assessment_id, start_date, end_date) VALUES(?,?,?,?)"
    cursor.execute(insert_sql, values)
    connection.commit()
    return print("Date created")


def hire_date():
    manager_id = input("Enter Manager ID: ")
    manager_id = int(manager_id)
    user_id = input("Enter user ID: ")
    user_id = int(user_id)
    start_date = input("Enter start date in YYYY-MM-DD format: ")
    values = (start_date)
    insert_sql = "INSERT INTO Report(user_id, start_date) VALUES(?,?,?)"
    cursor.execute(insert_sql, values)
    connection.commit()
    return print("Date hired.")

def add_user():
    manager_id = input("Enter Manager ID: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    password = input("Create password: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip = input("Enter zip code: ")
    date_created("Enter date taken in YYYY-MM-DD format: ")
    hire_date("Enter date taken in YYYY-MM-DD format: ")
    values = (first_name, last_name, email, phone, password, address, city, state, zip, date_created, hire_date)
    insert_sql = "INSERT INTO People(first_name, last_name, email, phone, password, address, city, state, zip) VALUES(?,?,?,?,?,?,?,?,?)"
    cursor.execute(insert_sql, values)
    connection.commit()
    print("User added")

def assess_user():
    user = input("User ID: ")
    manager_id = input('Manager ID: ')
    query = cursor.execute("UPDATE User SET Manager_id=? WHERE user_id=? ",(manager_id, user_id))
    connection.commit()
    print("User assessed")

def competency_report():
    user = input("Competency ID: ")
    manager_id = input('Manager ID:')
    user_id = input('User ID: ')
    query = cursor.execute("UPDATE User SET manager_id=? WHERE user_id=? ",(manager_id, user_id))
    connection.commit()
    print("New Competency Report")

def new_competency():
    user = input("User ID: ")
    manager_id = input('Manager ID: ')
    competency_id = ('Competency ID: ')
    competency_list [
        0 : "No Competency - Needs Training and Direction",
        1 : "Basic Competency - Needs Ongoing Support",
        2 : "Intermediate Competency - Needs Occasional Support",
        3 : "Advanced Competency - Completes Task Independently",
        4 : "Expert Competency - Can Effectively pass on this knowledge and can initiate optimizations"
    ]
    query = cursor.execute("UPDATE User SET Manager_id=? WHERE user_id=?, competency_id=?",(manager_id, user_id, competency_id, competency_list))
    connection.commit()
    print("Competency added") 

def competency_list():
    0 = "No Competency - Needs Training and Direction",
    1 = "Basic Competency - Needs Ongoing Support",
    2 = "Intermediate Competency - Needs Occasional Support",
    3 = "Advanced Competency - Completes Task Independently",
    4 = "Expert Competency - Can Effectively pass on this knowledge and can initiate optimizations"

def comptency_assessments():
    manager_id = input("Enter Manager ID: ")
    user_id = input("Enter User ID: ")
    assessment_id = input("Enter Assessment Id, ")
    date_taken = input("Enter date taken in YYYY-MM-DD format: ")
    competency_score = ()
    values = (manager_id, user_id, assessment_id, date_taken, competency_score)
    insert_sql = "INSERT INTO Report(user_id, assessment_id, date_taken, competency_score) VALUES(?,?,?,?)"
    cursor.execute(insert_sql, values)
    connection.commit()
    return print('Competency Assessment Data')

def new_assessment():

def results():

def edit_assessment():
    manager_id = input("Enter Manager ID: ")
    manager_id = int(manager_id)
    user_id = input("Enter user ID: ")
    user_id = int(user_id)
    assessment_id = input("Enter Assessment ID: ")
    assessment_id = int(assessment_id)
    start_date = input("Enter start date in YYYY-MM-DD format: ")
    end_date = input("Enter end date in YYYY-DD-MM format: ")
    values = (start_date, end_date)
    insert_sql = "INSERT INTO Report(user_id, assessment_id, start_date, end_date) VALUES(?,?,?,?)"
    cursor.execute(insert_sql, values)
    connection.commit()
    return print("Assessment Edited")

def edit_results():
    name = input('Enter User to update: ')
    update_value = input('Select what you would like to update:\n[N]ame\n[A]ddress\n[P]hone number:\n[E]mail\n')
    if update_value.lower() == 'n':
        new_name = input('Name: ')
        cursor.execute("UPDATE User Set name=? WHERE name = ?", (new_name, name))
        connection.commit()
    if update_value.lower() == 'a':
        street_address = input('Steet address: ')
        city = input('City: ')
        state = input('State: ')
        postal_code = input('Zip code: ')
        cursor.execute("UPDATE User SET street_address=?,city=?,state=?,postal_code=? WHERE name = ? ",(street_address,city,state,postal_code, name))
        connection.commit()
    elif update_value.lower() == 'p':
        phone = input(f'Phone:')
        cursor.execute("UPDATE User SET phone =? WHERE name = ?",(phone, name))
        connection.commit()
    elif update_value.lower() == 'e':
        email = input('New email:')
        cursor.execute("UPDATE User SET email =? WHERE name = ?",(email, name))
        connection.commit()
 
def edit_user():
    name = input('Enter user to update: ')
    update_value = input('Select what you would like to update:\n[N]ame\n[A]ddress\n[P]hone number:\n[E]mail\n')
    if update_value.lower() == 'n':
        new_name = input('Name: ')
        cursor.execute("UPDATE User Set name=? WHERE name = ?", (new_name, name))
        connection.commit()
    if update_value.lower() == 'a':
        street_address = input('Steet address: ')
        city = input('City: ')
        state = input('State: ')
        postal_code = input('Zip code: ')
        cursor.execute("UPDATE User SET street_address=?,city=?,state=?,postal_code=? WHERE name = ? ",(street_address,city,state,postal_code, name))
        connection.commit()
    elif update_value.lower() == 'p':
        phone = input(f'Phone:')
        cursor.execute("UPDATE User SET phone =? WHERE name = ?",(phone, name))
        connection.commit()
    elif update_value.lower() == 'e':
        email = input('New email:')
        cursor.execute("UPDATE User SET email =? WHERE name = ?",(email, name))
        connection.commit()

def edit_competency():
    competency_name = input("Enter name competency: ")
    description = input("Brief description of competency: ")
    values = (competency_name, description)
    insert_sql = "INSERT INTO Results(user_id, name, description) VALUES(?,?,?,)"
    cursor.execute(insert_sql, values)
    connection.commit()
    return print("Competency edited")

def edit_results():
    name = input('Enter User ID to update: ')
    update_value = input('Select what you would like to edit:\n[1]User Information\n[2]Competency: \n[3]Assessment\n[3]Assessment Result\n')
    if update_value == '1':
        user_info = input('Name: ')
        cursor.execute("UPDATE User Set name=? WHERE name = ?", (new_name, name))
        connection.commit()
    if update_value.lower() == 'a':
        street_address = input('Steet address: ')
        city = input('City: ')
        state = input('State: ')
        postal_code = input('Zip code: ')
        cursor.execute("UPDATE Customers SET street_address=?,city=?,state=?,postal_code=? WHERE name = ? ",(street_address,city,state,postal_code, name))
        connection.commit()
    elif update_value.lower() == 'p':
        phone = input(f'Phone:')
        cursor.execute("UPDATE Customers SET phone =? WHERE name = ?",(phone, name))
        connection.commit()
    elif update_value.lower() == 'e':
        email = input('New email:')
        cursor.execute("UPDATE Customers SET email =? WHERE name = ?",(email, name))
        connection.commit()
   
def delete_result():
    assres_id = input('Enter Assessment ID: ')
    cursor.execute("DELETE FROM Assessments WHERE assessment_id = ?",(assessment_id,))
    connection.commit()
    print(f'User:{assessment_id} DELETED.')

def assessment_id():

def assess_user():
    assessment_id = input("Assessment ID: ")
    manager_id = input('Manager ID: ')
    user_id = input('User ID: ')
    query = cursor.execute("UPDATE Reports SET manager_id=? WHERE assessment_id=? ",(manager_id, user_id, assessment_id))
    connection.commit()
    print("User assigned")

def delete_result():
    result_id = input("Enter Assessment ID: ")
    user_id = int(user_id)
    confirm = input(f'Are you sure you want to remove assessment #{assessment_id} from reports?\nPress (Y) for yes').lower()
    if confirm == 'y':
        sql_update = 'UDATE Competency_Tracking_Tool SET active = 0 WHERE assessment_id = ?'
        update_values = (assessment_id,)
        cursor.execute(sql_update, update_values)
        connection.commit()

def create_schema():
    with open('schema_table.txt') as schema:
        queries = schema.read()

        cursor.executescript(queries)
        connection.commit()

def insert_from_file():
    with open('query_backups.txt') as schema:
        queries = schema.read()

        cursor.executescript(queries)
        connection.commit()

# insert_from_file()
# view_inst()
# while True:

#menu()