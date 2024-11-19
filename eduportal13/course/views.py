from django.shortcuts import render
from datetime import datetime

# Create your views here.

def learn_django(request):
    return render(request , 'course/courseone.html' ,{'nm' : 'Django'})
    
'''  data =  {
       'stu1' : {'name' : 'Rahul' , 'roll' : 108},
        'stu2' : {'name' : 'Sohil' , 'roll' : 103},
        'stu3' : {'name' : 'Soham' , 'roll' : 105},
        'stu4' : {'name' : 'Rohan' , 'roll' : 107},
    }
    
    return render(request , 'course/courseone.html' , {'data' : data})'''
   
   
   # data = {'name' : 'Rahul' , 'roll' : 108}
    # return render(request , 'course/courseone.html' , {'data' : data})
    
    
'''    stu = {
       'stu1' : {'name' : 'Rahul' , 'roll' : 108},
        'stu2' : {'name' : 'Sohil' , 'roll' : 103},
        'stu3' : {'name' : 'Soham' , 'roll' : 105},
        'stu4' : {'name' : 'Rohan' , 'roll' : 107},
    }
    
    student = {'student' : stu}
    return render(request , 'course/courseone.html' , student) '''
    
    
    # return render(request , 'course/courseone.html')
    
   # student = {'name' : ['Rahul' , 'Soham' , 'Raj' , 'Anu']}
   # return render(request , 'course/courseone.html' , student)
    
    #return render(request , 'course/courseone.html' , {'nm' : 'Django'})
    
    # return render(request , 'course/courseone.html' , {'nm':'Django' , 'st':8})
    
   # return render(request , 'course/courseone.html' , {'nm' : True})
   # return render(request , 'course/courseone.html' , {'nm' : False})
    
   # return render(request , 'course/courseone.html' , {'p1': 56.24321 , 'p2' : 56.00000 , 'p3' : 56.37000})
    
    
    # d = datetime.now()
    # return render(request , 'course/courseone.html' , {'dt' : d})
    
      # return render(request , 'course/courseone.html' , {'nm' : 'Django is Awsome ... '})



  # cname = 'Django'
  # duration = '4 Months'
  # seats = 8
  # django_details = {'nm' : cname , 'du' : duration , 'st' : seats}
   # return render(request , 'course/courseone.html' , context = django_details)