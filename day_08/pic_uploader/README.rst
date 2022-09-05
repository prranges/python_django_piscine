=====
ImageUploader
=====
ImageUploader is a simple Django app - image gallery

How to:
-----------

1. Add "ImageUploader" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'app',
    ]

2. Include the gallery URLconf in your project urls.py like this::

    path('', include('app.urls')),

3. Run `python3 manage.py migrate` to create models.

4. Visit http://127.0.0.1:8000/ to view or add image.