# SOCIAL OPLESK
### 🏴‍☠️ HACKS - SERVERLESS - 1

<br/>

📚 tutorial de netlify functions [tutorial](https://docs.netlify.com/functions/build/?fn-language=js)
---

```diff
- NOTA HACER LAS PRÁCTICAS MEDIANTE VISUAL STUDIO CODE  
```

```diff
* Instalar la dependencia de netlify:
  npm install netlify-cli -g

* Crear el archivo netlify.toml en el root del proyecto"

* Configurar el archivo netlify.toml ejemplo:

[build]
functions = "functions"

[[redirects]]
from = "/*"
status = 200
to = "/.netlify/functions/:splat"

```
<br/>

|Hacks | Details | 
|----------|---------|
| H-1      | {"content":"get"} |
| H-2      | {"content":"post"} |
| H-3      | {"content":"put"} | 
| H-4      | {"content":"delete"} |
| H-5      | {"method":"get","content":"message"} |
| H-6      | {"method":"type", "content":"message"}|
| H-7      | {"email":"query@domain.com", "name":"add a name"} |
| H-8      | {"email":"body@domain.com", "alias":"add an alias"}  | 
| H-9      | {"payload":"data query"} |
| H-10      | {"payload":"data body"}|
<br/> 

## 🏆 H-1 

```sh
* ENDPOINT:(PATH: "/h1")

CREAR UN SERVERLESS QUE RESPONDA SI LA SOLICITUD ES DE TIPO "GET"

output => {"content":"get"}
```
<br/>


## 🏆 H-2 (PATH: "/H2")
```sh
* ENDPOINT:(PATH: "/h2")

CREAR UN SERVERLESS QUE RESPONDA SI LA SOLICITUD ES DE TIPO "POST"

output => {"content":"post"}
```
<br/>

## 🏆 H-3
```sh
* ENDPOINT:(PATH: "/h3")

CREAR UN SERVERLESS QUE RESPONDA SI LA SOLICITUD ES DE TIPO "PUT"

output => {"content":"put"}
```
<br/>

## 🏆 H-4
```sh
* ENDPOINT:(PATH: "/h4")

CREAR UN SERVERLESS QUE RESPONDA SI LA SOLICITUD ES DE TIPO "DELETE"

output => {"content":"delete"}

```
<br/>

## 🏆 H-5
```sh
* ENDPOINT:(PATH: "/h5")

CREAR UN SERVERLESS QUE RESPONDA SI LA SOLICITUD ES DE TIPO "GET"
EN CASO CONTRARIO RESPONDER CON LA SALIDA DE UN OBJETO {} SIN PROPIEDADES

TRUE  - output => {"content":"delete"}
FALSE - output => {}
```
<br/>


## 🏆 H-6
```sh
* ENDPOINT:(PATH: "/h6")

CREAR UN SERVERLESS QUE RESPONDA SI LA SOLICITUD CORRESPONDE CON ALGÚN METODO HTTP: "GET" | "POST" | "PUT" | "DELETE"
- EN CASO CONTRARIO RESPONDER CON LA SALIDA DE UN OBJETO {} SIN PROPIEDADES
- EN LA OPCIÓN type ANEXAR EL TIPO DE METODO HTTP
- LA PROPIEDAD content EN method ESPECIFICAR EL METODO HTTP

TRUE  - output => {"method":"type", "content":"message method"}
FALSE - output => {}
```
<br/>

## 🏆 H-7
```sh
* ENDPOINT:(PATH: "/h7?email="..."&name="...")

CREAR UN SERVERLESS QUE RESPONDA SI LA SOLICITUD ES DE TIPO "GET"
SE DEBE ENVIAR EL VALOR DEL email, name MEDIANTE QUERY STRING

output => {"email":"query@domain.com", "name":"add a name"}

```
<br/>

## 🏆 H-8
```sh
* ENDPOINT:(PATH: "/h8")

CREAR UN SERVERLESS QUE RESPONDA SI LA SOLICITUD ES DE TIPO "GET"
SE DEBE ENVIAR EL VALOR DEL email, name MEDIANTE BODY

- DEBES INSTALAR EL PAQUETE DE npm i middy
  EJEMPLO: let middy = require("middy") 

- PARA DAR EL FORMATO CORRECTO EN JSON, DEBES IMPORTAR EL MIDDLEWARE jsonBodyParser
  EJEMPLO: let {jsonBodyParser} = require("middy/middlewares");

- ENVIAR LOS DATOS EN UN JSON {"email","add an email", "alias":"add an alias"}


output => {"email":"body@domain.com", "alias":"add an alias"}

```
<br/>


## 🏆 H-9
```sh
* ENDPOINT:(PATH: "/h9?alias="...")

CREAR UN SERVERLESS QUE RESPONDA SI LA SOLICITUD ES DE TIPO "GET"
- SE DEBE ENVIAR EL VALOR DEL alias  MEDIANTE QUERY STRING
- BUSCAR UN VALOR VALIDO DENTRO DEL ARRAY DE ALIAS Y MOSTRAR SU SALIDA
- EN CASO DE NO ENCONTRAR EL alias EN EL ARRAY DE ALIAS ENVIAR UN MENSAJE DE not found

const Lista = ["foo","bar","baz","qux","fred"]

TRUE - output => {"payload":"bar"}
FALSE - output => {"payload":"not found"}

```
<br/>


## 🏆 H-10 (PATH: "/")
```sh
* ENDPOINT:(PATH: "/h10")

CREAR UN SERVERLESS QUE RESPONDA SI LA SOLICITUD ES DE TIPO "GET"
- SE DEBE ENVIAR EL VALOR DEL alias  MEDIANTE BODY
- BUSCAR UN VALOR VALIDO DENTRO DEL ARRAY DE ALIAS Y MOSTRAR SU SALIDA
- EN CASO DE NO ENCONTRAR EL alias EN EL ARRAY DE ALIAS ENVIAR UN MENSAJE DE not found
- PARA DAR EL FORMATO CORRETO EN JSON, DEBES IMPORTAR EL MIDDLEWARE jsonBodyParser
  EJEMPLO: let {jsonBodyParser} = require("middy/middlewares");

const Lista = ["foo","bar","baz","qux","fred"]

TRUE - output => {"payload":"bar"}
FALSE - output => {"payload":"not found"}
```
<br/>
