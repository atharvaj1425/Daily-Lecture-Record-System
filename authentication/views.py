from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.urls import reverse
from authentication.models import *
import re

# Create your views here.
def home(request):
    return render(request, "authentication/signin.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = auth.authenticate(username=username, password=pass1)  
        #lectures = LectureRecord.objects.filter(instructer_id=request.user.UniqueId)
        if user is not None:
            auth.login(request, user)
            fname = user.first_name
            messages.success(request, "success", extra_tags='success') 
            return redirect('dynamic_page')
            # if user.groups.filter(name='HOD').exists():
            #     return redirect('hoddash')
            # elif user.groups.filter(name='Admin').exists():
            #     return redirect('admindash')
            # elif user.groups.filter(name='Faculty').exists():
            #     return redirect('facultydash')
            #elif user.groups.filter(name='Executive').exists():
                #return render(request,'executive_dashboard')
        else:
            messages.error(request, "Invalid Cerds", extra_tags='error')
            return render(request, "authentication/signin.html")

    return render(request, "authentication/signin.html")

def dynamic_page(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    lectures = LectureRecord.objects.filter(instructer_id=request.user.UniqueId)
    #context = {'user_groups': user_groups}
    return render(request, "authentication/dynamic_page.html", {'lectures': lectures, 'user_groups': user_groups}) 

def hod(request):
    lectures = LectureRecord.objects.filter(instructer_id=request.user.UniqueId)
    return render(request, "authentication/hoddash.html", {'lectures': lectures}) 

def admin(request):
    lectures = LectureRecord.objects.filter(instructer_id=request.user.UniqueId)
    return render(request, "authentication/admin.html", {'lectures': lectures}) 

def faculty(request):
    lectures = LectureRecord.objects.filter(instructer_id=request.user.UniqueId)
    return render(request, "authentication/index.html", {'lectures': lectures}) 

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully", extra_tags='success')
    return redirect('home')

def dlr(request):
    timetable = LectureRecord.objects.filter(instructer_id=request.user.UniqueId)
    return render(request, "authentication/dlr.html", {'timetable': timetable})

def admin_dlr(request):
    timetable = LectureRecord.objects.filter(instructer_id=request.user.UniqueId)
    return render(request, "authentication/admin_dlr.html", {'timetable': timetable})

def dlr_history(request):
    history = FormData.objects.filter(instructer_id=request.user.UniqueId)
    return render(request, "authentication/dlr_history.html", {'history': history})

# def view_dlr(request):
#     if request.method == 'POST':
#         date = request.POST.get('date')
#         section = request.POST.get('section')
#     record = FormData.objects.filter(date=date, section=section)
#     return render(request, "authentication/dlr_report.html", {'record': record})

def view_dlr(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        section = request.POST.get('section')
        #records = get_object_or_404(FormData, date=date, section=section)
        records = FormData.objects.filter(date=date, section=section)
        
        # Regular expression pattern to match user IDs
        user_id_pattern = r'\bITF\d{1,10}\b'  # Matches "ITF" followed by 1 to 10 digits

        # List to hold records with remarks containing user IDs of other users
        records_with_other_user_ids = []

        # Check remarks of each record
        for record in records:
            if re.search(user_id_pattern, record.remarks):
                records_with_other_user_ids.append(record)
        return render(request, "authentication/dlr_report.html", {'records': records, 'records_with_other_user_ids': records_with_other_user_ids})
    else:
        messages.error(request, 'Record not found!!', extra_tags='record_not_found')
        redirect('dynamic_page')

def faculty_tt(request):
    if request.method == 'POST':
        instructor_id = request.POST.get('Instructor_ID')
    lectures = LectureRecord.objects.filter(instructer_id=instructor_id)
    return render(request, "authentication/faculty_tt_admin.html", {'lectures': lectures})

def testdlr_detail(request, dlr_id):
    dlr_data = get_object_or_404(LectureRecord, lr_id=dlr_id)
    # Logic to fetch and display details of a specific product
    return render(request, "authentication/form.html", {'data': dlr_data})

def updatedlr_detail(request, dlr_id):
    dlr_data = get_object_or_404(FormData, fd_id_id=dlr_id)
    #dlr_data = FormData.objects.filter(id=dlr_id)
    # Logic to fetch and display details of a specific product
    return render(request, "authentication/update_dlr_form.html", {'data': dlr_data})

def save_form_data(request, fd_id):
    if request.method == 'POST':
        section = request.POST.get('section')
        course_number = request.POST.get('course_number')
        course_name = request.POST.get('course_name')
        time = request.POST.get('time')
        day = request.POST.get('day')
        date = request.POST.get('date')
        instructer_id = request.POST.get('instructer_id')
        instructer_name = request.POST.get('instructer_name')
        assignment_given = request.POST.get('assignment_given')
        assignment_collected = request.POST.get('assignment_collected')
        assignment_distributed = request.POST.get('assignment_distributed')
        remarks = request.POST.get('remarks')

        # Check if there's an existing form data for the given date and fd_id_id
        existing_data = FormData.objects.filter(date=date, fd_id_id=fd_id).first()

        if existing_data:
            # If existing data found, return a response indicating form already exists
            #return HttpResponse('Form already exists')
            messages.error(request, 'Form already exists.', extra_tags='form_error')
            return redirect('/dlr')
        else:
            # No existing data found, proceed to save the form data
            form_data = FormData.objects.create(
                section=section,
                course_number=course_number,
                course_name=course_name,
                time=time,
                day=day,
                date=date,
                instructer_id=instructer_id,
                instructer_name=instructer_name,
                assignment_given=assignment_given,
                assignment_collected=assignment_collected,
                assignment_distributed=assignment_distributed,
                remarks=remarks,
                fd_id_id=fd_id
            )
        
            # Respond with success message
            #return HttpResponse('Data Inserted')
            messages.success(request, 'Form data inserted successfully.', extra_tags='form_success')
            return redirect('/dlr')
    else:
        # Handle GET request (if needed)
        return render(request, "authentication/form.html")
    
def update_form_data(request, fd_id):
    form_data = get_object_or_404(FormData, fd_id_id=fd_id)
    #url_id = reverse()
    #form_data = FormData.objects.filter(fd_id_id=fd_id)
    

    if request.method == 'POST':
        # Retrieve form data
        section = request.POST.get('section')
        course_number = request.POST.get('course_number')
        course_name = request.POST.get('course_name')
        time = request.POST.get('time')
        day = request.POST.get('day')
        date = request.POST.get('date')
        instructer_id = request.POST.get('instructer_id')
        instructer_name = request.POST.get('instructer_name')
        assignment_given = request.POST.get('assignment_given')
        assignment_collected = request.POST.get('assignment_collected')
        assignment_distributed = request.POST.get('assignment_distributed')
        remarks = request.POST.get('remarks')


        # Update the existing FormData object
        form_data.section = section
        form_data.course_number = course_number
        form_data.course_name = course_name
        form_data.time = time
        form_data.day = day
        form_data.date = date
        form_data.instructer_id = instructer_id
        form_data.instructer_name = instructer_name
        form_data.assignment_given = assignment_given
        form_data.assignment_collected = assignment_collected
        form_data.assignment_distributed = assignment_distributed
        form_data.remarks = remarks

        form_data.save()

        # Redirect to a success page or another view
        #return HttpResponse('update')  # Change 'success_page' to your actual URL name
        messages.success(request, 'Form updated successfully.', extra_tags='form_update')
        return redirect('/dlr')
    else:
        messages.error(request, 'Form not entered.', extra_tags='form_noentry')
        return redirect('/dlr')


    # If it's not a POST request, render the update form page
    #return render(request, "authentication/update_form_page.html", {'form_data': form_data})
    return render(request, "authentication/update_dlr_form.html")



# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from io import BytesIO
# from django.views import View


# def render_to_pdf(template_src, context_dict={}):
# 	template = get_template(template_src)
# 	html  = template.render(context_dict)
# 	result = BytesIO()
# 	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
# 	if not pdf.err:
# 		return HttpResponse(result.getvalue(), content_type='application/pdf')
# 	return None


# data = FormData.objects.all()
# context={'data' : data}

# #Opens up page as PDF
# class ViewPDF(View):
# 	def get(self, request, *args, **kwargs):

# 		pdf = render_to_pdf('authentication/dlr_report.html', context)
# 		return HttpResponse(pdf, content_type='application/pdf')


# #Automaticly downloads to PDF file
# class DownloadPDF(View):
# 	def get(self, request, *args, **kwargs):
	
# 		pdf = render_to_pdf('authentication/dlr_report.html', context)

# 		response = HttpResponse(pdf, content_type='application/pdf')
# 		filename = "Invoice_%s.pdf" %("12341231")
# 		content = "attachment; filename='%s'" %(filename)
# 		response['Content-Disposition'] = content
# 		return response


#from django.http import HttpResponse
#from django.template.loader import render_to_string
#from weasyprint import HTML
#from .models import FormData  # Import your FormData model

#def generate_pdf(request):
    # Fetch data from the FormData model
#    form_data = FormData.objects.all()  # Adjust this query as per your requirement

    # Render the HTML content dynamically using the 'dlr_report.html' template
#    html_content = render_to_string('dlr_report.html', {'form_data': form_data})

    # Convert HTML to PDF using weasyprint
#     pdf_file = HTML(string=html_content).write_pdf()

    # Serve the PDF file as a response
#    response = HttpResponse(pdf_file, content_type='application/pdf')
#    response['Content-Disposition'] = 'attachment; filename="dlr_report.pdf"'
#    return response



# def signup(request):
    # if request.method == "POST":
    #     username = request.POST['username'] 
    #     fname = request.POST['fname']
    #     lname = request.POST['lname']
    #     email = request.POST['email']
    #     pass1 = request.POST['pass1']
    #     pass2 = request.POST['pass2']
    #     if User.objects.filter(username=username).exists():
    #         messages.error(request, "Username already exists, try another username!")
    #         return redirect('home')
    #     if User.objects.filter(email=email):
    #         messages.error(request, "Email already registered, try another email!")
    #         return redirect('home')
    #     if len(username)>10:
    #         messages.error(request, "Username exceeds the limit of 10 characters")
    #     if pass1 != pass2:
    #         messages.error(request, "Passwords didn't match")
    #     if not username.isalnum():
    #         messages.error(request, "Username should be alpha numeric")   
    #         return redirect('home')
    #     myuser = User.objects.create_user(username, email, pass1)
    #     myuser.first_name = fname 
    #     myuser.last_name = lname
    #     myuser.save()

    #     messages.success(request, "Your account has been successfully created!!!")
        
    # return render(request, "authentication/signup.html")


