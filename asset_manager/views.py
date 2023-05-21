from django.shortcuts import render, get_object_or_404
from .models import Counter, Asset, Income, Outcome
from django.shortcuts import render, redirect


def index(request):
    assets, total_assets = get_total_assets()
    incomes, total_income = get_total_income()
    outcomes, total_outcome = get_total_outcome()

    context = {'assets_total_value': total_assets, 'incomes_total_value': total_income, 'outcomes_total_value': total_outcome}
    return render(request, 'main/index.html', context)


def asset(request):
    assets, total_value = get_total_assets()

    print(assets)
    return render(request, 'main/asset.html', {'assets': assets, 'total_value': total_value})


def get_total_assets():
    assets = Asset.objects.all()
    total_value = 0
    for asset in assets:
        total_value += asset.value
    return assets, total_value


def delete_asset(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    asset.delete()
    return redirect('asset')


def add_asset(request):
    if request.method == 'POST':
        name = request.POST['name']
        value = request.POST['value']
        asset = Asset.objects.create(name=name, value=value)
        asset.save()
        return redirect('asset')
    return render(request, 'main/asset.html')


def income(request):
    incomes, total_value = get_total_income()

    return render(request, 'main/income.html', {'incomes': incomes, 'total_value': total_value})


def get_total_income():
    incomes = Income.objects.all()
    total_value = 0
    for income in incomes:
        total_value += income.value
    return incomes, total_value


def delete_income(request, income_id):
    income = Income.objects.get(id=income_id)
    income.delete()
    return redirect('income')


def add_income(request):
    if request.method == 'POST':
        name = request.POST['name']
        value = request.POST['value']
        income = Income.objects.create(name=name, value=value)
        income.save()
        return redirect('income')
    return render(request, 'main/income.html')


def outcome(request):
    outcomes, total_value = get_total_outcome()

    return render(request, 'main/outcome.html', {'outcomes': outcomes, 'total_value': total_value})


def get_total_outcome():
    outcomes = Outcome.objects.all()
    total_value = 0
    for outcome in outcomes:
        total_value += outcome.value
    return outcomes, total_value


def delete_outcome(request, outcome_id):
    outcome = Outcome.objects.get(id=outcome_id)
    outcome.delete()
    return redirect('outcome')


def add_outcome(request):
    if request.method == 'POST':
        name = request.POST['name']
        value = request.POST['value']
        outcome = Outcome.objects.create(name=name, value=value)
        outcome.save()
        return redirect('outcome')
    return render(request, 'main/outcome.html')

