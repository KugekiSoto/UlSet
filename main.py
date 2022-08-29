from kivy.config import Config

Config.set("graphics", "resizable", '0')
Config.set("graphics", "width", '600')
Config.set("graphics", "height", '300')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send(num):
    client.send(num.encode('utf-8'))

Window.clearcolor = (70 / 255, 79 / 255, 59 / 255, 1)

class UlSetApp(App):
    def build(self):
        self.icon = 'logo_.png'
        self.value = GridLayout(cols=4)
        self.port = TextInput(text="port - ")
        self.host = TextInput(text="host - ")
        self.submit = Button(text="Connect", on_press=self.Submit)
        self.value.add_widget(self.port)
        self.value.add_widget(self.host)
        self.value.add_widget(self.submit)

        return self.value

    def Submit(self, obj):
        port = int(self.port.text)
        host = self.host.text
        client.connect((host,port))

        self.value.remove_widget(self.port)
        self.value.remove_widget(self.host)
        self.value.remove_widget(self.submit)

        self.value.add_widget(self.b())

    def b(self):
        box = GridLayout(cols=6, rows=3)

        btn_1 = Button(text='1', background_normal='button.jpg')
        btn_1.bind(on_press=lambda x: send('1'))
        box.add_widget(btn_1)

        btn_2 = Button(text='2', background_normal='button.jpg')
        btn_2.bind(on_press=lambda x: send('2'))
        box.add_widget(btn_2)

        btn_3 = Button(text='3', background_normal='button.jpg')
        btn_3.bind(on_press=lambda x: send('3'))
        box.add_widget(btn_3)

        btn_4 = Button(text='4', background_normal='button.jpg')
        btn_4.bind(on_press=lambda x: send('4'))
        box.add_widget(btn_4)

        btn_5 = Button(text='5', background_normal='button.jpg')
        btn_5.bind(on_press=lambda x: send('5'))
        box.add_widget(btn_5)

        btn_6 = Button(text='6', background_normal='button.jpg')
        btn_6.bind(on_press=lambda x: send('6'))
        box.add_widget(btn_6)

        btn_7 = Button(text='7', background_normal='button.jpg')
        btn_7.bind(on_press=lambda x: send('7'))
        box.add_widget(btn_7)

        btn_8 = Button(text='8', background_normal='button.jpg')
        btn_8.bind(on_press=lambda x: send('8'))
        box.add_widget(btn_8)

        btn_9 = Button(text='9', background_normal='button.jpg')
        btn_9.bind(on_press=lambda x: send('9'))
        box.add_widget(btn_9)

        btn_10 = Button(text='10', background_normal='button.jpg')
        btn_10.bind(on_press=lambda x: send('10'))
        box.add_widget(btn_10)

        btn_11 = Button(text='11', background_normal='button.jpg')
        btn_11.bind(on_press=lambda x: send('11'))
        box.add_widget(btn_11)

        btn_12 = Button(text='12', background_normal='button.jpg')
        btn_12.bind(on_press=lambda x: send('12'))
        box.add_widget(btn_12)

        btn_13 = Button(text='13', background_normal='button.jpg')
        btn_13.bind(on_press=lambda x: send('13'))
        box.add_widget(btn_13)

        btn_14 = Button(text='14', background_normal='button.jpg')
        btn_14.bind(on_press=lambda x: send('14'))
        box.add_widget(btn_14)

        btn_15 = Button(text='15', background_normal='button.jpg')
        btn_15.bind(on_press=lambda x: send('15'))
        box.add_widget(btn_15)

        btn_16 = Button(text='16', background_normal='button.jpg')
        btn_16.bind(on_press=lambda x: send('16'))
        box.add_widget(btn_16)

        btn_17 = Button(text='17', background_normal='button.jpg')
        btn_17.bind(on_press=lambda x: send('17'))
        box.add_widget(btn_17)

        btn_18 = Button(text='18', background_normal='button.jpg')
        btn_18.bind(on_press=lambda x: send('18'))
        box.add_widget(btn_18)

        return box



app = UlSetApp()
app.run()
