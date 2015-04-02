from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Account
from .serializers import AccountSerializer
from bits.models import Bit
from bits.serializers import BitSerializer
from community.models import Community
from community.serializers import CommunitySerializer


class AccountList(generics.ListAPIView):
    """
    URL: /api/v1/accounts/
    Methods: GET
    Returns: List of accounts
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class AccountCreate(generics.CreateAPIView):
    """
    URL: /api/v1/accounts/create/
    Methods: POST
    Returns: Creates an account
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


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


class AccountCommunities(generics.ListAPIView):
    """
    URL: /api/v1/account/<pk>/communities/
    Methods: GET
    Returns: List of communities associated with the account
    """
    serializer_class = CommunitySerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = get_object_or_404(Account, pk=self.kwargs['pk'])
        return Community.objects.filter(accounts=user)


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
