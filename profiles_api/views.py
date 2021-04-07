from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self,request):
        """create a hello message with a name request"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'massage':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object """
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test APIViewSet"""
    serializer_class=serializers.HelloSerializers

    def list(self,request):
        """Return a hello message """

        a_viewset=[
        'uses function(create,retreive,update,patial_update)',
        'automaticaly maps to urls using routers',
        'provides more functionality with less code'
        ]
        return Response({'message':'hello !','a_viewset':a_viewset})

    def create(self,request):
        """ create a new hwllo message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name} !'
            return Response({'message':message})
        else:
            return Response(
               serializer.errors,
               status=status.HTTP_400_BAD_REQUEST
            )

    def retreive(self,request,pk=None):
        """handle get objects by it's id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """handle updating part of an objct """
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """handle removing an object"""
        return Response({'http_method':'DELETE'})

                            
