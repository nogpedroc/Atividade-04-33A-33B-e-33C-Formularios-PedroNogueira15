from django.shortcuts import render, redirect
from .models import  SequelsPros, Chapters, TableInfo
from .forms import chaptersForm, sequelsProsForm

def homePage(request):
  sequelsPros = SequelsPros.objects.all()
  chapters = Chapters.objects.all()
  tableInfo = TableInfo.objects.all()
  return render(request, "homePage.html", context={'sequelsPros':sequelsPros,'chapters':chapters,'tableInfo':tableInfo})

def sequelsProsPage(request):
  sequelsPros = SequelsPros.objects.all()
  return render(request, "sequelsPros.html", context={'sequelsPros':sequelsPros})

def chaptersPage(request):
  chapters = Chapters.objects.all()
  return render(request, "chapters.html", context={'chapters':chapters})

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

def delete_sequelsPros(request, sequelsPros_id):
  sequelsPro = SequelsPros.objects.filter(id=sequelsPros_id).first()
  if request.method == 'POST':
    if 'Y' in request.POST:
      sequelsPro.delete()
    return redirect('sequelsProsPage')
  return render(request, 'del_sequelsPros.html', context={'sequelsPro':sequelsPro})

def delete_chapters(request, chapters_id):
  chapter = Chapters.objects.filter(id=chapters_id).first()
  if request.method == 'POST':
    if 'Y' in request.POST:
      chapter.delete()
    return redirect('chaptersPage')
  return render(request, 'del_chapters.html', context={'chapter':chapter})