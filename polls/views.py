from django.shortcuts import render


# Vue pour la page d'accueil
def home_view(request):
    # On peut passer des données au template ici
    context = {
        'username': 'Donald',
        'status': 'Admin'
    }
    return render(request, 'home.html', context)
