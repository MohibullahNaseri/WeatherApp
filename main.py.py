from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests
from requests.exceptions import ConnectionError
from kivy.uix.floatlayout import FloatLayout


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    city_name = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def out(self):
        if ConnectionError is not True:
            try:
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + '{}'.format(
                    self.city_name.text)
                response = requests.get(complete_url, timeout=10)
                x = response.json()
                try:
                    if x["cod"] != "404":
                        y = x["main"]
                        current_temperature = y["temp"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        in_celsius = current_temperature - 273.15
                        in_fahrenheit = in_celsius * (9 / 5) + 32
                        k_str = str(current_temperature)
                        c_str = int(in_celsius)
                        f_str = str(in_fahrenheit)
                        self.box = FloatLayout()
                        self.pop = Popup(title=str(self.city_name.text + ' Right Now'), content=self.box)
                        self.pop.open()
                        self.box.add_widget(
                            Label(text=("   {0:.0f}".format(c_str)) + '\N{DEGREE SIGN}C\n' + weather_description + '\n',
                                  font_size=90, pos_hint={'x': .01, 'y': -0.18},
                                  italic=True, ))
                        self.box.add_widget(Button(text='exit',
                                                   size_hint=(.2, .1), pos_hint={'x': 0, 'y': 0},
                                                   on_press=lambda *args: self.pop.dismiss()))

                        self.box.add_widget(
                            Label(text=str(self.city_name.text), pos_hint={'x': -.2, 'y': .2}, font_size=60,
                                  underline=True))
                    else:
                        self.box = BoxLayout(orientation='horizontal')
                        self.pop = Popup(title='Invalid Value', content=self.box)
                        self.pop.open()
                        self.box.add_widget(Button(text='exit',
                                                   size_hint=(.2, .1), pos_hint={'x': 0, 'y': 0.0},
                                                   on_press=lambda *args: self.pop.dismiss()))
                        self.box.add_widget(Label(text='Please enter valid city name!!!', font_size=32))
                except KeyError as e:
                    self.box = BoxLayout(orientation='horizontal')
                    self.pop = Popup(title='Invalid Value', content=self.box)
                    self.pop.open()
                    self.box.add_widget(Button(text='exit',
                                               size_hint=(.2, .1), pos_hint={'x': 0, 'y': 0.0},
                                               on_press=lambda *args: self.pop.dismiss()))
                    self.box.add_widget(Label(text='Please enter city name!!!', font_size=32))
            except ConnectionError as e:
                self.box = BoxLayout(orientation='horizontal')
                self.pop = Popup(title='No Internet Connection!!!', content=self.box)
                self.pop.open()
                self.box.add_widget(Button(text='exit',
                                           size_hint=(.2, .1), pos_hint={'x': 0.1, 'y': 0.01},
                                           on_press=lambda *args: self.pop.dismiss()))
                self.box.add_widget(Label(text='No Internet Connection!!!', font_size=32))

            self.city_name.text = ''
        else:
            self.box = BoxLayout(orientation='horizontal')
            self.pop = Popup(title='No Internet Connection!!!', content=self.box)
            self.pop.open()
            self.box.add_widget(Button(text='exit',
                                       size_hint=(.2, .1), pos_hint={'x': 0.1, 'y': 0.01},
                                       on_press=lambda *args: self.pop.dismiss()))
            self.box.add_widget(Label(text='No Internet Connection!!!', font_size=32))


class ThirdWindow(Screen):
    celsius = ObjectProperty(None)

    def fahrenheit(self, **kwargs):

        try:
            val_int = float(self.celsius.text)
            fahrenheit = val_int * (9 / 5) + 32
            str_val = int(fahrenheit)
            str_val1 = str(val_int)
            self.box_pop = BoxLayout(orientation='horizontal')
            self.box_pop.add_widget(
                Label(text='Not Sure? Google it!', size_hint=(.2, .1), pos_hint={'x': 0.02, 'y': 0}))
            self.box_pop.add_widget(
                Label(text=str_val1 + '\N{DEGREE SIGN}' + 'C' + ' = ' + "{0:.0f}".format(str_val) + '\N{DEGREE SIGN}' + 'F',
                      font_size=50, padding=[1000, 200], bold=True, underline=False,
                      pos=(1.5, 1)))
            self.pop_exit = Popup(title='Result', content=self.box_pop,
                                  size_hint=(1, 1), padding=[5, 5], background_color=(0, 0, 0),
                                  auto_dismiss=True, pos_hint={'x': 0, 'y': 0})
            self.box_pop.add_widget(
                Button(text='Back', size_hint=(.3, .1), on_press=lambda *args: self.pop_exit.dismiss()))
            self.celsius.text = ""
            self.pop_exit.open()
        except ValueError as e:
            self.box = BoxLayout(orientation='horizontal')
            self.pop = Popup(title='ValueError', content=self.box)
            self.pop.open()
            self.box.add_widget(Button(text='exit',
                                       size_hint=(.2, .1), pos_hint={'x': 0.1, 'y': 0.01},
                                       on_press=lambda *args: self.pop.dismiss()))
            self.box.add_widget(Label(text='Please Enter Valid Value!!!', font_size=32))

    def kalvin(self, **kwargs):
        try:
            val_int = float(self.celsius.text)
            kalvin = val_int + 273.15
            str_val = int(kalvin)
            str_val1 = str(val_int)
            self.box_pop = BoxLayout(orientation='horizontal')
            self.box_pop.add_widget(
                Label(text='Not Sure? Google it!', size_hint=(.2, .1), pos_hint={'x': 0.02, 'y': 0}))
            self.box_pop.add_widget(
                Label(text=str_val1 + '\N{DEGREE SIGN}' + 'C' + ' = ' + "{0:.0f}".format(str_val) + ' K',
                      font_size=50, padding=[1000, 200], bold=True, underline=False,
                      pos=(1.5, 1)))
            self.pop_exit = Popup(title='Result', content=self.box_pop,
                                  size_hint=(1, 1), padding=[5, 5], background_color=(0, 0, 0),
                                  auto_dismiss=True, pos_hint={'x': 0, 'y': 0})
            self.box_pop.add_widget(
                Button(text='Back', size_hint=(.3, .1), on_press=lambda *args: self.pop_exit.dismiss()))
            self.celsius.text = ""
            self.pop_exit.open()
        except ValueError as e:
            self.box = BoxLayout(orientation='horizontal')
            self.pop = Popup(title='ValueError', content=self.box)
            self.pop.open()
            self.box.add_widget(Button(text='exit',
                                       size_hint=(.2, .1), pos_hint={'x': 0.1, 'y': 0.01},
                                       on_press=lambda *args: self.pop.dismiss()))
            self.box.add_widget(Label(text='Please Enter Valid Value!!!', font_size=32))


class FinalWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('new_window.kv')


class Weather(App):
    def build(self):
        self.icon = 'png.png'
        return kv


if __name__ == '__main__':
    Weather().run()
