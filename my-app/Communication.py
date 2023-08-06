from __future__ import print_function, unicode_literals, absolute_import
from threading import *
import subprocess
import json
import tempfile
import os
from os.path import exists

#flet imports
import flet as ft

class Preferences(ft.UserControl):

    def build(self):
       
        #set items
        self.title = ft.Text("Communication Preferences", color = ft.colors.BLACK, size = 20)
        self.buffer = ft.Container(height = 1)

        self.email = ft.Text("Enter your email...", color = ft.colors.GREY_900, size = 15)
        self.emailField = ft.TextField(label="janedoe@gmail.com", 
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)

        self.time = ft.TextField("How often do you want PerfectDay updates?", 
            color = ft.colors.GREY_900, size = 15)
        self.timeField = ft.RadioGroup(content=ft.Column([
            ft.Radio(value="daily", label="Daily"),
            ft.Radio(value="biweekly", label="Twice Weekly"),
            ft.Radio(value="weekly", label="Weekly")]))
        
        self.dd = ft.Dropdown(
            width=100,
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
        )

        self.fieldCol = ft.Column(scroll = 'auto', height = 400, controls = [
            self.email,
            self.emailField,
            self.buffer,
            self.time,
            self.timeField,
            self.dd,
        ])

        Container = ft.Container(
             content=ft.Column(
            controls=[
                self.title,
                self.fieldCol
            ]
            )
        )

        return Container