from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import User

# Create your views here.
# functions that interact with the user

# ==========================================
# VON MIR (DJANGO DEFAULTS)
# ==========================================

# ==========================================
# VON EUCH (AUS DEM PDF - CONTROLLER)
# ==========================================

# Auth Controller
@require_POST
def register(request):
    email = request.POST.get("email", "").strip().lower()
    password = request.POST.get("password", "")

    errors = {}

    try:
        validate_email(email)
    except ValidationError:
        errors["email"] = "Bitte gib eine gültige E-Mail-Adresse ein."

    if len(password) < 8:
        errors["password"] = "Das Passwort muss mindestens 8 Zeichen lang sein."

    if errors:
        return JsonResponse({"errors": errors}, status=400)

    if User.objects.filter(email__iexact=email).exists():
        return JsonResponse(
            {"errors": {"email": "Diese E-Mail-Adresse ist bereits registriert."}},
            status=409,
        )

    User.objects.create_user(email=email, password=password)
    return JsonResponse({"message": "Benutzerkonto erstellt."}, status=201)

#     login()
#     logout()
#     request Forgotten Password()
#     reset Password()

# Profile Controller
#     get My Profile()
#     update Student Profil()
#     update Tutor Profil()
#     Switch Role()

# Tutor Controller
#     get Tutor Profile
#     update Tutor Profile
#     get Tutor Dashboard
