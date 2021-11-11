# import mysql.connector
from mysql.connector import connect, Error
from dotenv import dotenv_values


#TODO: load credentials from .env
#HOST="localhost"
#USER="talking_backend"
#PWD="tlkg_bcknd_0001"
#DATABASE="school_sensors"


def load_all_sensors():
    """
        Funkcia nacita vsetky existujuce senzory a ich najposlednejsie hodnoty
        Vracia list of JSON elements
    """

    config = dotenv_values(".env")
    # print(config)

    HOST=config["HOST"]
    USER=config["USER"]
    PWD=config["PASSWORD"]
    DATABASE=config["DATABASE"]


    all_sensors=[]
    # print(type(all_sensors))

    try:
        # skusam sa pripojit do DB
        my_db = connect(host=HOST, user=USER, password=PWD, database=DATABASE) 
        cursor = my_db.cursor()

        query = """
            select rooms.room_id, sensors.sensor_id, sensor_type, sensor_value, sensor_unit, MAX(time_stamp) 
            from rooms inner join sensors on sensors.sensor_id = rooms.sensor_id 
            group by room_id, sensor_type;
                """
        cursor.execute(query)
        available_sensors = cursor.fetchall()

        # prejdem vsetkymi vysledkami 'available_sensors' z DB 
        # a spravim z kazdeho JSON 'sensor' (=dictionary)
        # a hotovy element pridam do tuple 'all_sensors'
        for single_sensor in available_sensors:
            # print(single_sensor)    # test print
            sensor = {
                "room_id": single_sensor[0],
                "sensor_id": single_sensor[1],
                "sensor_type": single_sensor[2],
                "sensor_value": single_sensor[3], 
                "sensor_unit": single_sensor[4], 
                "latest_datetime": single_sensor[5]
            }
            #print(sensor)           # test print
            #print(type(sensor))
            
            all_sensors.append(sensor)

        # slusne uzavriem spojenie do DB
        cursor.close()

        return all_sensors


    except Error as e:
        print(e)
    


def load_single_sensor(sensor_id):
    """
        Funkcia vrati data pre konkretny senzor
    """
    config = dotenv_values(".env")
    # print(config)

    HOST=config["HOST"]
    USER=config["USER"]
    PWD=config["PASSWORD"]
    DATABASE=config["DATABASE"]

    all_sensors = []
    try:
        # skusam sa pripojit do DB
        my_db = connect(host=HOST, user=USER, password=PWD, database=DATABASE) 
        cursor = my_db.cursor()

        query = f"""
            select sensor_id, sensor_type, sensor_value, sensor_unit, Max(time_stamp) AS latest_datetime 
            from sensors            
            where sensors.sensor_id = {sensor_id} 
            group by sensor_type 
                """
        # print(query)

        cursor.execute(query)
        available_sensors = cursor.fetchall()

        # prejdem vsetkymi vysledkami 'available_sensors' z DB 
        # a spravim z kazdeho JSON 'sensor' (=dictionary)
        # a hotovy element pridam do tuple 'all_sensors'
        for single_sensor in available_sensors:
            # print(single_sensor)    # test print
            sensor = {
                "sensor_id": single_sensor[0],
                "sensor_type": single_sensor[1],
                "sensor_value": single_sensor[2],
                "sensor_unit": single_sensor[3], 
                "latest_datetime": single_sensor[4]
            }
            #print(sensor)           # test print
            #print(type(sensor))
            
            all_sensors.append(sensor)

        # slusne uzavriem spojenie do DB
        cursor.close()

        return all_sensors


    except Error as e:
        print(e)



if __name__ == "__main__":
    # x = load_all_sensors()
    # print("all sensors result:")
    # print(x)
    
    sensor_id = 1
    y = load_single_sensor(sensor_id)
    print("Data from sensor no: "+str(sensor_id))
    print(y)
