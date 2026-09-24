La API seleccionada es API-Sports.io, mas concretamente, su api dedicada para datos de Formula-1. Encontré esta API, el año pasado, buscando una API con la que obtener datos sobre formula 1 para un proyecto de clase. 

**Habitat**

'v1.formula-1.api-sports.io' Es una api deportiva, esta en especifico es una api de datos sobre formula 1 dentro de el servicio API-Sports.io a la cual se puede acceder directamente por https

---

## FICHA DE CAMPO 1

*Petición sin token de autenticación a API-Sports Formula-1 (abierta)*


**Llamada**

```
GET /rankings/drivers?season=2024 HTTP/2
Host: v1.formula-1.api-sports.io
User-Agent: EUNEIZ-ficha-campo/1.0
Accept-Encoding: gzip, deflate, br
Accept: application/json
Connection: close
```
Realizamos una petición, con el metodo GET sin ningun token. Simplemente llamamos a un endpoint en concreto para recibir datos sin incluir el token que exige la API

**Respuesta**
```
HTTP/2 403 Forbidden
Date: Thu, 24 Sep 2026 18:18:01 GMT
Content-Type: application/json
Cache-Control: private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Expires: Thu, 01 Jan 1970 00:00:01 GMT
Referrer-Policy: same-origin
X-Frame-Options: SAMEORIGIN
Server: cloudflare
Cf-Ray: a403ca0f6b31de0a-MAD

{"get": "","parameters": [],"errors": {"token": "Missing application key, Check our documentation on how to add your API key in headers.","error": "4xHe"},"results": 0,"paging": {"current": 1,"total": 1},"response": []}
```
En la respuesta vemos que nos devuelve un 403, informandonos de que la acción que acabamos de realizar está prohibida, pues detecta que no existe en la peticion la cabecera x-apisports-key, y asi lo responde en formato JSON. De momento no expone mas datos que el codigo de error, que podría dar pistas sobre la versión del backend. Tampoco vemos cabeceras de cuota.

**Riesgo**

El riesgo más observable, es el dar la información del error exacto. Este comportamiento, resulta peligroso, pues mostrar un codigo de error concreto, puede dar información a un actor malicioso, sobre las tecnologías utilizadas en la infraestructura

**Cliente**

**cliente.py** especie **abierta** de la lista **ESPECIES**


*Firmada por Nacho Monforte.*

---

## Ficha de campo 2

*Petición con token de autenticación a la API-Sports F1 (con token)*

**Llamada**
```
GET /rankings/drivers?season=2024 HTTP/2
Host: v1.formula-1.api-sports.io
User-Agent: EUNEIZ-ficha-campo/1.0
Accept-Encoding: gzip, deflate, br
Accept: application/json
Connection: close
X-Apisports-Key: b0d536ec28659334ce37b069654332f6 
```
Esta vez, hacemos la misma peticion que anteriormente, pero incluimos la cabecera X-Apisports-Key, que contiene la key de la API que necesitamos para poder realizar peticiones y que la API responda correctamente

