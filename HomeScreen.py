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

        # Open and append the file
        def existingActivities():
            dirpath = tempfile.gettempdir()
            file_exists = exists(dirpath + "AllActivities.json")
            if file_exists:
                f = open(dirpath + "AllActivities.json", "r")
                dataDict = json.load(f)
                f.close()
            # Temporary hardcoded
            else:
                dataDict = {
                    "user": "Person",
                    "email": "smukhyala@gmail.com",
                    "activities": [
                        {
                            "title":""
                        }
                    ]
                }
            mainData = dataDict
            return mainData

        EAval = existingActivities()
        subtitles = [activity['title'] for activity in EAval['activities']]

        #set items
        self.displayText = ft.Text('Welcome to PerfectDay!', color=ft.colors.BLACK, size = 25, height = 60)
        self.profileIcon = ft.IconButton(
                                            icon = ft.icons.PERSON, 
                                            icon_color=ft.colors.BLACK, 
                                            tooltip = "Profile")
        self.activityListText = ft.Text("Your current activities...", color=ft.colors.BLACK, size = 20)
        self.ActivityCards = ft.Column(scroll='auto',)

        for title in subtitles:
            pvalue_text = f"{title}"
            new_progress_card = ft.Container(
                    border_radius=20,
                    bgcolor=ft.colors.GREEN,
                    height=55,
                    width=150,
                    padding=15,
                    #on_click = lambda _: page.go('/ActivityManagerView')
                    content=ft.Column(
                        controls=[
                            ft.Text(value=pvalue_text, color=ft.colors.BLACK, size=10),
                        ]
                    )
                )
            self.ActivityCards.controls.append(new_progress_card)
    
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
                self.ActivityCards
            ],
        ),
        )
        #display Home container
        return Container