import flet as ft
import os
import json
import tempfile
from os.path import exists

class Home(ft.UserControl):
    def build(self):

        #set items
        self.displayTest = ft.Text('Welcome to PerfectDay!', color=ft.colors.BLACK)
        self.profileIcon = ft.Container(ft.IconButton(
                                            icon = ft.icons.PERSON, 
                                            icon_color=ft.colors.BLACK, 
                                            tooltip = "Profile"),)

        #define items in container
        Container = ft.Container(
            content=ft.Column(
            controls=[
                ft.Row(alignment='spaceBetween',
                       controls=[
                            self.displayTest,
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
                self.profileIcon,
            ],
        ),
        )

        #display Home container
        return Container

def main(page: ft.Page):
   
    page.title = "DoulAI"
    
    invisible_control = ft.Container(
        width=400,
        height=850,
        bgcolor=ft.colors.WHITE,
        border_radius=35,
    )
    RPage = ft.Column(alignment='end',
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
                                  ]
                              )
                          ),
                          invisible_control
                      ]
                      )
    MCont = ft.Container(
        width=400,
        height=850,
        bgcolor=ft.colors.WHITE,
        border_radius=35,
        content=ft.Stack(
            controls=[
                RPage,
            ]
        )
    )

    pages = {
        '/': ft.View(
            "/",
            [
                RPage
            ]
        ),
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    page.add(MCont)
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)