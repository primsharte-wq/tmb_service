from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Count
from .models import Category, Service, Modele, Gout, Commentaire
from .forms import RegistrationForm, CommentaireForm, MessageForm

def index(request):
    categories = Category.objects.all().annotate(services_count=Count('services'))[:6]
    recent_modeles = Modele.objects.all().order_by('-created_at')[:6]
    return render(request, 'index.html', {'categories': categories, 'recent_modeles': recent_modeles})

def services(request):
    categories = Category.objects.all().prefetch_related('services')
    return render(request, 'services.html', {'categories': categories})

def galerie(request):
    modeles = Modele.objects.all().select_related('service', 'service__categorie')
    categorie_id = request.GET.get('categorie')
    service_id = request.GET.get('service')
    if categorie_id:
        modeles = modeles.filter(service__categorie_id=categorie_id)
    if service_id:
        modeles = modeles.filter(service_id=service_id)
    categories = Category.objects.all()
    return render(request, 'galerie.html', {'modeles': modeles, 'categories': categories})

def modele_detail(request, modele_id):
    modele = get_object_or_404(Modele, id=modele_id)
    commentaires = modele.commentaires.all().select_related('profil')
    comment_form = CommentaireForm()
    message_form = MessageForm()
    user_liked = False
    if request.user.is_authenticated:
        user_liked = Gout.objects.filter(modele=modele, profil=request.user).exists()
    return render(request, 'modele_detail.html', {
        'modele': modele, 'commentaires': commentaires,
        'comment_form': comment_form, 'message_form': message_form, 'user_liked': user_liked
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if request.user.is_authenticated:
                message.profil = request.user
            message.save()
            messages.success(request, 'Merci pour votre message. Cliquez ici pour nous contacter sur WhatsApp')
            return redirect('contact')
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscription réussie! Vous pouvez maintenant vous connecter.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def toggle_like(request, modele_id):
    modele = get_object_or_404(Modele, id=modele_id)
    like, created = Gout.objects.get_or_create(modele=modele, profil=request.user)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'liked': liked, 'likes_count': modele.likes_count})
    return redirect('modele_detail', modele_id=modele_id)

@login_required
def add_comment(request, modele_id):
    modele = get_object_or_404(Modele, id=modele_id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.modele = modele
            commentaire.profil = request.user
            commentaire.save()
            messages.success(request, 'Commentaire ajouté avec succès!')
    return redirect('modele_detail', modele_id=modele_id)

# Create your views here.
