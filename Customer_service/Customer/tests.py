import json
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse

client = Client()

def test_register_view():
    # Test de l'enregistrement d'un nouvel utilisateur avec des données valides
    response = client.post(
        reverse('register_view'),
        json.dumps({
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'testpassword'
        }),
        content_type='application/json'
    )
    assert response.status_code == 200
    assert response.json() == {'message': 'User registered successfully'}

    # Test de l'enregistrement avec un nom d'utilisateur déjà existant
    response = client.post(
        reverse('register_view'),
        json.dumps({
            'username': 'testuser',  # Utilise le même nom d'utilisateur
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test2@example.com',
            'password': 'testpassword2'
        }),
        content_type='application/json'
    )
    assert response.status_code == 400
    assert response.json() == {'error': 'Username already exists'}

def test_login_view():
    # Test de la connexion avec des identifiants valides
    user = User.objects.create_user(username='testuser', password='testpassword')
    response = client.post(
        reverse('login_view'),
        json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }),
        content_type='application/json'
    )
    assert response.status_code == 200
    assert response.json() == {'message': 'Login successful', 'username': 'testuser', 'id': user.id}

    # Test de la connexion avec des identifiants invalides
    response = client.post(
        reverse('login_view'),
        json.dumps({
            'username': 'testuser',
            'password': 'wrongpassword'
        }),
        content_type='application/json'
    )
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid credentials'}

def test_logout_view():
    # Test de la déconnexion d'un utilisateur connecté
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.force_login(user)
    response = client.post(reverse('logout_view'))
    assert response.status_code == 200
    assert response.json() == {'message': f'Logout successful for {user.username}'}

    # Test de la déconnexion lorsque l'utilisateur n'est pas connecté
    response = client.post(reverse('logout_view'))
    assert response.status_code == 400
    assert response.json() == {'error': 'User not logged in'}

def test_list_users():
    # Test de la vue list_users
    response = client.get(reverse('list_users'))
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_user():
    # Création d'un utilisateur pour le test
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')

    # Test de la vue read_user avec un ID d'utilisateur valide
    response = client.get(reverse('read_user', args=[user.id]))
    assert response.status_code == 200
    assert response.json() == {'id': user.id, 'username': user.username, 'email': user.email}

    # Test de la vue read_user avec un ID d'utilisateur inexistant
    response = client.get(reverse('read_user', args=[1000]))  # ID qui n'existe pas
    assert response.status_code == 404
    assert response.json() == {'error': 'User not found'}

def test_update_user():
    # Création d'un utilisateur pour le test
    user = User.objects.create_user(username='testuser', password='testpassword')

    # Test de la vue update_user avec un ID d'utilisateur valide
    updated_data = {
        'username': 'updated_username',
        'password': 'newpassword'
    }
    response = client.put(
        reverse('update_user', args=[user.id]),
        json.dumps(updated_data),
        content_type='application/json'
    )
    assert response.status_code == 200
    assert response.json() == {'message': 'User updated successfully'}

    # Vérification que les données ont été effectivement mises à jour
    user.refresh_from_db()
    assert user.username == updated_data['username']
    assert user.check_password(updated_data['password'])

    # Test de la vue update_user avec un ID d'utilisateur inexistant
    response = client.put(
        reverse('update_user', args=[1000]),  # ID qui n'existe pas
        json.dumps(updated_data),
        content_type='application/json'
    )
    assert response.status_code == 404
    assert response.json() == {'error': 'User not found'}

def test_delete_user():
    # Création d'un utilisateur pour le test
    user = User.objects.create_user(username='testuser', password='testpassword')

    # Test de la vue delete_user avec un ID d'utilisateur valide
    response = client.delete(reverse('delete_user', args=[user.id]))
    assert response.status_code == 200
    assert response.json() == {'message': 'User deleted successfully'}

    # Vérification que l'utilisateur a bien été supprimé de la base de données
    with pytest.raises(User.DoesNotExist):
        User.objects.get(id=user.id)

    # Test de la vue delete_user avec un ID d'utilisateur inexistant
    response = client.delete(reverse('delete_user', args=[1000]))  # ID qui n'existe pas
    assert response.status_code == 404
    assert response.json() == {'error': 'User not found'}
