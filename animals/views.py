from rest_framework.views import APIView, Request, Response, status

from .models import Animal
from .serializers import AnimalSerializer

class AnimalMultiplyView(APIView):
    def get(self, _: Request):
        
        all_animals = Animal.objects.all()
        serializer = AnimalSerializer(all_animals, many = True)
        
        return Response(serializer.data)
        
    def post(self, request: Request):
        serializer = AnimalSerializer(data = request.data)
        
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    
class AnimalUpdateView(APIView):
    pass