import flet as ft
import os
import json
import tempfile
from os.path import exists
from HomeScreen import Home

def main(page: ft.Page):
    #Activities Screen
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
                              content=ft.Stack(
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
                              content=ft.Stack(
                                  controls=[
                                      Home(),
                                      ft.Container(height = 200),
                                      ft.ElevatedButton(text = "Make an Actvity!", on_click = lambda _: page.go('/ActivityView'))
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

    #Defining app page views
    pages = {
        '/': ft.View(
            "/",
            [
                Host
            ]
        ),
        '/ActivityView': ft.View(
            "/ActivityView",
            [
                ActivityMaker
            ]
        )
    }

    #transfer page function
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    #setup
    page.title = "PerfectDay"
    page.on_route_change = route_change
    page.go(page.route)
    page.add(Layout)

#run
ft.app(target=main)