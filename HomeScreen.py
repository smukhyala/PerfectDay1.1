import flet as ft

class Home(ft.UserControl):
    def build(self):
        #set items
        self.displayText = ft.Text('Welcome to PerfectDay!', color=ft.colors.BLACK)
        self.profileIcon = ft.IconButton(
                                            icon = ft.icons.PERSON, 
                                            icon_color=ft.colors.BLACK, 
                                            tooltip = "Profile")
    
        #define items in container
        Container = ft.Container(
            content=ft.Column(
            controls=[
                ft.Row(alignment='spaceBetween',
                       controls=[
                            self.profileIcon,
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
            ],
        ),
        )
        #display Home container
        return Container