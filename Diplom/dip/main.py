from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.config import Config
from kivy import platform
from libs.comps.myapp import MyApp

if platform == 'android':
    from android.permissions import Permission, request_permissions
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET])


class App(MDApp):
    screens = None

    def build(self):
        # необходимые параметры (иконка и название)
        self.title='Name'
        self.icon = ''
        # Только для теста на ПК
        Window.fullscreen = False
        Window.size = [350, 700]

        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.theme_style_switch_animation = True

        self.load_all_kv_files()
        self.screens = MyApp()
        return self.screens

    # функция которая вызовется автоматически при запуски приложения
    def on_start(self):
        self.screens.ids.mainscreen.ids.catalogscreen.generate_notes()

    # загрузка компонентов
    def load_all_kv_files(self):
        Builder.load_file('libs/comps/myapp.kv')
        Builder.load_file('libs/comps/loginscreen.kv')
        Builder.load_file('libs/comps/signupscreen.kv')
        Builder.load_file('libs/comps/mainscreen.kv')
        Builder.load_file('libs/comps/userscreen.kv')
        Builder.load_file('libs/comps/catalogscreen.kv')
        Builder.load_file('libs/comps/testscreen.kv')
        Builder.load_file('libs/comps/navbar.kv')
        Builder.load_file('libs/comps/note.kv')
        Builder.load_file('libs/comps/carcard.kv')
        Builder.load_file('libs/comps/dialogcontent.kv')
        Builder.load_file('libs/comps/offerwindow.kv')
        Builder.load_file('libs/comps/add_manager_button.kv')
        Builder.load_file('libs/comps/managerscreen.kv')


def main():
    Config.set('graphics', 'fullscreen', 'auto')
    Config.set('graphics', 'window_state', 'maximized')
    Config.set('graphics', 'resizable', 0)
    Config.write()
    app = App()
    app.run()


if __name__ == '__main__':
    main()
