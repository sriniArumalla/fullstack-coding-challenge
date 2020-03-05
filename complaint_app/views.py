from rest_framework import viewsets
from .models import UserProfile, Complaint
from .serializers import UserSerializer, UserProfileSerializer, ComplaintSerializer
from rest_framework.response import Response
from rest_framework import status
from complaint_app import models
# Create your views here.

def getUserDistrict(dist):
    if int(dist) < 10:
        return f'0{dist}'
    else:
        return dist

class ComplaintViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    # serializer_class = ComplaintSerializer
    # queryset = Complaint.objects.all()

    def get_queryset(self):
        user = self.request.user
        user_profile = user.UserProfile
        user_district = user_profile.district
        return Complaint.objects.filter(council_dist__endswith=user_district)


    # def list(self, request):
    #     # Get all complaints from the user's district
    #     user = self.request.user
    #     user_profile = user.userprofile
    #     user_district = getUserDistrict(user_profile.district)
    #     complaints = self.queryset.filter(account__endswith=user_district)
    #     serializer_instance = self.serializer_class(complaints, many=True)
    #
    #     return Response(serializer_instance.data, status=status.HTTP_200_OK)


class OpenCasesViewSet(viewsets.ModelViewSet):
  http_method_names = ['get']
  # openCases = models.Complaint.objects.all()
  def list(self, request):
    # Get only the open complaints from the user's district
    return Response()

class ClosedCasesViewSet(viewsets.ModelViewSet):
  http_method_names = ['get']
  def list(self, request):
    # Get only complaints that are close from the user's district
    return Response()

class TopComplaintTypeViewSet(viewsets.ModelViewSet):
  http_method_names = ['get']
  def list(self, request):
    # Get the top 3 complaint types from the user's district
    return Response()
