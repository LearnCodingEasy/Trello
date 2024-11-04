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
