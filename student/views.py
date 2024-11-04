from django.shortcuts import render, get_object_or_404,redirect
from .models import*
from django.contrib import messages
from .forms import StudentForm


# Create your views here.
def add_student(request):
    #form handling
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
     
            first_name =request.POST.get('first_name')
            last_name =request.POST.get('last_name')
            student_id =request.POST.get('student_id')
            gender =request.POST.get('gender')
            date_of_birth =request.POST.get('date_of_birth')
            student_class =request.POST.get('student_class')
            religion =request.POST.get('religion')
            joining_date =request.POST.get('joining_date')
            mobile_number =request.POST.get('mobile_number')
            admission_number=request.POST.get('admission_number')
            section =request.POST.get('section')
            student_image =request.FILES.get('student_image')
            
            
            #retriving parents data
            father_name =request.POST.get('father_name')
            father_occupation=request.POST.get('father_occupation')
            father_mobile =request.POST.get('father_mobile')
            father_email =request.POST.get('father_email')
            mother_name =request.POST.get('mother_name')
            mother_occupation =request.POST.get('mother_occupation')
            mother_mobile =request.POST.get('mother_mobile')
            mother_email =request.POST.get('mother_email')
            present_address =request.POST.get('present_address')
            permanent_address =request.POST.get('permanent_address')
            
            #save parent info -parent instance
            parent_instance = Parent.objects.create(
                father_name=father_name,
                father_occupation=father_occupation,
                father_mobile=father_mobile,
                father_email=father_email,
                mother_name=mother_name,
                mother_occupation=mother_occupation,
                mother_mobile=mother_mobile,
                mother_email=mother_email,
                present_address=present_address,
                permanent_address=permanent_address,
                
                
            )
            student = form.save(commit=False)
            student.parent = parent_instance
            student.save()
            
            messages.success(request, "Student added successfully")
            return redirect("student_list")
        else:
            print(form.errors)
    else:
        form = StudentForm()

    return render(request, "students/add-student.html", {'form': form})
            #save student info
    #         student = Student.objects.create(
    #             first_name=first_name,
    #             last_name=last_name,
    #             student_id=student_id,
    #             gender=gender,
    #             date_of_birth=date_of_birth,
    #             student_class=student_class,
    #             religion=religion,
    #             joining_date=joining_date,
    #             mobile_number=mobile_number,
    #             admission_number=admission_number,
    #             section=section,
    #             student_image=student_image,
    #             parent=parent_instance
                
    #         )
    #         messages.success(request,"student added successfully")
    #         return redirect("student_list")
    # else:
    #     form = StudentForm()
          
    # return render(request,"students/add-student.html", {'form': form})

def student_list(request):
    return rendering(request,"students/students.html")

def edit_student(request):
    return render(request,"students/edit-student.html")
def view_student(request):
    return render(request,"students/student-details.html")


