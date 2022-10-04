from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404

from .models import Animal
from .serializers import AnimalSerializer

class AnimalView(APIView):
    def get(self, _: Request) -> Response:
        
        all_animals = Animal.objects.all()
        serializer = AnimalSerializer(all_animals, many = True)
        
        return Response(serializer.data)
        
    def post(self, request: Request) -> Response:
        serializer = AnimalSerializer(data = request.data)
        
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    
class AnimalCRUDView(APIView):
    def patch(self, request: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, pk = animal_id)
        
        serializer = AnimalSerializer(animal, request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response(serializer.data)
    
    def get(self, _: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, pk = animal_id)
        
        serializer = AnimalSerializer(animal)
        
        return Response(serializer.data)
    
    def delete(self, _: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, pk = animal_id)
        animal.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)