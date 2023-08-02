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

        #check val
        def is_number(value):
            try:
                float(value)
                return True
            except ValueError:
                return False

        EAval = existingActivities()
        data = EAval

        self.displayText = ft.Text('Create and activity below...', color=ft.colors.BLACK, size=25, height=60)
        self.buffer = ft.Container(height = 14)

        #Temp
        self.TempIcon = ft.IconButton(icon=ft.icons.DEVICE_THERMOSTAT, 
                                    icon_color=ft.colors.RED, icon_size=60,
                                    tooltip="Temperature")
        self.TempHi = ft.TextField(label="Highest Preferred Temperature", 
                                    width = 250)
        self.TempLo = ft.TextField(label="Lowest Preferred Temperature", 
                                    width = 250)
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
        self.WindHi = ft.TextField(label="Highest Preferred Wind Speed", 
                                    width = 250)
        self.WindLo = ft.TextField(label="Lowest Preferred Wind Speed", 
                                    width = 250)
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
        self.HumidityHi = ft.TextField(label="Highest Preferred Humidity", 
                                    width = 250)
        self.HumidityLo = ft.TextField(label="Lowest Preferred Humidity", 
                                    width = 250)
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
        self.Name = ft.TextField(label="Activity Name", 
                                    width = 250)
        self.City = ft.TextField(label="Activity Location (City)", 
                                    width = 250)
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
            #if not all(is_number(val) for val in [user_data]):
                #print("Please enter valid numbers for temperature, wind, and humidity.")
                #return
            #else:
            '''
                column_controls = TopHubT.content.controls[0].controls  # Get the controls of the nested column
        task_name = column_controls[2].content.value  # Get the value of the text field
        task_category = column_controls[4].content.value  # Get the value of the dropdown
        task_occurrence = column_controls[6].content.value  # Get the value of the dropdown
        print(task_category, task_name, task_occurrence)
        # Create a new task dictionary
        new_task = {
            "name": task_name,
            "category": task_category,
            "occurrence": task_occurrence
        }
        # Add the new task to the task dictionary
        task_dict.append(new_task)
        # Write the updated task_dict to the Tasks.json file
        file_path = os.path.join(dirpath, "Tasks.json")
        with open(file_path, "w") as f:
            json.dump(task_dict, f)
        # Update the checklist display
        update_checklist(e)
                '''
            prefix = Container.content
            MaxHeatVal = prefix.controls[2].controls[1].controls[0].value
            user_data["HighTemp"] = MaxHeatVal
            MinHeatVal = prefix.controls[2].controls[1].controls[1].value
            user_data["LowTemp"] = MinHeatVal
            MaxWindVal = prefix.controls[4].controls[1].controls[0].value
            user_data["HighWind"] = MaxWindVal
            MinWindVal = prefix.controls[4].controls[1].controls[1].value
            user_data["LowWind"] = MinWindVal
            MaxHumiVal = prefix.controls[6].controls[1].controls[0].value
            user_data["HighHumidity"] = MaxHumiVal
            MinHumiVal = prefix.controls[6].controls[1].controls[1].value
            user_data["LowHumidity"] = MinHumiVal
            NameVal = prefix.controls[8].controls[1].controls[0].value
            user_data["ActivityChoice"] = NameVal
            user_data["title"] = user_data["ActivityChoice"]
            CityVal = prefix.controls[8].controls[1].controls[1].value
            user_data["CityChoice"] = CityVal
            user_data["subtitle"] = user_data["CityChoice"]
            neededKey = user_data["ActivityChoice"] + user_data["CityChoice"]
            print(user_data)

            def activityUniqueness(activities, key):
                for blocks in activities:
                    if "ActivityChoice" in blocks.keys() and "CityChoice" in blocks.keys():                                
                        if key == blocks["ActivityChoice"] + blocks["CityChoice"]:
                            return True
                return False

            if(not(activityUniqueness(data["activities"], neededKey))):
                with open(dirpath + "AllActivities.json", "w") as fp:
                    #print("app" + dirpath + "AllActivities.json")
                    data["activities"].append(user_data)
                    json.dump(data, fp, indent = 4)
                    print(data["activities"])
                    #activityList.data = data["activities"] <- make this a drop down or list of checkboxes that reads the curretn activities and displaus them

            return

        self.submitButton = ft.ElevatedButton(bgcolor = ft.colors.BLACK,
                        on_click=sendToJson, icon = ft.icons.LIBRARY_ADD_CHECK_ROUNDED, text = "Submit")

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
                self.InfoRow,
                self.submitButton,
            ],
        ),
        )
        #display Home container
        return Container