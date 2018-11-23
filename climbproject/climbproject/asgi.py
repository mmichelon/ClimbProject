# """
# ASGI entrypoint. Configures Django and then runs the application
# defined in the ASGI_APPLICATION setting.
# """
#
# import os
# import django
# from channels.routing import get_default_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
# django.setup()
# application = get_default_application()


import os
import channels.asgi
# from channels.asgi import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "climbapp.settings")
channel_layer = channels.asgi.get_channel_layer()
