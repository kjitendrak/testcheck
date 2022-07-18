import mysql.connector as connection

mydb = connection.connect(host = "localhost" , user ="root" , passwd = "@Jix" ,db="jitendra")
cursor = mydb.cursor()
#cursor.execute("create table sudhanshu.ineuron(employe_id int(10)  , emp_name varchar(80) , emp_mailid varchar(20),emp_salary int(6)) , emp_attendence int(3)")
print(cursor)




(44;"technician";"single";"secondary";"no";29;"yes";"no";"unknown";5;"may";151;1;-1;0;"unknown";"no"),
(33;"entrepreneur";"married";"secondary";"no";2;"yes";"yes";"unknown";5;"may";76;1;-1;0;"unknown";"no"),
(47;"blue-collar";"married";"unknown";"no";1506;"yes";"no";"unknown";5;"may";92;1;-1;0;"unknown";"no")
