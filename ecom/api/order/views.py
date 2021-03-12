from rest_framework import viewsets
from django.http import JsonResponse
from .serialize import OrderSerializer
from .models import Order
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({"error" : "Please log-in", "code" : "500"})
    
    if request.method == "POST":
        user_id = id
        transaction_id = request.POST["transaction_id"]
        amount = request.POST["total_amount"]
        products = request.POST["products"]
        total_products = len(products.split(",")[:-1])

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return JsonResponse({"error" : "user does not exist"})

        ordr = Order(user=user, products=products, transaction_id=transaction_id, total_amount=amount, total_prodcuts=total_products)
        ordr.save()
        return JsonResponse({"success" : True, "error" : False, "msg" : "order placed successfully"})

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("id")
    serializer_class = OrderSerializer