# Profiles/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import Profil
import json

@csrf_exempt
def create_Profil(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        profil = Profil.objects.create(
            firstname=data['firstname'],
            lastname=data['lastname'],
            email=data['email'],
            phone_number=data['phoneNumber']
        )
        return JsonResponse({'id': profil.id, 'status': 'created'}, status=201)

@csrf_exempt
def get_Profil(request, profil_id):
    try:
        profil = Profil.objects.get(id=profil_id)
        return JsonResponse({
            'id': profil.id,
            'firstname': profil.firstname,
            'lastname': profil.lastname,
            'email': profil.email,
            'phoneNumber': profil.phone_number
        }, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Profil not found'}, status=404)

@csrf_exempt
def update_Profil(request, profil_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            profil = Profil.objects.get(id=profil_id)
            profil.firstname = data['firstname']
            profil.lastname = data['lastname']
            profil.email = data['email']
            profil.phone_number = data['phoneNumber']
            profil.save()
            return JsonResponse({'status': 'updated'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Profil not found'}, status=404)

@csrf_exempt
def delete_Profil(request, profil_id):
    try:
        profil = Profil.objects.get(id=profil_id)
        profil.delete()
        return JsonResponse({'status': 'deleted'}, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Profil not found'}, status=404)
