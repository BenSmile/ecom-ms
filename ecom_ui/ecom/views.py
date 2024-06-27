from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

# Create your views here.

def login_view(request):
    return render(request, "login.html")



def register_view(request):
    return render(request, "register.html")



def home_view(request):

    access_token = request.COOKIES.get('access_token')
    if not access_token:
        return redirect('login')

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    user = requests.get('http://127.0.0.1:8000/api/customer', headers=headers)
    products = requests.get('http://127.0.0.1:8000/api/products', headers=headers)

    if user.status_code == 200 and products.status_code == 200:
        user_data = user.json()
        products_datas = products.json()
        return render(request, 'index.html', {'user': user_data, 'products': products_datas}, safe=False)
    else:
        return redirect('login')



def card_view(request):
    
    access_token = request.COOKIES.get('acces_token')
    if not access_token:
        return redirect('login')
    else:
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        cards = requests.get('http://127.0.0.1:8000/api/cards', headers=headers)
    
        if cards.status_code == 200:
            cards_datas = cards.json()
            return render(request, 'cards.html', {'cards': cards_datas})
        else:
            return redirect('login')



def profil_view(request):

    access_token = request.COOKIES.get('access_token')
    if not access_token:
        return redirect('login')

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get('http://127.0.0.1:8000/api/customer', headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        return render(request, 'profil.html', {'user': user_data})
    else:
        return redirect('login')



def notification_view(request):

    access_token = request.COOKIES.get('acces_token')
    if not access_token:
        return redirect('login')
    else:
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        notifications = requests.get('http://127.0.0.1:8000/api/notifications', headers=headers)
    
        if notifications.status_code == 200:
            notifications_datas = notifications.json()
            return render(request, 'notifications.html', {'notifications': notifications_datas})
        else:
            return redirect('login')