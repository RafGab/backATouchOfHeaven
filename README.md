# Proyecto A Touch of Heaven

## Descripción

Este proyecto es una aplicación web que permite gestionar recuerdos en formato de texto, fotos, videos y documentos. La aplicación utiliza una arquitectura de cliente-servidor donde el frontend está desarrollado con React y el backend con Django. La base de datos utilizada es PostgreSQL.

## Tecnologías

- **Backend**: Django
- **Frontend**: React
- **Base de datos**: PostgreSQL
- **Testing**: `pytest` para el backend y `vitest` para el frontend
- **Estilos**: CSS

## Características

- **API**: Se ha desarrollado una API RESTful usando Django REST Framework para la gestión de recuerdos.
- **Frontend**: La interfaz de usuario está desarrollada con React, con estilos personalizados en CSS.
- **Conexión Backend-Frontend**: La aplicación frontend se comunica con la API del backend para enviar y recibir datos.
- **Testing**:
  - **Backend**: Se han realizado pruebas utilizando `pytest` para asegurar que las funcionalidades del backend funcionen correctamente.
  - **Frontend**: Se han realizado pruebas utilizando `vitest` para asegurar que los componentes y funcionalidades del frontend estén correctamente implementados.

## Instalación

### Backend

1. Clona el repositorio:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```

2. Navega al directorio del backend:

    ```bash
    cd <DIRECTORIO_DEL_BACKEND>
    ```

3. Crea un entorno virtual y actívalo:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate     # Para Windows
    ```

4. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

5. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

6. Corre el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

### Frontend

1. Navega al directorio del frontend:

    ```bash
    cd <DIRECTORIO_DEL_FRONTEND>
    ```

2. Instala las dependencias:

    ```bash
    npm install
    ```

3. Ejecuta el servidor de desarrollo:

    ```bash
    npm start
    ```

## Pruebas

### Backend

Para ejecutar las pruebas en el backend, asegúrate de tener `pytest` instalado y corre el siguiente comando en el directorio del backend:

 ```bash
 pytest
   ```

### Frontend
Para ejecutar las pruebas en el frontend, asegúrate de tener vitest instalado y corre el siguiente comando en el directorio del frontend:

 ```bash
 vitest run
   ```

### Contribución
Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, por favor sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama para tus cambios 

```bash
(git checkout -b feature/nueva-funcionalidad).
```
Realiza tus cambios y realiza commit 

```bash
(git commit -am 'Añadida nueva funcionalidad')
```
Envía tus cambios 
```bash
(git push origin feature/nueva-funcionalidad).
```
Abre un pull request para revisión.