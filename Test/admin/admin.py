import mysql.connector
import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from collections import OrderedDict
from utils.datatable import DataTable
import hashlib
from kivy.lang import Builder

Builder.load_file('admin/admin.kv')


# dbConnect = {
#     'host':'localhost',
#     'user':'johanaltro',
#     'password':'jar12345',
#     'database':'bioing_project', #por crear
#     'port': 5306}
dbConnect = {
    'host':'remotemysql.com',
    'user':'qwQlvSlWFi',
    'password':'F3MLpKNrdf',
    'database':'qwQlvSlWFi',
    'port': 3306}

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.conn = mysql.connector.connect(**dbConnect)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM users")
        self.users = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM stocks")
        self.stocks = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM pacientes")
        self.stocks = self.cursor.fetchall()

        product_code = []
        product_name = []
        spinvals = []
        for i in range(len(self.stocks)):
            product_code.append(str(self.stocks[i][0]))
            name = self.stocks[i][1]
            if len(name)>30:
                name = name[:30]+'...'
            product_name.append(name)
        for x in range(len(product_code)):
            line = ' | '.join([product_code[x],product_name[x]])
            spinvals.append(line)
        self.ids.target_product.values = spinvals

        #Display Users
        content = self.ids.scrn_contents
        users = self.get_users()
        usersTable = DataTable(table=users)
        content.add_widget(usersTable)
        #Display pax
        pax_content = self.ids.scrn_pax
        pax = self.get_pax()
        paxTable = DataTable(table=pax)
        pax_content.add_widget(paxTable)
        #DisplayProducts
        product_scrn = self.ids.scrn_product_contents
        products = self.get_products()
        productsTable = DataTable(table=products)
        product_scrn.add_widget(productsTable)

    def logout(self):
        self.parent.parent.current = 'scrn_si'
    def user_or_pax(self):
        pax_fields = self.ids.target_user.text
        if (pax_fields == "Paciente"):
            print("Es paciente")
            self.add_pax_fields()
        elif(pax_fields == "Usuario"):
            print("Es usuario")
            self.add_user_fields()
    def add_pax_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_id = TextInput(hint_text='Documento')
        crud_first_ = TextInput(hint_text='Nombre')
        crud_last_ = TextInput(hint_text='Apellido')
        crud_weight = TextInput(hint_text='Peso')
        crud_nacimiento = TextInput(hint_text='F.Nac.')
        crud_tel = TextInput(hint_text='Tel')
        crud_submit_ = Button(text ='Agregar',size_hint_x=None,width=100,on_release= lambda x:
        self.add_pax(crud_id.text,crud_first_.text,crud_last_.text,crud_weight.text,crud_nacimiento.text,crud_tel.text))

        target.add_widget(crud_id)
        target.add_widget(crud_first_)
        target.add_widget(crud_last_)
        target.add_widget(crud_weight)
        target.add_widget(crud_nacimiento)
        target.add_widget(crud_tel)
        target.add_widget(crud_submit_)
    def add_pax(self,id_n,first_n,last_n,weight,nacimiento,tel):
        content = self.ids.scrn_pax
        content.clear_widgets()
        self.cursor.execute("INSERT INTO pacientes(documento,nombre,apellido,peso,nacimiento,Telefono) VALUES(%s,%s,%s,%s,%s,%s)",(id_n,first_n,last_n,weight,nacimiento,tel))
        self.conn.commit()
        pax = self.get_pax()
        paxTable = DataTable(table=pax)
        content.add_widget(paxTable)
    def add_user_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_first = TextInput(hint_text='Nombre')
        crud_last = TextInput(hint_text='Apellido')
        crud_user = TextInput(hint_text='Usuario')
        crud_password = TextInput(hint_text='Password')
        crud_des = Spinner(text='Operador',values=['Operador','Administrador','Paciente'])
        crud_submit = Button(text ='Agregar',size_hint_x=None,width=100,on_release= lambda x:
        self.add_user(crud_first.text,crud_last.text,crud_user.text,crud_password.text,
        crud_des.text))

        target.add_widget(crud_first)
        target.add_widget(crud_last)
        target.add_widget(crud_user)
        target.add_widget(crud_password)
        target.add_widget(crud_des)
        target.add_widget(crud_submit)
    def add_user(self,first,last,user,pwd,des):
        content = self.ids.scrn_contents
        content.clear_widgets()
        pwd = hashlib.sha256(pwd.encode()).hexdigest()
        self.cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s)",(first,last,user,pwd,des,datetime.datetime.now()))
        self.conn.commit()
        users = self.get_users()
        usersTable = DataTable(table=users)
        content.add_widget(usersTable)
    def update_user_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_first = TextInput(hint_text='Nombre')
        crud_last = TextInput(hint_text='Apellido')
        crud_user = TextInput(hint_text='Usuario')
        crud_password = TextInput(hint_text='Password')
        crud_des = Spinner(text='Operador',values=['Operador','Administrador','Paciente'])
        crud_submit = Button(text ='Cambiar',size_hint_x=None,width=100,on_release= lambda x:
        self.update_user(crud_first.text,crud_last.text,crud_user.text,crud_password.text,
        crud_des.text))

        target.add_widget(crud_first)
        target.add_widget(crud_last)
        target.add_widget(crud_user)
        target.add_widget(crud_password)
        target.add_widget(crud_des)
        target.add_widget(crud_submit)
    def update_user(self,first,last,user,pwd,des):
        content = self.ids.scrn_contents
        content.clear_widgets()
        pwd = hashlib.sha256(pwd.encode()).hexdigest()
        self.cursor.execute("UPDATE users SET first_name = %s,last_name = %s, username = %s, password = %s, designations = %s WHERE username = %s",(first,last,user,pwd,des,user))
        self.conn.commit()
        users = self.get_users()
        usersTable = DataTable(table=users)
        content.add_widget(usersTable)
    def remove_user_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_user = TextInput(hint_text='Usuario')
        crud_submit = Button(text ='Eliminar',size_hint_x=None,width=100,on_release= lambda x:
        self.remove_user(crud_user.text))

        target.add_widget(crud_user)
        target.add_widget(crud_submit)
    def remove_user(self,user):
        content = self.ids.scrn_contents
        content.clear_widgets()
        self.cursor.execute("DELETE FROM users WHERE username = %s",[user])
        self.conn.commit()
        users = self.get_users()
        usersTable = DataTable(table=users)
        content.add_widget(usersTable)

    def get_pax(self):
        conn = mysql.connector.connect(**dbConnect)
        cursor = conn.cursor()
        cursor.execute("SELECT documento,nombre,apellido,peso,nacimiento,Telefono FROM pacientes")
        users = cursor.fetchall()
        _users = OrderedDict(
            Documento =    {},
            Nombre =   {},
            Apellido =    {},
            Peso =    {},
            FNacimiento =     {},
            Telefono =  {}
        )
        id_numbers =    []
        first_names =   []
        last_names =    []
        user_names =    []
        passwords =     []
        designations =  []

        for i in range(len(users)):
            id_numbers.append(users[i][0])
            first_names.append(users[i][1])
            last_names.append(users[i][2])
            user_names.append(users[i][3])
            passwords.append(users[i][4])
            designations.append(users[i][5])


        users_length = len(first_names)
        idx = 0
        while idx < users_length:
            _users['Documento'][idx] = id_numbers[idx]
            _users['Nombre'][idx] = first_names[idx]
            _users['Apellido'][idx] = last_names[idx]
            _users['Peso'][idx] = user_names[idx]
            _users['FNacimiento'][idx] = passwords[idx]
            _users['Telefono'][idx] = designations[idx]
            idx += 1
        return _users
    def get_users(self):
        conn = mysql.connector.connect(**dbConnect)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        __users = OrderedDict(
            Nombre =   {},
            Apellido =    {},
            Usuario =    {},
            Password =     {},
            Rol =  {},
            FCreacion = {}
        )
        first_names =   []
        last_names =    []
        user_names =    []
        passwords =     []
        designations =  []
        creation_date = []
        for i in range(len(users)):
            first_names.append(users[i][0])
            last_names.append(users[i][1])
            user_names.append(users[i][2])
            pwd = users[i][3]
            if len(pwd) > 10:
                pwd = pwd[:10]+'...'
            passwords.append(pwd)
            designations.append(users[i][4])
            creation_date.append(users[i][5])

        users_length = len(first_names)
        idx = 0
        while idx < users_length:
            __users['Nombre'][idx] = first_names[idx]
            __users['Apellido'][idx] = last_names[idx]
            __users['Usuario'][idx] = user_names[idx]
            __users['Password'][idx] = passwords[idx]
            __users['Rol'][idx] = designations[idx]
            __users['FCreacion'][idx] = creation_date[idx]
            idx += 1
        return __users

    def add_product_fields(self):
        target = self.ids.ops_fields_P
        target.clear_widgets()
        crud_code = TextInput(hint_text='Codigo')
        crud_name = TextInput(hint_text='Nombre')
        crud_stock = TextInput(hint_text='En Stock')
        crud_sold = TextInput(hint_text='Vendidos')
        crud_order = TextInput(hint_text='Ult Venta')
        crud_purchase = TextInput(hint_text='Ult Pedido')
        crud_submit = Button(text ='Agregar',size_hint_x=None,width=100,on_release= lambda x:
        self.add_product(crud_code.text,crud_name.text,crud_stock.text,crud_sold.text,crud_order.text,crud_purchase.text))

        target.add_widget(crud_code)
        target.add_widget(crud_name)
        target.add_widget(crud_stock)
        target.add_widget(crud_sold)
        target.add_widget(crud_order)
        target.add_widget(crud_purchase)
        target.add_widget(crud_submit)
    def add_product(self,code,name,in_stock,sold,order,last_purchase):
        content = self.ids.scrn_product_contents
        content.clear_widgets()
        if sold == '':
            sold = 0
        if order == '':
            order = None
        if last_purchase == '':
            last_purchase = None
        self.cursor.execute("INSERT INTO stocks VALUES(%s,%s,%s,%s,%s,%s)",(code,name,int(in_stock),int(sold),order,last_purchase))
        self.conn.commit()
        products = self.get_products()
        productsTable = DataTable(table=products)
        content.add_widget(productsTable)
    def update_product_fields(self):
        target = self.ids.ops_fields_P
        target.clear_widgets()
        crud_code = TextInput(hint_text='Codigo')
        crud_name = TextInput(hint_text='Nombre')
        crud_stock = TextInput(hint_text='En Stock')
        crud_sold = TextInput(hint_text='Vendidos')
        crud_order = TextInput(hint_text='Ult Venta')
        crud_purchase = TextInput(hint_text='Ult Pedido')
        crud_submit = Button(text ='Modificar',size_hint_x=None,width=100,on_release= lambda x:
        self.update_product(crud_code.text,crud_name.text,crud_stock.text,crud_sold.text,crud_order.text,crud_purchase.text))

        target.add_widget(crud_code)
        target.add_widget(crud_name)
        target.add_widget(crud_stock)
        target.add_widget(crud_sold)
        target.add_widget(crud_order)
        target.add_widget(crud_purchase)
        target.add_widget(crud_submit)
    def update_product(self,code,name,in_stock,sold,order,last_purchase):
        content = self.ids.scrn_product_contents
        content.clear_widgets()
        if sold == '':
            sold = 0
        if order == '':
            order = None
        if last_purchase == '':
            last_purchase = None
        self.cursor.execute("UPDATE stocks SET product_code=%s,product_name= %s,in_stock=%s,sold=%s,last_order=%s,last_purchase=%s WHERE product_code=%s",(int(code),name,int(in_stock),int(sold),order,last_purchase,int(code)))
        self.conn.commit()
        products = self.get_products()
        productsTable = DataTable(table=products)
        content.add_widget(productsTable)
    def remove_product_fields(self):
        target = self.ids.ops_fields_P
        target.clear_widgets()
        crud_code = TextInput(hint_text='Codigo del Producto')
        crud_submit = Button(text ='Eliminar',size_hint_x=None,width=100,on_release= lambda x:
        self.remove_product(crud_code.text))

        target.add_widget(crud_code)
        target.add_widget(crud_submit)
    def remove_product(self,code):
        content = self.ids.scrn_product_contents
        content.clear_widgets()
        self.cursor.execute("DELETE FROM stocks WHERE product_code = %s",[int(code)])
        self.conn.commit()
        products = self.get_products()
        productsTable = DataTable(table=products)
        content.add_widget(productsTable)
    def get_products(self):
        conn = mysql.connector.connect(**dbConnect)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stocks")
        stocks = cursor.fetchall()
        _stocks = OrderedDict()
        _stocks['product_code'] =  {}
        _stocks['product_name'] =  {}
        _stocks['in_stock'] =      {}
        _stocks['sold'] =          {}
        _stocks['order'] =         {}
        _stocks['last_purchase'] = {}
        product_code =  []
        product_name =  []
        in_stock =      []
        sold =          []
        order =         []
        last_purchase = []
        for i in range(len(stocks)):
            product_code.append(stocks[i][0])
            name = stocks[i][1]
            if len(name)>10:
                name = name[:10]+'...'
            product_name.append(name)
            in_stock.append(stocks[i][2])
            sold.append(stocks[i][3])
            order.append(stocks[i][4])
            last_purchase.append(stocks[i][5])
            # try:
            #     sold.append(stocks[i][3])
            # except KeyError:
            #     sold.append('')
            # try:
            #     order.append(stocks[i][4])
            # except KeyError:
            #     order.append('')
            # try:
            #     last_purchase.append(stocks[i][5])
            # except KeyError:
            #     last_purchase.append('')
        products_length = len(product_code)
        idx = 0
        while idx < products_length:
            _stocks['product_code'][idx] = product_code[idx]
            _stocks['product_name'][idx] = product_name[idx]
            _stocks['in_stock'][idx] = in_stock[idx]
            _stocks['sold'][idx] = sold[idx]
            _stocks['order'][idx] = order[idx]
            _stocks['last_purchase'][idx] = last_purchase[idx]
            idx += 1
        return _stocks

    def change_screen(self, instance):
        if instance.text == 'Manage Products':
            self.ids.scrn_mngr.current = 'scrn_product_content'
        elif instance.text == 'Manage Users':
            self.ids.scrn_mngr.current = 'scrn_content'
        else:
            self.ids.scrn_mngr.current = 'scrn_analysis'
class AdminApp(App):
    def build(self):
        return AdminWindow()

if __name__ == '__main__':
    AdminApp().run()
