from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseCountSerializer(ModelSerializer):
    quantity_of_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_quantity_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = (
            "name",
            "preview",
            "description",
            "lessons",
            "quantity_of_lessons",
        )
