import mysql.connector

dbConnect = {
    'host':'localhost',
    'user':'johanaltro',
    'password':'jar12345',
    'database':'bioing_project', #por crear
    'port': 5306
    }
conn = mysql.connector.connect(**dbConnect)
cursor = conn.cursor()

# try:
#     with con:
#         cursor.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
#         cursor.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
#         cursor.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
#         cursor.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
#         cursor.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
#         cursor.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
#         cursor.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
#         cursor.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
#         cursor.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
# except:
#     pass


from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty


Builder.load_string("""

<MyLayout>:
    Button:
        text: "Get data"
        on_press: root.get_data()
        size_hint: 0.05, None
        height: 100
    RecycleView:
        id: rv
        size_hint_x: 0.95
        data: [{'text':"Id:{} Name:{} Stock:{} Sold:{} Order:{} Last_purchase:{}".format(product_code,product_name,in_stock,sold, order, last_purchase)} for product_code,product_name,in_stock,sold, order, last_purchase in root.rows]
        viewclass: "Label"
        RecycleBoxLayout:
            default_size: None, dp(56)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'

""")


class MyLayout(BoxLayout):
    rows = ListProperty([("product_code","product_name","in_stock","sold","order","last_purchase")])
    def get_data(self):
        cursor.execute("SELECT * FROM stocks")
        self.rows = cursor.fetchall()
        print(self.rows)


runTouchApp(MyLayout())