**Respuesta**
```
HTTP/2 200 OK
Date: Thu, 24 Sep 2026 18:18:01 GMT
Content-Type: application/json
Access-Control-Allow-Headers: x-rapidapi-key, x-apisports-key, x-rapidapi-host
Access-Control-Allow-Methods: GET, OPTIONS
Access-Control-Allow-Origin: *
Cache-Control: no-store, no-cache, must-revalidate
Expires: 0
Pragma: no-cache
Server: cloudflare
Vary: Accept-Encoding
X-Ratelimit-Limit: 10
X-Ratelimit-Remaining: 9
X-Ratelimit-Requests-Limit: 100
X-Ratelimit-Requests-Remaining: 94
Cf-Cache-Status: DYNAMIC
Cf-Ray: a403ca100b8bde0a-MAD

{"get":"rankings","parameters":{"season":"2024"},"errors":[],"results":24,"response":[{"position":1,"driver":{"id":25,"name":"Max Verstappen","abbr":"VER","number":3,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/25.png"},"team":{"id":1,"name":"Red Bull Racing","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/1.png"},"points":437,"wins":9,"behind":null,"season":2024},{"position":2,"driver":{"id":49,"name":"Lando Norris","abbr":"NOR","number":1,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/49.png"},"team":{"id":2,"name":"McLaren Racing","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/2.png"},"points":374,"wins":4,"behind":63,"season":2024},{"position":3,"driver":{"id":34,"name":"Charles Leclerc","abbr":"LEC","number":16,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/34.png"},"team":{"id":3,"name":"Scuderia Ferrari","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/3.png"},"points":356,"wins":3,"behind":81,"season":2024},{"position":4,"driver":{"id":97,"name":"Oscar Piastri","abbr":"PIA","number":81,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/97.png"},"team":{"id":2,"name":"McLaren Racing","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/2.png"},"points":292,"wins":2,"behind":145,"season":2024},{"position":5,"driver":{"id":24,"name":"Carlos Sainz Jr","abbr":"SAI","number":55,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/24.png"},"team":{"id":3,"name":"Scuderia Ferrari","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/3.png"},"points":290,"wins":2,"behind":147,"season":2024},{"position":6,"driver":{"id":51,"name":"George Russell","abbr":"RUS","number":63,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/51.png"},"team":{"id":5,"name":"Mercedes-AMG Petronas","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/5.png"},"points":245,"wins":2,"behind":192,"season":2024},{"position":7,"driver":{"id":20,"name":"Lewis Hamilton","abbr":"HAM","number":44,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/20.png"},"team":{"id":5,"name":"Mercedes-AMG Petronas","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/5.png"},"points":223,"wins":2,"behind":214,"season":2024},{"position":8,"driver":{"id":10,"name":"Sergio Perez","abbr":"PER","number":11,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/10.png"},"team":{"id":1,"name":"Red Bull Racing","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/1.png"},"points":152,"wins":0,"behind":285,"season":2024},{"position":9,"driver":{"id":4,"name":"Fernando Alonso","abbr":"ALO","number":14,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/4.png"},"team":{"id":17,"name":"Aston Martin F1 Team","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/17.png"},"points":70,"wins":0,"behind":367,"season":2024},{"position":10,"driver":{"id":36,"name":"Pierre Gasly","abbr":"GAS","number":10,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/36.png"},"team":{"id":13,"name":"Alpine F1 Team","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/13.png"},"points":42,"wins":0,"behind":395,"season":2024},{"position":11,"driver":{"id":6,"name":"Nico Hulkenberg","abbr":"HUL","number":27,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/6.png"},"team":{"id":14,"name":"Haas F1 Team","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/14.png"},"points":41,"wins":0,"behind":396,"season":2024},{"position":12,"driver":{"id":82,"name":"Yuki Tsunoda","abbr":"TSU","number":22,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/82.png"},"team":{"id":7,"name":"Racing Bulls","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/7.png"},"points":30,"wins":0,"behind":407,"season":2024},{"position":13,"driver":{"id":31,"name":"Lance Stroll","abbr":"STR","number":18,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/31.png"},"team":{"id":17,"name":"Aston Martin F1 Team","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/17.png"},"points":24,"wins":0,"behind":413,"season":2024},{"position":14,"driver":{"id":28,"name":"Esteban Ocon","abbr":"OCO","number":31,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/28.png"},"team":{"id":13,"name":"Alpine F1 Team","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/13.png"},"points":23,"wins":0,"behind":414,"season":2024},{"position":15,"driver":{"id":2,"name":"Kevin Magnussen","abbr":"MAG","number":20,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/2.png"},"team":{"id":14,"name":"Haas F1 Team","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/14.png"},"points":16,"wins":0,"behind":421,"season":2024},{"position":16,"driver":{"id":50,"name":"Alexander Albon","abbr":"ALB","number":23,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/50.png"},"team":{"id":12,"name":"Williams F1 Team","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/12.png"},"points":12,"wins":0,"behind":425,"season":2024},{"position":17,"driver":{"id":14,"name":"Daniel Ricciardo","abbr":"RIC","number":3,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/14.png"},"team":{"id":7,"name":"Racing Bulls","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/7.png"},"points":12,"wins":0,"behind":425,"season":2024},{"position":18,"driver":{"id":101,"name":"Oliver Bearman","abbr":"BEA","number":87,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/101.png"},"team":{"id":14,"name":"Haas F1 Team","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/14.png"},"points":7,"wins":0,"behind":430,"season":2024},{"position":19,"driver":{"id":105,"name":"Franco Colapinto","abbr":null,"number":43,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/105.png"},"team":{"id":12,"name":"Williams F1 Team","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/12.png"},"points":5,"wins":0,"behind":432,"season":2024},{"position":20,"driver":{"id":83,"name":"Guanyu Zhou","abbr":null,"number":24,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/83.png"},"team":{"id":18,"name":"Stake F1 Team Kick Sauber","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/18.png"},"points":4,"wins":0,"behind":433,"season":2024},{"position":21,"driver":{"id":89,"name":"Liam Lawson","abbr":"LAW","number":30,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/89.png"},"team":{"id":null,"name":null,"logo":null},"points":4,"wins":0,"behind":433,"season":2024},{"position":22,"driver":{"id":5,"name":"Valtteri Bottas","abbr":"BOT","number":77,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/5.png"},"team":{"id":18,"name":"Stake F1 Team Kick Sauber","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/18.png"},"points":null,"wins":0,"behind":437,"season":2024},{"position":23,"driver":{"id":92,"name":"Logan Sargeant","abbr":null,"number":2,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/92.png"},"team":{"id":12,"name":"Williams F1 Team","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/12.png"},"points":null,"wins":0,"behind":437,"season":2024},{"position":24,"driver":{"id":94,"name":"Jack Doohan","abbr":"DOO","number":7,"image":"https:\/\/media.api-sports.io\/formula-1\/drivers\/94.png"},"team":{"id":13,"name":"Alpine F1 Team","logo":"https:\/\/media.api-sports.io\/formula-1\/teams\/13.png"},"points":null,"wins":0,"behind":437,"season":2024}]}
```
En este caso vemos una respuesta completa, con los datos que habiamos pedido, dado a que en este caso, como hemos dicho antes, la peticion esta completa y con la key correcta

