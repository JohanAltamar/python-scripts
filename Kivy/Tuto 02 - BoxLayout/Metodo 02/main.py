import kivy
kivy.require('1.9.2')

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout

class Box01(BoxLayout):
	def __init__(self):
		super(Box01,self).__init__()
		self.BR = BoxRed()
		self.BG = BoxGreen()
		self.BB = BoxBlue()

		self.BR.add_widget(BoxBlue())
		self.BR.add_widget(BoxBlue())

		self.BG.add_widget(self.BB)

		self.add_widget(self.BR)
		#self.add_widget(BoxLayout()) #Crea espacio en blanco
		self.add_widget(self.BG)

class BoxGreen(BoxLayout):
	None

class BoxRed(BoxLayout):
	None

class BoxBlue(BoxLayout):
	None


class MainApp(App):
	title = 'BoxLayout Metodo 02'
	def build(self):
		return Box01()

if __name__ == "__main__":
	MainApp().run()
