from __future__ import print_function, unicode_literals, absolute_import
from threading import *
import subprocess
import json
import tempfile
import os
from os.path import exists

#flet imports
import flet as ft

class HomeText(ft.UserControl):

    def build(self):

        #set items
        self.displayText = ft.Text('Welcome to PerfectDay!', color=ft.colors.BLACK, size = 25, height = 35)
        self.subText = ft.Text('Create your ideal day based on your favorite weather!', color=ft.colors.GREY_600, size = 10, height = 20)
        self.activityListText = ft.Text("Your current activities...", color=ft.colors.BLACK, size = 20)
    
        #define items in container
        Container = ft.Container(
            content=ft.Column(
            controls=[
                self.displayText,
                self.subText,
                self.activityListText,
            ],
        ),
        )
        #display Home container
        return Container

class HomeTextBot(ft.UserControl):

    def build(self):

        self.Htu = ft.Text('So you want to know how to use PerfectDay?...', color = ft.colors.GREY_800, size = 18)
        self.AppDesc = ft.Text('At the top of your screen you will see tappable icons. These icons can be used to navigate to different components of PerfectDay. You can make activities, edit and delete them, manage your email and communication preferences, and eventually save CURRENT weather conditions. This project was developed using Flet. Contact smukhyala@gmail.com for quesitons about the app and feature requests.',
            color = ft.colors.GREY_400,
            size = 11)
        self.cr = ft.Text('Copyright, all rights reserved. Sanjay Mukhyala 2023', color = ft.colors.GREY_600, size = 13)

        Container = ft.Container(
            content = ft.Column(
                controls = [
                    self.Htu,
                    self.AppDesc,
                    self.cr
                ]
            )
        )
        return Container
