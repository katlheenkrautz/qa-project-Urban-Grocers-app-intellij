import requests
import configuration
import data

# Función para crear un nuevo usuario
def create_new_user(body):
    return requests.post(configuration.CREATE_USER_URL, json=body, headers=data.headers)

# Función para crear un nuevo kit
def post_new_client_kit(kit_body, auth_token):
    headers_with_auth = data.headers.copy()
    headers_with_auth["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.CREATE_KIT_URL, json=kit_body, headers=headers_with_auth)