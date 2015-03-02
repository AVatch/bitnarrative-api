from rest_framework import generics, status
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data,
                            status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad Request',
            'message': 'Account could not be created with received data.'
          }, status=status.HTTP_400_BAD_REQUEST)


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class AccountBits(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class MeDetail(APIView):
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        me = request.user
        serializer = AccountSerializer(me, context={'request': request})
        return Response(serializer.data)
