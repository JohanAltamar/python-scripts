from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

import mysql.connector
from collections import OrderedDict

dbConnect = {
    'host':'localhost',
    'user':'johanaltro',
    'password':'jar12345',
    'database':'bioing_project', #por crear
    'port': 5306
    }

Builder.load_string('''
<DataTable>:
    id: main_win
    RecycleView:
        viewclass: 'CustLabel'
        id: table_floor
        RecycleGridLayout:
            id:table_floor_layout
            cols: 5
            default_size: (None, 250)
            default_size_hint: (1, None)
            size_hint_y: None
            height: self.minimum_height
            spacing: 5
<CustLabel@Label>:
    bcolor:(1,1,1,1)
    canvas.before:
        Color:
            rgba: root.bcolor
        Rectangle:
            size: self.size
            pos:self.pos
''')
class DataTable(BoxLayout):
    def __init__(self,table ='', **kwargs):
        super().__init__(**kwargs)

        #products = self.get_products()
        products = table
        col_titles = [k for k in products.keys()]
        rows_len = len(products[col_titles[0]])
        self.columns = (len(col_titles))
        #print(rows_len)
        table_data = []
        for t in col_titles:
            table_data.append({'text':str(t),'size_hint_y':None,'height':50,'bcolor':(.59, .20, .63, 1)})
        for r in range(rows_len):
            for t in col_titles:
                table_data.append({'text':str(products[t][r]),'size_hint_y':None,'height':30, 'bcolor':(.30, .20, .35, 1)})
        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data
    #
    # def get_products(self):
    #     conn = mysql.connector.connect(**dbConnect)
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT * FROM stocks")
    #     stocks = cursor.fetchall()
    #     _stocks = OrderedDict()
    #     _stocks['product_code'] =  {}
    #     _stocks['product_name'] =  {}
    #     _stocks['in_stock'] =      {}
    #     _stocks['sold'] =          {}
    #     _stocks['order'] =         {}
    #     _stocks['last_purchase'] = {}
    #     product_code =  []
    #     product_name =  []
    #     in_stock =      []
    #     sold =          []
    #     order =         []
    #     last_purchase = []
    #     for i in range(len(stocks)):
    #         product_code.append(stocks[i][0])
    #         product_name.append(stocks[i][1])
    #         in_stock.append(stocks[i][2])
    #         sold.append(stocks[i][3])
    #         order.append(stocks[i][4])
    #         last_purchase.append(stocks[i][5])
    #     products_length = len(product_code)
    #     idx = 0
    #     while idx < products_length:
    #         _stocks['product_code'][idx] = product_code[idx]
    #         _stocks['product_name'][idx] = product_name[idx]
    #         _stocks['in_stock'][idx] = in_stock[idx]
    #         _stocks['sold'][idx] = sold[idx]
    #         _stocks['order'][idx] = order[idx]
    #         _stocks['last_purchase'][idx] = last_purchase[idx]
    #         idx += 1
    #     return _stocks
    #
# class DataTableApp(App):
#     def build(self):
#         return DataTableWindow()
#
# if __name__ == '__main__':
#     DataTableApp().run()
