import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

class MainWid(ScreenManager):
    wid1 = StringProperty("")
    def to_screen_c(self):
        self.wid1 = "screen_c"
        print (self.wid1)
class UnaScreen(Screen):
    pass

class MainApp(App):
    title = "Screen Manager"
    def build(self):
        return MainWid()

if __name__ == "__main__":
    MainApp().run()
