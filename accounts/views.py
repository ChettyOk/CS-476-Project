from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

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
        errors["email"] = "Please enter a valid email address."

    if len(password) < 8:
        errors["password"] = "The password must be at least 8 characters long."

    if errors:
        return JsonResponse({"errors": errors}, status=400)

    if User.objects.filter(email__iexact=email).exists():
        return JsonResponse(
            {"errors": {"email": "This email address is already registered."}},
            status=409,
        )

    User.objects.create_user(email=email, password=password)
    return JsonResponse({"message": "User account created."}, status=201)


@require_POST
def login(request):
    email = request.POST.get("email", "").strip().lower()
    password = request.POST.get("password", "")

    user = authenticate(request, username=email, password=password)

    if user is None:
        return JsonResponse(
            {"error": "Invalid email address or password."},
            status=401,
        )
    auth_login(request, user)
    return JsonResponse({"message": "Login successful."}, status=200)


@require_POST
def logout(request):
    auth_logout(request)
    return JsonResponse({"message": "Logout successful."}, status=200)


#
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
