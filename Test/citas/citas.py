from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from utils.datatable import DataTable
from collections import OrderedDict
from kivy.app import App
import re
import mysql.connector
import datetime

from kivy.lang import Builder

Builder.load_file('citas/citas.kv')

# dbConnect = {
#     'host':'localhost',
#     'user':'johanaltro',
#     'password':'jar12345',
#     'database':'bioing_project',
#     'port': 5306}
dbConnect = {
    'host':'remotemysql.com',
    'user':'qwQlvSlWFi',
    'password':'F3MLpKNrdf',
    'database':'qwQlvSlWFi',
    'port': 3306}
class FlatButton(ButtonBehavior):
    pass
class citasWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.conn = mysql.connector.connect(**dbConnect)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS citas (cod varchar(16),nombre varchar(16),freq varchar(16),qty varchar(16),fecha date, hora time)")
        #self.cursor.execute("TRUNCATE TABLE citas")
        content = self.ids.products
        meds = self.get_medicines()
        medsTable = DataTable(table=meds)
        content.add_widget(medsTable)
    def logout(self):
        self.parent.parent.current = "scrn_si"
    def find_pax(self):
        def edad(naci):
            hoy = datetime.date.today()
            if hoy < naci:
                print ('error en la fecha de nacimiento')
            else:
                ano = naci.year
                mes = naci.month
                dia = naci.day

                fecha = naci
                edad = 0
                while fecha < hoy:
                    edad += 1
                    fecha = datetime.date(ano+edad, mes, dia)

                #print 'Mi edad es: %s' % (edad-1)
            return (edad-1)
        self.conn = mysql.connector.connect(**dbConnect)
        self.cursor = self.conn.cursor()

        id_number = self.ids.pax_id.text
        self.cursor.execute('SELECT * FROM pacientes WHERE documento =%s',[id_number])
        user = self.cursor.fetchall()

        self.nacimiento = user[0][5]
        self.edad = edad(self.nacimiento)

        self.ids.pax_id.text = user[0][1]
        self.ids.pax_name.text=user[0][2]
        self.ids.pax_last_name.text=user[0][3]
        self.ids.pax_weight.text=user[0][4]
        self.ids.pax_bday.text= self.nacimiento.strftime('%Y-%m-%d')

        self.ids.cur_pax_name.text = (user[0][2] +" "+ user[0][3])
        self.ids.cur_pax_age.text = (str(self.edad) + " Años")
        self.ids.cur_pax_weight.text = (user[0][4] + " Kg")
    def update_pax(self):
        self.conn = mysql.connector.connect(**dbConnect)
        self.cursor = self.conn.cursor()

        documento = self.ids.pax_id.text
        nombre = self.ids.pax_name.text
        apellido = self.ids.pax_last_name.text
        peso = self.ids.pax_weight.text
        nac = self.ids.pax_bday.text

        sql='''UPDATE pacientes SET documento= %s,nombre=%s,apellido=%s,peso=%s,
                nacimiento=%s WHERE documento = %s'''
        self.cursor.execute(sql,(documento,nombre,apellido,peso,nac,documento))
        self.conn.commit()

        self.ids.cur_pax_name.text = (nombre +" "+ apellido)
        self.ids.cur_pax_age.text = nac
        self.ids.cur_pax_weight.text = (peso + " Kg")
    def schedule_medicines(self):
        target=self.ids.programar_medicinas
        target.clear_widgets()
        # flat = FlatButton()
        agregar = Button(text='Agregar',on_release=lambda x:self.add_medicine_fields())
        modificar = Button(text='Modificar',on_release=lambda x:self.update_medicine_fields())
        borrar = Button(text='Borrar',on_release=lambda x:self.remove_medicine_fields())

        # target.add_widget(flat)
        if (self.ids.pax_id.text) != (''):
            target.add_widget(agregar)
            target.add_widget(modificar)
            target.add_widget(borrar)
            self.conn = mysql.connector.connect(**dbConnect)
            self.cursor = self.conn.cursor()
            Table_name = "schedule_medicines"
            sql = ("CREATE TABLE IF NOT EXISTS %s (pax_user varchar(45), cod varchar(45),ch varchar(45),fecha DATE,hora TIME)" %Table_name)
            self.cursor.execute(sql)

    def add_medicine_fields(self):
        hoy =datetime.datetime.today().strftime('%Y-%m-%d')
        target = self.ids.medecine_boxlayout
        target.clear_widgets()
        crud_code = TextInput(hint_text='Codigo',size_hint_x=0.15,multiline=False)
        crud_name = TextInput(id='buscada',hint_text='Medicamento',size_hint_x=0.25)
        crud_freq = TextInput(hint_text='Freq',size_hint_x=0.085)
        crud_qty = TextInput(hint_text='Qty',size_hint_x=0.075)
        crud_fecha_inicio = TextInput(text=hoy,hint_text='Fecha',size_hint_x=0.2)
        crud_hora_inicio = TextInput(hint_text='Hora',size_hint_x=0.09)
        crud_submit = Button(text='Añadir',on_release=lambda x:
        self.add_medicine(crud_code.text,crud_freq.text,crud_qty.text,
        crud_fecha_inicio.text,crud_hora_inicio.text),size_hint_x=0.15)

        target.add_widget(crud_code)
        target.add_widget(crud_name)
        target.add_widget(crud_freq)
        target.add_widget(crud_qty)
        target.add_widget(crud_fecha_inicio)
        target.add_widget(crud_hora_inicio)
        target.add_widget(crud_submit)
    def update_medicine_fields(self):
        hoy =datetime.datetime.today().strftime('%Y-%m-%d')
        target = self.ids.medecine_boxlayout
        target.clear_widgets()
        crud_code = TextInput(hint_text='Codigo',size_hint_x=0.15)
        crud_name = TextInput(hint_text='Medicamento',size_hint_x=0.25)
        crud_freq = TextInput(hint_text='Freq',size_hint_x=0.085)
        crud_qty = TextInput(hint_text='Qty',size_hint_x=0.075)
        crud_fecha_inicio = TextInput(text = hoy,hint_text='Fecha',size_hint_x=0.2)
        crud_hora_inicio = TextInput(hint_text='Hora',size_hint_x=0.09)
        crud_submit = Button(text='Cambiar',on_release=lambda x:
        self.update_medicine(crud_code.text,crud_freq.text,
        crud_qty.text,crud_fecha_inicio.text,crud_hora_inicio.text),size_hint_x=0.15)

        target.add_widget(crud_code)
        # target.add_widget(crud_name)
        target.add_widget(crud_freq)
        target.add_widget(crud_qty)
        target.add_widget(crud_fecha_inicio)
        target.add_widget(crud_hora_inicio)
        target.add_widget(crud_submit)
    def remove_medicine_fields(self):
        target = self.ids.medecine_boxlayout
        target.clear_widgets()
        crud_code = TextInput(hint_text='Codigo',size_hint_x=0.15)
        crud_name = TextInput(hint_text='Medicamento',size_hint_x=0.25)
        crud_submit = Button(text='Quitar',on_release=lambda x:
        self.remove_medicine(crud_code.text),size_hint_x=0.1)

        target.add_widget(crud_code)
        #target.add_widget(crud_name)
        target.add_widget(crud_submit)

    def add_medicine(self,cd,fr,qt,st,hr):
        content = self.ids.products
        content.clear_widgets()
        self.conn = mysql.connector.connect(**dbConnect)
        self.cursor = self.conn.cursor()
        #BUSQUEDA DE MEDICAMENTO EN DB
        self.cursor.execute("SELECT product_name FROM stocks WHERE product_code =%s",[cd])
        nm = self.cursor.fetchall()

        sql = ("INSERT INTO citas(cod, nombre, freq, qty, fecha, hora) VALUES (%s,%s,%s,%s,%s,%s)")
        valores = (cd,nm[0][0],fr,qt,st,hr)
        self.cursor.execute(sql,valores)
        self.conn.commit()
        meds = self.get_medicines()
        medsTable = DataTable(table=meds)
        content.add_widget(medsTable)

        self.ids.medecine_boxlayout.clear_widgets()
    def update_medicine(self,cd,fr,qt,st,hr):
        content = self.ids.products
        content.clear_widgets()
        self.conn = mysql.connector.connect(**dbConnect)
        self.cursor = self.conn.cursor()

        sql = ("UPDATE citas SET cod=%s,freq=%s,qty=%s,fecha=%s, hora=%s WHERE cod = %s")
        valores = (cd,fr,qt,st,hr,cd)
        self.cursor.execute(sql,valores)
        self.conn.commit()
        meds = self.get_medicines()
        medsTable = DataTable(table=meds)
        content.add_widget(medsTable)
        self.ids.medecine_boxlayout.clear_widgets()
    def remove_medicine(self,cd):
        content = self.ids.products
        content.clear_widgets()

        sql = "DELETE FROM citas WHERE cod = %s"
        self.cursor.execute(sql,[cd])
        self.conn.commit()
        meds = self.get_medicines()
        medsTable = DataTable(table=meds)
        content.add_widget(medsTable)
        self.ids.medecine_boxlayout.clear_widgets()

    def end_visit(self):
        conn = mysql.connector.connect(**dbConnect)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM citas")
        meds = cursor.fetchall()
        user = self.ids.pax_id.text
        for i in range(len(meds)):
            timestr = (datetime.datetime.min + meds[i][5]).strftime("%H:%M")
            timedtime =datetime.datetime.strptime(timestr,'%H:%M').time()

            time = datetime.datetime.combine(meds[i][4],timedtime)
            # print(time)

            freq = int(meds[i][2])
            qty = int(meds[i][3])
            # print(freq)
            # print(qty)
            for j in range(qty):
                sql = "INSERT INTO schedule_medicines VALUES (%s,%s,%s,%s,%s,%s)"
                values = (user,meds[i][0],meds[i][6],time,True,False)
                cursor.execute(sql,values)
                conn.commit()
                #print(values)
                time = time + datetime.timedelta(hours=freq)
        self.ids.pax_id.text = ''
        self.ids.pax_name.text = ''
        self.ids.pax_last_name.text = ''
        self.ids.pax_weight.text = ''
        self.ids.pax_bday.text = ''

        self.ids.cur_pax_name.text = ''
        self.ids.cur_pax_age.text = ''
        self.ids.cur_pax_weight.text = ''

        cursor.execute("TRUNCATE TABLE citas")

        self.ids.products.clear_widgets()
        self.ids.medecine_boxlayout.clear_widgets()
        self.ids.programar_medicinas.clear_widgets()
        content = self.ids.products
        meds = self.get_medicines()
        medsTable = DataTable(table=meds)
        content.add_widget(medsTable)


    def get_medicines(self):
        conn = mysql.connector.connect(**dbConnect)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM citas")
        meds = cursor.fetchall()
        _meds = OrderedDict(
            Codigo =   {},
            Medicamento =    {},
            Freq =    {},
            Total =     {},
            Inicio =  {},
            Hora = {}
        )
        cod =   []
        name =    []
        freq =    []
        qty =     []
        start =  []
        hour = []

        for i in range (len(meds)):
            cod.append(meds[i][0])
            name.append(meds[i][1])
            freq.append(meds[i][2])
            qty.append(meds[i][3])
            start.append(meds[i][4])
            hour.append(meds[i][5])
        meds_length = len(cod)
        idx = 0
        while idx < meds_length:
            _meds['Codigo'][idx] = cod[idx]
            _meds['Medicamento'][idx] = name[idx]
            _meds['Freq'][idx] = freq[idx]
            _meds['Total'][idx] = qty[idx]
            _meds['Inicio'][idx] = start[idx]
            _meds['Hora'][idx] = hour[idx]
            idx+=1
        return _meds

class citasApp(App):
    title = 'Programacion de Medicamentos'
    def build(self):
        return citasWindow()

if __name__ == '__main__':
    citasApp().run()
