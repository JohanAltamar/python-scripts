from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from admin.admin import AdminWindow
from signin.signin import SigninWindow
from citas.citas import citasWindow

class MainWindow(BoxLayout):
    admin_widget = AdminWindow()
    signin_widget = SigninWindow()
    citas_widget = citasWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.scrn_si.add_widget(self.signin_widget)
        self.ids.scrn_admin.add_widget(self.admin_widget)
        self.ids.scrn_citas.add_widget(self.citas_widget)

class MainApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    MainApp().run()
