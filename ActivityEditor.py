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

        self.displayText = ft.Text('Create and activity below...', color=ft.colors.BLACK, size=25, height=60)
        self.buffer = ft.Container(height = 20)

        #Temp
        self.TempIcon = ft.IconButton(icon=ft.icons.DEVICE_THERMOSTAT, 
                                    icon_color=ft.colors.RED, icon_size=60,
                                    tooltip="Temperature")
        self.TempHi = ft.TextField(label="Highest Preferred Temperature", width = 200)
        self.TempLo = ft.TextField(label="Lowest Preferred Temperature")
        self.TempFieldCol = ft.Column(controls=[])
        self.TempFieldCol.controls.append(self.TempHi)
        self.TempFieldCol.controls.append(self.TempLo)
        self.TempRow = ft.Row(controls=[])
        self.TempRow.controls.append(self.TempIcon)
        self.TempRow.controls.append(self.TempFieldCol)

        #Wind
        self.WindIcon = ft.IconButton(icon=ft.icons.WIND_POWER, 
                                    icon_color=ft.colors.BLUE, icon_size=60,
                                    tooltip="Wind")
        self.WindHi = ft.TextField(label="Highest Preferred Wind Speed")
        self.WindLo = ft.TextField(label="Lowest Preferred Wind Speed")
        self.WindFieldCol = ft.Column(controls=[])
        self.WindFieldCol.controls.append(self.WindHi)
        self.WindFieldCol.controls.append(self.WindLo)
        self.WindRow = ft.Row(controls=[])
        self.WindRow.controls.append(self.WindIcon)
        self.WindRow.controls.append(self.WindFieldCol)

        #Humidity
        self.HumidityIcon = ft.IconButton(icon=ft.icons.WAVES, 
                                    icon_color=ft.colors.ORANGE, icon_size=60,
                                    tooltip="Humidity")
        self.HumidityHi = ft.TextField(label="Highest Preferred Humidity")
        self.HumidityLo = ft.TextField(label="Lowest Preferred Humidity")
        self.HumidityFieldCol = ft.Column(controls=[])
        self.HumidityFieldCol.controls.append(self.HumidityHi)
        self.HumidityFieldCol.controls.append(self.HumidityLo)
        self.HumidityRow = ft.Row(controls=[])
        self.HumidityRow.controls.append(self.HumidityIcon)
        self.HumidityRow.controls.append(self.HumidityFieldCol)

        #Name and City
        self.InfoIcon = ft.IconButton(icon=ft.icons.PLACE, 
                                    icon_color=ft.colors.GREEN, icon_size=60,
                                    tooltip="Name & City")
        self.Name = ft.TextField(label="Activity Name")
        self.City = ft.TextField(label="Activity Location (City)")
        self.InfoFieldCol = ft.Column(controls=[])
        self.InfoFieldCol.controls.append(self.Name)
        self.InfoFieldCol.controls.append(self.City)
        self.InfoRow = ft.Row(controls=[])
        self.InfoRow.controls.append(self.InfoIcon)
        self.InfoRow.controls.append(self.InfoFieldCol)

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
                self.displayText,  
                self.TempRow,
                self.buffer,
                self.WindRow,
                self.buffer,
                self.HumidityRow,
                self.buffer,
                self.InfoRow
            ],
        ),
        )
        #display Home container
        return Container