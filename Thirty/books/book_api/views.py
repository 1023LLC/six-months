# from django.shortcuts import render, get_object_or_404

# from book_api.serializer import BookSerializer

# from .models import Book

# from django.http import JsonResponse

# from rest_framework.response import Response

# from rest_framework.decorators import api_view

# from rest_framework import status


# @api_view(['GET'])
# def books_list(request):
#    books = Book.objects.all()
#    serializer = BookSerializer(books, many=True)
#    return Response(serializer.data)

# @api_view(['POST'])
# def book_create(request):
    
#     if request.method == 'POST':
#         serializer = BookSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
      
# @api_view(['GET', 'PUT', 'DELETE'])  
# def book(request, pk):
    
#     book = get_object_or_404(Book, pk=pk)
    
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
    
    
#     if request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
#     if request.method == 'DELETE':
#         book.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.views import APIView 
from .models import Book
from .serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
 
 
class BookCreate(APIView):
    def post(self, request):
        
        serializer = BookSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class BookDetail(APIView):
    
    def get_book_by_pk(self, pk):
        return get_object_or_404(Book, pk=pk)

    
    def get(self, request, pk):
        book =  self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        book =  self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        book =  self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

