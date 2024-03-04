from kivy.app import App
from kivy.uix.widget import Widget


class KindredMaker(Widget):
    pass


class KindredMakerApp(App):
    def build(self):
        return KindredMaker()


if __name__ == '__main__':
    KindredMakerApp().run()
