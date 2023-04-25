from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from .filters import OrderFilter
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def home(request):
    # Show all records in home page
    records = Record.objects.all()

	# Filter
    my_Filter = OrderFilter(request.GET, queryset=records)
    records = my_Filter.qs
    

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.error(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records,
					     'my_Filter': my_Filter,})


def logout_user(request):
    logout(request)
    messages.info(request, "You Have Been Logged Out")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.error(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
	
def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully")
		return redirect('home')
	else:
		messages.error(request, "You Must Be Logged In To Do That...")
		return redirect('home')

def is_valid_url(url):
    try:
        URLValidator()(url)
        return True
    except ValidationError:
        return False

def add_record(request):
	# Set username in input field 
	form = AddRecordForm(request.POST or None, initial={'username':request.user})
	if request.user.is_authenticated:
		if request.method == "POST":
			# Checking valid URL
			url = request.POST.get("video_link")
			if form.is_valid() and is_valid_url(url):
				print(is_valid_url(url))
				add_record = form.save()
				messages.success(request, "Record Added!")
				return redirect('home')
			else:
				messages.error(request, "Enter correct URL!")
		return render(request, 'add_record.html', {
			'form':form,})
	else:
		messages.error(request, "You Must Be Logged In...")
		return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			# Checking valid URL for update
			url = form.cleaned_data.get('video_link')
			if is_valid_url(url):
				print(is_valid_url(url))
				form.save()
				messages.success(request, "Record Has Been Updated!")
				return redirect('home')
			else:
				print('Don"t valid URL')
			messages.error(request, "Enter correct URL!")
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.error(request, "You Must Be Logged In...")
		return redirect('home')
	
    