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
from HomeScreen import HomeText, HomeTextBot
from ActivityCreator import Maker
from ActivityManagement import Editor
from Communication import Preferences
#from .daemon import Daemon
"""
PerfectDay1.1, IOS app by Sanjay Mukhyala 2023.
"""

def main(page: ft.Page):

    #background task -> unable to instantiate????
    async def do_background_task(self, widget, **kwargs):
        d = Daemon()
        while True:
            self.counter += 1
            d.job()
            await asyncio.sleep(43200)

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

    # Open and append the file
    def existingActivities():
        #dirpath = tempfile.gettempdir()
        dirpath = "/Users/sanjay/projects/python/PerfectDay/PerfectDay1.1/"
        file_exists = exists(dirpath + "AllActivities.json")
        if file_exists:
            with open(dirpath + "AllActivities.json", "r") as f:
                dataDict = json.load(f)
        else:
            dataDict = {
                "user": "Person",
                "email": "smukhyala@gmail.com",
                "activities": [
                    {

                    }
                ]
            }
        mainData = dataDict
        return mainData

    EAval = existingActivities()
    TopCap = [activity['title'] for activity in EAval['activities']]
    BotCap = [activity['subtitle'] for activity in EAval['activities']]

    # setup activity cards with names
    ActivityCards = ft.Column(scroll='auto', height = 300)
    for top_text, bot_text in zip(TopCap, BotCap):
        new_progress_card = ft.Container(
            border_radius=20,
            bgcolor=ft.colors.BLACK,
            height=100,
            width=350,
            padding=15,
            #on_click=lambda _: page.go('/ActivityManagerView'),
            content=ft.Column(
                controls=[
                    ft.Text(value=top_text, color=ft.colors.WHITE, size=15, weight=ft.FontWeight.W_100, height = 20),
                    ft.Container(width = 320, height = 2, border_radius = 5, bgcolor = ft.colors.BLUE),
                    ft.Text(value=bot_text, color=ft.colors.WHITE, size=12, italic = True, height = 15, width = 400),
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

    #Email and frequency screen
    EmailAndFrequency = ft.Column(alignment='end',
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
                                        Preferences()
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
                                        Editor(),
                                  ]
                              )
                          ),
                      ]
                    )

    #Animate to the host screen
    buffer = ft.Container(width = 1)
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
                                    ft.Row(alignment='spaceBetween', width = 360,
                                        controls=[
                                                ft.IconButton(icon = ft.icons.DIRECTIONS_RUN,
                                                    icon_color=ft.colors.BLACK,
                                                    tooltip = "Make an Activity!",
                                                    on_click = lambda _: page.go('/ActivityMakerView')),
                                                ft.IconButton(icon = ft.icons.MARK_EMAIL_READ_OUTLINED,
                                                    icon_color=ft.colors.BLACK,
                                                    tooltip = "Edit Communication Info!",
                                                    on_click = lambda _: page.go('/EmailAndFrequencyView')),
                                                ft.IconButton(icon = ft.icons.FORMAT_LIST_NUMBERED_OUTLINED,
                                                    icon_color=ft.colors.BLACK,
                                                    tooltip = "Edit Activities!",
                                                    #on_click = lambda _: page.go('/ActivityManagerView')
                                                    ),
                                                ft.IconButton(icon = ft.icons.CLOUD,
                                                    icon_color=ft.colors.BLACK,
                                                    tooltip = "Grab Current Weather!",
                                                    #on_click = lambda _: page.go('/ActivityManagerView')
                                                    ),
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
                                      HomeText(),
                                      ActivityCards,
                                      HomeTextBot()

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

    # Construct the pages
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
        '/EmailAndFrequencyView': ft.View(
            "/EmailAndFrequencyView",
            [
                EmailAndFrequency
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
