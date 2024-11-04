# Trello

## Github

###### 📁 Git Clone Project

```cmd
git clone https://github.com/LearnCodingEasy/Trello.git
```

###### 📝 Create File Gitignore

```
.gitignore
```

###### 🖊️ Write Inside File

```
node_modules/
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## LICENSE

Create File 📝 [ LICENSE ]

```text
LICENSE
```

```text
MIT License
Copyright (c) 2024 Hossam Rashad
📍 +0201091642528
📍 +0201101853042
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## Vite Press

###### 🖥️ Create Vuepress

```cmd
npm init vuepress trello_vuepress
```

###### 🖥️ Command Path

```cmd
cd trello_vuepress
```

###### 🖥️ Install Sass

```cmd
npm install -D sass-embedded
```

###### 📝 Create File

```
index.md
```

###### 🖥️ Run Vue Press

```cmd
npm run docs:dev
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## Django

### 🖥️ Virtual Environment

###### 🖥️ Create Virtual Environment 🐍

```cmd
python -m venv trello_virtual_environment
```

###### 🚀 Activate Virtual Environment 🔋

```cmd
trello_virtual_environment\Scripts\activate
```

### 🔧 Install Django

###### 🔧 Install Django 🦄

```cmd
pip install django
```

### 🛠️ Django Libraries

###### 🛠️ Install Django Libraries 📚

1 - 🌐 Django Rest Framework

```cmd
pip install djangorestframework
```

2 - 🔒 Django Rest Framework Simplejwt 🛡️

```cmd
pip install djangorestframework-simplejwt
```

3 - 🌍 Django Cors Headers 🔗

```cmd
pip install django-cors-headers
```

4 - 🖼️ pillow 📷

```
pip install pillow
```

### 📂 Create Django Project

```cmd
django-admin startproject trello_django
```

### 👤 Create Django App Account

```cmd
cd trello_django
```

```cmd
python manage.py startapp account
```

### ⚙️ Settings

#### ⚙️ Page Settings [ settings.py ] 📝

```python
# Page [trello/trello_django/trello_django/settings.py]

from datetime import timedelta

# The address of the site that points to the local server.
WEBSITE_URL = "http://127.0.0.1:8000"

# Define the default user model used in the application.
AUTH_USER_MODEL = "account.User"

# SIMPLE_JWT library settings to specify the validity period of tokens
# Access Token Validity (30 days)
# Refresh Token Validity (180 days)
# Disable Auto Refresh Tokens
SIMPLE_JWT = {
  "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
  "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
  "ROTATE_REFRESH_TOKENS": False,
}

# Django REST Framework settings for identity and permissions verification
# Use JWT for identity verification
# Allow only authenticated users
REST_FRAMEWORK = {
  "DEFAULT_AUTHENTICATION_CLASSES": (
      "rest_framework_simplejwt.authentication.JWTAuthentication",
  ),
  "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

# Allow CORS requests from specific addresses
# Allow requests from this origin
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
]

# Allow CSRF requests from specific addresses
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
]

INSTALLED_APPS = [
    # ...
    # Apps
    "account",
    # Libraries
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
]

MIDDLEWARE = [
    # Libraries [ Django Cors Headers ]
    "corsheaders.middleware.CorsMiddleware",
    # ...
]
# Access path for static files (such as CSS and JavaScript files)
STATIC_URL = "static/"
# Access path for media files (such as images and files uploaded by users)
MEDIA_URL = "media/"
# Specify a "media" folder in the project to store uploaded media files
MEDIA_ROOT = BASE_DIR / "media"
```

### 🧑 Account Page [ models.py ]

#### 🧑 App [ Account ] Page [ models.py ] 📝

```python
# 📄 صفحة [trello/trello_django/account/models.py]

import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

# 👥 Dedicated manager to create and manage users
# 👥 مدير مخصص لإنشاء وإدارة المستخدمين
class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        # ✉️ Verify email entry
        # ✉️ تحقق من إدخال البريد الإلكتروني
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 👤 Create a regular user
    # 👤 إنشاء مستخدم عادي
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    # 🛡️ Create an administrative user (super user)
    # 🛡️ إنشاء مستخدم إداري (سوبر يوزر)
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(name, email, password, **extra_fields)


