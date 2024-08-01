from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex
from libs.settings.settings import Colors
from kivymd.app import MDApp
from libs.comps.add_manager_button import Manager_button
from libs.add.bd import *
import json

class LoginScreen(MDScreen):
    def focus(self):
        self.ids.login.line_color_normal = get_color_from_hex(Colors().darktext)
        self.ids.login.hint_text_color_normal = get_color_from_hex(Colors().darktext)
    
    def check_data(self):
        # получение данных из полей
        login = self.ids.login._get_text()
        password = self.ids.password._get_text()
        # проверка на существование данных
        if login and password:
            #переход на другой экран
            client_data = read('clients')
            manager_data = read('managers')
            for i in range(len(client_data)):
                if (login == client_data[i]['client_login'] and password == client_data[i]['client_password']):
                    MDApp.get_running_app().screens.ids.screenmanager.current = 'mainscreen'
                    with open("id_client.json", "w") as f:
                        json.dump({"id": client_data[i]['id_client']}, f)
                else:
                    pass
            for i in range(len(manager_data)):
                if (login == manager_data[i]['manager_login'] and password == manager_data[i]['manager_password']):
                    MDApp.get_running_app().screens.ids.screenmanager.current = 'mainscreen'
                    MDApp.get_running_app().screens.ids.mainscreen.ids.navbar.ids.buttons.add_widget(Manager_button())
                    with open("id_manager.json", "w") as f:
                        json.dump({"id": manager_data[i]['id_manager']}, f)
                else:
                    pass
        else:
            pass

def read_identified_id_client():
    with open("id_client.json", "r") as f:
        data = json.load(f)
        id_client = data.get("id")
        return(id_client)
    
def clear_identified_id_client():
    with open("id_client.json", "r") as f:
        pass

def read_identified_id_manager():
    with open("id_manager.json", "r") as f:
        data = json.load(f)
        id_manager = data.get("id")
        return(id_manager)
    
def clear_identified_id_manager():
    with open("id_manager.json", "r") as f:
        pass