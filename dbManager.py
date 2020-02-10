import mysql.connector

class dbManager:
    """
    This class contains the methods used to create, save, and close a MySQL database

    """
    def createDb(self):

        mydb = mysql.connector.connect(host='localhost', user='root', passwd='47890218')

        mycursor = mydb.cursor()

        mycursor.execute('CREATE DATABASE companyInformation')

        mycursor.execute('SHOW DATABASES')
        for x in mycursor:
            print(x)

        mycursor.execute('CREATE TABLES contactInformation (RecordID INT AUTO_INCREMENT PRIMARY KEY')
        mycursor.execute('CREATE TABLES salesInformation (RecordID INT AUTO_INCREMENT PRIMARY KEY')
        mycursor.execute('CREATE TABLES addressInformation (RecordID INT AUTO_INCREMENT PRIMARY KEY')
        mycursor.execute('CREATE TABLES userInformation (RecordID INT AUTO_INCREMENT PRIMARY KEY')
        mycursor.execute('CREATE TABLES securityInformation (RecordID INT AUTO_INCREMENT PRIMARY KEY')

        mycursor.execute('SHOW TABLES')
        for x in mycursor:
            print(x)