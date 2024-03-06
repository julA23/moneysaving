import datetime
from django.shortcuts import render, redirect
from .models import Account, Transaction, Budget
from django.http import HttpResponseRedirect
from main.forms import TransactionForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Sum



@login_required(login_url='/login')
def dashboard(request):
    user = request.user
    transactions = Transaction.objects.filter(user=request.user)
    last_login_str = request.COOKIES.get('last_login')
    last_login_date = datetime.datetime.strptime(last_login_str, '%Y-%m-%d %H:%M:%S.%f')
    formatted_last_login = last_login_date.strftime('%d %B %Y')
    date_now = timezone.now().date()
    testing = date_now
    context = {
        'user': request.user.username,
        'account': 'account',
        'transactions': transactions,
        'budgets': 'budgets',
        'last_login': formatted_last_login,
        'date_now': date_now,
    }
    return render(request, 'main.html', context)

testing = timezone.now().date()

def switch_date(value):
    global testing  # Declare testing as a global variable
    if value == "tomorrow":
        testing = testing + timezone.timedelta(days=1)
    elif value == "yesterday":
        testing = testing - timezone.timedelta(days=1)
    elif value == "today":
        testing = timezone.now().date()

def edit_transaction(request, id):
    transaction = Transaction.objects.get(pk=id)

    form = TransactionForm(request.POST or None, instance= transaction)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:dashboard'))
    context = {'form':form}
    return render(request, "edit_transaction.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def remove_transaction(request, id):
    transaction = Transaction.objects.get(pk = id)
    transaction.delete()
    return HttpResponseRedirect(reverse('main:dashboard'))

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def create_transaction(request):
    form = TransactionForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        transaction = form.save(commit=False)
        transaction.user = request.user
        transaction.save()
        return HttpResponseRedirect(reverse('main:dashboard'))

    context = {'form': form}
    return render(request, "create_transaction.html", context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:dashboard")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def show_xml(request):
    data = Transaction.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Transaction.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Transaction.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Transaction.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_transaction_json_today(request):
    today = timezone.now().date()
    transaction_item = Transaction.objects.filter(timestamp__date=today, user=request.user)
    return HttpResponse(serializers.serialize('json', transaction_item))

def get_transaction_json_yesterday(request):
    switch_date("yesterday")
    yesterday = testing
    transaction_item = Transaction.objects.filter(timestamp__date=yesterday, user=request.user)
    return HttpResponse(serializers.serialize('json', transaction_item))

def get_transaction_json_tomorrow(request):
    switch_date("tomorrow")
    tomorrow = testing
    transaction_item = Transaction.objects.filter(timestamp__date=tomorrow, user=request.user)
    return HttpResponse(serializers.serialize('json', transaction_item))

def get_transaction_json_income(request):
    transaction_item = Transaction.objects.filter(timestamp__date=testing, user=request.user, category=Transaction.TRANSACTION_TYPES[0][1])
    return HttpResponse(serializers.serialize('json', transaction_item))

def get_transaction_json_expenses(request):
    transaction_item = Transaction.objects.filter(timestamp__date=testing, user=request.user, category=Transaction.TRANSACTION_TYPES[1][1])
    return HttpResponse(serializers.serialize('json', transaction_item))

def get_transaction_json_transfer(request):
    transaction_item = Transaction.objects.filter(timestamp__date=testing, user=request.user, category=Transaction.TRANSACTION_TYPES[2][1])
    return HttpResponse(serializers.serialize('json', transaction_item))

def get_transaction_json_all(request):
    transaction_item = Transaction.objects.filter(timestamp__date=testing, user=request.user)
    return HttpResponse(serializers.serialize('json', transaction_item))

def format_last_login(request):
    testing_str = testing.strftime('%Y-%m-%d')
    last_login_date = datetime.datetime.strptime(testing_str, '%Y-%m-%d')
    formatted_last_login = last_login_date.strftime('%d %B %Y')
    return JsonResponse({'formatted_last_login': formatted_last_login})

def format_today(request):
    today = timezone.now().date()
    switch_date("today")
    today_str = today.strftime('%Y-%m-%d')
    today_date = datetime.datetime.strptime(today_str, '%Y-%m-%d')
    formatted_today = today_date.strftime('%d %B %Y')
    return JsonResponse({'formatted_today': formatted_today})

def financial_report(request):
    # Filter transactions by type
    income = Transaction.objects.filter(timestamp__date=testing, user=request.user, category=Transaction.TRANSACTION_TYPES[0][1])
    expenses = Transaction.objects.filter(timestamp__date=testing, user=request.user, category=Transaction.TRANSACTION_TYPES[1][1])
    transfer = Transaction.objects.filter(timestamp__date=testing, user=request.user, category=Transaction.TRANSACTION_TYPES[2][1])

    # Calculate total amounts
    income_total = sum(transaction.amount for transaction in income) or 0
    expenses_total = sum(transaction.amount for transaction in expenses) or 0
    transfer_total = sum(transaction.amount for transaction in transfer) or 0

    return JsonResponse({
        'income_total': income_total,
        'expenses_total': expenses_total,
        'transfer_total': transfer_total,
    })



@csrf_exempt
def add_transaction_ajax(request):
    if request.method == 'POST':
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        transaction_type = request.POST.get("transaction_type")
        category = request.POST.get("category")
        user = request.user

        new_product = Transaction(amount=amount, description=description, transaction_type=transaction_type, category=category, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

