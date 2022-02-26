# To run

1. create vertual env
2. run pip install -r requirements.txt
3. run python manage.py makemigrations
4. run python manage.py migration
5. run python manage.py runserver

Or use DockerFile to make an image and docker-compose.

## Go to localhost 8000

## Urls 
```
vehicles/
vehicles<drf_format_suffix:format>
vehicle/<str:pk>
vehicle/<str:pk><drf_format_suffix:format>
vehicle/<str:pk>/distance [name='pk']
vehicle/<str:pk>/distance<drf_format_suffix:format> [name='pk']
vehicle/<str:pk>/history
vehicle/<str:pk>/history<drf_format_suffix:format>
health
```