# 🧑 Custom User Form
# 🧑 نموذج المستخدم المخصص
class User(AbstractBaseUser, PermissionsMixin):
    # 🔑 Define the primary field to be UUID
    # 🔑 تعريف الحقل الأساسي ليكون UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 📛 User Data Properties
    # 📛 خصائص بيانات المستخدم
    name = models.CharField(max_length=255, blank=True, null=True, default="")
    surname = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=15, blank=True, null=True)
    # 🖼️ Profile Picture
    # 🖼️ صورة شخصية
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    # 🖼️ Cover Photo
    # 🖼️ صورة الغلاف
    cover = models.ImageField(upload_to="covers", blank=True, null=True)

    # ⚙️ User Status
    # ⚙️ حالة المستخدم
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # 📅 Join Date & Last Login
    # 📅 تاريخ الانضمام وآخر تسجيل دخول
    # Automatic
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    # 📋 Custom Admin Link
    # 📋 ربط المدير المخصص
    objects = CustomUserManager()

    # 👥 Friends and Characteristics of Friendships
    # 👥 الأصدقاء وخصائص الصداقات
    friends = models.ManyToManyField("self")
    friends_count = models.IntegerField(default=0)
    people_you_may_know = models.ManyToManyField("self")

    # 📋 Tasks and Their Number
    # 📋 المهام وعددها
    task_count = models.IntegerField(default=0)

    # 🔒 إعدادات تسجيل الدخول: البريد الإلكتروني كمحدد رئيسي لتسجيل الدخول
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    # 🖼️ Function to get cover image link With default link if none exists
    # 🖼️ دالة للحصول على رابط صورة الغلاف مع رابط افتراضي إذا لم تكن موجودة
    def get_avatar(self):
        if self.avatar:
            return settings.WEBSITE_URL + self.avatar.url
        else:
            return "https://picsum.photos/200/200"

    def get_cover(self):
        if self.cover:
            return settings.WEBSITE_URL + self.cover.url
        else:
            return "https://picsum.photos/200/200"


# 📬 Friend Request Form
# 📬 نموذج طلب الصداقة
class FriendshipRequest(models.Model):
    # 📝 Friend request cases
    # 📝 حالات طلب الصداقة
    SENT = "sent"
    NOT_SENT = "not sent"
    ACCEPTED = "accepted"
    WAITING = "Waiting"
    REJECTED = "rejected"

    STATUS_CHOICES = (
        (SENT, "Sent"),
        (NOT_SENT, "Not Sent"),
        (ACCEPTED, "Accepted"),
        (WAITING, "Waiting"),
        (REJECTED, "Rejected"),
    )
    # 🔑 Friend Request UUID Essential Field
    # 🔑 حقل أساسي UUID لطلب الصداقة
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 🧑 User receiving the request
    # 🧑 المستخدم المستلم للطلب
    created_for = models.ForeignKey(
        User, related_name="received_friendshiprequests", on_delete=models.CASCADE
    )
    # 📅 Creation date
    # 📅 تاريخ الإنشاء
    created_at = models.DateTimeField(auto_now_add=True)
    # 🧑 The user who sent the request
    # 🧑 المستخدم المرسل للطلب
    created_by = models.ForeignKey(
        User, related_name="created_friendshiprequests", on_delete=models.CASCADE
    )
    # 📝 Order Status
    # 📝 حالة الطلب
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NOT_SENT)

```

### 🆕 Makemigrations

###### 🛠️ Modifications To Models File

###### 🛠️ تعديلات على ملف النماذج

```cmd
python manage.py makemigrations
```

### 🛠️ Makemigrations

###### 🛠️ Migrate To The Database

###### 🛠️ الانتقال إلى قاعدة البيانات

```cmd
python manage.py migrate
```

### 🧑 Account Page [ admin.py ]

#### 🧑 App [ Account ] Page [ admin.py ] 📝

```python
from django.contrib import admin
from .models import User
admin.site.register(User)
```

### 🧑 Account Page [ serializers.py ]

#### 🧑 App [ Account ] Page [ serializers.py ] 📝

```python
serializers.py
```

```python
#  📝 Page [ trello/trello_django/account/serializers.py ]
from rest_framework import serializers
from .models import User, FriendshipRequest

# 🧑 سيريلايزر لمستخدم

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # النموذج المرتبط بالسيريلايزر
        model = User
        # الحقول المطلوبة
        fields = (
            "id",
            "name",
            "surname",
            "email",
            "date_of_birth",
            "gender",
            "get_avatar",
            "get_cover",
            # Friends
            "friends_count",
            # Tasks
            "task_count",
        )


