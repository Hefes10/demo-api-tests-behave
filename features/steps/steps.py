import json
import os
import requests
from behave import when, then

BASE_URL = os.getenv('BASE_URL', 'http://localhost:3000')

@when('hago GET a "{path}"')
def step_get(context, path):
    context.response = requests.get(f"{BASE_URL}{path}")

@when('hago POST a "{path}" con json:')
def step_post(context, path):
    payload = json.loads(context.text)
    context.response = requests.post(f"{BASE_URL}{path}", json=payload)

@then('el status code es {code:d}')
def step_status(context, code):
    assert context.response.status_code == code, f"Esperado {code}, obtenido {context.response.status_code}: {context.response.text}"

@then('el json contiene "{key}" con {value}')
def step_json_contains(context, key, value):
    data = context.response.json()
    try:
        exp = json.loads(value)
    except Exception:
        exp = value.strip('"')
    assert key in data, f"No se encuentra clave '{key}' en {data}"
    assert data[key] == exp, f"Valor esperado para '{key}': {exp}, obtenido: {data[key]}"