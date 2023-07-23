import psycopg2 as psycopg2

#try:
connection = psycopg2.connect(
    host="127.0.0.1",
    database="Example",
    user="postgres",
    password="123456",
    port="5433"
)

#except BaseException:
#    print('не получилось')
''' cursor = connection.cursor()
 cursor.execute(''' '''CREATE TABLE STUDENT
     (ADMISSION INT PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL,
     AGE INT NOT NULL,
     COURSE CHAR(50),
     DEPARTMENT CHAR(50));'''    '''  )
records = cursor.fetchall()

print("Table created successfully")

print("Database opened successfully")

cursor.close()  '''
cur = connection.cursor()

cur.execute(
    "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3432, 'Ivan', 18, 'Computer Science', 'ICT')"
)

connection.commit()
print("Record inserted successfully")



# cursor.close()


cur.execute("SELECT admission, name, age, course, department from STUDENT")

rows = cur.fetchall()
for row in rows:
    print("ADMISSION =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("COURSE =", row[3])
    print("DEPARTMENT =", row[4], "\n")

print("Operation done successfully")
connection.close()

print(connection)
