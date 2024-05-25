from flet import *
from models.Faccion.Faccion import Faccion
class Comp2(UserControl):
    def __init__(self,page):
        super().__init__(page)
        self.faccion=[Faccion('República Galáctica'),Faccion('CSI'),Faccion('Imperio Galáctico'),Faccion('Alianza Rebelde')]
        self.faccionesflet=GridView( 
        runs_count=5,
        max_extent=350,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5
        )
    def llenarfacciones(self):
        for faccion in self.faccion:
            self.faccionesflet.controls.append(
                Container(
                    border_radius=20,
                    bgcolor=colors.GREY,
                    padding=10,
                    content=Column(
                        spacing=5,
                        controls=[
                        Text(f"{faccion.faccion}", size=20, text_align=TextAlign.CENTER),
                    ]
                        
                    )
                )
            )
    def build(self):
        self.llenarfacciones()
        return Container(
            margin=10,
            padding=10,
        content=Column(
                alignment=alignment.center,
                controls=[
                Text('Facciones', size=50,weight=FontWeight.BOLD),
                Text('Aqui encontraras las facciones existentes'),
                self.faccionesflet,
                FilledButton(
                    on_click=lambda _: self.page.go('/'), 
                    content=Text('Ir a Inicio', size=25, color='black')
                )
                ]
            ) 
        )