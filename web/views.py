from django.template import RequestContext
from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from api.models import UserProfile
from api.models import Project
from .form import UserProfileForm
from .form import ProjectForm
from django.contrib.auth import logout as auth_logout
from api.models import Project
from api.models import UserProfile
from api.models import Task

def index(request):
	return render_to_response('pages/index.html',{})

def projects(request):
	project_list = Project.objects.all()
	return render(request, 'pages/projects.html',{'project_list': project_list})

def about(request):
	return render(request, 'pages/about.html',{})

def members(request):
	members_list = UserProfile.objects.all()
	return render(request, 'pages/members.html',{'members_list': members_list})

def member_page(request,user_id):
	user = get_object_or_404(UserProfile, id=user_id)
	return render(request, 'pages/member_page.html',{'user': user})

def user_new(request, user_id):
	user = get_object_or_404(UserProfile, id=user_id)
	if UserProfile.objects.filter(firstname=firstname).exists():
		user = UserProfile.objects.get(firstname=firstname)
	else:
		return render(request, 'pages/edituser.html', {'invalid_firstname': True})

	if request.method == "POST":
		userprofileform = UserProfileForm (request.POST)
		if userprofileform.is_valid():
			user = userprofileform.save()
			return redirect('pages-members')
	else:
		userprofileform = UserProfileForm()

	return render(request, 'pages/edituser.html', {'userprofileform': userprofileform})

def user_edit(request, user_id):
	user = get_object_or_404(UserProfile, id=user_id)
	if request.method == "POST":
		userprofileform = UserProfileForm(request.POST, instance=user)
		if userprofileform.is_valid():
			user = userprofileform.save()
			return redirect('pages-member-detail', user_id)
	else:
		userprofileform = UserProfileForm(instance=user)

	return render(request, 'pages/edituser.html', {'userprofileform': userprofileform})	

def tasks(request):
	task_list = Task.objects.all()
	return render(request, 'pages/tasks.html', {'task_list': task_list})

def events(request):
	return render(request, 'pages/events.html',{})

def gallery(request):
	return render(request, 'pages/gallery.html',{})

def login(request):
	return render(request, 'pages/login.html',{})

def links(request):
	return render(request, 'pages/links.html',{})

def privacy(request):
	return render(request, 'pages/privacy.html',{})

def project_detail(request, project_id):
	if Project.objects.filter(pk=project_id).exists():
		project = Project.objects.get(pk=project_id)
	else:
		project = None

	return render(request, 'pages/project_detail.html', {'project': project})

def project_new(request):
	if request.method == "POST":
		projectform = ProjectForm (request.POST)
		if projectform.is_valid():
			project = projectform.save()
			return redirect('project-detail', project_id=project.project_id)
	else:
		projectform = ProjectForm()

	return render(request, 'pages/project_edit.html', {'projectform': projectform})

def project_edit(request, project_id):
	if Project.objects.filter(pk=project_id).exists():
		project = Project.objects.get(pk=project_id)
	else:
		return render(request, 'pages/project_edit.html', {'invalid_project_id': True})

	if request.method == "POST":
		projectform = ProjectForm(request.POST, instance=project)
		if projectform.is_valid():
			project = projectform.save()
			return redirect('project-detail', project_id=project.project_id)
	else:
		projectform = ProjectForm(instance=project)

	return render(request, 'pages/project_edit.html', {'projectform': projectform,
														'editing': True})

def logout(request):
	auth_logout(request)
	return redirect('/')
