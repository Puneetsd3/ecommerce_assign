from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CartSerializer, OrderSerializer, DiscountCodeSerializer
from .models import cart_store, order_store, discount_code_store  # Import global variables

@api_view(['POST'])
def add_to_cart(request, user_id):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        item_data = serializer.validated_data
        cart_store.add_item(user_id, item_data)  # Use the global cart_store
        return Response(cart_store.get_cart(user_id), status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_cart(request, user_id):
    return Response(cart_store.get_cart(user_id), status=status.HTTP_200_OK)

@api_view(['POST'])
def checkout(request, user_id):
    items = cart_store.get_cart(user_id)
    if not items:
        return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

    total_amount = sum(item['price'] for item in items)
    
    discount_code = request.data.get('discount_code')
    
    if discount_code and discount_code_store.use_code(discount_code):
        total_amount *= 0.9  # Apply 10% discount
    
    order = order_store.create_order(user_id=user_id, total_amount=total_amount, items=items)
    
    cart_store.clear_cart(user_id)  # Clear cart after checkout
    
    return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def generate_discount(request):
    order_count = len(order_store.orders)
    
    if order_count % 5 == 0:
        discount_code_store.generate_code(order_count)
        code = list(discount_code_store.codes.keys())[-1]
        return Response(DiscountCodeSerializer({'code': code}).data, status=status.HTTP_201_CREATED)
    
    return Response({"message": "No discount generated"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def admin_stats(request):
    total_purchases = len(order_store.orders)
    total_amount = sum(order['total_amount'] for order in order_store.orders)
    
    used_discount_codes = [code for code, used in discount_code_store.codes.items() if used]
    
    return Response({
        'total_purchases': total_purchases,
        'total_amount': total_amount,
        'discount_codes': used_discount_codes,
        'total_discounted_amount': sum(order['total_amount'] * 0.1 for order in order_store.orders if order['total_amount'] < sum(item['price'] for item in order['items']))
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def index(request):
    """Render the index page."""
    return render(request, 'index.html')
