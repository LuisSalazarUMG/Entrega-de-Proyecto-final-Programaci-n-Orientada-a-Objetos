from flet import View
from views.home import Home
from views.comp2 import Comp2
from views.comp3 import Comp3
from views.comp4 import Comp4
from views.comp5 import Comp5
from controls.NavBar import NavBar
#from views.reservaciones import Reservaciones
def routes_handler(page):
  return {
    '/':View(
        route='/',
        controls=[
          #escribe aqui el componente que corresponda
          NavBar(page),
          Home(page)
        ]
      ),
    '/facciones':View(
        route='/facciones',
        controls=[
          #escribe aqui el componente que corresponda
          NavBar(page),
          Comp2(page)
        ]
      ),
      '/personajes':View(
        route='/personajes',
        controls=[
          #escribe aqui el componente que corresponda
          NavBar(page),
          Comp3(page)
        ]
      ),
      '/mapa':View(
        route='/mapa',
        controls=[
          #escribe aqui el componente que corresponda
          NavBar(page),
          Comp4(page)
        ]
      ),
      '/usuario':View(
        route='/usuario',
        controls=[
          #escribe aqui el componente que corresponda
          NavBar(page),
          Comp5(page)
        ]
      ),
    #copia y pega a partir de esta jerarquí­a para añadir más rutas
  }