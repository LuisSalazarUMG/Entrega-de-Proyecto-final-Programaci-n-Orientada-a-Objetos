import flet as ft

class Home(ft.UserControl):
    def __init__(self, page):
        super().__init__(page)

    def build(self):
        return ft.Column(
            controls=[
                ft.Text('Bienvenido, Luis Fernando Salazar Torres'),
                ft.FilledButton(
                    on_click=lambda _: self.page.go('/facciones'), 
                    content=ft.Text('Ir a Facciones', size=25, color='black')
                ),
                ft.FilledButton(
                    on_click=lambda _: self.page.go('/personajes'), 
                    content=ft.Text('Ir a Personaje', size=25, color='black')
                ),
                ft.FilledButton(
                    on_click=lambda _: self.page.go('/mapa'), 
                    content=ft.Text('Ir a Mapa', size=25, color='black')
                ),
                ft.FilledButton(
                    on_click=lambda _: self.page.go('/usuario'), 
                    content=ft.Text('Ir a Usuario', size=25, color='black')
                ),
            ]
        )