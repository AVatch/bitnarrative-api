from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions

from accounts.models import Account
from content.models import Content
from bits.models import Bit
from bits.serializers import BitSerializer


class BitList(generics.ListCreateAPIView):
    queryset = Bit.objects.all()
    serializer_class = BitSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        b = serializer.save()
        b.accounts.add(user)


class AccountBitList(generics.ListAPIView):
    serializer_class = BitSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        Returns the bits of a user
        """
        user = get_object_or_404(Account, pk=self.kwargs['pk'])
        return Bit.objects.filter(accounts=user)


class ContentBitList(generics.ListAPIView):
    serializer_class = BitSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        Returns the bits of a user
        """
        content = get_object_or_404(Content, pk=self.kwargs['pk'])
        bits = content.bits.filter(content=content).order_by('-view_count')
        return bits


class ContentTopBitList(generics.ListAPIView):
    serializer_class = BitSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        Returns the top bits of a content
        """
        content = get_object_or_404(Content, pk=self.kwargs['pk'])
        bits = content.bits.order_by('-view_count')[:3]
        return bits


class BitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bit.objects.all()
    serializer_class = BitSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_update(self, serializer):
        user = self.request.user
        b = serializer.save()
        b.accounts.add(user)
