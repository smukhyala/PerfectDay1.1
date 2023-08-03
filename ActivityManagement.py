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
        self.buffer = ft.Container(height = 2)
        self.general = ft.Text("General Settings:", color = ft.colors.BLACK, size = 17)
        self.weather = ft.Text("Weather Settings:", color = ft.colors.BLACK, size = 17)

        d = "p"
        self.MaxTemp = ft.Text("Maximum Temperature:", color = ft.colors.GREY_900, size = 15)
        self.MaxTempField = ft.TextField(label=f"Current: {d}", 
                                    width = 300,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MinTemp = ft.Text("Minimum Temperature:", color = ft.colors.GREY_900, size = 15)
        self.MinTempField = ft.TextField(label=f"Current: {d}", 
                                    width = 300,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MaxWind = ft.Text("Maximum Wind:", color = ft.colors.GREY_900, size = 15)
        self.MaxWindField = ft.TextField(label=f"Current: {d}", 
                                    width = 300,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MinWind = ft.Text("Minimum Wind:", color = ft.colors.GREY_900, size = 15)
        self.MinWindField = ft.TextField(label=f"Current: {d}", 
                                    width = 300,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MaxHumi = ft.Text("Maximum Humidity:", color = ft.colors.GREY_900, size = 15)
        self.MaxHumiField = ft.TextField(label=f"Current: {d}", 
                                    width = 300,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.MinHumi = ft.Text("Manimum Humidity:", color = ft.colors.GREY_900, size = 15)
        self.MinHumiField = ft.TextField(label=f"Current: {d}", 
                                    width = 300,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.Name = ft.Text("Activity Name:", color = ft.colors.GREY_900, size = 15)
        self.NameField = ft.TextField(label=f"Current: {d}", 
                                    width = 300,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)
        self.City = ft.Text("Current City:", color = ft.colors.GREY_900, size = 15)
        self.CityField = ft.TextField(label=f"Current: {d}", 
                                    width = 300,
                                    height = 35,
                                    border_color = ft.colors.BLACK,
                                    bgcolor = ft.colors.GREY_100,
                                    color = ft.colors.BLACK)

        self.CaptionColumn = ft.Column(alignment = "left",
            contents = [
                self.Name,
                self.City,
                self.MaxTemp,
                self.MinTemp,
                self.MaxWind,
                self.MinWind,
                self.MaxHumi,
                self.MinHumi,
            ])
        self.FieldColumn = ft.Column(alignment = "right",
            contents = [
                self.NameField,
                self.CityField,
                self.MaxTempField,
                self.MinTempField,
                self.MaxWindField,
                self.MinWindField,
                self.MaxHumiField,
                self.MinHumiField,
            ])
        self.Row = ft.Row(contents = [self.CaptionColumn, self.FieldColumn])

        #define items in container
        Container = ft.Container(
            content=ft.Column(
            controls=[
                self.Row,
            ],
        ),
        )
        #display Home container
        return Container