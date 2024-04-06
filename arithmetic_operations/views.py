from django.shortcuts import render
from .helper_functions import HelperClass


# Create your views here.
def index(request, *args, **kwargs):

    if request.method == 'GET':
        return render(request, "index.html")

    elif request.method == 'POST':

        request_post = request.POST
        if 'expression' not in request_post:
            result = {
                'success': False,
                'value': 'Expression not supplied in.'
            }
            return render(request, "index.html", context=result)

        str_input = request_post.get('expression', None)

        cls_instance = HelperClass()
        validity_response = cls_instance.__call__(str_input)

        if validity_response['success']:
            validity_response['expression_sent'] = str_input
            return render(request, "index.html", context=validity_response)
        else:
            result = {
                'success': False,
                'message': validity_response['message'],
                'expression_sent': str_input
            }
            return render(request, "index.html", context=result)
