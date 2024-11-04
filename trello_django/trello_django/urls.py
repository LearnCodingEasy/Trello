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
