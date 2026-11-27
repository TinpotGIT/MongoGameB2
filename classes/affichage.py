import rich
from rich import panel
from item import Item

class Affichage():

    def display_vue(vue):
        pass

    def show_error(error: str):
        pass

    def create_info_box(titre: str, info: str, box_color: str, text_color: str):
        pass

    def create_select_box(titre: str, items: list[Item], index: int, box_color: str, text_color: str, hover_color: str):
        pass