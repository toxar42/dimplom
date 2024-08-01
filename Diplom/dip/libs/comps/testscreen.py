from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex
from libs.settings.settings import Colors
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from libs.comps.dialogcontent import OfferWindow
from libs.comps.carcard import CarCard
from kivymd.uix.button import MDFlatButton
from libs.add.ES import *
from libs.add.bd import *

class TestScreen(MDScreen):
    answers = []
    num = 0
    dialog = None
    # здесь текст вопросов который будет виден
    questions = ['Каковы ваши ежедневные потребности от автомобиля?', 
                 'В какой бюджет вы бы хотели уложиться?', 
                 'Какой тип кузова вам подходит?', 
                 'Для каких целей вы собираетесь использовать автомобиль?', 
                 'Какой привод в автомобиле вам нужен?']
    # ответы на вопросы
    buttons = {'вопрос1': ['комфорт', 'вместимость', 'экономичность'], 
               'вопрос2': ['1000000-2000000', '2000000-3000000', '3000000-4000000'], 
               'вопрос3': ['седан', 'универсал', 'кроссовер'], 
               'вопрос4': ['городские поездки', 'поездки загород', 'off-road приключения'], 
               'вопрос5': ['передний', 'задний', 'полный']}
    # функция для записи ответов на вопросы
    def write_answer(self, answer):
        self.num += 1
        self.answers.append(Fact(answer))
        self.ids.question_num.text = f'Вопрос {self.num + 1}'
        result = self.answers
        try:
            self.ids.question.text = self.questions[self.num]
            self.ids.answer_1.text = self.buttons[f'вопрос{self.num + 1}'][0]
            self.ids.answer_2.text = self.buttons[f'вопрос{self.num + 1}'][1]
            self.ids.answer_3.text = self.buttons[f'вопрос{self.num + 1}'][2]
        except Exception as ex:
            self.num = 0
            identify(result)
            self.open_offer()
            self.reload()

    # перезарядка теста
    def reload(self):
        self.answers.clear()
        self.ids.question_num.text = f'Вопрос {self.num + 1}'
        self.ids.question.text = self.questions[self.num]
        self.ids.answer_1.text = self.buttons[f'вопрос{self.num+1}'][0]
        self.ids.answer_2.text = self.buttons[f'вопрос{self.num+1}'][1]
        self.ids.answer_3.text = self.buttons[f'вопрос{self.num+1}'][2]
    
    def open_offer(self):
        # анализ по массиву ответов и открытие диалогового окна с предложением
        auto = read_identified_car()
        print(auto)
        car_data = read('cars')
        photos = read("cars_photos")
        for i in range(len(car_data)):
            if (auto == car_data[i]['car_brand']+' '+car_data[i]['car_model']+' '+car_data[i]['car_release_year']):
                self.open_dialog(car_data[i]['id_car'], car_data[i]['car_brand']+' '+car_data[i]['car_model']+' '+car_data[i]['car_release_year'],
                (photos[i]['car_photo']).decode("utf-8"),f"{car_data[i]['car_price']}",f"{car_data[i]['car_eng_power']}",f"{car_data[i]['car_wheel_drive']}")
                clear_identified_car()
                auto = ''
    # диалоговое окно
    def open_dialog(self, id_, name, image, price, hp, privod):
        self.dialog = None
        self.content = OfferWindow()
        offer = CarCard(id_=id_,name=name,image=image,price=f'Цена: {price}р.',horsepower=f'Л.С.: {hp}',privod=f'Привод: {privod}')
        offer.width = MDApp.get_running_app().screens.ids.screenmanager.width * .8 - dp(20)
        offer.ids.button.width = dp(80)
        offer.ids.text_button.text = 'Запись'
        self.content.ids.carcard.add_widget(offer)
        if not self.dialog:
            self.dialog = MDDialog(
                size_hint=(.9, None),
                height=dp(250),
                radius=(dp(10), dp(10), dp(10), dp(10)),
                type='custom',
                title="Мы предлагаем",
                content_cls=self.content,
                auto_dismiss=True,
                buttons=[MDFlatButton(text="Закрыть", on_release=lambda x:self.dialog.dismiss())],
            )
            self.dialog.open()

