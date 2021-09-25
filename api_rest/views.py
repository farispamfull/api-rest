from django.http import JsonResponse


def error_404(request, exception):
    massage = 'This endpoint is not found'
    response = JsonResponse(data={'message': massage, 'status_code': 404})
    response.status_code = 404
    return response


def error_500(request):
    massage = 'Something went wrong'
    response = JsonResponse(data={'message': massage, 'status_code': 500})
    response.status_code = 500
    return response
