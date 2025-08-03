Una aplicación web completa construida con Python y Django para gestionar una lista de tareas personales. Este proyecto demuestra la implementación de funcionalidades CRUD completas y una interfaz de usuario moderna y responsiva.

Características Principales
Crear Tareas: Añadir nuevas tareas a través de un formulario estilizado.
Leer/Listar Tareas: Ver todas las tareas existentes en una lista clara, con indicadores visuales para el estado y la prioridad.
Actualizar Tareas: Modificar los detalles de una tarea existente (nombre, prioridad, estado).
Eliminar Tareas: Borrar tareas de forma segura a través de una página de confirmación.
Diseño Responsivo: Interfaz estilizada con Tailwind CSS y componentes de Flowbite para una experiencia de usuario agradable en diferentes dispositivos.
Tecnologías Utilizadas
Backend: Python, Django
Frontend: HTML5, Tailwind CSS, Flowbite
Base de Datos: PostgreSQL
Control de Versiones: Git y GitHub

Configuración de la Base de Datos (PostgreSQL)

Este proyecto utiliza PostgreSQL como base de datos. Sigue estos pasos para configurarla:

1.  Instalar PostgreSQL:
    Descarga e instala PostgreSQL desde el sitio oficial: https://www.postgresql.org/download/windows/
    Durante la instalación, establece una contraseña para el usuario 'postgres'.

2.  Instalar el adaptador de Python:
    Abre tu terminal y ejecuta:
    ```bash
    pip install psycopg2-binary
    ```

3.  Crear Base de Datos y Usuario en PostgreSQL:
    Abre tu terminal (CMD o PowerShell) y navega al directorio 'bin' de tu instalación de PostgreSQL (ej. C:\Program Files\PostgreSQL\<version>\bin).
    Conéctate a psql como el usuario 'postgres':
    ```bash
    psql -U postgres
    ```
    Dentro de psql, ejecuta los siguientes comandos (reemplaza 'tu_contraseña_segura' con una contraseña fuerte):
    ```sql
    CREATE DATABASE todolist_db;
    CREATE USER todolist_user WITH PASSWORD 'tu_contraseña_segura';
    GRANT ALL PRIVILEGES ON DATABASE todolist_db TO todolist_user;
    \q
    ```
    Luego, conéctate a la nueva base de datos y otorga permisos al esquema public:
    ```bash
    psql -U postgres -d todolist_db
    ```
    ```sql
    GRANT ALL PRIVILEGES ON SCHEMA public TO todolist_user;
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO todolist_user;
    GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO todolist_user;
    ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO todolist_user;
    ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO todolist_user;
    \q
    ```

4.  Configurar Django (settings.py):
    Abre 'todo_project/settings.py' y actualiza la sección DATABASES para que apunte a tu base de datos PostgreSQL. Asegúrate de reemplazar 'TU_CONTRASEÑA_SEGURA' con la contraseña real que estableciste para 'todolist_user'.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'todolist_db',
            'USER': 'todolist_user',
            'PASSWORD': 'TU_CONTRASEÑA_SEGURA',  # ¡CAMBIA ESTO!
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5.  Aplicar Migraciones:
    Desde la raíz de tu proyecto, ejecuta las migraciones para crear las tablas en PostgreSQL:
    ```bash
    python manage.py migrate
    ```

Uso

1.  Asegúrate de tener la base de datos PostgreSQL configurada y las migraciones aplicadas.
2.  Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```
3.  Abre tu navegador y ve a http://127.0.0.1:8000/.
4.  Regístrate como un nuevo usuario y comienza a gestionar tus tareas.
