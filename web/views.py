
from django.shortcuts import render


def inicio(request):
    contexto = {
        'titulo': 'Mi Proyecto Django',
        'subtitulo': 'Desarrollo web con Python, Django y CSS',
        'descripcion': (
            'Aplicación web que demuestra la configuración del entorno '
            'virtual, el control de versiones y el uso de plantillas.'
        ),
        'modulos': [
            {
                'nombre': 'Entorno virtual',
                'descripcion': 'Aislamiento de dependencias con venv.',
                'icono': '01'
            },
            {
                'nombre': 'Framework Django',
                'descripcion': 'Organización del proyecto mediante MVT.',
                'icono': '02'
            },
            {
                'nombre': 'Git y GitHub',
                'descripcion': 'Control de versiones y trabajo colaborativo.',
                'icono': '03'
            },
            {
                'nombre': 'HTML y CSS',
                'descripcion': 'Plantillas dinámicas y diseño adaptable.',
                'icono': '04'
            }
        ]
    }

    return render(request, 'web/index.html', contexto)
