import data
import sender_stand_request

# Función para obtener el cuerpo de la solicitud del usuario con un nombre específico
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

# Función para obtener el token de autenticación de un nuevo usuario
def get_new_user_token(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.create_new_user(user_body)
    assert user_response.status_code == 201
    return user_response.json()["authToken"]

# Función para obtener el cuerpo de la solicitud del kit con un nombre específico
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Prueba positiva
def positive_assert(kit_body):
    auth_token = get_new_user_token("Andrea")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Prueba negativa (código 400)
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token("Andrea")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400

# Función para obtener el cuerpo de la solicitud del kit sin el parámetro "name"
def get_kit_body_without_name():
    current_body = data.kit_body.copy()
    # Eliminar el parámetro "name" del cuerpo de la solicitud
    del current_body["name"]
    return current_body

# Función para obtener el cuerpo de la solicitud con "name" de tipo numérico
def get_kit_body_with_numeric_name():
    current_body = data.kit_body.copy()
    current_body["name"] = 123  # Tipo numérico (inválido)
    return current_body

#1. Prueba: Verificar que se puede crear un kit con un nombre de un solo carácter
def test_create_kit_with_one_character_name():
    # Paso 1: Crear el cuerpo de la solicitud con un nombre de un solo carácter
    kit_body = get_kit_body("a")

    # Paso 2: Obtener el token de autenticación
    auth_token = get_new_user_token("Andrea")

    # Paso 3: Enviar la solicitud para crear el kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Paso 4: Verificar que el código de respuesta sea 201
    assert kit_response.status_code == 201, f"Error: Se esperaba código 201, pero se obtuvo {kit_response.status_code}"

    # Paso 5: Verificar que el campo 'name' en la respuesta coincide con el campo 'name' en la solicitud
    assert kit_response.json()["name"] == kit_body["name"], f"Error: El nombre en la respuesta no coincide. Esperado: {kit_body['name']}, Obtenido: {kit_response.json()['name']}"

#2. Prueba: Verificar que se puede crear un kit con un nombre de 511 caracteres
def test_create_kit_with_511_characters_name():
    # Paso 1: Crear el cuerpo de la solicitud con un nombre de 511 caracteres
    long_name = "a" * 511  # Crear un string con 511 caracteres
    kit_body = get_kit_body(long_name)

    # Paso 2: Obtener el token de autenticación
    auth_token = get_new_user_token("Andrea")

    # Paso 3: Enviar la solicitud para crear el kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Paso 4: Verificar que el código de respuesta sea 201
    assert kit_response.status_code == 201, f"Error: Se esperaba código 201, pero se obtuvo {kit_response.status_code}"

    # Paso 5: Verificar que el campo 'name' en la respuesta coincide con el campo 'name' en la solicitud
    assert kit_response.json()["name"] == kit_body["name"], f"Error: El nombre en la respuesta no coincide. Esperado: {kit_body['name']}, Obtenido: {kit_response.json()['name']}"

#3. Prueba: Verificar que no se puede crear un kit con un nombre vacío
def test_create_kit_with_empty_name():
    # Paso 1: Crear el cuerpo de la solicitud con un nombre vacío
    kit_body = get_kit_body("")  # Nombre vacío

    # Paso 2: Obtener el token de autenticación
    auth_token = get_new_user_token("Andrea")

    # Paso 3: Enviar la solicitud para crear el kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Paso 4: Verificar que el código de respuesta sea 201
    assert kit_response.status_code == 201, f"Error: Se esperaba código 201, pero se obtuvo {kit_response.status_code}"

    # Paso 5: Verificar que el campo 'name' en la respuesta coincida con el campo 'name' en la solicitud
    assert kit_response.json()["name"] == kit_body["name"], f"Error: El nombre en la respuesta no coincide. Esperado: {kit_body['name']}, Obtenido: {kit_response.json()['name']}"

#4. Prueba: Verificar que no se puede crear un kit con un nombre de más de 512 caracteres
def test_create_kit_with_512_characters_name():
    # Paso 1: Crear el cuerpo de la solicitud con un nombre de 512 caracteres
    long_name = "a" * 512  # Crear un string con 512 caracteres
    kit_body = get_kit_body(long_name)

    # Paso 2: Obtener el token de autenticación
    auth_token = get_new_user_token("Andrea")

    # Paso 3: Enviar la solicitud para crear el kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Paso 4: Verificar que el código de respuesta sea 400
    assert kit_response.status_code == 400, f"Error: Se esperaba código 400, pero se obtuvo {kit_response.status_code}"

#5. Prueba: Verificar que se puede crear un kit con un nombre que contiene caracteres especiales
def test_create_kit_with_special_characters_name():
    # Paso 1: Crear el cuerpo de la solicitud con un nombre que contiene caracteres especiales
    special_characters_name = '"№%@'  # Nombre con caracteres especiales
    kit_body = get_kit_body(special_characters_name)

    # Paso 2: Obtener el token de autenticación
    auth_token = get_new_user_token("Andrea")

    # Paso 3: Enviar la solicitud para crear el kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Paso 4: Verificar que el código de respuesta sea 201
    assert kit_response.status_code == 201, f"Error: Se esperaba código 201, pero se obtuvo {kit_response.status_code}"

    # Paso 5: Verificar que el campo 'name' en la respuesta coincide con el campo 'name' en la solicitud
    assert kit_response.json()["name"] == kit_body["name"], f"Error: El nombre en la respuesta no coincide. Esperado: {kit_body['name']}, Obtenido: {kit_response.json()['name']}"

#6. Prueba: Verificar que se puede crear un kit con un nombre que contiene espacios
def test_create_kit_with_spaces_in_name():
    # Paso 1: Crear el cuerpo de la solicitud con un nombre que contiene espacios
    name_with_spaces = " A Aaa "  # Nombre con espacios
    kit_body = get_kit_body(name_with_spaces)

    # Paso 2: Obtener el token de autenticación
    auth_token = get_new_user_token("Andrea")

    # Paso 3: Enviar la solicitud para crear el kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Paso 4: Verificar que el código de respuesta sea 201
    assert kit_response.status_code == 201, f"Error: Se esperaba código 201, pero se obtuvo {kit_response.status_code}"

    # Paso 5: Verificar que el campo 'name' en la respuesta coincide con el campo 'name' en la solicitud
    assert kit_response.json()["name"] == kit_body["name"], f"Error: El nombre en la respuesta no coincide. Esperado: {kit_body['name']}, Obtenido: {kit_response.json()['name']}"

#7. Prueba: Verificar que se puede crear un kit con un nombre que contiene solo números
def test_create_kit_with_numeric_name():
    # Paso 1: Crear el cuerpo de la solicitud con un nombre que contiene solo números
    numeric_name = "123"  # Nombre con solo números
    kit_body = get_kit_body(numeric_name)

    # Paso 2: Obtener el token de autenticación
    auth_token = get_new_user_token("Andrea")

    # Paso 3: Enviar la solicitud para crear el kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Paso 4: Verificar que el código de respuesta sea 201
    assert kit_response.status_code == 201, f"Error: Se esperaba código 201, pero se obtuvo {kit_response.status_code}"

    # Paso 5: Verificar que el campo 'name' en la respuesta coincide con el campo 'name' en la solicitud
    assert kit_response.json()["name"] == kit_body["name"], f"Error: El nombre en la respuesta no coincide. Esperado: {kit_body['name']}, Obtenido: {kit_response.json()['name']}"

#8. Prueba: Verificar que no se puede crear un kit sin el parámetro "name"
def test_create_kit_without_name():
    # Paso 1: Crear el cuerpo de la solicitud sin el parámetro "name"
    kit_body = get_kit_body_without_name()

    # Paso 2: Obtener el token de autenticación
    auth_token = get_new_user_token("Andrea")

    # Paso 3: Enviar la solicitud para crear el kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Paso 4: Verificar que el código de respuesta sea 400
    assert kit_response.status_code == 400, f"Error: Se esperaba código 400, pero se obtuvo {kit_response.status_code}"

#9. Prueba: Verificar que no se puede crear un kit con "name" de tipo numérico
def test_create_kit_with_numeric_type_name():
    # Paso 1: Crear el cuerpo de la solicitud con "name" numérico
    kit_body = get_kit_body_with_numeric_name()

    # Paso 2: Obtener el token de autenticación
    auth_token = get_new_user_token("Andrea")

    # Paso 3: Enviar la solicitud para crear el kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Paso 4: Verificar que el código de respuesta sea 400
    assert kit_response.status_code == 400, f"Error: Se esperaba código 400, pero se obtuvo {kit_response.status_code}"

