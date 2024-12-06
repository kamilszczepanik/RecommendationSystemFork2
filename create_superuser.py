import os
from django.contrib.auth import get_user_model

User = get_user_model()

login = 'admin123'
email = 'admin@example.com'
password = 'SecurePassword123'

if not User.objects.filter(login=login).exists():
    User.objects.create_superuser(login=login, email=email, password=password)
    print(f"Superuser {login} created successfully.")
else:
    print(f"Superuser {login} already exists.")