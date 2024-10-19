# ind-80-dj5-blog-word-count-htmx
Membuat aplikasi blog menggunakan Django versi 5.x dan HTMX

## 1. SETUP

#### 1. Lokasi

#### 2. Membuat remote repositori

#### 3. Mengklon remote repositori

#### 4. Membuat lingkungan virtual

#### 5. Menginstal Django


## 2. PROYEK DJANGO

#### 1. Membuat proyek Django

        modified:   README.md
        new file:   config/config/__init__.py
        new file:   config/config/asgi.py
        new file:   config/config/settings.py
        new file:   config/config/urls.py
        new file:   config/config/wsgi.py
        new file:   config/manage.py

#### 2. Membuat root direktori 'src'

        modified:   README.md
        renamed:    config/config/__init__.py -> config/__init__.py
        renamed:    config/config/asgi.py -> config/asgi.py
        renamed:    config/config/settings.py -> config/settings.py
        renamed:    config/config/urls.py -> config/urls.py
        renamed:    config/config/wsgi.py -> config/wsgi.py
        renamed:    config/manage.py -> manage.py

#### 3. Menjalankan server Django

#### 4. Mejalankan migrasi untuk mengakses admin panel

#### 5. Membuat superuser


## 3. SETTINGS

#### 1. Menseting bahasa dan waktu

        modified:   README.md
        modified:   config/settings.py

#### 2. Menseting absolute path untuk templates

        modified:   README.md
        modified:   config/settings.py

        # testing
        (venv312511) λ python manage.py check

        # results
        C:\Users\ING\Desktop\workspace\80-ind-dj5-jadual-vaksin\src\config\settings.py
        C:\Users\ING\Desktop\workspace\80-ind-dj5-jadual-vaksin\src\config
        C:\Users\ING\Desktop\workspace\80-ind-dj5-jadual-vaksin\src

        System check identified no issues (0 silenced).

#### 3. Menseting absolute path untuk file statis

        modified:   README.md
        modified:   config/settings.py

        (venv312511) λ python manage.py check
        System check identified no issues (0 silenced).

#### 4. Menseting absolute path untuk file media

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py

        (venv312511) λ python manage.py check
        System check identified no issues (0 silenced).


## 4. DATABASE

#### 1. Membuat postgres database

        E:\_WORKSPACE\laragon\www
        λ psql -U postgres
        psql (16.2)
        WARNING: Console code page (437) differs from Windows code page (1252)
                 8-bit characters might not work correctly. See psql reference
                 page "Notes for Windows users" for details.
        Type "help" for help.

        postgres=# CREATE DATABASE ind_80_dj5_blog_word_count_htmx;
        CREATE DATABASE
        postgres=#

#### 2. Menseting path untuk menghubungan proyek ke database

        # DB: PostgreSQL
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'ind_80_dj5_blog_word_count_htmx', 
                'USER': 'postgres', 
                'PASSWORD': 'postgres',
                'HOST': 'localhost', 
                'PORT': '5433',
            }
        }

          File "C:\Users\ING\Desktop\workspace\ind-80-dj5-blog-word-count-htmx\venv312511\Lib\site-packages\django\db\backends\postgresql\base.py", line 29, in <module>
            raise ImproperlyConfigured("Error loading psycopg2 or psycopg module")
        django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 or psycopg module

        modified:   README.md
        modified:   config/settings.py

#### 3. Menginstal psycopg2-binary

        (venv312511) λ python -m pip install psycopg2-binary
        Collecting psycopg2-binary
          Downloading psycopg2_binary-2.9.10-cp312-cp312-win_amd64.whl.metadata (5.0 kB)
        Downloading psycopg2_binary-2.9.10-cp312-cp312-win_amd64.whl (1.2 MB)
           ---------------------------------------- 1.2/1.2 MB 7.2 MB/s eta 0:00:00
        Installing collected packages: psycopg2-binary
        Successfully installed psycopg2-binary-2.9.10

        C:\Users\ING\Desktop\workspace\ind-80-dj5-blog-word-count-htmx\src(main -> origin)(venv312511) λ python manage.py check
        System check identified no issues (0 silenced).

#### 4. Melindungi file penting

        BASE_DIR = Path(__file__).resolve().parent.parent

        # Start langkah 1: Melindungi file penting
        import environ
        env = environ.Env()
        environ.Env.read_env()
        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
        # End langkah 1: Melindungi file penting

        # SECRET_KEY = 'django-insecure-@0l9(24a_h=-2-+&6n3dgs%*&)nk05(327n9&009gy$0m4un35'

        # Start langkah 2: Melindungi file penting
        SECRET_KEY = env('SECRET_KEY')
        # End langkah 2: Melindungi file penting

        # Start langkah 3: Melindungi file penting
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': env('DB_NAME'),
                'USER': env('DB_USER'),
                'PASSWORD': env('DB_PASSWORD'),
                'PASSWORD': env('DB_HOST'),
                'PASSWORD': env('DB_PORT'),
            }
        }
        # End langkah 3: Melindungi file penting

        (venv312511) λ pip install django-environ
        Collecting django-environ
          Using cached django_environ-0.11.2-py2.py3-none-any.whl.metadata (11 kB)
        Using cached django_environ-0.11.2-py2.py3-none-any.whl (19 kB)
        Installing collected packages: django-environ
        Successfully installed django-environ-0.11.2

        System check identified no issues (0 silenced).

        new file:   .env
        new file:   .env.example
        modified:   README.md
        modified:   config/settings.py


## 5. PROYEK DJANGO VS APLIKASI DJANGO


## 6. APLIKASI DJANGO

#### 1. Membuat aplikasi main

        modified:   README.md
        new file:   app/main/__init__.py
        new file:   app/main/admin.py
        new file:   app/main/apps.py
        new file:   app/main/migrations/__init__.py
        new file:   app/main/models.py
        new file:   app/main/tests.py
        new file:   app/main/views.py

#### 2. Mengintegrasikan aplikasi main dengan proyek

        modified:   README.md
        modified:   app/main/apps.py
        modified:   config/settings.py

        (venv312511) λ python manage.py check
        System check identified no issues (0 silenced).

#### 3. Halo Dunia! Waktu Jakarta sekarang

        modified:   README.md
        modified:   app/main/views.py
        modified:   config/urls.py


## 7. URLs, VIEWS, TEMPLATES
