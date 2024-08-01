from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from kivy.metrics import dp
from kivymd.theming import ThemeManager
from libs.add.bd import *
from libs.comps.loginscreen import read_identified_id_client
import random

class DialogWindow(MDBoxLayout):

    card_id = None
    def __init__(self, card_id):
        super(DialogWindow, self).__init__(card_id)
        self.card_id = card_id
    # получение данных из полей проверка данных из полей и запись данных в бд
    def register(self):
        self.time = self.ids.time._get_text()
        self.date = self.ids.date._get_text()
        if self.time and self.date:
            car_id = self.card_id
            date = self.date
            time = self.time
            client_id = read_identified_id_client()
            # manager_data = read('managers')
            # manager_id = random.randint(1,len(manager_data))
            columns = "view_data, view_time,  Clients_id_client, Cars_id_car"
            values = (date, time,  client_id, car_id)
            insert('views', columns, values)
            self.parent.parent.parent.dismiss()

class OfferWindow(MDBoxLayout):
    pass
