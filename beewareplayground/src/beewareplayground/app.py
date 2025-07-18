"""
My first application
"""

import faker

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class BeeWarePlayground(toga.App):
    def startup(self):
        main_box = toga.Box(direction=COLUMN)

        name_label = toga.Label(
            "Your name: ",
            margin=(0, 5),
        )
        self.name_input = toga.TextInput(flex=1)

        name_box = toga.Box(direction=ROW, margin=5)
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            margin=5,
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    # def say_hello(self, widget):
    #     print(f"Hello, {self.name_input.value}")

    async def say_hello(self, widget):
        # await self.main_window.dialog(
        #     # toga.InfoDialog(
        #     #     f"Hello, {self.name_input.value}",
        #     #     f"A message from {fake.name()}: {fake.text()}",
        #     # )
        #     # ### This path is inside the APP DATA (so it'd get nuked when the app is uninstalled)
        #     # toga.InfoDialog(
        #     #     str(self.paths.data / "test"),
        #     #     str(self.paths.data / "test")
        #     # )
        # )
        ### Opening a File Select Dialog isn't supported in android yet, but there ARE workarounds::
        # https://github.com/beeware/toga/discussions/1990
        # https://stackoverflow.com/questions/1043918/open-file-dialog-mvvm
        # But there is no easy way. Everything I've seen so far is very hacky.

        self.main_window.open_file_dialog("some title")

def main():
    return BeeWarePlayground()
