from django.shortcuts import render
from .forms import ParcelQuoteForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ParcelQuote
from .serializers import ParcelQuoteSerializer
from rest_framework.renderers import JSONRenderer

def quote_me(request):
    if request.method == 'POST':
        form = ParcelQuoteForm(request.POST)
        if form.is_valid():
            quote = form.save()
            return render(request, 'quote/result.html', {'quote': quote})
        else:
            print("Form errors:", form.errors)  # 🔍 Add this line to debug
    else:
        form = ParcelQuoteForm()
    return render(request, 'quote/quote_form.html', {'form': form})



@api_view(['GET'])
def get_parcel_quotes(request):
    quotes = ParcelQuote.objects.all()
    serializer = ParcelQuoteSerializer(quotes, many=True)
    return Response(serializer.data)



