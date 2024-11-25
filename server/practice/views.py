from django.shortcuts import render

def dashboard(request):
    return render(request, 'practice/dashboard.html')

def categories(request):
    return render(request, 'categories.html')

def products(request):
    return render(request, 'products.html')

# def tables(request):
#     return render(request, 'tables.html')

def staff(request):
    return render(request, 'staff.html')

def pos(request):
    return render(request, 'practice/pos.html')

def kitchen(request):
    return render(request, 'kitchen.html')

def reports(request):
    return render(request, 'reports.html')

def settings(request):
    return render(request, 'settings.html')

def logout_view(request):
    # Add logout functionality here
    return render(request, 'logout.html')