class FriendshipRequestSerializer(serializers.ModelSerializer):
    # 👤 Sender information using UserSerializer (read-only)
    # 👤 معلومات المرسل باستخدام المستخدمين (القراءة فقط)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = FriendshipRequest
        # 🆔 Request ID and sender data
        # 🆔 طلب معرف وبيانات المرسل
        fields = (
            "id",
            "created_by",
        )

```

### 🧑 Account Page [ forms.py ]

#### 🧑 App [ Account ] Page [ forms.py ] 📝

```python
# 📄 ملف [ trello/trello_django/account/forms.py ]

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

# 📝 نموذج التسجيل
class SignupForm(UserCreationForm):
    # 🔧 إعدادات النموذج: تحديد الحقول المطلوبة
    class Meta:
        model = User
        fields = (
            # 🧑 الاسم الأول
            "name",
            # 🧑 اللقب
            "surname",
            # 📧 البريد الإلكتروني
            "email",
            # 📅 تاريخ الميلاد
            "date_of_birth",
            # ⚧ الجنس
            "gender",
            # 🔑 كلمة المرور
            "password1",
            # 🔑 تأكيد كلمة المرور
            "password2",
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            # 🧑 User's name
            # 🧑 الاسم الأول
            "name",
            # 📧 User's email
            # 📧 البريد الإلكتروني
            "email",
            # 🖼️ User's profile picture
            # 🖼 صورة ملف تعريف المستخدم
            "avatar",
        )

```

### 🧑 Account Page [ api.py ]

#### 🧑 App [ Account ] Page [ api.py ] 📝

```python
api.py
```

```python
# 📄 ملف [ trello/trello_django/account/api.py ]

# 🌐 API for User Signup and Profile Info Retrieval
# 🌐 API لتسجيل المستخدم واسترجاع معلومات الحساب

from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from .forms import SignupForm, ProfileForm
from .models import User, FriendshipRequest
from .serializers import UserSerializer, FriendshipRequestSerializer

