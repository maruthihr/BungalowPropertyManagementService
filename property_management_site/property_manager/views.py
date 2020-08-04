from .models import Property
from .serializers import PropertySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

class ResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 500

# Create your views here.
class PropertyList(ListAPIView):
    pagination_class = ResultsSetPagination
    def get_queryset(self):
        query_parameters = self.request.query_params.items()
        queryset = Property.objects.all()
        filters = []
        for key, value in query_parameters:
            if key != 'page':
                filter = ".filter({}='{}')".format(key, value)
                filters.append(filter)
        queryset = eval("queryset{}".format("".join(filters)))
        return queryset

    def get_serializer_class(self):
        return PropertySerializer


    def post(self, request, format=None):
       """
       Create a new property if the property with this zillow_id does not exist
       """
       serializer = PropertySerializer(data=request.data)
       print(request.data)
       if serializer.is_valid():
           # check if object already exists.
           if not Property.objects.filter(zillow_id=request.data['zillow_id']).exists():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
           else:
               return Response({"message": "Item already exists"}, status=status.HTTP_409_CONFLICT)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

