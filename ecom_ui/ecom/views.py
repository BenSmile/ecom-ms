from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

# Create your views here.

def login_view(request):
    return render(request, "login.html")



def register_view(request):
    return render(request, "register.html")



def get_session_data(request):
    if 'user' in request.session:
        user_data = request.session['user']
        return JsonResponse(user_data)
    else:
        return JsonResponse({'error': 'Session data not found'}, status=404)


def home_view(request):

    access_token = request.COOKIES.get('access_token')
    if not access_token:
        return redirect('login')

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    user = get_session_data()

    products = requests.get('http://127.0.0.1:8000/api/products', headers=headers)

    if products.status_code == 200:
        products_datas = products.json()
        return render(request, 'index.html', {'user': user, 'products': products_datas}, safe=False)
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
        user = get_session_data()
        cards = requests.get(f'http://127.0.0.1:8000/api/cards/{user.id}', headers=headers)
    
        if cards.status_code == 200:
            cards_datas = cards.json()
            return render(request, 'cards.html', {'cards': cards_datas})
        else:
            return redirect('login')



def profil_view(request):

    access_token = request.COOKIES.get('access_token')
    if not access_token:
        return redirect('login')
    else:
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        if response.status_code == 200:
            user = get_session_data()
            response = requests.get(f'http://127.0.0.1:8000/api/customer/{user.id}', headers=headers)
            return render(request, 'profil.html', {'user': user})
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

        user = get_session_data()
        notifications = requests.get(f'http://127.0.0.1:8000/api/notifications/{user.id}', headers=headers)
    
        if notifications.status_code == 200:
            notifications_datas = notifications.json()
            return render(request, 'notifications.html', {'notifications': notifications_datas})
        else:
            return redirect('login')