from run import create_app
from database import db
from models import Phase

# Fases del Ciclo de Vida del Desarrollo de Software
SDLC_PHASES = [
    {
        "name": "Planificación",
        "description": "Definición del alcance, propósito del sistema y viabilidad del proyecto.",
        "order": 1
    },
    {
        "name": "Análisis",
        "description": "Recopilación y análisis de los requisitos del sistema y del negocio.",
        "order": 2
    },
    {
        "name": "Diseño",
        "description": "Diseño de la arquitectura del software, UI/UX y base de datos.",
        "order": 3
    },
    {
        "name": "Implementación (Desarrollo)",
        "description": "Escritura de código y construcción del software según el diseño.",
        "order": 4
    },
    {
        "name": "Pruebas",
        "description": "Validación y verificación del software para encontrar y corregir errores.",
        "order": 5
    },
    {
        "name": "Despliegue",
        "description": "Liberación del software en un entorno de producción para el usuario final.",
        "order": 6
    },
    {
        "name": "Mantenimiento",
        "description": "Actualizaciones, soporte y mejora continua del software post-lanzamiento.",
        "order": 7
    }
]

def seed_db():
    app = create_app()
    with app.app_context():
        # Crear todas las tablas
        db.create_all()
        
        # Verificar si ya existen fases
        if Phase.query.count() == 0:
            for p_data in SDLC_PHASES:
                phase = Phase(name=p_data['name'], description=p_data['description'], order=p_data['order'])
                db.session.add(phase)
            db.session.commit()
            print("Base de datos inicializada y poblada con las fases SDLC.")
        else:
            print("La base de datos ya contiene datos.")

if __name__ == '__main__':
    seed_db()
