from .models import Person, Task
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'username', 'gender', 'tasks']


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['task_title', 'task_description', 'is_complete', 'task_category',
                  'start_date', 'completed_date', 'owner']
        # read_only_fields = ['owner']

    # completed_date = serializers.ReadOnlyField('completed_date')
    # owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

