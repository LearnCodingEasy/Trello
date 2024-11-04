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
