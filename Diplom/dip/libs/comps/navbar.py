from kivymd.uix.boxlayout import MDBoxLayout
from libs.settings.settings import Colors

class NavBar(MDBoxLayout):
    def change_color(self, instance):
        if instance in self.ids.values():
            current_id = list(self.ids.keys())[list(self.ids.values()).index(instance)]
            for i in range(3):
                if f'nav{i + 1}' == current_id:
                    self.ids[f'nav{i + 1}'].text_color = Colors().lightgrey
                else:
                    self.ids[f'nav{i + 1}'].text_color = Colors().darkgrey