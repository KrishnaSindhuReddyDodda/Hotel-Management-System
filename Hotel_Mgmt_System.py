import sqlite3
conn = sqlite3.connect('Hotel_Management_System.db')
print("================CONNECTION ESTABLISHED============")
cursor = conn.cursor()


#DROP TABLES IN DATABASE IF EXISTS
cursor.execute('DROP TABLE IF EXISTS Customer');
cursor.execute('DROP TABLE IF EXISTS Reservation');
cursor.execute('DROP TABLE IF EXISTS Room');
cursor.execute('DROP TABLE IF EXISTS RoomType');
cursor.execute('DROP TABLE IF EXISTS Payment');
cursor.execute('DROP TABLE IF EXISTS Invoice');
cursor.execute('DROP TABLE IF EXISTS Charge');
cursor.execute('DROP TABLE IF EXISTS Service');


#CREATING TABLES INTO DATABASE
cursor.execute( '''CREATE TABLE Customer ( C_ID Int NOT NULL,
                                           Name Varchar(20),
                                           Email Varchar(30),
                                           Age Int,
                                           Sex Char(1) )''' )

print("------------------CUSTOMER TABLE CREATED SUCCESSFULLY--------------")
cursor.execute('''CREATE TABLE Reservation (R_ID Int NOT NULL,
                                            arrivalDate Text,
                                            departureDate Text,
                                            customizedPrice Varchar(6),
                                            status Int)''' )
print("------------------RESERVATION TABLE CREATED SUCCESSFULLY-------------")
cursor.execute('''CREATE TABLE Room ( RoomNumber Int NOT NULL,
                                      floor Int,
                                      roomCapacity Int)''')
print("-------------------ROOM TABLE CREATED SUCCESSFULLY-----------------")
cursor.execute('''CREATE TABLE RoomType (room_number Int,
                                         roomType Varchar(20),
                                         description Varchar(50),
                                         RoomPrice Varchar(20))''')
print("-------------------ROOM TYPE TABLE CREATED SUCCESSFULLY-----------------")
cursor.execute('''CREATE TABLE Payment (P_ID Int NOT NULL,
                                        paymentType Varchar(20),
                                        description Varchar(20))''')
print("-------------------PAYMENT TABLE CREATED SUCCESSFULLY-----------------")
cursor.execute('''CREATE TABLE Invoice (invoiceNumber Int NOT NULL,
                                        Payment_date Text,
                                        Total Int,
                                        Status Int)''')
print("-------------------INVOICE TABLE CREATED SUCCESSFULLY-----------------")
cursor.execute('''CREATE TABLE Charge (date Text,
                                       units Int,
                                       quantity Float)''')
print("-------------------CHARGE TABLE CREATED SUCCESSFULLY-----------------")
cursor.execute('''CREATE TABLE Service(service_ID Int NOT NULL,
                                       description Varchar(30),
                                       unitPrice Int)''')
print("-------------------SERVICE TABLE CREATED SUCCESSFULLY-----------------")



# INSERT VALUES INTO TABLES

cursor.execute (''' INSERT INTO Customer ( C_ID, Name, Email, Age, Sex) VALUES (1,"Krishna" , "doddakrishnasindhureddy@gmail.com" , 23, "F") ,
                                                                                (2,"Vipula","vipulareddy123@gmail.com", 21,"F"),
                                                                                (3,"Raghuveer","naraha2@uwm.edu",25,"M"),
                                                                                (4,"Vinay","vinayreddykanula@gmail.com",20,"M"),
                                                                                (5,"Pranaya","pkotha@uwm.edu",27,"F")''' )
conn.commit()
cursor.execute (''' INSERT INTO Reservation (R_ID, arrivalDate, departureDate, customizedPrice, status) VALUES (11 , "2021-07-13" , "2021-07-16" , "$234" , 1),
                                                                                                               (12 , "2021-06-13" , "2021-06-16" , "$124" , 0),
                                                                                                               (13 , "2021-05-13" , "2021-05-16" , "$164" , 1),
                                                                                                               (14 , "2021-04-13" , "2021-04-16" , "$190" , 0),
                                                                                                               (15 , "2021-01-13" , "2021-01-16" , "$290" , 1)''')
conn.commit()
cursor.execute (''' INSERT INTO Room ( RoomNumber, floor, roomCapacity) VALUES (101, 1, 4) ,
                                                                               (203, 2 , 3), 
                                                                               (306, 3 ,5),
                                                                               (205, 2, 4),
                                                                               (106, 1 , 4)''')
