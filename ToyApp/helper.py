
from rest_framework.response import Response
class GetallObjectsMixin:
    model = None
    serializer = None
    def get(self, request, format=None):
        alldata = self.model.objects.all()
        serializer = self.serializer(alldata, many=True)
        return Response(serializer.data)

