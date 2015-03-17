from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(('GET',))
@authentication_classes((SessionAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def api_root(request, format=None):
    return Response({
        'me': reverse('me-detail', request=request, format=format),
        # 'me-bits': reverse('me-bit-detail', request=request, format=format),
        'accounts': reverse('account-list', request=request, format=format),
        'content': reverse('content-list', request=request, format=format),
        'content parse': reverse('content-parse', request=request, format=format),
        'bit': reverse('bit-list', request=request, format=format),
    })