conn.commit()
cursor.execute (''' INSERT INTO RoomType (room_number,roomType, description, RoomPrice) VALUES (101, "1BHK" , "With good interior design","345$") ,
                                                                                               (106, "2BHK" , "With good power supply and interior design", "567$") ,
                                                                                               (203, "3BHK" , "Good deal with low price" , " 545$"),
                                                                                               (306, "2BHK" , "With open kitchen design", "245$"),
                                                                                               (205, "3BHK" , "With good interior design and ll new equipments" , "745$"),
                                                                                               (106, "1BHK" , "With good design" , "190$")''')
conn.commit()
cursor.execute (''' INSERT INTO Payment( P_ID, paymentType, description) VALUES (1111 , "CREDIT CARD", "paid in advance") ,
                                                                                (1112,  "CASH", "ill pay on arrival"),
                                                                                (1113, "DEBIT CARD", "paid just now") ''')
conn.commit()
cursor.execute (''' INSERT INTO Charge ( date, units, quantity) VALUES ("2021-06-29" , 3 , 34.8) ,
                                                                       ("2021-01-2" , 8 , 567.09),
                                                                       ("2020-06-9" , 13 , 349.8),
                                                                       ("2001-08-22" , 37 , 3498.8)''')
conn.commit()
cursor.execute (''' INSERT INTO Invoice(invoiceNumber, Payment_date, Total, Status) VALUES (91, "2021-05-06",123,1),
                                                                                           (92, "2021-04-01",983,0),           
                                                                                           (93, "2021-05-2" ,343,0),
                                                                                           (94, "2021-06-24" ,723,1) ''')
conn.commit()
cursor.execute (''' INSERT INTO Service(service_ID, description, unitPrice) VALUES (21, "Good customer service" ,5) ,
                                                                                   (22, "Neat" ,6),
                                                                                   (23, "Very bad" ,2) ''')
conn.commit()


# TO GET CUSTOMER TABLE  
cursor.execute(""" SELECT * FROM Customer """);
print(cursor.fetchall())
print()

# TO GET RESERVATION TABLE  
cursor.execute(""" SELECT * FROM Reservation """);
print(cursor.fetchall())
print()

# TO GET ROOM TABLE
cursor.execute(""" SELECT * FROM Room """);
print(cursor.fetchall())
print()

# TO GET ROOM Type TABLE  
cursor.execute(""" SELECT * FROM RoomType """);
print(cursor.fetchall())
print()

# TO GET Payment TABLE
cursor.execute(""" SELECT * FROM Payment """);
print(cursor.fetchall())
print()

# TO GET Invoice TABLE  
cursor.execute(""" SELECT * FROM Invoice """);
print(cursor.fetchall())
print()

# TO GET Charge TABLE  
cursor.execute(""" SELECT * FROM Charge """ );
print(cursor.fetchall())
print()


# TO GET Service TABLE  
cursor.execute(""" SELECT * FROM Service """);
print(cursor.fetchall())

print("Older CUSTOMER TABLE")
cursor.execute(""" SELECT Name, Age, Sex FROM Customer """)
print(cursor.fetchall())
print()

cursor.execute("UPDATE Customer SET Age=Age+1 WHERE Sex='M' ")
print()
print("UPDATED CUSTOMER TABLE")
cursor.execute(""" SELECT  Name, Age, Sex FROM Customer """);
print(cursor.fetchall())
conn.commit()
print()
print()

print("CUSTOMER TABLE BEFORE DELETION")
cursor.execute("""SELECT C_ID, Age, Sex FROM Customer""")
print(cursor.fetchall())
print()
print()
print("====================================================")
cursor.execute("""SELECT P_ID,paymentType FROM Payment LIMIT 2""")
print(cursor.fetchall())
print()
print()


# DELETE A RECORD FROM CUSTOMER WHERE  ID=3  
cursor.execute(""" DELETE FROM Customer WHERE C_ID = 3 """)
print("UPDATED ROOM TABLE")
cursor.execute(""" SELECT  C_ID, Age, Sex FROM Customer ORDER BY Age,C_ID""");
print(cursor.fetchall())
conn.commit()
print()
print()


# DROP TABLE SERVICE FROM A DATABASE 
cursor.execute( """ DROP TABLE SERVICE """)
conn.commit()
print("======DROPPED SERVICE TABLE=========")
cursor.execute("select * from SQLite_master")
print()
tables = cursor.fetchall()
print("AVAILABLE TABLES")
for table in tables:

        print("%s"%(table[1]))
# DROP TABLE INVOICE FROM A DATABASE 
cursor.execute( """ DROP TABLE Invoice """)
conn.commit()
print()
print()
print()
print("======DROPPED INVOICE TABLE=========")
cursor.execute("select * from SQLite_master")
tables = cursor.fetchall()
print("AVAILABLE TABLES IN HOTEL MANAGEMENT DATABASE")
for table in tables:

        print("%s"%(table[1]))
print()
print()
        

#CLOSES A CONNECTION
conn.close()                                 
print("================CONNECTION CLOSED===========================")
        















