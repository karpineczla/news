from django.shortcuts import render, redirect
from .models import CustomUser
from django.views.generic.detail import DetailView
from django.views.generic.list  import ListView
from accounts.forms import hoursForm

class TutorView(DetailView):
    model = CustomUser
    template_name = "tutor_single.html"
    context_object_name = "tut"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Hours"] = self.object.Hours.split(",")
        context["Days"] = self.object.Days.split(",")
        context["Bio"] = self.object.Bio.split(",")
        context["Ta_Classes"] = self.object.Ta_Classes
        return context
    
class TutorListView(ListView):
    model = CustomUser
    template_name = "tutor_list.html"
    context_object_name = "tuts"

    def get_tuts(self):
        return CustomUser.objects
    
def change_times(request):
        user = request.user  # Get the current logged-in user
        if request.method == 'POST':
            form = hoursForm(request.POST, instance=user)  # Pass the user instance here
            if form.is_valid():
                form.save()
                return redirect('tutor_list')
        else:
             form = hoursForm(instance=user)
             
        return render(request,'change_times.html',{'hours_form':hoursForm})

