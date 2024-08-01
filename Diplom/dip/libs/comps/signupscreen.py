from kivymd.uix.screen import MDScreen
import re
from kivy.utils import get_color_from_hex
from libs.settings.settings import Colors
from kivymd.app import MDApp
from libs.add.bd import *
import json

class SignupScreen(MDScreen):

    def validate_email(self, email):
        if re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return True
        else:
            return False
        
    def focus(self):
        self.ids.login.line_color_normal = get_color_from_hex(Colors().darktext)
        self.ids.login.hint_text_color_normal = get_color_from_hex(Colors().darktext)
        self.ids.password.line_color_normal = get_color_from_hex(Colors().darktext)
        self.ids.password.hint_text_color_normal = get_color_from_hex(Colors().darktext)
        self.ids.name.line_color_normal = get_color_from_hex(Colors().darktext)
        self.ids.name.hint_text_color_normal = get_color_from_hex(Colors().darktext)
        self.ids.surname.line_color_normal = get_color_from_hex(Colors().darktext)
        self.ids.surname.hint_text_color_normal = get_color_from_hex(Colors().darktext)

    
    def check_data(self):
        # получение данных из полей
        check = 0
        name = self.ids.name._get_text()
        surname = self.ids.surname._get_text()
        login = self.ids.login._get_text()
        password = self.ids.password._get_text()
        # проверка на существование данных
        if name and surname and login and password:
            # запись в бд а так же переход на другой экран
            client_data = read('clients')
            # проверка на существование логина в базе данных
            for i in range(len(client_data)):
                if (login != client_data[i]['client_login']):
                    check = 1
                else:
                    pass
            if (check == 1):
                columns = "client_surname, client_name, client_login, client_password"
                values = (surname, name, login, password)
                insert('clients', columns, values)
                MDApp.get_running_app().screens.ids.screenmanager.current = 'mainscreen'    
            print(check)    
        else:
            pass