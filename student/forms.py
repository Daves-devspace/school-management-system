from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name', 'student_id', 'gender', 
            'date_of_birth', 'student_class', 'religion', 
            'joining_date', 'mobile_number', 'admission_number', 
            'section', 'student_image'
        ]