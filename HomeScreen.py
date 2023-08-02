from __future__ import print_function, unicode_literals, absolute_import
from threading import *
import subprocess
import json
import tempfile
import os
from os.path import exists

#flet imports
import flet as ft

# temporary directory for first time use / setting up file system on the default device
dirpath = tempfile.gettempdir()

class Home(ft.UserControl):

    def build(self):

        #set items
        self.displayText = ft.Text('Welcome to PerfectDay!', color=ft.colors.BLACK, size = 25, height = 60)
        self.profileIcon = ft.IconButton(
                                            icon = ft.icons.PERSON, 
                                            icon_color=ft.colors.BLACK, 
                                            tooltip = "Profile")
        self.activityListText = ft.Text("Your current activities...", color=ft.colors.BLACK, size = 20)
    
        #define items in container
        Container = ft.Container(
            content=ft.Column(
            controls=[
                ft.Row(alignment='spaceBetween',
                       controls=[
                            self.profileIcon,
                            ft.Row(alignment='center',
                                  controls=[
                                      ft.Row(alignment='center',
                                             controls=[
                                             ],
                                             ),
                                  ],
                                  ),
                       ],
                       ),
                self.displayText,
                self.activityListText,
            ],
        ),
        )
        #display Home container
        return Container