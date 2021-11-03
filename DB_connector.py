from dotenv import dotenv_values
from flask import Flask
from flask import Flask,render_template, request
from flask_mysqldb import MySQL

config = dotenv_values(".env")


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = config["USER"]
app.config['MYSQL_PASSWORD'] = config["PASSWORD"]
app.config['MYSQL_DB'] = 'databaza'

mysql = MySQL(app)

#app route je tu kvoli flasku, ak chces skriptu spustit #samostatne tak len pridaj pod importy app = #Flask(__name__) a pod returnom este tuto podmienku: if #__name__ == '__main__':
 #  app.run()

# ak sa ti velmi chce tak skopci cely kod z gitu, ten app #route vlastne znamena v akom endpointe sa executene ##senzordata
   
@app.route('/senzordata', method = ['GET'])
def senzory():
   if request.method == 'GET':
        teplota = request.form.get['teplota']
        vlhkost = request.form.get['vlhkost']
        senzor1 = teplota
        senzor2 = vlhkost
        cursor = mysql.connection.cursor()
        cursor.execute(''' select room_id, sensor_type, sensor_value, sensor_unit, time_stamp AS latest_datetime from rooms inner join sensors on rooms.sensor_id = sensors.sensor_id where sensor_type = "temperature" group by room_id union select room_id, sensor_type, sensor_value, sensor_unit, time_stamp AS latest_datetime from rooms inner join sensors on rooms.sensor_id = sensors.sensor_id where sensor_type = "humidity" group by room_id; ''',(teplota,vlhkost))
   mysql.connection.commit()
   cursor.close()
   return senzory()
