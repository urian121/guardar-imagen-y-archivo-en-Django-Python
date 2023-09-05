# Guardar imagen en Django Python 🐍

###### 1. Crear un entorno virtual, hay muchas formas

Opción 1: Crear entorno virtual con el paquete virtualenv, puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/
`	  
		  pip install virtualenv
		  virtualenv --version
		  virtualenv env
		 `

Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
`python -m venv env`

###### 2. Activar ambiente virtual

      . env/Script/activate
     Para desactivar mi entorno virtual  ` deactivate`

###### 3. Instalar Djando desde el manejador de paquete de Python Pip

    python -m pip install Django
    pip install Django
    Nota: para instalar Django en una version especifica
    pip install Django==4.2.4

###### 4. Instalar el paquete (biblioteca) Pillow, este tiene que ver como procesar la subida de imagen en el servidor

    Pillow es la librería que nos permitirá usar el campo ImageField para poder guardar imágenes

    - https://pypi.org/project/Pillow/
      pip install Pillow

###### 5. Instalar Driver para conectar Gestor de BD MySQL con Django (opcional)

    pip install mysqlclient

###### 6. Crear el proyecto con Djando

    `django-admin startproject project_core .`
    El punto . es crucial le dice al script que instale Django en el directorio actual

     Ya en este punto se puede correr el proyecto que a creado Django,
      python manage.py runserver

###### 7. Crear mi primera aplicación en Django

    python manage.py startapp amigos

###### 8. Crear el archivo requirements.txt para tener todos mis paquetes a la mano

    pip freeze > requirements.txt
    Nota: para instalar los paquetes solo basta ejecutar

###### 9. Instalar nuestra aplicación (amigos) ya creada en el proyecto

    archivo settings.py
    INSTALLED_APPS = [
    ----,
    'amigos',
    ]

##### 1. Configurar tu settings.py

    	import os
    	MEDIA_URL = '/media/'
    	MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#### 2. Configurar tu archivo urls.py del proyecto

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
    	# tus urls
    ]

    if settings.DEBUG:
    	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#### 3. Definiendo tu models.py

    from django.db import models

    class Documento(models.Model):
    	descripcion = models.CharField(max_length=255, blank=True)
    	documento = models.FileField(upload_to='documentos/')
    	subido_a = models.DateTimeField(auto_now_add=True)

#### 4. Definiendo tu forms.py

    from django import forms
    from .models import *

    class DocumentoForm(forms.ModelForm):
    	class Meta:
    		model = Documento
    		fields = ('descripcion', 'documento', )

#### 5. Define tu views.py

    def mi_metodo(request):
    	if request.method == 'POST':
    		form = DocumentoForm(request.POST, request.FILES)
    		if form.is_valid():
    			form.save()
    			return redirect('index')
    	else:
    		form = DocumentoForm()
    	return render(request, 'mi_template.html', {
    		'form': form
    	})

#### 6 Pintando el formulario en tu plantilla index.html

    <form method="post" enctype="multipart/form-data">
    	{% csrf_token %}
    	{{ form.as_p }}
    	<button type="submit">Subir</button>
      </form>
