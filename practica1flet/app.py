import flet as ft
from routes import routes_handler

def main(page: ft.Page):
    #esta propagación de campos sirve para redireccionar (hacia atras)
  def view_pop(e):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)

  #esta subrutina sirve como propagación de cambios cada que cambiemos de ruta
  def route_change(route):
    #esto es para depurar en consola hacia que ruta nos dirigimos
    print(page.route)
    #cada que abrimos una nueva ruta, la pantalla tiene que limpiarse antes
    page.views.clear()
    #agregamos el router, para que se contemple la opción de distintas vistas de pantalla
    page.views.append(
      routes_handler(page)[page.route]
    )
    page.update()

  #este evento generará la acción de cambio de vista
  page.on_route_change = route_change
  page.go('/')


ft.app(target=main)