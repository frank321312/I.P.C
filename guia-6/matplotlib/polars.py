import pandas as pd

data = {
    'Jurisdicción': [
        'Ciudad Autónoma de Buenos Aires', 'Buenos Aires', 'Catamarca', 'Chaco', 'Chubut',
        'Córdoba', 'Corrientes', 'Entre Ríos', 'Formosa', 'Jujuy', 'La Pampa', 'La Rioja',
        'Mendoza', 'Misiones', 'Neuquén', 'Río Negro', 'Salta', 'San Juan', 'San Luis',
        'Santa Cruz', 'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur',
        'Tucumán'
    ],
    'Capital': [
        '', 'La Plata', 'San Fernando del Valle de Catamarca', 'Resistencia', 'Rawson',
        'Córdoba', 'Corrientes', 'Paraná', 'Formosa', 'San Salvador de Jujuy', 'Santa Rosa', 'La Rioja',
        'Mendoza', 'Posadas', 'Neuquén', 'Viedma', 'Salta', 'San Juan', 'San Luis',
        'Río Gallegos', 'Santa Fe', 'Santiago del Estero', 'Ushuaia', 'San Miguel de Tucumán'
    ],
    'Población (hab)': [
        3075646, 17541141, 415438, 1204541, 618994, 3760450, 1120801, 1385961,
        605193, 770881, 358428, 393531, 1990338, 1261294, 664057, 747610,
        1424397, 781217, 508328, 365698, 3536418, 978313, 173715, 1694656
    ],
    'Superficie (km2)': [
        205.9, 305907.4, 101486.1, 99763.3, 224302.3, 164707.8, 89123.3, 78383.7,
        75488.3, 53244.2, 143492.5, 91493.7, 149069.2, 29911.4, 94422, 202168.6,
        155340.5, 88296.2, 75347.1, 244457.5, 133249.1, 136934.3, 910324.4, 22592.1
    ],
    'PBI': [
        154863803.5, 292689868, 6150949.159, 9832642.672, 17747854.21, 69363739.19,
        7968012.982, 20743409.1, 3807057.419, 6484938.334, 6990262.458, 5590515.628,
        33431369.11, 9646825.835, 22564106.16, 10264584.42, 13438834.91, 8262308.568,
        11780849.36, 11663738.04, 81588690.27, 8387858.731, 7049276.383, 13856198.9
    ],
}

df = pd.DataFrame(data)
