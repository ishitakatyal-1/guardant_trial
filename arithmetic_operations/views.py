from django.shortcuts import render
from .helper_functions import AuxillaryFunctions


# Create your views here.
def index(request):

    if request.method == "GET":    
        request_payload = request.GET

        str_input = ''

        cls_instance = AuxillaryFunctions()
        validity_response = cls_instance.__call__(str_input)

        if validity_response['success']:
            return validity_response
        else:
            result = {
                'success': False,
                'value': validity_response['error_message']
            }

        data = { 'result': result}

        return render(request, 'index.html', context=data)
