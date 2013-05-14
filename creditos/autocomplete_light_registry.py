import autocomplete_light

from cities_light.models import City
from models import Cliente

autocomplete_light.register(City, search_fields=('search_names',),
    autocomplete_js_attributes={'placeholder': 'Nombre de la ciudad..'})
autocomplete_light.register(Cliente, search_fields=('nombre',),
    autocomplete_js_attributes={'placeholder': 'Nombre del cliente..'})
