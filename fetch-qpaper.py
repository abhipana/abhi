import mysql.connector 
from mysql.connector import Error
import os

                # functin to create file.
                # this function accept 2 parameter data and file naame
                # file name include the extension of file depending on the extension file is generated.
                # data is actual content which file has.
def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    # with open(filename, 'wb') as file:
    #     file.write(data)

    # open file object with write mode in the file name given
    fileobject = open(filename,'wb')
    # write the content to file.
    fileobject.write(data)
    # trigger print function. after print close the adobe reader.
    os.startfile(filename, "print")
    # for p in psutil.process_iter(): 
    #     if 'AcroRd' in str(p):
    #         p.kill()

# Function to read blob content form the database based on the parameter passed.
# can change it to what ever u want, like id, name etc.
def readBLOB(usn):
    print("Reading BLOB data from student table")

    try:
        # establishing the mysql connection with python using mysql drivers.
        # host: base url of the application, since it is not hosted anywhere and running only locally
        # it is localhost. if it is hosted in any platform like godady/domain.com/cheapname etc repleace
        # with actual URL.
        # database: it is the database name given in mysql
        # user: default user of mysql is root. if u are using specific user then replace with the actual user name 
        # password: for root there is no password by default. if u are using specific user name corrosponding password.

        connection = mysql.connector.connect(host='localhost',
                                             database='robot-invigilation',
                                             user='root',
                                             password='')
        # set the cursor to the table, based on the cursor position all operation performed 
        cursor = connection.cursor()
        # SQL query to get the table data.
        sql_fetch_blob_query = "SELECT * from `set-qpaper` where id = %s"
        # execte the query defined.
        cursor.execute(sql_fetch_blob_query, (usn,))
        record = cursor.fetchall() 

        # loop until record has value
        for row in record:
            # assign the blob content to file variable.
            # row[1/2/3/4..] position depends of the table structure u created. here the file position is 
            # 4 hence it is 3. Index starts from 0.
            file = row[3]
            print("Storing question paper on disk \n");
            write_file(file, 'qpaper1.pdf')
            # write_file(file, 'qpaper1')

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# here you need to pass the identified fingerprint id instead of 1.
# readBLOB(fingerPrintId)
readBLOB(1)
