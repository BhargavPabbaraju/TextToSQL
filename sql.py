import sqlite3

### Connect to sqlite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table , retreieve result
cursor = connection.cursor()

cursor.execute('''DROP TABLE IF EXISTS pokemon;''')

### Create the table
pokemon_schema = """
CREATE TABLE pokemon(id INT, name VARCHAR(25), type1 VARCHAR(25), type2 VARCHAR(25), atk INT, 
def INT, spatk INT, spdef INT, speed INT);
"""

cursor.execute(pokemon_schema)

### Insert some records
cursor.execute('''INSERT INTO pokemon(id, name, type1, type2,  atk, def, spatk, spdef, speed) 
VALUES (1, 'Bulbasaur', 'Grass', 'Poison', 45, 49, 49, 65, 45);''')

cursor.execute('''INSERT INTO pokemon(id, name, type1, type2,  atk, def, spatk, spdef, speed) 
VALUES (2, 'Ivysaur', 'Grass', 'Poison', 60, 62, 63, 80, 60);''')

cursor.execute('''INSERT INTO pokemon(id, name, type1, type2,  atk, def, spatk, spdef, speed) 
VALUES (3, 'Venusaur', 'Grass', 'Poison', 80, 82, 83, 100, 80);''')

cursor.execute('''INSERT INTO pokemon(id, name, type1, type2,  atk, def, spatk, spdef, speed) 
VALUES (4, 'Charmander', 'Fire', NULL, 39, 52, 43, 50, 65);''')

cursor.execute('''INSERT INTO pokemon(id, name, type1, type2,  atk, def, spatk, spdef, speed) 
VALUES (5, 'Charmeleon', 'Fire', NULL, 58, 64, 58, 65, 80);''')

cursor.execute('''INSERT INTO pokemon(id, name, type1, type2,  atk, def, spatk, spdef, speed) 
VALUES (6, 'Charizard', 'Fire', 'Flying', 78, 84, 78, 85, 100);''')

cursor.execute('''INSERT INTO pokemon(id, name, type1, type2,  atk, def, spatk, spdef, speed) 
VALUES (7, 'Squirtle', 'Water', NULL, 44, 48, 65, 50, 43);''')

cursor.execute('''INSERT INTO pokemon(id, name, type1, type2,  atk, def, spatk, spdef, speed) 
VALUES (8, 'Wartortle', 'Water', NULL, 59, 63, 80, 65, 58);''')

cursor.execute('''INSERT INTO pokemon(id, name, type1, type2,  atk, def, spatk, spdef, speed) 
VALUES (9, 'Blastoise', 'Water', NULL, 79, 83, 100, 85, 78);''')

#Display the records
print("Inserted records are:")
data = cursor.execute('''SELECT * FROM pokemon;''')

for row in data:
    print(row)

#Close the connection
connection.commit()
connection.close()