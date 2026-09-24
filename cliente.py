"""Cliente de captura: una peticion HTTP por especie."""

"""Para poder utilizar este cliente, primero hay que definir la variable de entorno F1_KEY con la clave de la API. Para ello, accedemos manualmente a la api en https://api-sports.io/ e iniciamos sesion.
   Luego vamos al panel izquierdo, y en my access, dentro de Account, arribba a la derecha podemos ver nuestra clave de API. La copiamos y la pegamos en la variable de entorno F1_KEY"""

"""Para utilizar burp suite para capturar las peticiones, definimos la variable de entorno BURP con el valor 1."""

"""Es importante tener en cuenta, que he tenido algunos problemas de compatibilidad entre python 3.14 y burp suite, por lo que recomiendo utilizar python 3.12 para capturar peticiones y respuestas con burp suite"""

import os, requests, urllib3
from urllib.parse import quote
BURP = os.getenv("BURP", "0") == "1"
PROXY = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"} if BURP else None
F1_KEY = os.getenv("F1_KEY", "")
BASE = "https://v1.formula-1.api-sports.io/rankings/drivers"
COMUNES = {"User-Agent": "EUNEIZ-ficha-campo/1.0", "Accept": "application/json",
           "Connection": "close"}
urllib3.disable_warnings()

ESPECIES = [
    ("abierta", "GET", f"{BASE}?season=2024", {}, None),
    ("con-token", "GET", f"{BASE}?season=2024", {"x-apisports-key": F1_KEY}, None),
    ("error", "GET", f"{BASE}?season='",
     {"x-apisports-key": F1_KEY}, None),
]

def capturar(nombre, metodo, url, extra, cuerpo):
    r = requests.request(metodo, url, headers={**COMUNES, **extra}, json=cuerpo,
                         proxies=PROXY, verify=not BURP, timeout=20)
    print(f"\n=== especie: {nombre} ===")
    print(f"metodo:    {metodo} {url}")
    print(f"cabeceras: {dict(r.request.headers)}")
    print(f"cuerpo:    {cuerpo}")
    print(f"respuesta: {r.status_code} {r.reason} | {len(r.content)} B")
    print(f"cab. resp: {dict(r.headers)}")
    print(f"cuerpo resp (600 car.): {r.text[:600]}")

for especie in ESPECIES:
    capturar(*especie)