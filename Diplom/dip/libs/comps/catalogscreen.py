from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from libs.comps.carcard import CarCard
from libs.add.bd import *

class CatalogScreen(MDScreen):
    
    # генерация карточек автомобилей
    def generate_notes(self):
        # создание записей и добавление их на страницу
        car_data = read('cars')
        photos = read("cars_photos")
        try:
            self.ids.list.clear_widgets()
        except Exception as ex:
            print(ex)
        for i in range(len(car_data)):
            self.ids.list.add_widget(CarCard(id_=car_data[i]['id_car'],
            name=car_data[i]['car_brand']+
            ' '+car_data[i]['car_model']+' '+car_data[i]['car_release_year'],image=(photos[i]['car_photo']).decode("utf-8"),
            price=f"Цена: {car_data[i]['car_price']}р.",horsepower=f"Л.С.: {car_data[i]['car_eng_power']}",privod=f"Привод: {car_data[i]['car_wheel_drive']}"))