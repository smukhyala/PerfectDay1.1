from __future__ import print_function, unicode_literals, absolute_import
from threading import *
import subprocess
import json
import tempfile
import os
from os.path import exists

#flet imports
import flet as ft

class Editor(ft.UserControl):

    def build(self):

        #set items
        self.title = ft.Text("Current Preferences", color = ft.colors.BLACK, size = 20, weight=ft.FontWeight.BOLD, bgcolor = ft.colors.GREY_300)
        self.buffer = ft.Container(height = 1)
        self.general = ft.Text("General Settings:", color = ft.colors.GREY_900, size = 17, weight=ft.FontWeight.W_600)
        self.weather = ft.Text("Weather Settings:", color = ft.colors.GREY_900, size = 17, weight=ft.FontWeight.W_600)

        d = "p"
        self.MaxTemp = ft.Text("Maximum Temperature:", 
                            color = ft.colors.GREY_900, size = 15, 
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.MaxTempField = ft.TextField(label=f"Current: {d}", 
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MaxTempRow = ft.Row(controls = [self.MaxTemp, self.MaxTempField])

        self.MinTemp = ft.Text("Minimum Temperature:", 
                            color = ft.colors.GREY_900, size = 15, 
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.MinTempField = ft.TextField(label=f"Current: {d}", 
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MinTempRow = ft.Row(controls = [self.MinTemp, self.MinTempField])

        self.MaxWind = ft.Text("Maximum Wind:", 
                            color = ft.colors.GREY_900, size = 15, 
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.MaxWindField = ft.TextField(label=f"Current: {d}", 
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MaxWindRow = ft.Row(controls = [self.MaxWind, self.MaxWindField])

        self.MinWind = ft.Text("Minimum Wind:", 
                            color = ft.colors.GREY_900, size = 15, 
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.MinWindField = ft.TextField(label=f"Current: {d}", 
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MinWindRow = ft.Row(controls = [self.MinWind, self.MinWindField])

        self.MaxHumi = ft.Text("Maximum Humidity:", 
                            color = ft.colors.GREY_900, size = 15, 
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.MaxHumiField = ft.TextField(label=f"Current: {d}", 
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MaxHumiRow = ft.Row(controls = [self.MaxHumi, self.MaxHumiField])

        self.MinHumi = ft.Text("Manimum Humidity:", 
                            color = ft.colors.GREY_900, size = 15, 
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.MinHumiField = ft.TextField(label=f"Current: {d}", 
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MinHumiRow = ft.Row(controls = [self.MinHumi, self.MinHumiField])

        self.Name = ft.Text("Activity Name:", 
                            color = ft.colors.GREY_900, size = 15, 
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.NameField = ft.TextField(label=f"Current: {d}", 
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.NameRow = ft.Row(controls = [self.Name, self.NameField])

        self.City = ft.Text("Current City:", 
                            color = ft.colors.GREY_900, size = 15, 
                            bgcolor = ft.colors.GREY_100, width = 180)
        self.CityField = ft.TextField(label=f"Current: {d}", 
                                    width = 120,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.CityRow = ft.Row(controls = [self.City, self.CityField])

        self.submitButton = ft.ElevatedButton(bgcolor = ft.colors.BLACK,
                        icon = ft.icons.CHECK, text = "Save")#on_click=sendToJson)

        self.FieldColumn = ft.Column(alignment = "left", scroll = "auto", height = 500,
            controls = [
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
            ])

        #define items in container
        Container = ft.Container(
            content=ft.Column(
            controls=[
                self.title,
                self.FieldColumn,
                self.submitButton
            ],
        ),
        )
        #display Home container
        return Container