from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from polls.forms import AppointmentForm
from .models import Article, Doctor,Category,Comment
from django.core.paginator import Paginator

def home_view(request):
    articles = Article.objects.all().order_by('-created_at')
    doctor = Doctor.objects.first()
    
    doctors_preview = Doctor.objects.all()[:3]
    
    context = {
        'doctor_name': doctor.name if doctor else 'Nom de la Docteure',
        'doctor_photo':'images/1740545979732.jfif',
        'articles': articles,
        'doctors_preview': doctors_preview, # <-- Ajouté ici
    }
    
    return render(request, 'home.html', context)


def doctors_list_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors_list.html', {'doctors': doctors})

def doctor_detail_view(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    articles = Article.objects.filter(author=doctor).order_by('-created_at')
    
    context = {
        'doctor': doctor,
        'articles': articles,
    }
    return render(request, 'doctor_detail.html', context)

def article_detail_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.all().order_by('-created_at') if hasattr(article, 'comments') else []
    
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        content = request.POST.get('content') 
        if author_name and content:
            Comment.objects.create(article=article, author_name=author_name, content=content) 
            return redirect('article_detail', slug=article.slug)

    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'article_detail.html', context)


def articles_list_view(request):
    category_slug = request.GET.get('category')
    articles_list = Article.objects.all().order_by('-created_at')
    
    # Filtrage par catégorie si un slug est fourni
    if category_slug:
        articles_list = articles_list.filter(category__slug=category_slug)
    
    # Pagination : 6 articles par page
    paginator = Paginator(articles_list, 6)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    
    categories = Category.objects.all() if 'Category' in globals() else []
    
    context = {
        'articles': articles,
        'categories': categories,
        'selected_category': category_slug,
    }
    return render(request, 'articles_list.html', context)

def about_view(request):

    static_data = {
        "titre_principal": "À propos de la plateforme",
        "sous_titre": "Un espace d'échange, de recherche médicale et de sensibilisation pour rapprocher les professionnels de santé et les patients.",
        "pourquoi_titre": "Pourquoi cet espace médical ?",
        "pourquoi_texte": "Face aux défis de la santé publique et au besoin croissant d'informations médicales fiables, cette plateforme a été conçue comme un pont numérique.",
        "nom_docteure": "Dr. Aïcha Mbarga",
        "specialite": "Cardiologie & Prévention Cardiovasculaire",
    }

    context = {
        'doctor': Doctor.objects.first(),
        'page_data': static_data, 
    }
    return render(request, 'about.html', context)


def appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            
            subject = f"Nouveau rendez-vous de {appointment.patient_name}"
            message = (
                f"Un nouveau rendez-vous a été demandé :\n\n"
                f"Patient : {appointment.patient_name}\n"
                f"E-mail : {appointment.patient_email}\n"
                f"Téléphone : {appointment.patient_phone}\n"
                f"Médecin : {appointment.doctor}\n"
                f"Date souhaitée : {appointment.preferred_date}\n"
                f"Motif : {appointment.reason}"
            )
            try:
                send_mail(
                    subject,
                    message,
                    'contact@ynodev.ovh',
                    ['fotsoyvesdonald@gmail.com'], 
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Erreur d'envoi d'e-mail : {e}")

            messages.success(request, "Votre demande de rendez-vous a bien été envoyée. Nous vous contacterons rapidement pour confirmation.")
            return redirect('appointment')
    else:
        form = AppointmentForm()

    context = {
        'form': form,
        'doctors': Doctor.objects.all(),
    }
    return render(request, 'appointment.html', context)