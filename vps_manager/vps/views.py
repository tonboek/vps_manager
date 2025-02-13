from .models import VPS
from .serializers import VPSSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render

def index_page(request):
	return render(request, 'index.html')

class VPSListCreateView(APIView):
	"""
	Создание нового VPS и получение списка всех VPS.
	"""
	def get(self, request):
		vps_list = VPS.objects.all()
		serializer = VPSSerializer(vps_list, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = VPSSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			print(serializer.data)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VPSDetailView(APIView):
	"""
	Получение, обновление и удаление конкретного VPS по его uid.
	"""
	def get_object(self, uid):
		try:
			return VPS.objects.get(uid=uid)
		except VPS.DoesNotExist:
			return None

	def get(self, request, uid):
		vps = self.get_object(uid)
		if vps:
			serializer = VPSSerializer(vps)
			return Response(serializer.data)
		return Response({"error": "VPS not found"}, status=status.HTTP_404_NOT_FOUND)

	def patch(self, request, uid):
		vps = self.get_object(uid)
		if vps:
			serializer = VPSSerializer(vps, data=request.data, partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return Response({"error": "VPS not found"}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, uid):
		vps = self.get_object(uid)
		if vps:
			vps.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response({"error": "VPS not found"}, status=status.HTTP_404_NOT_FOUND)