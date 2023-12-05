# SOCIAL OPLESK
### 🏴‍☠️ HACKS - BACKEND - 1

<br/>

📚 tutorial de flask - 1 [tutorial](https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24)
<br/>
📚 tutorial de flask - 2 [tutorial](https://www.moesif.com/blog/technical/api-development/Building-RESTful-API-with-Flask/)
<br/>
📚 tutorial de flask - 3 [tutorial](https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask)
---

```diff
- NOTA HACER LAS PRÁCTICAS MEDIANTE VISUAL STUDIO CODE  
```

```diff
* Instalar el framework:
  npm install flask

* Crear el archivo app.py en modo debug

* ejecutar el servidor en terminal: flask run --debug

```
<br/>

|Hacks | Details | 
|----------|---------|
| H-1      | {"payload":"get"} |
| H-2      | {"payload":"post"} |
| H-3      | {"payload":"put"} | 
| H-4      | {"payload":"delete"} |
| H-5      | {"method":"get","payload":"message"} |
| H-6      | {"method":"type", "payload":"message"}|
| H-7      | {"email":"query@domain.com", "name":"add a name"} |
| H-8      | {"email":"body@domain.com", "alias":"add an alias"}  | 
| H-9      | {"payload":"data query"} |
| H-10      | {"payload":"data body"}|
<br/> 

## 🏆 H-1 

```sh
* ENDPOINT:(PATH: "/h1")

CREAR UN ENDPOINT QUE RESPONDA SI LA SOLICITUD ES DE TIPO "GET"

METHOD:   "GET"
TYPE: JSON

output => {"payload":"get"}
```
<br/>


## 🏆 H-2
```sh
* ENDPOINT:(PATH: "/h2")

CREAR UN ENDPOINT QUE RESPONDA SI LA SOLICITUD ES DE TIPO "POST"

METHOD:   "POST"
TYPE: JSON

output => {"payload":"post"}
```
<br/>

## 🏆 H-3
```sh
* ENDPOINT:(PATH: "/h3")

CREAR UN ENDPOINT QUE RESPONDA SI LA SOLICITUD ES DE TIPO "PUT"

METHOD:   "PUT"
TYPE: JSON

output => {"payload":"put"}
```
<br/>

## 🏆 H-4
```sh
* ENDPOINT:(PATH: "/h4")

CREAR UN ENDOPOINT QUE RESPONDA SI LA SOLICITUD ES DE TIPO "DELETE"

ENDPOINT: /h4
METHOD:   "DELETE"
TYPE: JSON

output => {"payload":"delete"}

```
<br/>

## 🏆 H-5
```sh
* ENDPOINT:(PATH: "/h5")

CREAR UN ENDPOINT QUE RESPONDA SI LA SOLICITUD ES DE TIPO "GET"
EN CASO CONTRARIO RESPONDER CON LA SALIDA DE UN OBJETO {} SIN PROPIEDADES

TRUE  - output => {"payload":"success", "error": False}
FALSE - output => {}
```
<br/>


## 🏆 H-6
```sh
* ENDPOINT:(PATH: "/h6")

CREAR UN ENDPOINT QUE RESPONDA SI LA SOLICITUD CORRESPONDE CON ALGÚN METODO HTTP: "GET" | "POST"| "DELETE"
- EN CASO CONTRARIO RESPONDER CON LA SALIDA DE UN OBJETO sin payload data {} 
- EN LA OPCIÓN type ANEXAR EL TIPO DE METODO HTTP
- LA PROPIEDAD content EN method ESPECIFICAR EL METODO HTTP

TRUE  - output => {"method":"type", "payload":"success", "error":False}
FALSE - output => {"method":"type", "payload":None, "error":False}
```
<br/>

## 🏆 H-7
```sh
* ENDPOINT:(PATH: "/h7?email="....."&name=".....")

CREAR UN ENDPOINT QUE RESPONDA SI LA SOLICITUD ES DE TIPO "GET"
SE DEBE ENVIAR EL VALOR DEL email, name MEDIANTE QUERY STRING

output => {
            "payload":{"email":"foo@foo.com", "name":"fooziman"},
            "error":{"available":False,"err_msg":None},
            "status":200
          }

```
<br/>

## 🏆 H-8
```sh
* ENDPOINT:(PATH: "/h8")

CREAR UN ENDPOINT QUE RESPONDA SI LA SOLICITUD ES DE TIPO "POST"
SE DEBE ENVIAR EL VALOR DEL email, name MEDIANTE BODY

- ENVIAR LOS DATOS EN UN JSON {"email","add an email", "alias":"add an alias"}


output => {
            "payload":{"email":"foo@foo.com", "name":"fooziman"},
            "error":{"available":False,"err_msg":None},
            "status":200
          }

```
<br/>


## 🏆 H-9
```sh
* ENDPOINT:(PATH: "/h9?alias="...")

CREAR UN ENDPOINT QUE RESPONDA SI LA SOLICITUD ES DE TIPO "GET"
- SE DEBE ENVIAR EL VALOR DEL alias  MEDIANTE QUERY STRING
- BUSCAR UN VALOR VALIDO DENTRO DE LA LISTA DE ALIAS Y MOSTRAR SU SALIDA
- EN CASO DE NO ENCONTRAR EL alias EN LA LISTA DE ALIAS ENVIAR UN MENSAJE DE not found

const Lista = ["foo","bar","baz","qux","fred"]


TRUE - output => {
            "payload":"bar",
            "error":{"available":False,"err_msg":None},
            "status":200
          }


FALSE - output => {
            "payload":"not found",
            "error":{"available":False,"err_msg":None},
            "status":404
          }

```
<br/>


## 🏆 H-10 (PATH: "/h10")
```sh
* ENDPOINT:(PATH: "/h10")

CREAR UN ENDPOINT QUE RESPONDA SI LA SOLICITUD ES DE TIPO "POST"
- SE DEBE ENVIAR EL VALOR DEL alias  MEDIANTE BODY
- BUSCAR UN VALOR VALIDO DENTRO DE LA LISTA DE ALIAS Y MOSTRAR SU SALIDA
- EN CASO DE NO ENCONTRAR EL alias EN LA LISTA DE ALIAS ENVIAR UN MENSAJE DE not found

const Lista = ["foo","bar","baz","qux","fred"]

TRUE - output => {"payload":"bar"}
FALSE - output => {"payload":"not found"}
```
<br/>
