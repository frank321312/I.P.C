import pandas as pd

data = {
    'nombre': ['Violeta', 'Carla', 'Manuela', 'Lucia', 'Emilia', 'Mariana', 'Aldo'],
    'apellido': ['Perez', 'Guanca', 'Gomez', 'Capon', 'Duzac', 'Szischik', 'Rastrelli'],
    'dni': [42000000, 42001001, 42002002, 37010020, 40001002, 38090080, 38111222],
    'año_nac': [1997, 1998, 1998, 1993, 2003, 1993, 1994],
    'mail': ['vp@fi.uba.ar', 'cg@fi.uba.ar', None, None, None, 'ms@fi.uba.ar', 'ar@fi.uba.ar'],
    'carrera': ['Informática', 'Mecánica', 'Química', 'Informática', 'Informática', 'Electrónica', 'Informática']
}

df = pd.DataFrame(data)