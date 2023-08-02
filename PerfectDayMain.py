from __future__ import print_function, unicode_literals, absolute_import
from threading import *
import subprocess
import json
import tempfile
import asyncio
import os
from os.path import exists

#flet imports
import flet as ft
from HomeScreen import Home
from ActivityEditor import Maker

"""
PerfectDay1.1, IOS app by Sanjay Mukhyala 2023.
"""

def main(page: ft.Page):

    #test print function
    def print_all_activities():
        dirpath = tempfile.gettempdir()
        file_path = dirpath + "AllActivities.json"

        if exists(file_path):
            with open(file_path, "r") as f:
                data = json.load(f)
                print(json.dumps(data, indent=4))
        else:
            print("AllActivities.json file does not exist.")

    #print_all_activities()

    # Open and append the file
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

    EAval = existingActivities()
    TopCap = [activity['title'] for activity in EAval['activities']]
    BotCap = [activity['subtitle'] for activity in EAval['activities']]

    # setup activity cards with names
    ActivityCards = ft.Column(scroll='auto',)
    for top_text, bot_text in zip(TopCap, BotCap):
        new_progress_card = ft.Container(
            border_radius=20,
            bgcolor=ft.colors.GREEN,
            height=75,
            width=150,
            padding=15,
            on_click=lambda _: page.go('/ActivityManagerView'),
            content=ft.Column(
                controls=[
                    ft.Text(value=top_text, color=ft.colors.BLACK, size=12, height = 15),
                    ft.Text(value=bot_text, color=ft.colors.BLUE, size=10, height = 15),
                ]
            )
        )
        ActivityCards.controls.append(new_progress_card)

    #Activity Maker Screen
    ActivityMaker = ft.Column(alignment='end',
                      controls=[
                          ft.Container(
                              width=400,
                              height=850,
                              bgcolor=ft.colors.WHITE,
                              border_radius=35,
                              animate=ft.animation.Animation(600, ft.AnimationCurve.DECELERATE),
                              animate_scale=ft.animation.Animation(400, curve='decelerate'),
                              padding=ft.padding.only(top=50, left=20, right=20, bottom=5),
                              content=ft.Column(
                                  controls=[
                                        ft.IconButton(
                                            icon = ft.icons.ARROW_BACK, 
                                            icon_color=ft.colors.BLACK, 
                                            icon_size=24,
                                            on_click = lambda _: page.go('/'),
                                            tooltip = "Go Back"),
                                        Maker()
                                  ]
                              )
                          ),
                          
                      ]
                      )
    
    #Errors Screen
    ErrorLog = ft.Column(alignment='end',
                      controls=[
                          ft.Container(
                              width=400,
                              height=850,
                              bgcolor=ft.colors.WHITE,
                              border_radius=35,
                              animate=ft.animation.Animation(600, ft.AnimationCurve.DECELERATE),
                              animate_scale=ft.animation.Animation(400, curve='decelerate'),
                              padding=ft.padding.only(top=50, left=20, right=20, bottom=5),
                              content=ft.Column(
                                  controls=[
                                        ft.IconButton(
                                            icon = ft.icons.ARROW_BACK, 
                                            icon_color=ft.colors.BLACK, 
                                            icon_size=24,
                                            on_click = lambda _: page.go('/'),
                                            tooltip = "Go Back"),
                                  ]
                              )
                          ),
                          
                      ]
                      )
    
    #Activity Management Screen
    ActivityManager = ft.Column(alignment='end',
                      controls=[
                          ft.Container(
                              width=400,
                              height=850,
                              bgcolor=ft.colors.WHITE,
                              border_radius=35,
                              animate=ft.animation.Animation(600, ft.AnimationCurve.DECELERATE),
                              animate_scale=ft.animation.Animation(400, curve='decelerate'),
                              padding=ft.padding.only(top=50, left=20, right=20, bottom=5),
                              content=ft.Column(
                                  controls=[
                                        ft.IconButton(
                                            icon = ft.icons.ARROW_BACK, 
                                            icon_color=ft.colors.BLACK, 
                                            icon_size=24,
                                            on_click = lambda _: page.go('/'),
                                            tooltip = "Go Back"),
                                  ]
                              )
                          ),
                          
                      ]
                      )
    
    #Animate to the host screen
    Host = ft.Column(alignment='end',
                      controls=[
                          ft.Container(
                              width=400,
                              height=850,
                              bgcolor=ft.colors.WHITE,
                              border_radius=35,
                              animate=ft.animation.Animation(600, ft.AnimationCurve.DECELERATE),
                              animate_scale=ft.animation.Animation(400, curve='decelerate'),
                              padding=ft.padding.only(top=50, left=20, right=20, bottom=5),
                              content=ft.Column(
                                  controls=[
                                      Home(),
                                      ActivityCards,
                                      ft.ElevatedButton(text = "Make an Activity!", on_click = lambda _: page.go('/ActivityMakerView')),
                                      ft.ElevatedButton(text = "Check for Email Mistakes!", on_click = lambda _: page.go('/ErrorLogView')),
                                      ft.ElevatedButton(text = "Make an Activity!", on_click = lambda _: page.go('/ActivityManagerView'))
                                  ]
                              )
                          ),
                          
                      ]
                      )

    #Construct the app
    Layout = ft.Container(
        width=400,
        height=850,
        bgcolor=ft.colors.WHITE,
        border_radius=35,
        content=ft.Stack(
            controls=[
                Host,
            ]
        )
    )

    global pages
    pages = {
        '/': ft.View(
            "/",
            [
                Host
            ]
        ),
        '/ActivityMakerView': ft.View(
            "/ActivityMakerView",
            [
                ActivityMaker
            ]
        ),
        '/ErrorLogView': ft.View(
            "/ErrorLogView",
            [
                ErrorLog
            ]
        ),
        '/ActivityManagerView': ft.View(
            "/ActivityManagerView",
            [
                ActivityManager
            ]
        ),
    }

    # Transfer page function
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    # Setup
    page.title = "PerfectDay"
    page.on_route_change = route_change
    page.go(page.route)
    page.add(Layout)


ft.app(target=main)