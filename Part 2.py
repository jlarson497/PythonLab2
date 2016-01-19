import sqlite3

###Global variables
sqlite_file = 'chainsaw_juggling_db.sqlite'    #name of sqlite db file
table_jugglers = "chainsaw_juggling_record_holders"
new_field1 = 'juggler'
field_type1 = 'TEXT'
new_field2 = 'country'
field_type2 = 'TEXT'
new_field3 = 'catches'
field_type3 = 'INTEGER'



def setup_database():
    #connect to db
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    #create new SQLite table with 3 columns

    c.execute('CREATE TABLE IF NOT EXISTS {tn}'
          '({nf1} {ft1},'
          '{nf2} {ft2},'
          '{nf3} {ft3})'
          .format(tn=table_jugglers,
                  nf1=new_field1, ft1=field_type1,
                  nf2=new_field2, ft2=field_type2,
                  nf3=new_field3, ft3=field_type3))

    ins = 'INSERT INTO {tn} VALUES(?, ?, ?)'.format(tn=table_jugglers)
    #add a few records in
    #c.execute(ins, ("Ian Stewart", "Canada", 94))
    #c.execute(ins, ("Aaron Gregg", "Canada", 88))
    #c.execute(ins, ("Chad Taylor", "USA", 78))

    c.execute('SELECT * FROM chainsaw_juggling_record_holders')
    rows = c.fetchall()
    print(rows)
    conn.commit()
    c.close()

def main():
    setup_database()
    menu()

#brings up the menu and allows you to choose what to you want to do
def menu():
    choice = input("Would you like to [A]dd, [D]elete, or E[X}it? ")
    if choice == "A":
        name = input('Name: ')
        country = input('Country: ')
        catches = int(input('Number of Catches: '))
        add_to_db(name, country, catches)
        menu()
    if choice == 'D':
        name = input('Name of juggler you would like to delete: ')
        delete_from_db(name)
        menu()
    if choice == 'X':
        exit()


#method to add a new record
def add_to_db(name, country, catches):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    ins = 'INSERT INTO {tn} VALUES(?, ?, ?)'.format(tn=table_jugglers)
    c.execute(ins, (name, country, catches))
    c.execute('SELECT * FROM chainsaw_juggling_record_holders')
    rows = c.fetchall()
    print(rows)
    conn.commit()
    c.close()

#method to delete a record
def delete_from_db(name):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('DELETE FROM chainsaw_juggling_record_holders WHERE juggler = (?)', (name,))
    conn.commit()
    c.close()

if __name__ == '__main__':
    main()

