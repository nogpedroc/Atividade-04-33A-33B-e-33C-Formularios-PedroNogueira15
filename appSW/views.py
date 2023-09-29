from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import  SequelsPros, Chapters, TableInfo
from .forms import chaptersForm, sequelsProsForm

@login_required
def homePage(request):
  sequelsPros = SequelsPros.objects.all()
  chapters = Chapters.objects.all()
  tableInfo = TableInfo.objects.all()
  return render(request, "homePage.html", context={'sequelsPros':sequelsPros,'chapters':chapters,'tableInfo':tableInfo})

@login_required
def sequelsProsPage(request):
  sequelsPros = SequelsPros.objects.all()
  return render(request, "sequelsPros.html", context={'sequelsPros':sequelsPros})

@login_required
def chaptersPage(request):
  chapters = Chapters.objects.all()
  return render(request, "chapters.html", context={'chapters':chapters})

@login_required
def add_sequelsPros(request):
  if request.method == 'GET':
    form = sequelsProsForm()
    return render(request, "sequelsProsForm.html", context={'form':form,'action':'Adicionar'})
  elif request.method == 'POST':
    form = sequelsProsForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('sequelsProsPage')
    return render(request, "sequelsProsForm.html", context={'form':form,'action':'Adicionar'})

@login_required
def add_chapters(request):
  if request.method == 'GET':
    form = chaptersForm()
    return render(request, "chaptersForm.html", context={'form':form,'action':'Adicionar'})
  elif request.method == 'POST':
    form = chaptersForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('chaptersPage')
    return render(request, "chaptersForm.html", context={'form':form,'action':'Adicionar'})

@login_required
def update_sequelsPros(request, sequelsPros_id):
  if request.method == 'GET':
    sequelsPros = SequelsPros.objects.all()
    sequelsPro = SequelsPros.objects.filter(id=sequelsPros_id).first()
    form = sequelsProsForm(instance=sequelsPro)
    return render(request, "sequelsProsForm.html", context={'form':form,'sequelsPros':sequelsPros,'action':'Atualizar'})
  elif request.method == 'POST':
    sequelsPro = SequelsPros.objects.filter(id=sequelsPros_id).first()
    form = sequelsProsForm(request.POST, instance=sequelsPro)
    if form.is_valid():
      form.save()
      return redirect('sequelsProsPage')
    return render(request, "sequelsProsForm.html", context={'form':form,'sequelsPros':sequelsPros,'action':'Atualizar'})

@login_required
def update_chapters(request, chapters_id):
  if request.method == 'GET':
    chapters = Chapters.objects.all()
    chapter = Chapters.objects.filter(id=chapters_id).first()
    form = chaptersForm(instance=chapter)
    return render(request, "chaptersForm.html", context={'form':form,'chapters':chapters,'action':'Atualizar'})
  elif request.method == 'POST':
    chapter = Chapters.objects.filter(id=chapters_id).first()
    form = chaptersForm(request.POST, instance=chapter)
    if form.is_valid():
      form.save()
      return redirect('chaptersPage')
    return render(request, "chaptersForm.html", context={'form':form,'chapters':chapters,'action':'Atualizar'})

@login_required
def delete_sequelsPros(request, sequelsPros_id):
  sequelsPro = SequelsPros.objects.filter(id=sequelsPros_id).first()
  if request.method == 'POST':
    if 'Y' in request.POST:
      sequelsPro.delete()
    return redirect('sequelsProsPage')
  return render(request, 'del_sequelsPros.html', context={'sequelsPro':sequelsPro})

@login_required
def delete_chapters(request, chapters_id):
  chapter = Chapters.objects.filter(id=chapters_id).first()
  if request.method == 'POST':
    if 'Y' in request.POST:
      chapter.delete()
    return redirect('chaptersPage')
  return render(request, 'del_chapters.html', context={'chapter':chapter})

def register_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
        request.POST['username'], 
        request.POST['email'], 
        request.POST['password']
    )
    user.save()
    return(redirect('homePage'))
  return render(request, 'register.html', context={"action":"Adicionar"})

def confirm_logout(request):
  if request.method == "POST":
    if 'Y' in request.POST:
      return(redirect('logout_user'))
    return redirect('homePage')
  return render(request, 'logout.html')

def logout_user(request):
  logout(request)
  return redirect('/accounts/login/')