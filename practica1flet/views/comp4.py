from flet import *
from models.Mapa.Mapa import Mapa
class Comp4(UserControl):
    def __init__(self,page):
        super().__init__(page)
        self.mapa=[Mapa('Coruscant'),Mapa('Felucia'),Mapa('Kamino'),Mapa('Geonosis'),Mapa('Mustafar'),Mapa('Utapau'),Mapa('Kashyyyk'),Mapa('Hoth'),Mapa('Endor'),Mapa('Tatooine'),Mapa('Dagobah'),Mapa('Yavin IV'),Mapa('Naboo'),Mapa('Polis Massa'),Mapa('Estrella de la Muerte'),Mapa('Tantive IV'),Mapa('Mygeeto')]
        self.mapasflet=GridView( 
        runs_count=5,
        max_extent=350,
        child_aspect_ratio=4.4,
        spacing=5,
        run_spacing=5
        )
    def llenarmapas(self):
        for mapa in self.mapa:
            self.mapasflet.controls.append(
                Container(
                    border_radius=20,
                    bgcolor=colors.GREY,
                    padding=10,
                    content=Column(
                        spacing=5,
                        controls=[
                        Text(f"{mapa.mapa}", size=20, text_align=TextAlign.CENTER),
                    ]
                        
                    )
                )
            )
    def build(self):
        self.llenarmapas()
        return Container(
            margin=10,
            padding=10,
        content=Column(
                alignment=alignment.center,
                controls=[
                Text('Mapas', size=50,weight=FontWeight.BOLD),
                Text('Aqui encontraras los mapas existentes'),
                self.mapasflet,
                FilledButton(
                    on_click=lambda _: self.page.go('/'), 
                    content=Text('Ir a Inicio', size=25, color='black')
                )
                ]
            ) 
        )