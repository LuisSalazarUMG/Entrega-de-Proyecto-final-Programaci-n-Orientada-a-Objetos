from flet import *
from models.Personaje.Personaje import Personaje
class Comp3(UserControl):
    def __init__(self,page):
        super().__init__(page)
        self.personaje=[Personaje('Soldados de Infantería'),Personaje('Infantería Pesada'),Personaje('Francotiradores'),Personaje('Ingenieros')]
        self.personajesflet=GridView( 
        runs_count=5,
        max_extent=350,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5
        )
    def llenarpersonajes(self):
        for personaje in self.personaje:
            self.personajesflet.controls.append(
                Container(
                    border_radius=20,
                    bgcolor=colors.GREY,
                    padding=10,
                    content=Column(
                        spacing=5,
                        controls=[
                        Text(f"{personaje.personaje}", size=20, text_align=TextAlign.CENTER),
                    ]
                        
                    )
                )
            )
    def build(self):
        self.llenarpersonajes()
        return Container(
            margin=10,
            padding=10,
        content=Column(
                alignment=alignment.center,
                controls=[
                Text('Personajes', size=50,weight=FontWeight.BOLD),
                Text('Aqui encontraras los personajes existentes'),
                self.personajesflet,
                FilledButton(
                    on_click=lambda _: self.page.go('/'), 
                    content=Text('Ir a Inicio', size=25, color='black')
                )
                ]
            ) 
        )