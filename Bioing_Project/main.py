import kivy
import mysql.connector
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty, StringProperty

dbConnect = {
    'host':'localhost',
    'user':'johanaltro',
    'password':'jar12345',
    'database':'python',
    'port': 5306}
conn = mysql.connector.connect(**dbConnect)
cursor = conn.cursor()
def create_table_pacientes(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pax_info(
        id      int primary key not null,
        nombre  text            not null,
        doc     text            not null,
        tel     text            not null,
        fecha   date            not null
        )
        """)

class SSAM(ScreenManager):
    def __init__(self,**kwargs):
        super(SSAM, self).__init__()
    wid_user =      ObjectProperty(None)
    wid_pass =      ObjectProperty(None)
    wid_clientes =  StringProperty("login")
    wid_salir =     StringProperty("")

    wid_pax_name =  ObjectProperty(None)
    wid_pax_id =    ObjectProperty(None)
    wid_pax_date =  ObjectProperty(None)
    wid_pax_tel =   ObjectProperty(None)


    def connect_to_drs_db(self,*arg):

        try:
            user= self.wid_user.text
            contr= self.wid_pass.text
            cursor.execute('SELECT name, pass FROM database_py WHERE name = %s AND pass = %s',(user, contr))
            names = {name[0] for name in cursor.fetchall()}
            if user in names:
                print ("Login to Drs database succesfull.")
                self.wid_clientes = "clientes"
                create_table_pacientes(cursor)
                self.ids.user_login.clear_widgets()
            else:
                print("Usuario y/o contrasena no son correctos. Ingrese nuevamente")
                print(self.wid_user.text + self.wid_pass.text )
                self.wid_clientes = "login"
            self.wid_user.text = ""
            self.wid_pass.text = ""
        except Exception as e:
            print(e)
    def salir(self):
        print('Salida exitosa')
        self.wid_salir = 'login'
        conn.close()
    def check_pax(self, *arg):
        try:
            pax_doc = self.wid_pax_id.text
            cursor.execute('SELECT * FROM pax_info WHERE doc = %s ',(pax_doc,))
            docs = {doc[0] for doc in cursor.fetchall()}
            if pax_doc in docs:
                print ("Pax already exists. Displaying pax info.")
            else:
                print("Pax not found. Complete the fills to create.")
        except Exception as e:
            print(e)
    def new_pax(self, *arg):
        name = self.wid_pax_name.text
        id_ =  self.wid_pax_id.text
        tele = self.wid_pax_tel.text
        bdate =self.wid_pax_date

        try:
            cursor.execute("INSERT INTO pax_info (nombre, doc, tel, fecha) VALUES (%s,%s,%s,%s)", (name, id_, tele, bdate))
        except Exception as e:
            print(e)
class MainApp(App):
    title = "Sistema de Suministro Automatizado de Medicamentos"
    def build(self):
        return SSAM()
if __name__ == '__main__':
    MainApp().run()
