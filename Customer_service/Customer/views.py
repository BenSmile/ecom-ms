from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        
        if username and password:
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)
            
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            return JsonResponse({'message': 'User registered successfully'})
        else:
            return JsonResponse({'error': 'Invalid data'}, status=400)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful', 'username': user.username})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)



@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        username = request.session.get('username')
        if username:
            logout(request)
            return JsonResponse({'message': f'Logout successful for {username}'})
        else:
            return JsonResponse({'error': 'User not logged in'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def list_users(request):
    if request.method == 'GET':
        users = User.objects.all().values('id', 'username', 'first_name', 'last_name', 'email')
        users_list = list(users)
        return JsonResponse(users_list, safe=False)


@csrf_exempt
def read_user(request, user_id):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=user_id)
            return JsonResponse({
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
            })
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
            


@csrf_exempt
def update_user(request, pk):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            user = User.objects.get(id=pk)
            user.username = data.get('username', user.username)
            if 'password' in data:
                user.set_password(data['password'])
            user.save()
            return JsonResponse({'message': 'User updated successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def delete_user(request, pk):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(id=pk)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
