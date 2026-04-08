from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profil, Category, Service, Modele, Commentaire, Gout, Message

class ProfilAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'created_at')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (('Rôle', {'fields': ('role',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (('Rôle', {'fields': ('role',)}),)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom', 'created_at')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'created_at')

class ModeleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'service', 'created_at', 'likes_count')
    def likes_count(self, obj): return obj.likes_count
    likes_count.short_description = 'Likes'

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('modele', 'profil', 'contenu_preview', 'created_at')
    def contenu_preview(self, obj): return obj.contenu[:50] + '...' if len(obj.contenu) > 50 else obj.contenu
    contenu_preview.short_description = 'Contenu'

class GoutAdmin(admin.ModelAdmin):
    list_display = ('modele', 'profil', 'created_at')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephone', 'created_at')

admin.site.register(Profil, ProfilAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Modele, ModeleAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Gout, GoutAdmin)
admin.site.register(Message, MessageAdmin)

admin.site.site_header = 'Administration TMB Service'
admin.site.site_title = 'TMB Service Admin'

# Register your models here.
