from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import redirect_to_login
from django.views import generic as views
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.urls import reverse, reverse_lazy

from django.contrib.auth import views as auth_views, get_user_model, forms as auth_forms
from shop.accounts.forms import CreateUserForm

UserModel = get_user_model()


class LoginUserView(auth_views.LoginView):
    template_name = "accounts/login.html"

    # def get_success_url(self):
    #   # return whatever you want
    #   pass


class RegisterUserView(views.CreateView):
    form_class = CreateUserForm  # Your custom user creation form
    template_name = "accounts/register.html"  # Template for registration form
    success_url = reverse_lazy("index")  # URL to redirect after successful registration

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        Additionally, log in the user after registration.
        """
        response = super().form_valid(form)
        login(self.request, self.object)  # Log in the user after successful registration
        return response


# class LoginUserView(views.View):
#     form_class = auth_forms.AuthenticationForm
#
#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': self.form_class()
#         }
#
#         return render(request, 'accounts/login_user.html', context)
#
#     def post(self, request, *args, **kwargs):
#         # form = self.form_class(request.POST or None)
#         # if form.is_valid():
#         # username, password = request.POST["username"], request.POST["password"]
#         #
#         # user = authenticate(username=username, password=password)
#         # print(user)
#
#         # if user is not None:
#         #     # Add the user to the session
#         #     login(request, user)
#         login(request, User.objects.get(pk=2))
#         return redirect("index")

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')
