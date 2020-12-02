from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from app1.models import Contact, ServiceEnq, CourseEnq

# Create your views here.

def AdminHome(reqest):
    return render(reqest, 'adminapp/adminhome.html')

# =========================contact us ============================
# Contact Us list view
@method_decorator(login_required, name='dispatch')
class ContactUsList(ListView):
    model = Contact
    template_name = 'adminapp/contactuslist.html'
    context_object_name = 'contactenq'


@login_required
def DeleteContactEnq(request, id):
    mydict = {'msg':'Enquiry Deleted'}
    item = Contact.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return HttpResponseRedirect("/contactenqlist/")
    return render(request, 'adminapp/delete_contact_enquiry.html', { "item": item })


@login_required
def DeleteCourseEnq(request, id):
    mydict = {'msg':'Service Enq Deleted'}
    item = CourseEnq.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return HttpResponseRedirect("/courseenqlist/")
    return render(request, 'adminapp/delete_course_enquiry.html', { "item": item })

#
# class DeleteContactEnq(DeleteView):
#     model = Contact
#     def get_success_url(self):
#         return reverse('contactus_list')


# =========================Service Enq ============================
# Service Enq list view
@method_decorator(login_required, name='dispatch')
class ServiceEnqList(ListView):
    model = ServiceEnq
    template_name = 'adminapp/serviceenqlist.html'
    context_object_name = 'serviceenq'

@login_required
def DeleteServiceEnq(request, id):
    item = ServiceEnq.objects.get(id=id)
    mydict = {'msg':'Service Enq Deleted'}
    if request.method == "POST":
        item.delete()
        return HttpResponseRedirect("/serviceenqlist/")
    # del_serv_enq = ServiceEnq.objects.all()
    return render(request, 'adminapp/delete_service.html', { "item": item })

# =========================Course Enq ============================
#Course Enq list view
@method_decorator(login_required, name='dispatch')
class CourseEnqList(ListView):
    model = CourseEnq
    template_name = 'adminapp/courseenqlist.html'
    context_object_name = 'courseenq'

@login_required
def DeleteServiceEnq(request, id):
    item = ServiceEnq.objects.get(id=id)
    mydict = {'msg':'Service Enq Deleted'}
    if request.method == "POST":
        item.delete()
        return HttpResponseRedirect("/serviceenqlist/")
    # del_serv_enq = ServiceEnq.objects.all()
    return render(request, 'adminapp/delete_service.html', { "item": item })



@login_required
def DeleteCourseEnq(request, id):
    mydict = {'msg':'Service Enq Deleted'}
    item = CourseEnq.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return HttpResponseRedirect("/courseenqlist/")
    return render(request, 'adminapp/delete_course_enquiry.html', { "item": item })
