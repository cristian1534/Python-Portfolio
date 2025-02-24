from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Project  # Asegúrate de que esta línea esté presente
import requests
from django.http import FileResponse
import os
from django.http import JsonResponse
from .models import Contact
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from datetime import datetime, timedelta


@csrf_exempt
def contact(request):
    if request.method == 'POST':
        try:
            contact = Contact.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                subject=request.POST.get('subject'),
                message=request.POST.get('message')
            )
            return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def download_cv(request):
    file_path = '/Users/development/Desktop/Porfolio Python/Python/static/cv/CV.pdf'
    try:
        response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Cristian_Machuca_CV.pdf"'
        return response
    except FileNotFoundError as e:
        print(f"File not found at: {file_path}")  # Debug print
        from django.http import Http404
        raise Http404("CV file not found")

def get_github_data():
    # Try to get cached data first
    cached_data = cache.get('github_repos')
    if cached_data:
        return cached_data

    username = "cristian1534"
    repos = []
    page = 1
    
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Python'
    }
    
    try:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            repos = response.json()
        else:
            print(f"GitHub API Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")
        return {'public_repos': 0, 'repositories': [], 'profile_url': f"https://github.com/{username}"}

    data = {
        'public_repos': len(repos),
        'repositories': repos,
        'profile_url': f"https://github.com/{username}"
    }
    
    # Cache the data for 1 hour
    cache.set('github_repos', data, 3600)
    
    return data

class IndexView(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add projects to context
        projects = Project.objects.all()
        print(f"Number of projects found: {projects.count()}")  # Debug line
        context['projects'] = projects
        
        github_data = get_github_data()
        total_repos = len(github_data['repositories'])
        
        repos_per_page = 4
        total_pages = (total_repos + repos_per_page - 1) // repos_per_page
        
        try:
            page = max(1, min(int(self.request.GET.get('page', 1)), total_pages))
        except ValueError:
            page = 1
            
        start_idx = (page - 1) * repos_per_page
        end_idx = start_idx + repos_per_page
        
        sliced_repos = github_data['repositories'][start_idx:end_idx]
        context['github_data'] = {
            'public_repos': total_repos,
            'repositories': sliced_repos,
            'total_pages': total_pages,
            'current_page': page
        }
        return context

def about(request):
    context = {
        'github_data': get_github_data()
    }
    return render(request, 'portfolio/about.html', context)
