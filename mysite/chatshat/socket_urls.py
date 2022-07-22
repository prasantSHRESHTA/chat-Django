from django.urls import path

from chatshat import connection

websockets_urls = [
   path('', connection.connection.as_asgi())
]
