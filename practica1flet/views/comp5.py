from flet import *
from models.Usuario.Usuario import Usuario
class Comp5(UserControl):
    def __init__(self,page):
        super().__init__(page)
        self.usuario=[Usuario('Usuario1'),Usuario('Usuario2'),Usuario('Usuario3'),Usuario('Usuario4')]
        self.usuariosflet=GridView( 
        runs_count=5,
        max_extent=350,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
        )
    def llenarusuarios(self):
        for usuario in self.usuario:
            self.usuariosflet.controls.append(
                Container(
                    border_radius=20,
                    bgcolor=colors.GREY,
                    padding=10,
                    content=Column(
                        spacing=5,
                        controls=[
                        Text(f"{usuario.usuario}", size=20, text_align=TextAlign.CENTER),
                    ]
                        
                    )
                )
            )
    def build(self):
        self.llenarusuarios()
        return Container(
            margin=10,
            padding=10,
        content=Column(
                alignment=alignment.center,
                controls=[
                Text('Usuarios', size=50,weight=FontWeight.BOLD),
                Text('Aqui encontraras los usuarios existentes'),
                self.usuariosflet,
                FilledButton(
                    on_click=lambda _: self.page.go('/'), 
                    content=Text('Ir a Inicio', size=25, color='black')
                )
                ]
            ) 
        )