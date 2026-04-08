from django.conf import settings

def whatsapp_number(request):
    return {'WHATSAPP_NUMBER': settings.WHATSAPP_NUMBER}