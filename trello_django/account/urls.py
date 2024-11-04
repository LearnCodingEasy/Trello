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
