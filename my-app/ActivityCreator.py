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
        data = EAval

        self.displayText = ft.Text('Create an activity below...', color=ft.colors.BLACK, size=25, height=60)
        self.buffer = ft.Container(height = 3)
        self.warningMSG = ft.Text('Activities will not be saved if entries are invalid...', color=ft.colors.RED_900, size = 12, height = 30)

        #Temp
        self.TempIcon = ft.IconButton(icon=ft.icons.DEVICE_THERMOSTAT,
                                    icon_color=ft.colors.BLACK, icon_size=60,
                                    tooltip="Temperature")
        self.TempHi = ft.TextField(label="Highest Preferred Temperature",
                                    width = 250,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.TempLo = ft.TextField(label="Lowest Preferred Temperature",
                                    width = 250,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.TempFieldCol = ft.Column(controls=[])
        self.TempFieldCol.controls.append(self.TempHi)
        self.TempFieldCol.controls.append(self.TempLo)
        self.TempRow = ft.Row(controls=[])
        self.TempRow.controls.append(self.TempIcon)
        self.TempRow.controls.append(self.TempFieldCol)

        #Wind
        self.WindIcon = ft.IconButton(icon=ft.icons.WIND_POWER,
                                    icon_color=ft.colors.BLACK, icon_size=60,
                                    tooltip="Wind")
        self.WindHi = ft.TextField(label="Highest Preferred Wind Speed",
                                    width = 250,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.WindLo = ft.TextField(label="Lowest Preferred Wind Speed",
                                    width = 250,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.WindFieldCol = ft.Column(controls=[])
        self.WindFieldCol.controls.append(self.WindHi)
        self.WindFieldCol.controls.append(self.WindLo)
        self.WindRow = ft.Row(controls=[])
        self.WindRow.controls.append(self.WindIcon)
        self.WindRow.controls.append(self.WindFieldCol)

        #Humidity
        self.HumidityIcon = ft.IconButton(icon=ft.icons.WAVES,
                                    icon_color=ft.colors.BLACK, icon_size=60,
                                    tooltip="Humidity")
        self.HumidityHi = ft.TextField(label="Highest Preferred Humidity",
                                    width = 250,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.HumidityLo = ft.TextField(label="Lowest Preferred Humidity",
                                    width = 250,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.HumidityFieldCol = ft.Column(controls=[])
        self.HumidityFieldCol.controls.append(self.HumidityHi)
        self.HumidityFieldCol.controls.append(self.HumidityLo)
        self.HumidityRow = ft.Row(controls=[])
        self.HumidityRow.controls.append(self.HumidityIcon)
        self.HumidityRow.controls.append(self.HumidityFieldCol)

        #Name and City
        self.InfoIcon = ft.IconButton(icon=ft.icons.PLACE,
                                    icon_color=ft.colors.BLACK, icon_size=60,
                                    tooltip="Name & City")
        self.Name = ft.TextField(label="Activity Name",
                                    width = 250,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100)
        self.City = ft.TextField(label="Activity Location (City)",
                                    width = 250,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100)
        self.InfoFieldCol = ft.Column(controls=[])
        self.InfoFieldCol.controls.append(self.Name)
        self.InfoFieldCol.controls.append(self.City)
        self.InfoRow = ft.Row(controls=[])
        self.InfoRow.controls.append(self.InfoIcon)
        self.InfoRow.controls.append(self.InfoFieldCol)

        def sendToJson(self):
            #add to json
            user_data = {
            "title": "",
            "subtitle": "",
            "icon": "",
            "HighTemp": 0,
            "LowTemp": 0,
            "HighWind": 0,
            "LowWind": 0,
            "HighHumidity": 0,
            "LowHumidity": 0,
            "ActivityChoice": "nothing",
            "CityChoice": "San Francisco"}

            def checkValidInt(value):
                try:
                    num = int(value)
                    if num >= 0:
                        return True
                    else:
                        return False
                except ValueError:
                    return False

            def checkValidString(value):
                return isinstance(value, str)

            prefix = Container.content.controls[2]
            MaxHeatVal = prefix.controls[0].controls[1].controls[0].value
            if checkValidInt(MaxHeatVal):
                user_data["HighTemp"] = MaxHeatVal
            MinHeatVal = prefix.controls[0].controls[1].controls[1].value
            if checkValidInt(MinHeatVal):
                user_data["LowTemp"] = MinHeatVal
            MaxWindVal = prefix.controls[2].controls[1].controls[0].value
            if checkValidInt(MaxWindVal):
                user_data["HighWind"] = MaxWindVal
            MinWindVal = prefix.controls[2].controls[1].controls[1].value
            if checkValidInt(MinWindVal):
                user_data["LowWind"] = MinWindVal
            MaxHumiVal = prefix.controls[4].controls[1].controls[0].value
            if checkValidInt(MaxHumiVal):
                user_data["HighHumidity"] = MaxHumiVal
            MinHumiVal = prefix.controls[4].controls[1].controls[1].value
            if checkValidInt(MinHumiVal):
                user_data["LowHumidity"] = MinHumiVal
            NameVal = prefix.controls[6].controls[1].controls[0].value
            if checkValidString(NameVal):
                user_data["ActivityChoice"] = NameVal
                user_data["title"] = user_data["ActivityChoice"]
            CityVal = prefix.controls[6].controls[1].controls[1].value
            if checkValidString(CityVal):
                user_data["CityChoice"] = CityVal
                user_data["subtitle"] = user_data["CityChoice"]

            neededKey = user_data["ActivityChoice"] + user_data["CityChoice"]
            def activityUniqueness(activities, key):
                for blocks in activities:
                    if "ActivityChoice" in blocks.keys() and "CityChoice" in blocks.keys():
                        if key == blocks["ActivityChoice"] + blocks["CityChoice"]:
                            return True
                return False

            if(not(activityUniqueness(data["activities"], neededKey))):
                # Append only if all conditions are met
                if all([
                    checkValidInt(user_data["HighTemp"]),
                    checkValidInt(user_data["LowTemp"]),
                    checkValidInt(user_data["HighWind"]),
                    checkValidInt(user_data["LowWind"]),
                    checkValidInt(user_data["HighHumidity"]),
                    checkValidInt(user_data["LowHumidity"]),
                    checkValidString(user_data["ActivityChoice"]),
                    checkValidString(user_data["CityChoice"])
                ]):
                    with open(dirpath + "AllActivities.json", "w") as fp:
                        #print("app" + dirpath + "AllActivities.json")
                        data["activities"].append(user_data)
                        json.dump(data, fp, indent = 4)
                        print(data["activities"])
                        #activityList.data = data["activities"] <- make this a drop down or list of checkboxes that reads the curretn activities and displaus them
            return

        self.submitButton = ft.ElevatedButton(bgcolor = ft.colors.BLACK,
                        on_click=sendToJson, icon = ft.icons.LIBRARY_ADD_CHECK_ROUNDED, text = "Submit")

        self.parameterCol = ft.Column(alignment = "left", scroll = "auto", height = 420,
            controls = [
                self.TempRow,
                self.buffer,
                self.WindRow,
                self.buffer,
                self.HumidityRow,
                self.buffer,
                self.InfoRow,
            ])

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
                self.parameterCol,
                self.warningMSG,
                self.submitButton,
            ],
        ),
        )
        #display Home container
        return Container
