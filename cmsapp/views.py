from django.http import HttpResponse
# just for testing
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from forms import LoginForm, CallCenterReportForm, NotificationForm

# Create your views here.
class HomeView(TemplateView):

    template_name = "base.html"

class DashboardView(TemplateView):

    template_name = "login.html"

class NotificationView(FormView):

    template_name = "Notification.html"
    form_class = NotificationForm
    success_url="/notification/"

    def form_valid(self, form):
        decision = form.cleaned_data["decision"]
        description = form.cleaned_data["description"]
        agency = form.cleaned_data["agency"]
        form.save()
        return super(NotificationView, self).form_valid(form)


class ReportView(FormView):

    template_name = "report.html"
    form_class = CallCenterReportForm
    success_url = "/report/"


    def form_valid(self, form):
        form.save()
        return super(ReportView, self).form_valid(form)

class ResourceView(TemplateView):

    template_name = "login.html"

class LoginView(FormView):

    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                # Redirect to a success page.
                return super(LoginView, self).form_valid(form)
            else:
                # Return a 'disabled account' error message
                return HttpResponse("disabled")
        else:
            return HttpResponse("no user")
