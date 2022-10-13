from django.shortcuts import render
from .serializers import TaskSeriallizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task


@api_view(['GET'])
def my_api_view(request):
    data = {
        'text': 'Hello, my team !'
    }
    return Response(data)


@api_view(['GET'])
def tasklist_view(request):
    tasks = Task.objects.all()
    serializer = TaskSeriallizer(tasks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def task_detail_view(request, id):
    tasks = Task.objects.get(id=id)
    serializer = TaskSeriallizer(tasks, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def task_create_view(request):
    serializer = TaskSeriallizer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response({"Created: Object is created !"})


@api_view(['POST'])
def task_update_view(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSeriallizer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete_view(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    return Response({"info":"Object was deleted"})
