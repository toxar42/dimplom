from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from libs.comps.note import Note

class ManagerScreen(MDScreen):
    # выход из профиля
    def exit(self):
        # переключения экрана
        MDApp.get_running_app().screens.ids.screenmanager.current = 'loginscreen'
    
    # генерация записей на осмотр бибики
    def generate_notes(self):
        # пример записей и добавление их на страницу
        try:
            self.ids.list.clear_widgets()
        except Exception as ex:
            print(ex)
        for i in range(10):
            self.ids.list.add_widget(Note(id=i, date=f'{i*2}.{i}.2024', time=f'{i}:{i*3}'))