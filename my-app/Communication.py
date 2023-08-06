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

        self.email = ft.Text("Enter your email...", color = ft.colors.GREY_700, size = 15)
        self.emailField = ft.TextField(label="janedoe@gmail.com", 
                                    width = 200,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)

        self.time = ft.Text("How often do you want PerfectDay updates?", 
            color = ft.colors.GREY_900, size = 15)
        self.TimeDD = ft.Dropdown(
            width=300,
            options=[
                ft.dropdown.Option("Every hour", color = ft.colors.BLACK),
                ft.dropdown.Option("Four times a day", color = ft.colors.BLACK),
                ft.dropdown.Option("Three times a day", color = ft.colors.BLACK),
                ft.dropdown.Option("Twice a day", color = ft.colors.BLACK),
                ft.dropdown.Option("Once a day", color = ft.colors.BLACK),
                ft.dropdown.Option("Every other day", color = ft.colors.BLACK),
                ft.dropdown.Option("Once a week", color = ft.colors.BLACK),
                ft.dropdown.Option("Twice per month", color = ft.colors.BLACK),
                ft.dropdown.Option("Monthly", color = ft.colors.BLACK),
            ],
        )

        self.submitButton = ft.ElevatedButton(bgcolor = ft.colors.BLACK,
            icon = ft.icons.LIBRARY_ADD_CHECK_ROUNDED, text = "Submit")

        self.fieldCol = ft.Column(scroll = 'auto', height = 400, controls = [
            self.email,
            self.emailField,
            self.buffer,
            self.time,
            self.TimeDD,
            self.submitButton
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