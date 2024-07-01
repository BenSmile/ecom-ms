# views.py
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer
import json

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_customer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Connexion réussie
            login(request, user)
            # Redirection vers la page d'accueil ou une autre page après connexion
            return redirect('home')
        else:
            # Échec de l'authentification
            return JsonResponse({'message' : 'Informations incorrectes !'})
    else:
        # Demande GET (affichage du formulaire de connexion)
        return JsonResponse(user)



def create_customer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        customer = Customer.objects.create(**data)
        return JsonResponse({'id': customer.id}, status=201)

def get_customers(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        datas = {"customers": list(customers.values())}
        return JsonResponse(datas)

def get_customer(request):
    if request.method == 'GET':
        user = request.user
        customer = get_object_or_404(Customer, id=user.id)
        return JsonResponse({
            'id': customer.id,
            'firstname': customer.firstname,
            'lastname': customer.lastname,
            'email': customer.email,
            'phoneNumber': customer.phoneNumber
        })

@csrf_exempt
def update_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        for key, value in data.items():
            setattr(customer, key, value)
        customer.save()
        return JsonResponse({'message': 'Customer updated'})

@csrf_exempt
def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'DELETE':
        customer.delete()
        return JsonResponse({'message': 'Customer deleted'})
