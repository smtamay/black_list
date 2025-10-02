# Proyecto FastAPI con PostgreSQL

Este proyecto es un microservicio construido con **FastAPI** y utiliza **PostgreSQL** como base de datos. Se ejecuta dentro de contenedores Docker para facilitar el despliegue y la gestión del entorno.

---

## Requisitos

* Docker 

---

## Estructura del Proyecto

* `app/` → Código fuente de la aplicación.
* `Dockerfile` → Imagen de Docker para el servicio `app`.
* `docker-compose.yml` → Configuración de los servicios `app` y `db`.
* `.env` → Variables de entorno.
* `requirements.txt` → Dependencias de Python.

---

## Variables de Entorno

El archivo `.env` contiene:

```env
# Configuración de la BD
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres

# Conexión de SQLAlchemy
DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}

# Entorno de la app
ENV=development
```

> Nota: No es necesario cambiar nada si usas los valores por defecto.

---

## Construcción y Ejecución

Para construir y correr los contenedores:

```bash
docker-compose up --build
```

Esto hará lo siguiente:

1. Construir la imagen `app` desde el `Dockerfile`.
2. Levantar un contenedor de PostgreSQL (`db`) y mapear el puerto 5432.
3. Levantar un contenedor de la aplicación (`app`) y mapear el puerto 8000.
4. Ejecutar el script `/code/app/start_app.sh` dentro del contenedor `app`.

> El contenedor `app` espera a que la base de datos esté lista antes de iniciar.

---

## Acceder a la Aplicación

* API: [http://localhost:8000](http://localhost:8000)
* Swagger UI (documentación automática de FastAPI): [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Comandos Útiles

* Levantar los contenedores en segundo plano:

```bash
docker-compose up -d
```
