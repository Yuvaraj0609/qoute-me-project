from django.shortcuts import render
from .forms import ParcelQuoteForm

def quote_me(request):
    if request.method == 'POST':
        form = ParcelQuoteForm(request.POST)
        if form.is_valid():
            # Do calculation or API call here
            quote = form.save()
            return render(request, 'quote/result.html', {'quote': quote})
    else:
        form = ParcelQuoteForm()
    return render(request, 'quote/quote_form.html', {'form': form})


