from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer

@api_view(['GET', 'POST'])
def user_api_view(request):
    
    if request.method == 'GET':
        users = User.objects.all().values('id', 'username', 'email', 'password')
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':        
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk):
    # queryset
    user = User.objects.filter(id=pk).first()

    # validations
    if user:

        # retrieve
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)
        
        # update
        elif request.method == 'PUT':        
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

        # delete
        elif request.method == 'DELETE':        
            user.delete()
            return Response({"message": "Eliminado correctamente"}, status=200)

    return Response({"message": "No existe el usuario"}, status=404)    