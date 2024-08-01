from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from libs.comps.note import Note
from libs.add.bd import *
from libs.comps.loginscreen import read_identified_id_client,clear_identified_id_client,read_identified_id_manager

class UserScreen(MDScreen):
    # выход из профиля

    def exit(self):
        # переключения экрана
        MDApp.get_running_app().screens.ids.screenmanager.current = 'loginscreen'
        clear_identified_id_client()

    # генерация записейна осмотр бибики
    def generate_notes(self):
        # пример записей и добавление их на страницу
        views_data = read('views')
        client_data = read('clients')
        id_client = read_identified_id_client()
        try:
            self.ids.list.clear_widgets()
        except Exception as ex:
            print(ex)
        for i in range(len(client_data)):
            if (client_data[i]['id_client'] == id_client):
                self.ids.usersurname.text = client_data[i]['client_surname']
                self.ids.username.text = client_data[i]['client_name']
        for i in range(len(views_data)):
            if (views_data[i]['Clients_id_client'] == id_client):
                self.ids.list.add_widget(Note(id=views_data[i]['id_view'], date=views_data[i]['view_data'], time=views_data[i]['view_time']))