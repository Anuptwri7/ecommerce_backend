# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_backend.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()
import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Replace these with your desired superuser credentials
SUPERUSER_EMAIL = "admin@example.com"
SUPERUSER_USERNAME = "admin"
SUPERUSER_PASSWORD = "admin123"

# Check if superuser already exists
if not User.objects.filter(username=SUPERUSER_USERNAME).exists():
    User.objects.create_superuser(
        username=SUPERUSER_USERNAME,
        email=SUPERUSER_EMAIL,
        password=SUPERUSER_PASSWORD
    )
    print("Superuser created successfully.")
else:
    print("Superuser already exists.")
