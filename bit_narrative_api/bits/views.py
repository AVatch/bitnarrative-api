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


class BitList(generics.ListCreateAPIView):
    """
    URL: /api/v1/bit/
    Methods: GET, POST
    Returns: List all bits or create a new one
    """
    queryset = Bit.objects.all()
    serializer_class = BitSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        b = serializer.save()
        b.accounts.add(user)


class BitDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    URL: /api/v1/bit/<pk>/
    Methods: GET, PUT, DELETE
    Returns: Manage bit object
    """
    queryset = Bit.objects.all()
    serializer_class = BitSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_update(self, serializer):
        user = self.request.user
        b = serializer.save()
        b.accounts.add(user)


class BitAccounts(generics.ListAPIView):
    """
    URL: /api/v1/bit/<pk>/accounts/
    Methods: GET
    Returns: List of accounts associated with bit
    """
    serializer_class = AccountSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        bit = get_object_or_404(Bit, pk=self.kwargs['pk'])
        return Account.objects.filter(bits=bit)


class BitRating(APIView):
    """
    URL: /api/v1/bit/<pk>/rate/<rating_type>/
    Methods: POST
    Returns: Rate a bit. An account can only rate a bit once.
    """
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, pk, rating_type, format=None):
        bit = Bit.objects.get(pk=pk)

        if request.user not in bit.accounts.all():
            bit.accounts.add(request.user)
            bit.view_count += 1
            if rating_type == "up":
                bit.up_count += 1
            elif rating_type == "down":
                bit.down_count += 1
            else:
                return Response({'status': 'Bad Request',
                                 'message': 'Invalid rating type'
                                 }, status=status.HTTP_400_BAD_REQUEST)
            bit.save()
            return Response({'status': 'Ok',
                             'message': 'Bit rated.'
                             }, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'Bad Request',
                             'message': 'Account already rated bit.'
                             }, status=status.HTTP_400_BAD_REQUEST)
