import paho.mqtt.client as mqtt
import mysql.connector
from datetime import *
import time
from twilio.rest import Client #Enviar mensajes a WhatsApp

global_check = 0
#WhatsApp
account_sid = "AC50a41c2e1a3f644b657f03477f812fb9"
auth_token  = "8aeebe351de6354716626071039e3f56"
clientW = Client(account_sid, auth_token)
def enviar_mensaje_WhatsApp(phone_number):
    phone_number = "whatsapp:+57" + phone_number
    message = clientW.messages.create(
        to= phone_number,
        from_="whatsapp:+14155238886",
        body="Es hora de tomar su medicina! Dirijase hacia la estación.")

#MQTT
mensaje_payload = ''
mqtt_topics = [("paciente/1140857788",2),("1140857788",2)]
def on_message(client, userdata, msg):
    global mensaje_payload
    global mensaje_topic
    mensaje_topic = msg.topic
    mensaje_payload = str(msg.payload.decode("utf-8","ignore"))
    print(mensaje_topic,mensaje_payload)
    check_llamar(mensaje_payload)

def on_connect(client, userdata, flags, rc):
    print("Conectado con el codigo: " + str(rc))
    for topic in mqtt_topics:
        client.subscribe(topic)
# dbConnect = {
#     'host':'localhost',
#     'user':'johanaltro',
#     'password':'jar12345',
#     'database':'bioing_project',
#     'port': 5306}
def check_llamar(numero):
    conn = mysql.connector.connect(**dbConnect)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM schedule_medicines WHERE llamar = 1 AND pax_user =%s",[numero])
    meds = cursor.fetchall()
    print("Se encontraron: ", meds)
    if (len(meds)>0):
        cursor.execute("UPDATE schedule_medicines SET activo = 0, llamar = 0 WHERE pax_user=%s",[numero])
        conn.commit()
        print("Medicina para " + numero + " confirmada con exito.")
dbConnect = {
    'host':'remotemysql.com',
    'user':'qwQlvSlWFi',
    'password':'F3MLpKNrdf',
    'database':'qwQlvSlWFi',
    'port': 3306}

def fetch_database_info():
    now = datetime.now()
    now_mas_1=now + timedelta(minutes=1)
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    now_mas_1 = now_mas_1.strftime('%Y-%m-%d %H:%M')
    conn = mysql.connector.connect(**dbConnect)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM schedule_medicines")
    meds = cursor.fetchall()
    #print(now)
    #print(now_mas_1)
    for i in range(len(meds)):
        #print(meds[i])
        user_topic = meds[i][0]
        channel = meds[i][2]
        time_to_call = (meds[i][3]).strftime('%Y-%m-%d %H:%M')
        #phone_number = meds[i][6]
        if now == time_to_call:
            client.publish(user_topic,channel,qos=2)
            print('['+now+']: '+'Llamando a ' + user_topic + ' al canal ' + channel)
            #enviar_mensaje_WhatsApp()
            cursor.execute("UPDATE schedule_medicines SET activo = 0, llamar = 1 WHERE fecha =%s",[now])
            conn.commit()
    now = datetime.now()
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    while now <now_mas_1:
        #print("Esperando cambio de minuto")
        time.sleep(3)
        now = datetime.now()
        now = datetime.now().strftime('%Y-%m-%d %H:%M')

def recall():
    conn = mysql.connector.connect(**dbConnect)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM schedule_medicines")
    meds = cursor.fetchall()

    for i in range(len(meds)):
        #print(meds[i])
        user_topic = meds[i][0]
        channel = meds[i][2]
        time_to_call = meds[i][3]
        now = datetime.now()
        diff = now - time_to_call
        diff = diff.seconds

        time_to_call = (meds[i][3]).strftime('%Y-%m-%d %H:%M')
        now = now.strftime('%Y-%m-%d %H:%M')
        if diff <= 600:#10minutos
            print(diff)
            client.publish(user_topic,channel)
            print('['+now+']: '+'Rellamando a ' + user_topic + ' al canal ' + channel +
            '. Recuerdo de : ' + time_to_call)
            cursor.execute("UPDATE schedule_medicines SET activo = 0, llamar = 0 WHERE fecha =%s",[now])
            conn.commit()
    time.sleep(10)

client = mqtt.Client("SSAM",False)

client.on_connect = on_connect
client.on_message = on_message

client.connect("m15.cloudmqtt.com",11405,60)
client.username_pw_set("lhfrtzri","O_WZ6e61KPY_")

client.loop_start()

print("Subscribing to topic","paciente/1140857788")

while True:

    fetch_database_info()
    #recall()