# 📝 Signup API Endpoint
# 📝 واجهة برمجية للتسجيل
@api_view(["POST"])
@authentication_classes([])  # 🚫 لا تتطلب مصادقة
@permission_classes([])  # 🚫 لا تتطلب أذونات
def signup(request):
    data = request.data
    message = "success"

    # 🧾 Initialize signup form with request data
    # 🧾 تهيئة نموذج التسجيل باستخدام بيانات الطلب
    form = SignupForm(
        {
            "name": data.get("name"),
            "surname": data.get("surname"),
            "email": data.get("email"),
            "date_of_birth": data.get("date_of_birth"),
            "gender": data.get("gender"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    # ✅ Check if form is valid
    # ✅ التحقق من صحة النموذج
    if form.is_valid():
        # 🛠️ Save the new user
        # 🛠️ حفظ المستخدم الجديد
        user = form.save()
        # 🔓 Activate the account
        # 🔓 تأكيد الحساب مباشرة
        user.is_active = True
        user.save()

        return JsonResponse({"message": message, "email_sent": True}, safe=False)
    else:
        # ❌ If errors exist, return them
        # ❌ إذا كان هناك أخطاء
        message = form.errors.as_json()
    # 🔍 Print errors for debugging
    # 🔍 طباعة الأخطاء لأغراض التصحيح
    print(message)
    return JsonResponse({"message": message}, safe=False)


# 👤 User Info API Endpoint
# 👤 واجهة برمجية لاسترجاع معلومات المستخدم
@api_view(["GET"])
def me(request):
    return JsonResponse(
        {
            "id": request.user.id,
            "name": request.user.name,
            "surname": request.user.surname,
            "email": request.user.email,
            "date_of_birth": request.user.date_of_birth,
            "gender": request.user.gender,
        }
    )


@api_view(["POST"])
def editprofile(request):
    # 👤 Get current user and new email data
    # 👤 احصل على بيانات بريد إلكتروني حالية وبيانات بريد إلكتروني جديدة
    user = request.user
    email = request.data.get("email")

    # 📧 Check if email is already in use by another user
    # 📧 تحقق مما إذا كان البريد الإلكتروني قيد الاستخدام بالفعل من قبل مستخدم آخر
    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({"message": "email already exists"})
    else:
        # 📝 Initialize profile form with request data and files
        # 📝 تهيئة نموذج الملف الشخصي مع بيانات الطلب والملفات
        form = ProfileForm(request.POST, request.FILES, instance=user)

        # ✅ Validate and save profile if valid
        # ✅ التحقق من صحة وحفظ الملف الشخصي إذا كان صالحًا
        if form.is_valid():
            form.save()

        # 🔄 Serialize updated user data
        # 🔄 قم بتسلسل بيانات المستخدم المحدثة
        serializer = UserSerializer(user)
        return JsonResponse({"message": "information updated", "user": serializer.data})


@api_view(["POST"])
def editpassword(request):
    # 🔒 Initialize password change form with request data
    # 🔒 تهيئة نموذج تغيير كلمة المرور مع بيانات الطلب
    user = request.user
    form = PasswordChangeForm(data=request.POST, user=user)

    # ✅ Validate and save new password if valid
    # ✅ التحقق من صحة وحفظ كلمة مرور جديدة إذا كانت صالحة
    if form.is_valid():
        form.save()
        return JsonResponse({"message": "success"})
    else:
        # ❌ Return errors if form is invalid
        # ❌ أخطاء الإرجاع إذا كان النموذج غير صالح
        return JsonResponse({"message": form.errors.as_json()}, safe=False)


# 🌐 Friendship Request and Friends Management API
# 🌐 واجهة برمجية لإدارة طلبات الصداقة وإدارة الأصدقاء
@api_view(["POST"])
def send_friendship_request(request, pk):
    # 👤 Get the user to whom the friendship request is being sent
    # 👤 جلب المستخدم الذي يتم إرسال طلب الصداقة إليه
    user = User.objects.get(pk=pk)

    # 🔍 Check if a request already exists between the users
    # 🔍 التحقق مما إذا كان هناك طلب صداقة موجود بالفعل بين المستخدمين
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
        created_by=user
    )
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(
        created_by=request.user
    )

    if not check1 or not check2:
        # ✉️ Create a new friendship request if it doesn't exist
        # ✉️ إنشاء طلب صداقة جديد إذا لم يكن موجودًا
        friendrequest = FriendshipRequest.objects.create(
            created_for=user, created_by=request.user
        )
        return JsonResponse({"message": "friendship request created"})
    else:
        return JsonResponse({"message": "request already sent"})


@api_view(["GET"])
def friends(request, pk):
    # 👥 Get the friends and requests for the specified user
    # 👥 جلب الأصدقاء والطلبات للمستخدم المحدد
    user = User.objects.get(pk=pk)
    requests = []

    # 📝 Check if the current user is the requested user
    # 📝 التحقق مما إذا كان المستخدم الحالي هو نفس المستخدم المطلوب
    if user == request.user:
        requests = FriendshipRequest.objects.filter(
            created_for=request.user, status=FriendshipRequest.SENT
        )
        requests = FriendshipRequestSerializer(requests, many=True).data

    # 👫 Retrieve all friends of the user
    # 👫 جلب جميع أصدقاء المستخدم
    friends = user.friends.all()

    return JsonResponse(
        {
            "user": UserSerializer(user).data,
            "friends": UserSerializer(friends, many=True).data,
            "requests": requests,
        },
        safe=False,
    )


@api_view(["GET"])
def my_friendship_suggestions(request):
    # 🤝 Suggest users the current user may know
    # 🤝 اقتراح المستخدمين الذين قد يعرفهم المستخدم الحالي
    serializer = UserSerializer(request.user.people_you_may_know.all(), many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["POST"])
def handle_request(request, pk, status):
    # 🛠️ Handle and update the status of a friendship request
    # 🛠️ معالجة وتحديث حالة طلب الصداقة
    user = User.objects.get(pk=pk)
    friendship_request = FriendshipRequest.objects.filter(created_for=request.user).get(
        created_by=user
    )
    friendship_request.status = status
    friendship_request.save()

    # 👥 Add each user to the other's friends list if accepted
    # 👥 إضافة كل مستخدم إلى قائمة أصدقاء الآخر إذا تم قبول الطلب
    user.friends.add(request.user)
    user.friends_count += 1
    user.save()

    request_user = request.user
    request_user.friends_count += 1
    request_user.save()

    return JsonResponse({"message": "friendship request updated"})

```

### 🧑 Account Page [ urls.py ]

#### 🧑 App [ Account ] Page [ urls.py ] 📝

```python
urls.py
```

```python

# 📄 ملف [ trello/trello_django/account/urls.py ]

# 🌐 URL Configuration for User and Friend Management API
# 🌐 تكوين الروابط لواجهة برمجية لإدارة المستخدم والأصدقاء

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api

urlpatterns = [
    # 👤 Retrieve current user's information
    # 👤 استرجاع معلومات المستخدم الحالي
    path("me/", api.me, name="me"),
    # 📝 Signup for new users
    # 📝 تسجيل مستخدمين جدد
    path("signup/", api.signup, name="signup"),
    # 🔑 Obtain JWT token for login
    # 🔑 الحصول على رمز JWT لتسجيل الدخول
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    # ♻️ Refresh JWT token
    # ♻️ تحديث رمز JWT
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # ✏️ Edit user profile
    # ✏️ تعديل ملف المستخدم
    path("editprofile/", api.editprofile, name="editprofile"),
    # 🔒 Change user password
    # 🔒 تغيير كلمة مرور المستخدم
    path("editpassword/", api.editpassword, name="editpassword"),
    # 🤝 Retrieve suggested friends
    # 🤝 استرجاع الأصدقاء المقترحين
    path(
        "friends/suggested/",
        api.my_friendship_suggestions,
        name="my_friendship_suggestions",
    ),
    # 👫 Retrieve friends of a user
    # 👫 استرجاع أصدقاء المستخدم
    path("friends/<uuid:pk>/", api.friends, name="friends"),
    # ✉️ Send friendship request
    # ✉️ إرسال طلب صداقة
    path(
        "friends/<uuid:pk>/request/",
        api.send_friendship_request,
        name="send_friendship_request",
    ),
    # 🛠️ Handle friendship request (accept/reject)
    # 🛠️ معالجة طلب الصداقة (قبول/رفض)
    path("friends/<uuid:pk>/<str:status>/", api.handle_request, name="handle_request"),
]
```

### ⚙️ Project Page [ urls.py ]

#### ⚙ Project Page [ urls.py ] 📝

```python
# 📄 ملف [ trello/trello_django/trello_django/urls.py ]

# 🌐 Main URL Configuration for Django Project
# 🌐 تكوين الروابط الرئيسية لمشروع Django

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🔗 Include URLs from the 'account' app for API endpoints
    # 🔗 تضمين روابط تطبيق 'account' للنقاط البرمجية
    path("api/", include("account.urls")),
    # 🔧 Admin panel for site management
    # 🔧 لوحة تحكم الإدارة لإدارة الموقع
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 🖼️ Serve media files during development
# 🖼️ عرض ملفات الوسائط أثناء التطوير
```

### 👤 Superuser

#### ⚙ Create Superuser

```cmd
python manage.py createsuperuser
```

```cmd
Email: learncodingeasy0100@gmail.com
Password: ******
Password (again): ******
Superuser created successfully.
```

### 🚀 Run Server

###### 👉️ Go To

---

```cmd
http://127.0.0.1:8000/
```

```cmd
http://127.0.0.1:8000/admin
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## Vue

### 🖥️ Create Vue Project

###### 📁 Create Vue Project

```cmd
npm create vue@latest
```

###### 🚀 Choose Vite [ Project name & Select a framework] 🛠️

```cmd
√ Project name: ... trello_vue
√ Add TypeScript? ... [No] / Yes
√ Add JSX Support? ... [No] / Yes
√ Add Vue Router for Single Page Application development? ... No / [Yes]
√ Add Pinia for state management? ... No / [Yes]
√ Add Vitest for Unit Testing? ... [No] / Yes
√ Add an End-to-End Testing Solution? » [No]
√ Add ESLint for code quality? ... No / [Yes]
√ Add Prettier for code formatting? ... No / [Yes]
√ Add Vue DevTools 7 extension for debugging? (experimental) ... [No] / Yes

Scaffolding project in E:\Projects\trello\trello_vue...

Done. Now run:
  cd trello_vue
  npm install
  npm run format
  npm run build
  npm run dev
```

```cmd
cd trello_vue
```

```cmd
npm install
```

```cmd
npm run format
```

```cmd
npm run build
```

```cmd
npm run dev
```

### 📚 Install Vue Libraries

###### 📚 Install Vue Libraries

- 1️⃣ Tailwind

```cmd
npm install -D tailwindcss postcss autoprefixer
```

```cmd
npx tailwindcss init -p
```

- 2️⃣ PrimeVue

```cmd
npm install primevue primeicons
```

```cmd
npm install @primevue/themes
```

```cmd
npm install quill
```

- 3️⃣ scss

```cmd
npm install -D sass@latest
```

- 4️⃣ Axios

```cmd
npm install axios
```

- 5️⃣ Font Awesome

```cmd
npm i --save @fortawesome/fontawesome-svg-core @fortawesome/vue-fontawesome@latest @fortawesome/vue-fontawesome@prerelease @fortawesome/free-solid-svg-icons @fortawesome/free-brands-svg-icons @fortawesome/free-regular-svg-icons
```

- 6️⃣ Pwa

```cmd
npm install -D vite-plugin-pwa
```

- 7️⃣ Prism

```cmd
npm i prismjs
```

```cmd
npm i vue-prism-component
```

- 8️⃣ Swiper

```cmd
npm i swiper
```

### 📦 Setup Vue Libraries

###### 1️⃣ Tailwind

- Configure Tailwind

- 📝 File [ tailwind.config.js ]

```js
// Page [ trello/trello_vue/tailwind.config.js ]
export default defineConfig({
  // ...
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"]
  // ...
});
```

- 📝 File [ main.css ]

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

###### - 2️⃣ PrimeVue

- 📝 Create Page [ primeTheme.js ] Inside stores

```
primeTheme.js
```

```js
// Page [ trello/trello_vue/src/stores/primeTheme.js ]

import { reactive } from "vue";
export default {
  install: (app) => {
    const _appState = reactive({ theme: "Aura", darkTheme: false });
    app.config.globalProperties.$appState = _appState;
  }
};
```

- 📝 Create Page [ Theme/ThemeSwitcher.vue ] Inside components

```
Theme/ThemeSwitcher.vue
```

```html
<template>
  <span class="">
    <ul class="flex list-none m-0 p-0 gap-2 items-center">
      <li>
        <button
          type="button"
          class="inline-flex w-8 h-8 p-0 items-center justify-center surface-0 dark:surface-800 border border-surface-200 dark:border-surface-600 rounded-full"
          @click="onThemeToggler"
        >
          <i :class="`dark:text-white pi ${iconClass}`" />
        </button>
      </li>
    </ul>
  </span>
</template>
```

```js
<script>
  import { updatePreset, updateSurfacePalette } from '@primevue/themes'

  export default {
    data() {
      return {
        iconClass: 'pi-moon',
        selectedPrimaryColor: 'noir',
        selectedSurfaceColor: null
      }
    },
    methods: {
      onThemeToggler() {
        const root = document.getElementsByTagName('html')[0]
        root.classList.toggle('p-dark')
        this.iconClass = this.iconClass === 'pi-moon' ? 'pi-sun' : 'pi-moon'
      },

      updateColors(type, color) {
        if (type === 'primary') this.selectedPrimaryColor = color.name
        else if (type === 'surface') this.selectedSurfaceColor = color.name

        this.applyTheme(type, color)
      },
      applyTheme(type, color) {
        if (type === 'primary') {
          updatePreset(this.getPresetExt())
        } else if (type === 'surface') {
          updateSurfacePalette(color.palette)
        }
      },
      onRippleChange(value) {
        this.$primevue.config.ripple = value
      }
    },
    computed: {
      rippleActive() {
        return this.$primevue.config.ripple
      }
    }
  }
</script>
```

- 📝 Create Page [ presets/Noir.js ] Inside src

```
presets/Noir.js
```

```js
import { definePreset } from "@primevue/themes";
import Aura from "@primevue/themes/aura";

const Noir = definePreset(Aura, {
  semantic: {
    primary: {
      50: "{surface.50}",
      100: "{surface.100}",
      200: "{surface.200}",
      300: "{surface.300}",
      400: "{surface.400}",
      500: "{surface.500}",
      600: "{surface.600}",
      700: "{surface.700}",
      800: "{surface.800}",
      900: "{surface.900}",
      950: "{surface.950}"
    },
    colorScheme: {
      light: {
        primary: {
          color: "{primary.950}",
          contrastColor: "#ffffff",
          hoverColor: "{primary.900}",
          activeColor: "{primary.800}"
        },
        highlight: {
          background: "{primary.950}",
          focusBackground: "{primary.700}",
          color: "#ffffff",
          focusColor: "#ffffff"
        }
      },
      dark: {
        primary: {
          color: "{primary.50}",
          contrastColor: "{primary.950}",
          hoverColor: "{primary.100}",
          activeColor: "{primary.200}"
        },
        highlight: {
          background: "{primary.50}",
          focusBackground: "{primary.300}",
          color: "{primary.950}",
          focusColor: "{primary.950}"
        }
      }
    }
  }
});

export default Noir;
```

###### - 3️⃣ scss

###### - 4️⃣ Axios

```js
// Axios  Import
// Axios  استيراد
import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:8000";

app.use(router, axios);
```

###### - 5️⃣ Font Awesome

```js
// Page [ trello/trello_vue/src/main.js ]

// Font Awesome
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
// Add Free Icons Styles To SVG Core
library.add(fas, far, fab);

// eslint-disable-next-line vue/multi-word-component-names
app.component("fa", FontAwesomeIcon);
```

###### - 6️⃣ Pwa

- 📝 Edit Page [ vite.config.js ]

```js
import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// For Pwa
// https://vite-pwa-org.netlify.app/guide/
import { VitePWA } from "vite-plugin-pwa";

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // For Pwa
    VitePWA({
      registerType: "autoUpdate",
      workbox: {
        globPatterns: ["**/*.{js,css,html,ico,png,svg}"],
        clientsClaim: true,
        skipWaiting: true,
        cleanupOutdatedCaches: false,
        offlineGoogleAnalytics: true,
        sourcemap: true,
        runtimeCaching: [
          {
            urlPattern: ({ request }) =>
              request.destination === "document" ||
              request.destination === "script" ||
              request.destination === "style" ||
              request.destination === "image" ||
              request.destination === "font",
            handler: "StaleWhileRevalidate",
            options: {
              cacheName: "assets-cache",
              expiration: {
                maxEntries: 100,
                maxAgeSeconds: 60 * 60 * 24 * 30
              }
            }
          }
        ]
      },
      devOptions: {
        enabled: true
      },
      injectRegister: "auto",
      includeAssets: ["**/*"],
      manifest: {
        name: "Script Youtube",
        short_name: "Script Youtube",
        description: "My Awesome App Script Youtube",
        theme_color: "#ffffff",
        icons: [
          {
            src: "./images/icons/script_youtube_icon_72x72.png",
            type: "image/png",
            sizes: "72x72",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_96x96.png",
            type: "image/png",
            sizes: "96x96",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_128x128.png",
            type: "image/png",
            sizes: "128x128",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_144x144.png",
            type: "image/png",
            sizes: "144x144",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_152x152.png",
            type: "image/png",
            sizes: "152x152",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_192x192.png",
            type: "image/png",
            sizes: "192x192",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_384x384.png",
            type: "image/png",
            sizes: "384x384",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_512x512.png",
            type: "image/png",
            sizes: "512x512",
            purpose: "any maskable"
          }
        ],
        screenshots: [
          {
            src: "./images/screenshots/screenshots.png",
            sizes: "640x480",
            type: "image/png",
            form_factor: "wide"
            // "form_factor": "narrow"
          }
        ]
      }
    })
  ],
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url))
    }
  }
});
```

- 🖼️ Add Image Inside Public

```
├── public/
│   ├── images/
│   |   ├── icons/
│   │   |   ├── 🖼️ trello_icon_72x72.png
│   │   |   ├── 🖼️ trello_icon_96x96.png
│   │   |   ├── 🖼️ trello_icon_128x128.png
│   │   |   ├── 🖼️ trello_icon_144x144.png
│   │   |   ├── 🖼️ trello_icon_152x152.png
│   │   |   ├── 🖼️ trello_icon_192x192.png
│   │   |   ├── 🖼️ trello_icon_384x384.png
│   │   |   ├── 🖼️ trello_icon_512x512.png
│   |   ├── screenshots/
│   │   |   ├── 🖼️ screenshots.png
```

###### 👉️ Go To Website To Resize Image

```
https://www.iloveimg.com/resize-image
```

###### - 7️⃣ Prism

###### - 8️⃣ Swiper

###### - 9️⃣ Pinia

- 🧞‍♂️ User Store
- 📝 Create Page [ user.js ] Inside Stores

```
user.js
```

```js
// Page [ trello/trello_vue/src/stores/user.js ]
import { defineStore } from "pinia";
import axios from "axios";
export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    user: {
      isAuthenticated: false,
      id: null,
      name: null,
      surname: null,
      email: null,
      date_of_birth: null,
      access: null,
      refresh: null,
      friends_count: 0,
      // User gender 👤
      gender: null,
      // 🖼️ Profile picture
      // 🖼 صورة الملف الشخصي
      avatar: null,
      // 🖼️ Cover photo
      // 🖼️ صورة الغلاف
      cover: null,
      // 📋 Number of tasks
      // 📋 عدد المهام
      task_count: 0
    }
  }),
  actions: {
    // 🔄 Initialize the store
    // 🔄 تهيئة المخزن
    initStore() {
      if (localStorage.getItem("user.access")) {
        console.log("User has access!");
        this.user.isAuthenticated = true;
        this.user.id = localStorage.getItem("user.id");
        this.user.name = localStorage.getItem("user.name");
        this.user.surname = localStorage.getItem("user.surname");
        this.user.email = localStorage.getItem("user.email");
        this.user.date_of_birth = localStorage.getItem("user.date_of_birth");
        this.user.gender = localStorage.getItem("user.gender");
        this.user.avatar = localStorage.getItem("user.avatar");
        this.user.cover = localStorage.getItem("user.cover");
        this.user.access = localStorage.getItem("user.access");
        this.user.refresh = localStorage.getItem("user.refresh");
        this.refreshToken();
        this.user.friends_count = localStorage.getItem("user.friends_count");
        this.user.task_count = localStorage.getItem("user.task_count");
      }
    },
    // 🔑 Set access and refresh tokens
    // 🔑 إعداد رموز الوصول والتحديث
    setToken(data) {
      console.log("setToken", data);
      this.user.access = data.access;
      this.user.refresh = data.refresh;
      this.user.isAuthenticated = true;
      localStorage.setItem("user.access", data.access);
      localStorage.setItem("user.refresh", data.refresh);

      console.log("user.access: ", localStorage.getItem("user.access"));
    },
    // ❌ Remove tokens and clear user data
    // ❌ إزالة الرموز ومسح بيانات المستخدم
    removeToken() {
      console.log("removeToken");
      this.user.refresh = null;
      this.user.access = null;
      this.user.isAuthenticated = false;
      this.user.id = null;
      this.user.name = null;
      this.user.surname = null;
      this.user.email = null;
      this.user.date_of_birth = null;
      this.user.gender = null;
      this.user.avatar = null;
      this.user.cover = null;
      this.user.friends_count = null;
      this.user.task_count = null;

      localStorage.setItem("user.access", "");
      localStorage.setItem("user.refresh", "");
      localStorage.setItem("user.id", "");
      localStorage.setItem("user.name", "");
      localStorage.setItem("user.surname", "");
      localStorage.setItem("user.email", "");
      localStorage.setItem("user.date_of_birth", "");
      localStorage.setItem("user.gender", "");
      localStorage.setItem("user.avatar", "");
      localStorage.setItem("user.cover", "");
      localStorage.setItem("user.friends_count", "");
      localStorage.setItem("user.task_count", "");
    },
    // ✍️ Set user info in state and localStorage
    // ✍️ تعيين بيانات المستخدم في الحالة و localStorage
    setUserInfo(user) {
      console.log("setUserInfo", user);
      this.user.id = user.id;
      this.user.name = user.name;
      this.user.surname = user.surname;
      this.user.email = user.email;
      this.user.date_of_birth = user.date_of_birth;
      this.user.gender = user.gender;
      this.user.avatar = user.avatar;
      this.user.cover = user.cover;
      this.user.friends_count = user.friends_count;
      this.user.task_count = user.task_count;
      localStorage.setItem("user.id", this.user.id);
      localStorage.setItem("user.name", this.user.name);
      localStorage.setItem("user.surname", this.user.surname);
      localStorage.setItem("user.email", this.user.email);
      localStorage.setItem("user.date_of_birth", this.user.date_of_birth);
      localStorage.setItem("user.gender", this.user.gender);
      localStorage.setItem("user.avatar", this.user.avatar);
      localStorage.setItem("user.cover", this.user.cover);
      localStorage.setItem("user.friends_count", this.user.friends_count);
      localStorage.setItem("user.task_count", this.user.task_count);
    },
    // 🔄 Refresh access token
    // 🔄 تحديث رمز الوصول
    refreshToken() {
      axios
        .post("/api/refresh/", {
          refresh: this.user.refresh
        })
        .then((response) => {
          this.user.access = response.data.access;
          localStorage.setItem("user.access", response.data.access);
          axios.defaults.headers.common["Authorization"] =
            "Bearer " + response.data.access;
        })
        .catch((error) => {
          console.log(error);
          this.removeToken();
        });
    }
  }
});
```

```

```
