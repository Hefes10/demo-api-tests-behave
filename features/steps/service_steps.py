import json
import os
import requests
from behave import given, when, then

def base_url():
    return os.getenv("BASE_URL", "http://localhost:3000")

@given('el servicio está arriba')
def step_service_up(context):
    r = requests.get(f"{base_url()}/health", timeout=5)
    assert r.status_code == 200

@when('hago GET a "{path}"')
def step_get(context, path):
    context.resp = requests.get(f"{base_url()}{path}", timeout=5)

@when('hago POST a "{path}" con json')
def step_post_json(context, path):
    body = {}
    if context.text:
        body = json.loads(context.text)
    context.resp = requests.post(f"{base_url()}{path}", json=body, timeout=5)

@then('el status code es {code:d}')
def step_status_code(context, code):
    assert context.resp.status_code == code, (
        f"Status esperado {code}, real {context.resp.status_code}, body={getattr(context.resp,'text',None)}"
    )

@then('el campo "{key}" es {val:d}')
def step_field_int(context, key, val):
    data = context.resp.json()
    assert key in data, f"Campo '{key}' no encontrado en respuesta: {data}"
    assert int(data[key]) == val, f"Esperado {key}={val}, real {data[key]}"