La autenticación, la realiza mediante esta misma key, sin embargo, no se ven aqui mecanismos de rotaciion ni caducidad del token en la respuesta. Vemos que expone los datos pedidos, pero ningun tipo de dato sensible. Por otro lado, a diferencia de la anterior respuesta, si que vemos en este caso limites de cuotas, como X-Ratelimit-Limit, y X-Ratelimit-Requests-Limit, además de las que nos faltan por realizar.

**Riesgo**

Podemos ver un riesgo claro, y es que el token vieja en una cabecera de texto plano dentro del tunel TLS del transporte, por lo que cualquier intercepción del canal, puede ver la credencial completa.

**Cliente**

**cliente.py** especie **con-token** de la lista **ESPECIES**

*Firmada por Nacho Monforte* 

---

## Ficha de campo 3

*Peticion en busca de un error extraño de la API*

**Llamada**
```
GET /rankings/drivers?season=' HTTP/2
Host: v1.formula-1.api-sports.io
User-Agent: EUNEIZ-ficha-campo/1.0
Accept-Encoding: gzip, deflate, br
Accept: application/json
Connection: close
X-Apisports-Key: b0d536ec28659334ce37b069654332f6
```
Esta llamada busca provocar que la API devuelva un error, para ver como gestiona estos mismos la API, lo hacemos lanzando una petición, con token, sin embargo, pasando un valor imposible en el campo pedido. En este caso, en el campo donde se debería especificar la temporada que se quiere consultar, en vez de un año valido, introducimos un " ' " 

**Respuesta**
```
HTTP/2 200 OK
Date: Thu, 24 Sep 2026 18:18:01 GMT
Content-Type: application/json
Access-Control-Allow-Headers: x-rapidapi-key, x-apisports-key, x-rapidapi-host
Access-Control-Allow-Methods: GET, OPTIONS
Access-Control-Allow-Origin: *
Cache-Control: no-store, no-cache, must-revalidate
Expires: 0
Pragma: no-cache
Server: cloudflare
Vary: Accept-Encoding
Cf-Cache-Status: DYNAMIC
Cf-Ray: a403ca111c3bde0a-MAD

{"get":"rankings","parameters":{"season":"'"},"errors":{"plan":"Free plans do not have access to this season, try from 2022 to 2024."},"results":0,"paging":{"current":1,"total":1},"response":[]}
```
En la respuesta, vemos que el codigo devuelto es un 200, porque la petición se hace sin problemas, debido a que la key pasada es correcta. Sin embargo, el problema viene cuando la peticion en vez de introducir un año valido, introducimos una commilla. 

En la respuesta podemos ver que al API no rechaza la comilla por tipo, sino que lanza un mensaje de que los planes gratis, no tienen acceso a años fuera del intervalo del 2022 al 2024. Lo que refleja que probablemente el backend sanitiza las entradas de forma laxa. 

Por otro lado observamos que no aparece ninguna cabecera de limite por cuota. Por lo que, potencialmente, las peticiones rechazadas en la validación, a pesar de que devuelvan 200, no descuentan requests del maximo.

**Riesgo**

El riesgo potencial que se observa es este mismo comportamiento comentado. A pesar de que la petición era erronea y que no se devuelven datos en 'response', esta petición llega al cliente, y al no descontar peticiones de la cuota dada, permite realizar las llamadas deseadas en el tiempo deseado, posiblemente abriendo la puerta a una denegación de servicios. Además, es probable que la validación de entrada de datos, no valide de manera correcta los datos de entrada. De esta manera, esta misma validación de entradas, podría ser potencialmente esquivable.

**Cliente**

**cliente.py** especie **error** de la lista **ESPECIES**

*Firmado por Nacho Monforte*