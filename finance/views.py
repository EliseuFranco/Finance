from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Register, Expenses


def sumSpent(cat):
    expense = Expenses.objects.all()
    registo = Register.objects.filter()
    total_spent = 0

    for data in registo:
        for user in expense:
            if ''.join(str(user.user).split()) == data.first_name + data.last_name and user.category not in ['Salário','Dividendo']:
                total_spent += user.expense_value
    
    return total_spent

def existUser(email):
    return Register.objects.filter(email=email).exists()

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        surname = request.POST.get('surname', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if not name or not surname or not email or not password:
            return render(request, 'register.html', {'error': 'Todos os campos são obrigatórios.'})

        if existUser(email):
            return render(request, 'register.html', {'error': 'Já existe um registo com esse email'})

        user = Register.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name,
            last_name=surname
        )
        user.save()
        return redirect('login')

    return render(request, 'Register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('expense')
        else:
            return render(request, 'login.html', {'error': "Credenciais inválidas"})

    return render(request, 'login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def expense(request):

    expenses = Expenses.objects.filter(user=request.user)
    salario = 0
 
    categories = ["Alimentação", "Lazer", "Desporto", "Jogos", "Casa", "Dividendo", "Salário"]
    categories.sort()
    
    if request.method == 'POST':
        descr = request.POST.get('descricao', '').strip()
        value = request.POST.get('valor', '').strip()
        cat = request.POST.get('categoria', '').strip()
        date = request.POST.get('date', '').strip()
        escolha = request.POST.get('escolha', '').strip()

        if descr and value and cat and date:
            try:
                value = float(value)
                
                new_expense = Expenses(
                    expense_name=descr,
                    expense_value=value,
                    category=cat,
                    date=date,
                    choose=escolha,
                    user=request.user
                )
                

                new_expense.save()

                expenses = Expenses.objects.filter(user=request.user)
                exp = sumSpent(cat)

                return render(request, 'expense.html', {"success": "Dados adicionados com sucesso.", "expense": expenses, 'categoria': categories, 'spend': exp,  'salario': salario})
            
            except ValueError:
                return render(request, 'expense.html', {"error": "Valor inválido.", 'expense': expenses, 'categoria': categories})
        else:
            return render(request, 'expense.html', {"error": "Todos os campos são obrigatórios.", 'expense': expenses, 'categoria': categories, 'salario': salario})

    exp = sumSpent("")
    return render(request, 'expense.html', {'expense': expenses, 'categoria': categories, 'spend': exp, 'salario': salario})
