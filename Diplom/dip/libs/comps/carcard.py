from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from libs.comps.dialogcontent import DialogWindow
from kivy.metrics import dp

class CarCard(MDCard):
    dialog = None
    def __init__(self, id_, name, image, price, horsepower, privod):
        super(CarCard, self, ).__init__(id_, name, image, price, horsepower, privod)
        self.id_ = id_
        self.ids.name.text = name
        self.ids.image.source = image
        self.ids.price.text = price
        self.ids.horsepower.text = horsepower
        self.ids.privod.text = privod
    
    # открытие диалогового окна записи на просмотр
    def open_dialog(self):
        self.content = DialogWindow(card_id = self.id_)
        if not self.dialog:
            self.dialog = MDDialog(
                size_hint=(.9, None),
                height=dp(250),
                radius=(dp(10), dp(10), dp(10), dp(10)),
                type='custom',
                title="Запись",
                content_cls=self.content,
                auto_dismiss=True
            )
            self.dialog.open()
        self.dialog = None
