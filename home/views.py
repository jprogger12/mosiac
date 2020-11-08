from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import ContactInfomation, TeamPerson, TeamPersonContact, Project, Customer, About, BlogLetter, OurService, \
    Category, Comment, HomeHeader
from .forms import MessageForm, CommentForm, EmailForm


# Create your views here.

def getdoskastring(name, link):
    '''navbar dan keyingi doskaga qiymat berish uchun'''
    doska = {
        'name': name,
        'link': link,
    }
    return doska


def index(request):
    header = HomeHeader.objects.all()
    abouts = About.objects.first()
    customers = Customer.objects.all()
    os = OurService.objects.all()
    data = {
        'head':header,
        'os':os,
        'customers': customers,
        'ab': abouts,
        'is_home': True,

    }
    return render(request, 'home/index.html', data)


def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.name = form.cleaned_data.get("name")
            form.email = form.cleaned_data.get("email")
            form.subject = form.cleaned_data.get("subject")
            form.message = form.cleaned_data.get("message")
            form.save()

    data = {
        'infor': ContactInfomation.objects.first(),
        'dos': getdoskastring('Contact Us', 'Contact')
    }

    return render(request, 'home/contact.html', data)


def team(request):
    teamPerson = TeamPerson.objects.all()
    teamPersonConatcts = TeamPersonContact.objects.all()
    projects = Project.objects.all()[:4]

    data = {
        'teamPerson': teamPerson,
        'teamPC': teamPersonConatcts,
        'pro': projects,
        'dos': getdoskastring('Our Team', 'Team')
    }
    return render(request, 'home/team.html', data)


def project(request, tip=None):
    if tip is None:
        projects = Project.objects.all()

    else:

        projects = Project.objects.filter(category=tip).all()

    paginator = Paginator(projects, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/project.html', {'pro': page_obj, 'dos': getdoskastring('Our Project', 'Project')})


def services(request):
    os = OurService.objects.all()
    projects = Project.objects.all()[:4]

    return render(request, 'home/services.html',
                  {'pro': projects, 'os': os, 'dos': getdoskastring('Our Services', 'Services')})


def about(request):
    abouts = About.objects.first()
    customers = Customer.objects.all()
    return render(request, 'home/about.html',
                  {'customers': customers, 'ab': abouts, 'dos': getdoskastring('About Us', 'About')})


def blog(request, tip=None):
    if tip is None:
        blogs = BlogLetter.objects.all()
    else:
        blogs = BlogLetter.objects.filter(category=tip).all()

    paginator = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/blog.html', {'blog': page_obj, 'dos': getdoskastring('Our Blog', 'Blog')})


class BlogView(ListView):
    paginate_by = 4
    model = BlogLetter
    # queryset = BlogLetter.objects.all()
    template_name = 'home/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['blog2'] = BlogLetter.objects.all()[3:6]
        context['dos'] = getdoskastring('Our Blog', 'Blog')
        context['data'] = {'is_home': True}
        return context





class BlogViewD(ListView):

    paginate_by = 4

    template_name = 'home/blog.html'

    def get_queryset(self):
        # print(get_blog_popular())
        return BlogLetter.objects.filter(category=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        # context['blogl'] = BlogLetter.objects.order_by('date')
        context['blog2'] = BlogLetter.objects.all()[2:5]
        context['dos'] = getdoskastring('Our Blog', 'Blog')
        context['data'] = {'is_home': True}
        return context


class BlogDetailView(DetailView):
    model = BlogLetter
    slug_field = 'slug'
    template_name = 'home/blog-single.html'

    # queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['blog2'] = BlogLetter.objects.all()[2:5]
        context['is_home'] = {'is_home': True}
        return context


class AddComment(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        blo = BlogLetter.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            form.blogId = blo
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.save()

        return redirect(blo.get_absolute_url())


class AddEmail(View):
    def post(self, request):
        form = EmailForm(request.POST)

        if form.is_valid():

            form.save()

        return redirect('/')