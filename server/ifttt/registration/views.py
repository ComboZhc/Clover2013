from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from forms import UserCreationForm

def register(request):
    t = 'registration/register.html'
    #if request.user.is_authenticated():
    #    return render_to_response(t)
    form = UserCreationForm()
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.flash['message'] = 'Account created successfully'
            return redirect('django.contrib.auth.views.login')
    return render_to_response(t, {'form': form}, context_instance=RequestContext(request))

def home(request):
    t = 'registration/home.html'
    return render_to_response(t, context_instance=RequestContext(request))