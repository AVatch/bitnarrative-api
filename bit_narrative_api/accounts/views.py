from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import Account
from accounts.serializers import AccountSerializer
from bits.models import Bit
from bits.serializers import BitSerializer


class AccountList(generics.ListCreateAPIView):
    """
    URL: /api/v1/accounts/
    Methods: GET, POST
    Returns: List of accounts
    """
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
    """
    URL: /api/v1/account/<pk>/
    Methods: GET, PUT, DELETE
    Returns: Handle an individual account object
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class AccountBits(generics.ListAPIView):
    """
    URL: /api/v1/account/<pk>/bits/
    Methods: GET
    Returns: List of bits associated with the account
    """
    serializer_class = BitSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = get_object_or_404(Account, pk=self.kwargs['pk'])
        return Bit.objects.filter(accounts=user)


class MeDetail(APIView):
    """
    URL: /api/v1/me/
    Methods: GET
    Returns: Account object of the authenticated user making the request.
    """
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        me = request.user
        serializer = AccountSerializer(me, context={'request': request})
        return Response(serializer.data)
