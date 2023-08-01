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

class Maker(ft.UserControl):

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
        self.displayText = ft.Text('Create and activity below...', color=ft.colors.BLACK, size = 25, height = 60)
        self.TempIcon = ft.IconButton(
                                            icon = ft.icons.DEVICE_THERMOSTAT, 
                                            icon_color=ft.colors.BLACK, 
                                            icon_size = 42,
                                            tooltip = "Temperature")
        self.TempHi = ft.TextField(label = "Highest Preferred Temperature")
        self.TempLo = ft.TextField(label = "Lowest Preferred Temperature")
        self.TempFieldCol = ft.Column(controls=[])
        self.TempFieldCol.controls[0] = self.TempHi
        self.TempFieldCol.controls[1] = self.TempLo
        self.TempRow = ft.Row(alignments = 'spaceBetween', controls=[])
        self.TempRow.controls[0] = self.TempIcon
        self.TempRow.controls[1] = self.TempFieldCol

        #define items in container
        Container = ft.Container(
            content=ft.Column(
            controls=[
                ft.Row(alignment='spaceBetween',
                       controls=[
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
                self.TempRow
            ],
        ),
        )
        #display Home container
        return Container