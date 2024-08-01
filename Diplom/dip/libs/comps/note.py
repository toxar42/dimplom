from kivymd.uix.card import MDCardSwipe
from kivymd.app import MDApp
from libs.add.bd import *

class Note(MDCardSwipe):
    note_id = None
    def __init__(self, id, date, time, *args, **kwargs):
        super(Note, self).__init__(id, date, time, *args, **kwargs)
        self.note_id = id
        self.ids.date.text = str(date)
        self.ids.time.text = str(time)     
    # удаление заметки
    def delete_note(self, instance):
        delete('views','id_view',self.note_id)
        self.parent.remove_widget(instance)
        