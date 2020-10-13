from django.shortcuts import render
from django.core import serializers
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import edit as generics
from .utils import *
from .models import Marker
from .models import Category
from .models import SubCategory
from django.shortcuts import redirect
from .forms import MarkerUpdateForm
from django.views import View
from django.template.loader import render_to_string
from django.forms.models import model_to_dict
import folium
import json


# index
def index(request):
    if request.method == "GET":
        return render(request, 'index.html', {})


# send email to user
def create_marker(request):
    """create marker"""

    if request.method == "GET":
        return HttpResponse("not available for browser")

    if request.method == "POST":
        post_data = request.POST
        id = save_marker(post_data)

        update_url = request.META['HTTP_HOST'] + "/update-marker/" + str(id)
        email_marker_form_url(post_data['email'], id, update_url)
        data = {
            'message': "successfully created",
            'update_url': update_url
        }
        return JsonResponse(data)


def getAllMarkers(request):
    """Get all DB Markers"""

    if request.method == "GET":
        markers = list(Marker.objects.filter(is_active=True).values('id', 'email', 'latitude', 'longitude', 'category',
                                                                    'sub_category'))
        data = {
            'message': "successfully fetched!",
            'data': markers
        }
        return JsonResponse(data)


def categories(request):
    """Get all DB Categories"""

    if request.method == "GET":
        category = list(Category.objects.values('id', 'category'))
        data = {
            'message': "category successfully fetched!",
            'data': category
        }
        return JsonResponse(data)


def subcategories(request):
    if request.method == "POST":
        post_data = request.POST
        data = list(SubCategory.objects.filter(category_id=post_data['id']).values('id', 'sub_category'))
        #import pdb;pdb.set_trace()
        data = {
            'message': "category successfully fetched!",
            'data': data
        }
    else:
        data = {
            'message': "category successfully fetched!",
            'data': data
        }

    return JsonResponse(data)


def search(request):
    if request.method == "POST":
        post_data = request.POST
        if post_data['categories']:
            data = list(Marker.objects.filter(category_id=post_data['categories'],
                                              sub_category_id=post_data['subcategories']).values('id', 'email',
                                                                                                 'latitude',
                                                                                                 'longitude'))
            data = {
                'message': "search successfully!",
                'data': data
            }
    return JsonResponse(data)


def save_marker(data):
    """saving location in DB"""
    print(data)
    m = Marker(latitude=float(data['latitude']),
               longitude=float(data['longitude']), email=data['email'])
    m.wrap_location()
    m.save()

    return m.id


def email_marker_form_url(to_email, marker_id, url):
    """sending marker form url through email"""
    subject, from_email, to = 'complete the marker', 'admin@example.com', to_email

    html_content = render_to_string(
        'map/marker_email.html',
        {'update_url': url}
    )
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


class MarkerUpdate(generics.UpdateView):
    """Marker update view"""

    model = Marker
    template_name = 'map/marker_update_form.html'
    form_class = MarkerUpdateForm

    def post(self, request, *args, **kwargs):
        instance = Marker.objects.get(id=kwargs['pk'])
        form = self.form_class(request.POST or None, instance=instance)

        if form.is_valid():
            # instance['is_active'] = True
            instance.is_active = True
            # import pdb;pdb.set_trace()
            form.save()
            return redirect('/')

        return render(
            request, self.template_name, {'form': form})

    def categories(request):
        """Get all DB Categories"""

        if request.method == "GET":
            category = list(Category.objects.values('id', 'category'))
            data = {
                'message': "category successfully fetched!",
                'data': category
            }
            return JsonResponse(data)

    def load_cities(request, *args, **kwargs):

        if request.method == "GET":
            category_id = request.GET.get('category')
            data = list(SubCategory.objects.filter(category_id=category_id).values('id', 'sub_category'))
            data = {
                'message': "category successfully fetched!",
                'data': data
            }
        else:
            data = {
                'message': "category successfully fetched!",
                'data': data
            }

        return JsonResponse(data)
