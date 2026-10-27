from django.shortcuts import render
from .models import Article, Doctor

# Vue pour la page d'accueil
def home_view(request):
    articles = Article.objects.all().order_by('-created_at')
    
    doctor = Doctor.objects.first()
    
    context = {
        'doctor_name': doctor.name if doctor else 'Nom de la Docteure',
        'doctor_photo': doctor.photo.url if (doctor and doctor.photo) else 'images/dr-photo.jpg',
        'articles': articles,
    }
    
    return render(request, 'home.html', context)


def doctors_list_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors_list.html', {'doctors': doctors})