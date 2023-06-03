from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
import mysql.connector
import os
import subprocess
from tkinter import *
import time
from tkinter.font import Font


# set window size
db = mysql.connector.connect(host="localhost",user="root",passwd="subarna",database="login")
mycur = db.cursor()
Window.size = (300, 450)
KV = '''
Screen:

    MDCard:
        size_hint: None, None
        size: 300, 450
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 65
        spacing: 20
        orientation: 'vertical'
        MDIcon:
            icon: 'Notes creater.png'
            icon_color: 0, 0, 0, 0
            halign: 'center'
            font_size: 180
        MDTextFieldRound:
            id: user
            icon_left: "account-check"
            hint_text: "Username"
            foreground_color: "black"
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}
        MDTextFieldRound:
            id: password
            icon_left: "key-variant"
            hint_text: "Password"
            foreground_color: "black"
            size_hint_x: None
            width: 220
            font_size: 20            
            pos_hint: {"center_x": 0.5}
            password: True
        MDFillRoundFlatButton:
            text: "LOG IN"
            font_size: 15
            pos_hint: {"center_x": 0.5}
            on_press: app.login()
        MDFillRoundFlatButton:
            text: "REGISTER"
            font_size: 15
            pos_hint: {"center_x": 0.5}
            on_press: app.register()
'''


class LoginApp(MDApp):
    dialog = None

    def build(self):
        # define theme colors
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.accent_palette = "Green"
        # load and return kv string
        return Builder.load_string(KV)

    def login(self):
        # check entered username and password
        user_varify = self.root.ids.user.text
        pas_varify = self.root.ids.password.text
        sql = "select * from register where username = %s and password = %s"
        mycur.execute(sql,[(user_varify),(pas_varify)])
        results = mycur.fetchall()
        if results:
                self.dialog = MDDialog(
                    title="Log In",
                    text=f"Welcome {self.root.ids.user.text} ",
                    buttons=[
                        MDFlatButton(
                            text="Ok", text_color=self.theme_cls.primary_color,
                            on_release=self.close
                        ),
                    ],
                )

                Window.close()

                def Speech():
                    os.system("guispeech2text.py")

                def T2S():
                    #execfile
                    os.system("textSummary.py")
                
                window = Tk()
                window.title("Menu")
                window.geometry("300x450")
                window.config(bg = "white")
                window.resizable(height = "false",width = "false")
                font1 = Font(family = "times",size = 20, weight = "bold")
                button1 = Button(window,text = "Speech-to-Text",font = font1 , bg = "green", fg = "white",padx = 5, pady = 5,width=15,activebackground = "blue", activeforeground = "yellow",command = Speech)
                button1.place(x=20,y=100)  # side = top / left / right / bottom
                button3 = Button(window,text = "Text-Summarization",font = font1 , bg = "yellow", fg = "white",padx = 5, pady = 5,width=15,command = T2S)
                button3.place(x=20,y=300)
                window.mainloop()
        else:
            self.dialog = MDDialog(
                    title="Log In",
                    text=f"Invalid Username Or Password",
                    buttons=[
                        MDFlatButton(
                            text="Ok", text_color=self.theme_cls.primary_color,
                            on_release=self.close
                        ),
                    ],
                )
            self.dialog.open()
       


    def register(self):
            username_info = self.root.ids.user.text
            password_info = self.root.ids.password.text
            if username_info == "":
               print("error")
            elif password_info == "":
               print("error")
            else:
              sql = "insert into register values(%s,%s)"
              t = (username_info, password_info)
              mycur.execute(sql, t)
              db.commit()
              self.dialog = MDDialog(
              title="register",
              text=f"Welcome {self.root.ids.user.text}! Registered Successfully",
                    buttons=[
                        MDFlatButton(
                            text="Ok", text_color=self.theme_cls.primary_color,
                            on_release=self.close
                        ),
                    ],
                )
            # open and display dialog
            self.dialog.open()
            self.root.ids.user.text=""
            self.root.ids.password.text=""



    def close(self, instance):
        # close dialog
        self.dialog.dismiss()
# run app
LoginApp().run()