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
        #make schedule
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
                #replace
                ft.dropdown.Option("Every hour"),
                ft.dropdown.Option("Four times a day"),
                ft.dropdown.Option("Three times a day"),
                ft.dropdown.Option("Twice a day"),
                ft.dropdown.Option("Once a day"),
                ft.dropdown.Option("Every other day"),
                ft.dropdown.Option("Once a week"),
                ft.dropdown.Option("Twice per month"),
                ft.dropdown.Option("Monthly"),
            ],
        )

        def sendToJson():
            return True

        self.submitButton = ft.ElevatedButton(bgcolor = ft.colors.BLACK, text = "Save", on_click = sendToJson())

        #view local files
        #rewrite file -> copy the same as AllActivities.json and use w to rewrite

        def sendToJson3rd(self):
            #add to json
            user_info = {
            "email": "",
            }

            def checkValidString(value):
                return isinstance(value, str)

            EmailVal = Container.content.controls[1].controls[1].value
            if checkValidString(EmailVal):
                user_info["email"] = EmailVal

            neededKey = user_data["ActivityChoice"] + user_data["CityChoice"]
            def activityUniqueness(activities, key):
                for blocks in activities:
                    if "ActivityChoice" in blocks.keys() and "CityChoice" in blocks.keys():
                        if key == blocks["ActivityChoice"] + blocks["CityChoice"]:
                            return True
                return False

            if(neededKey):
                # Append only if all conditions are met
                    with open(dirpath + "AllActivities.json", "w") as fp:
                        #print("app" + dirpath + "AllActivities.json")
                        data["activities"].append(user_data)
                        json.dump(data, fp, indent = 4)
                        print(data["activities"])
                        #activityList.data = data["activities"] <- make this a drop down or list of checkboxes that reads the curretn activities and displaus them
            return




        ErrorLogs = ""
        #dirpath = tempfile.gettempdir()
        dirpath = "/Users/sanjay/projects/python/PerfectDay/PerfectDay1.1"
        def errorLog(self):
            file_exists_log = exists(dirpath + "DaemonErrors.log")

            if file_exists_log:
                f = open(dirpath + "DaemonErrors.log", "r")
                ErrorLogs = f.read()
                f.close()

            else:
                ErrorLogs = "All good!"

        self.ErrorTitle = ft.Text("Current Email Errors:", color = ft.colors.BLACK, size = 20)
        self.ErrorMsg = ft.Text(ErrorLogs, color = ft.colors.BLACK, size = 10)

        self.fieldCol = ft.Column(scroll = 'auto', height = 400, controls = [
            self.email,
            self.emailField,
            #self.buffer,
            #self.time,
            #self.TimeDD,
            self.submitButton,
            self.ErrorTitle,
            self.ErrorMsg,
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
