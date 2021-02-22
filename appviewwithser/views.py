from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from modelApp.models import Students as Stud, Students
from .serializer import StudSer
from rest_framework import status

class StudView(APIView):
    def get(self,request):
        x=[]
        # print(x[8])
        emps = Students.objects.all()
        serializer = Students(emps,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = Students(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'new object added to database'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudDet(APIView):
    def get(self,request,pk):
        emp = Students.objects.get(eno=pk)
        serializer = StudSer(emp)
        return Response(serializer.data)
    def put(self,request,pk):
        emp = Students.objects.get(eno=pk)
        serializer = StudSer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'new object added to database'})
        else:
            return Response({'message':'record not updated successfully'})
    def delete(self,request,pk):
        emp = Stud.objects.get(eno=pk)
        emp.delete()
        # serializer = EmpSer(emp, data=request.data)
        return Response({'message': 'record deleted successfully'})

