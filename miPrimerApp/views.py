from django.shortcuts import render

# Create your views here.
def miIndex(request):
    data = {
        'nombre': 'Juan José',
        'apellido':'Reyes Herrera',
        'profesion':'Estudiante',
        'edad': 22,
        'ciudad': 'Talca',
        'imagen': '../static/img/images.jpg',
    }
    return render(request, 'miPrimerApp/index.html',data)

def proyecto (request):
    info = {
        'seccion': 'libros',
        'libro': [
            {
                'id': 1,
                'nombre': 'Frankenstein',
                'descripcion':'Es un libro que trata de la historia de un hombre que en busca del objetivo de revivir a los muertos y defasiar a dios, crea un mounstro',
                'imagen': '../static/img/frankensteinCOLOR.webp'
            },
            {
                'id': 2,
                'nombre': 'Ready player One',
                'descripcion':'se trata de un mundo distopico el cual basa toda su economia y sistemas politicos en un videojuego inmersivo que inventó una persona, esta persona al morir desata el caos en el mundo al decir que en este mismo juego, escondio un easter egg que convertira al que lo encuentre en el dueño de este mismo juego',
                'imagen': '../static/img/48ffd5ba5f507fc2ba9986d0531cd615.webp'
            },
            {
                'id': 3,
                'nombre': 'La biblia',
                'descripcion':'la biblia de one piece, todo un misterio',
                'imagen': '../static/img/images (1).jpg'
            },
        ]
    }
    return render(request, 'miPrimerApp/proyecto.html',info)
