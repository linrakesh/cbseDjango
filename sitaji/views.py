# from django.shortcuts import render,get_object_or_404
# from .models import student

# # Create your views here.
# def index(request):
#     all_student = student.objects.all()
#     return render(request,'index.html',{"students":all_student})

# def detail(request,student_id):
# 	# single_student = student.objects.get(pk=student_id)
# 	single_student = get_object_or_404(student,pk=student_id)
# 	return render(request,'detail.html',{"student":single_student})

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
#import required for user login 
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import View
# import required for mixins
from django.contrib.auth.mixins import LoginRequiredMixin
# import required for delete object
from django.urls import reverse_lazy

from .models import student
from .forms  import UserForm

class indexView(generic.ListView):
	template_name = 'sitaji/index.html'
	context_object_name ="students"
	paginate_by = 6
		
	def get_queryset(self):
		return student.objects.all()

class detailView(generic.DetailView):
	model = student 
	template_name = 'sitaji/detail.html'

class studentAdd(LoginRequiredMixin,CreateView):
	model = student
	fields = ['name','fname','email','image']
	login_url = '/login'

class studentUpdate(LoginRequiredMixin,UpdateView):
	model = student
	fields = ['name','fname','email','image']
	login_url = '/login'

class studentDelete(DeleteView):
	model = student
	success_url = reverse_lazy('sitaji:index')

class UserFormView(View):
	form_class = UserForm
	template_name = 'sitaji/registration_form.html'

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			#cleaned_normalized data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#authenticate
			user = authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('sitaji:index')
		
		return render(request,self.template_name,{'form':form})

