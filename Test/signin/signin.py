# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import mysql.connector
import hashlib

Builder.load_file('signin/signin.kv')

dbConnect = {
    'host':'remotemysql.com',
    'user':'qwQlvSlWFi',
    'password':'F3MLpKNrdf',
    'database':'qwQlvSlWFi',
    'port': 3306}

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def check_user(self,usern,passwd):
        passwd = hashlib.sha256(passwd.encode()).hexdigest()
        conn = mysql.connector.connect(**dbConnect)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",[usern,passwd])
        result = cursor.fetchall()
        print(result)
        if (usern == result[0][2]) and (passwd == result[0][3]):
            print ("Ingreso Exitoso")
            a = True
            # info.text = '[color=#00FF00]Ingreso exitoso!!![/color]'
            if(result[0][4] == 'Administrador'):
                self.parent.parent.current = 'scrn_admin'
            elif(result[0][4] == 'Operador'):
                self.parent.parent.current = 'scrn_citas'
                self.parent.parent.parent.ids.scrn_citas.children[0].ids.loggedin_user.text = usern
            else:
                print("Rol no encontrado")
        else:
            a = False
            print(usern)
            print(passwd)
            info.text = '[color=#FF0000]Usuario y/o Contraseña no coinciden[/color]'
        # a = False
        return a
    def validate_user(self):

        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        user.text = ''
        pwd.text = ''

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]Ingrese usuario y/o Contraseña[/color]'
        else:
            # if uname == 'admin' and passw == 'admin':
            a = self.check_user(uname,passw)
            if(a):
                #info.text = '[color=#00FF00]Ingreso exitoso!!![/color]'
                info.text = '[color=#FFFFFF] [/color]'
                #self.parent.parent.current = 'scrn_admin'
            else:
                info.text = '[color=#FF0000]Usuario y/o Contraseña no coinciden[/color]'
                passw = ''

class SigninApp(App):
    title = "SSAM"
    def build(self):
        return SigninWindow()

if __name__ == '__main__':
    SigninApp().run()
