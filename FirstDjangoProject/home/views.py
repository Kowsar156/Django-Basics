from django.shortcuts import render
from django.http import HttpResponse
from home.forms import studentForm, infoForm
from home.models import student
from django.db import connection

def home(request):
    name = "Kowsar"
    email = "kowsarmahmud156@gmail.com"
    contact_list = []
    x = {"Name":"Shikhi", "Email":"shs@gmail.com"}
    contact_list.append(x)
    x = {"Name":"Payel", "Email":"sap@gmail.com"}
    contact_list.append(x)
    x = {"Name":"Farhan", "Email":"ft@gmail.com"}
    contact_list.append(x)
    return render(request, 'demo.html', {'Name': name, 'Email': email, 'Contacts': contact_list})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def StudentForm(request):
    if request.method == "POST":
        form = studentForm(request.POST)
        newStudent = form.save()
        return HttpResponse("<h1>Student added successfully</h1>")
    else:
        form = studentForm()
        return render(request, 'input.html', {'form': form})
    
def getInfo(request):
    if request.method == 'POST':
        form = infoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            targetStudent = student.objects.get(name=name)
            return render(request, 'infoViewer.html', {'targetStudent': targetStudent})
    else:
        form = infoForm()
        return render(request, 'studentInfo.html', {'form': form})

def getAllInfo(request):
    allStudents = student.objects.all()
    return render(request, 'allInfoViewer.html', {'students': allStudents})

def getUpdatedInfo(request):
    pupil = student.objects.get(pk=1)
    pupil.cls = 17
    pupil.save()
    all_students = student.objects.all()
    for s in all_students:
        s.cls = 17
        s.save()
    return render(request, 'allInfoViewer.html', {'students': all_students})

def getInfoBySQL(request):
    cursor = connection.cursor()
    sql = 'SELECT * FROM STUDENT'
    cursor.execute(sql)
    result = cursor.fetchall()
    allStudents = []
    for row in result:
        name = row[1]
        cls = row[2]
        roll = row[3]
        s = {'name': name, 'cls': cls, 'roll': roll}
        allStudents.append(s)
    return render(request, 'allInfoViewer.html', {'students': allStudents})