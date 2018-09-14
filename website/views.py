from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView
from website.forms import *
from website.models import Game




def index(request):
    user_form = UserForm()
    template_name = 'index.html'
    return render(request, template_name, {"user_form": user_form})

# Create your views here.
def register(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        return login_user(request)

    elif request.method == 'GET':
        user_form = UserForm()
        template_name = 'register.html'
        return render(request, template_name, {'user_form': user_form})


def login_user(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # Obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username=request.POST.get('username')
        password=request.POST.get('password')
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return HttpResponseRedirect('/')

        else:
            # Bad login details were provided. So we can't log the user in.
            return HttpResponse("Invalid login details supplied.")

    return render(request, 'login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage. Is there a way to not hard code
    # in the URL in redirects?????
    return HttpResponseRedirect('/')

def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/games')
    else:
        form = ModelFormWithFileField()
    return render(request, 'game/game_form.html', {'form': form})

def add_friend(request):
    form = FriendForm()
    return render(request, 'friend_form.html', {'form': form})

class Game_List_View(ListView):
    """
    Game_List_View inherits ListView and is using the Game model
    """
    model = Game 
    context_object_name = 'game_list'
    template_name = 'game/game_list.html'

class Game_Detail_View(DetailView):
    """
    Game_Detail_View inherits DetailView and is using the Game model
    """
    model = Game
    context_object_name = 'game_detail'
    template_name = 'game/game_detail.html'

class Game_Form_View(FormView):
    """
    Game_Form_View inherits FormView and is using the Game model and using Game_Form.html template. This renders a 'new' form view that User can create a new game listing. form_class is inheriting the actual form that is going to include the necessary fields that receive the proper format.
    """
    template_name = 'game/game_form.html'
    form_class = GameForm
    success_url = '/games'

    def form_valid(self, form):

        form.save()
        return super(Game_Form_View, self).form_valid(form)


class Game_Update_View(UpdateView):
    """
    Game_Update_View inherits UpdateView and is using the game_update_form.html template.
    The view is using the Game model and is making name and description editable
    Once the edits have been made, the success_url is redirecting to the url written.
    """
    model = Game
    fields = ['name','description', 'image']
    template_name = 'game/game_update_form.html'
    success_url = '/games/'
    
class Game_Delete_View(DeleteView):
    model = Game
    template_name = 'game/game_delete.html'
    success_url = '/games/'

    def game_delete(request, pk, template_name='game/game_delete.html'):
        game = get_object_or_404(Game, pk=pk)    
        if request.method=='POST':
            game.delete()
            return redirect('game_list')
        return render(request, template_name, {'object':game})