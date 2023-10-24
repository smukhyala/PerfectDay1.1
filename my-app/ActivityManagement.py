from __future__ import print_function, unicode_literals, absolute_import
from threading import *
import subprocess
import json
import tempfile
import os
from os.path import exists

#flet imports
import flet as ft

#make it so you pick activity from dropdown
#fix dropdown addition
#Flet docs dont have nosdnf;pdf

class Editor(ft.UserControl):

    def build(self):

        def existingActivities():
            dirpath = tempfile.gettempdir()
            file_exists = exists(dirpath + "AllActivities.json")
            if file_exists:
                with open(dirpath + "AllActivities.json", "r") as f:
                    dataDict = json.load(f)
            # Temporary hardcoded
            else:
                dataDict = {
                    "user": "Person",
                    "email": "smukhyala@gmail.com",
                    "activities": [
                        {
                            "title": "",
                            "subtitle": ""
                        }
                    ]
                }
            mainData = dataDict
            return mainData

        self.title = ft.Text("Current Preferences", color = ft.colors.BLACK, size = 20, weight=ft.FontWeight.BOLD, bgcolor = ft.colors.GREY_300)
        self.subtitle = ft.Text("Select an activity below...", color = ft.colors.GREY_600, size = 16)
        self.buffer = ft.Container(height = 1, width = 1)
        self.general = ft.Text("General Settings:", color = ft.colors.GREY_900, size = 17, weight=ft.FontWeight.W_600)
        self.weather = ft.Text("Weather Settings:", color = ft.colors.GREY_900, size = 17, weight=ft.FontWeight.W_600)

        self.ActivityDD = ft.Dropdown(
            width=300,
            bgcolor = ft.colors.BLACK,
            options=[
            ],
        )

        self.DDCont = ft.Container(
            content = [
                self.ActivityDD,
            ]
        )

        EAval = existingActivities()
        TopCap = [activity['title'] for activity in EAval['activities']]
        BotCap = [activity['subtitle'] for activity in EAval['activities']]
        counter = [len(EAval['activities'])]
        for top_text, bot_text, i in zip(TopCap, BotCap, counter): #replace second TopCap with a counter
            self.ActivityDD.options.append(ft.dropdown.Option(f"{i}. {top_text} in {bot_text}"))

        temp = "_"
        self.MaxTemp = ft.Text("Maximum Temperature:",
                            color = ft.colors.GREY_900, size = 15,
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.MaxTempField = ft.TextField(label=f"Current: {temp}",
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MaxTempRow = ft.Row(controls = [self.MaxTemp, self.MaxTempField])

        self.MinTemp = ft.Text("Minimum Temperature:",
                            color = ft.colors.GREY_900, size = 15,
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.MinTempField = ft.TextField(label=f"Current: {temp}",
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MinTempRow = ft.Row(controls = [self.MinTemp, self.MinTempField])

        self.MaxWind = ft.Text("Maximum Wind:",
                            color = ft.colors.GREY_900, size = 15,
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.MaxWindField = ft.TextField(label=f"Current: {temp}",
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MaxWindRow = ft.Row(controls = [self.MaxWind, self.MaxWindField])

        self.MinWind = ft.Text("Minimum Wind:",
                            color = ft.colors.GREY_900, size = 15,
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.MinWindField = ft.TextField(label=f"Current: {temp}",
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MinWindRow = ft.Row(controls = [self.MinWind, self.MinWindField])

        self.MaxHumi = ft.Text("Maximum Humidity:",
                            color = ft.colors.GREY_900, size = 15,
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.MaxHumiField = ft.TextField(label=f"Current: {temp}",
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MaxHumiRow = ft.Row(controls = [self.MaxHumi, self.MaxHumiField])

        self.MinHumi = ft.Text("Manimum Humidity:",
                            color = ft.colors.GREY_900, size = 15,
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.MinHumiField = ft.TextField(label=f"Current: {temp}",
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MinHumiRow = ft.Row(controls = [self.MinHumi, self.MinHumiField])

        self.Name = ft.Text("Activity Name:",
                            color = ft.colors.GREY_900, size = 15,
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.NameField = ft.TextField(label=f"Current: {temp}",
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.NameRow = ft.Row(controls = [self.Name, self.NameField])

        self.City = ft.Text("Current City:",
                            color = ft.colors.GREY_900, size = 15,
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.CityField = ft.TextField(label=f"Current: {temp}",
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.CityRow = ft.Row(controls = [self.City, self.CityField])

        self.submitButton = ft.ElevatedButton(bgcolor = ft.colors.BLACK,
                        icon = ft.icons.CHECK, text = "Save")#on_click=sendToJson)

        self.FieldColumn = ft.Column(alignment = "left", scroll = "auto", height = 500)

        def update_content(selected_index):
            self.FieldColumn.controls = []  # Clear existing controls
            print(selected_index)
            selected_index = selected_index - 1 #index start at 0, user count starts at 1
            if selected_index >= 0:  # Check if a valid activity is selected
                print("selected")
                selected_activity = EAval['activities'][selected_index]
                self.NameField.label = f"Current: {selected_activity['title']}"
                self.CityField.label = f"Current: {selected_activity['subtitle']}"
                # Update other fields similarly based on the selected activity

                # ... (populate other fields based on the selected activity)

                # Add the controls to the FieldColumn
                self.FieldColumn.controls.extend([
                    self.buffer,
                    self.general,
                    self.NameRow,
                    self.buffer,
                    self.CityRow,
                    self.buffer,
                    self.buffer,
                    self.weather,
                    self.MaxTempRow,
                    self.buffer,
                    self.MinTempRow,
                    self.buffer,
                    self.MaxWindRow,
                    self.buffer,
                    self.MinWindRow,
                    self.buffer,
                    self.MaxHumiRow,
                    self.buffer,
                    self.MinHumiRow,
                    # ... (add other rows)
                ])

                print(self.FieldColumn.controls[1])
                #make a function that transfers the user to a different location, updates, and then goes back.
            else:
                print("no")
                self.FieldColumn.controls = []

        # Define a function to handle the dropdown value change event
        def dropdown_changed(e):
            DDval = self.DDCont.content[0].value
            selected_index = DDval[0]
            update_content(int(DDval[0]))

        # Create a button to trigger the dropdown change event
        self.refreshButton = ft.ElevatedButton(bgcolor=ft.colors.BLACK, text="Refresh", on_click = dropdown_changed)

        self.buttonRow = ft.Row(controls = [self.submitButton, self.buffer, self.refreshButton])

        #define items in container
        Container = ft.Container(
            content=ft.Column(
            controls=[
                self.title,
                self.subtitle,
                self.ActivityDD,
                #self.ActivityDropdown,
                self.FieldColumn,
                self.buttonRow
            ],
        ),
        )
        #display Home container
        return Container
