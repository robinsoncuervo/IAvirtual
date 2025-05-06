import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('es_ES')  # Datos en español

# Habilidades disponibles
HABILIDADES = [
    'plomero', 'jardinero', 'goteras', 'aseo', 'oficios varios',
    'mercado', 'mandados', 'albanil', 'descargar', 'escolta',
    'mecanico', 'pintura', 'reparacion', 'modisteria', 'Análisis de Datos',
    'programador', 'musica', 'cantante', 'cocinero', 'mesero'
]

UBICACIONES = ['Robledo', 'Poblado', 'Castilla', 'Manrique', 'guayabal', 'santacruz', 'itagui', 'envigado']

def generar_freelancer(id):
    num_habilidades = random.randint(1, 3)
    habilidades = random.sample(HABILIDADES, num_habilidades)
    
    return {
        'id': id,
        'nombre': fake.name(),
        'habilidades': habilidades,
        'valoracion': round(random.uniform(3.5, 5.0), 1),
        'experiencia': random.randint(1, 10),
        'tarifa': random.randint(15, 100),
        'ubicacion': random.choice(UBICACIONES),
        'telegram_id': f"@{fake.user_name()}",
        'telefono': fake.phone_number(),
        'created_at': (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat()
    }

# Generar 100 freelancers
datos = [generar_freelancer(i+1) for i in range(100)]

# Escribir CSV
with open('freelancers.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'nombre', 'habilidades', 'valoracion', 'experiencia', 
                 'tarifa', 'ubicacion', 'telegram_id', 'telefono', 'created_at']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for freelancer in datos:
        # Convertir lista de habilidades a string entre comillas
        freelancer['habilidades'] = '{"' + '","'.join(freelancer['habilidades']) + '"}'
        writer.writerow(freelancer)

print("Archivo 'freelancers.csv' generado con éxito!")





import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('es_ES')  # Datos en español

# Configuración
HABILIDADES = [
    'plomero', 'jardinero', 'goteras', 'aseo', 'oficios varios',
    'mercado', 'mandados', 'albanil', 'descargar', 'escolta',
    'mecanico', 'pintura', 'reparacion', 'modisteria', 'Análisis de Datos',
    'programador', 'musica', 'cantante', 'cocinero', 'mesero'
]

UBICACIONES = ['Robledo', 'Poblado', 'Castilla', 'Manrique', 'guayabal', 'santacruz', 'itagui', 'envigado']

ESTADOS_DISPONIBILIDAD = ['Disponible ahora', 'Ocupado 2 dias', 'Disponible proximo dia', 'En vacaciones']

def generar_freelancer(id):
    num_habilidades = random.randint(1, 5)
    habilidades = random.sample(HABILIDADES, num_habilidades)
    
    return {
        'id': id,
        'nombre': fake.name(),
        'habilidades': habilidades,
        'valoracion': round(random.uniform(3.5, 5.0), 1),
        'experiencia': random.randint(1, 10),
        'tarifa': random.randint(15, 100),
        'ubicacion': random.choice(UBICACIONES),
        'telegram_id': f"@{fake.user_name()}",
        'telefono': fake.phone_number(),
        'disponibilidad': random.choice(ESTADOS_DISPONIBILIDAD),
        'created_at': (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat()
    }

# Generar 100 freelancers
datos = [generar_freelancer(i+1) for i in range(100)]

# Escribir CSV
with open('freelancers_con_disponibilidad.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = [
        'id', 'nombre', 'habilidades', 'valoracion', 'experiencia',
        'tarifa', 'ubicacion', 'telegram_id', 'telefono', 'disponibilidad', 'created_at'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for freelancer in datos:
        # Convertir lista de habilidades a formato array de Postgres
        freelancer['habilidades'] = '{"' + '","'.join(freelancer['habilidades']) + '"}'
        writer.writerow(freelancer)

print("Archivo 'freelancers_con_disponibilidad.csv' generado con éxito!")