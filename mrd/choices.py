MONTH_CHOICES = (
    ["1", "1"],
    ["2", "2"],
    ["3", "3"],
    ["4", "4"],
    ["5", "5"],
    ["6", "6"],
    ["7", "7"],
    ["8", "8"],
    ["9", "9"],
    ["10", "10"],
    ["11", "11"],
    ["12", "12"],

)

YEAR_CHOICES = [
    ["1", "1"],
    ["2", "2"],
    ["3", "3"],
    ["4", "4"],
    ["5", "5"],
    ["6", "6"],
    ["7", "7"],
    ["8", "8"],
    ["9", "9"],
    ["10", "10"],

]

resguardo = [
    ["OF", "OFICINA"],
    ["ARC", "Archivo Central"],
    ["LG", "Logicsa"],

]

credito = [
    ["ACTIVO", "Activo"],
    ["CANCELADO", "Cancelado"],

]

STATUS_CHOICES = [
    ('IN', 'En custodia'),
    ('OUT', 'Fuera de custodia'),
    ('DELETE', 'Baja'),
    ('DESTROYED', 'Destruido'),
]

SEGURIDAD_CHOICES = [
    ('P', 'Publico'),
    ('I', 'Interno'),
    ('C', 'Confidencial'),
]