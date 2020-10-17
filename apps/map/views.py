from django.shortcuts import render
from django.core import serializers
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import edit as generics
from .utils import *
from .models import Marker
import crypt
from .models import Category
from .models import SubCategory
from django.shortcuts import redirect
from .forms import MarkerUpdateForm
from django.views import View
from django.template.loader import render_to_string
from django.forms.models import model_to_dict
from Crypto.Cipher import AES
#import base64
from base64 import b64encode, b64decode
import re
import requests
import folium
import json
import six
from django.db.models import Q
import secrets
import string

ENCRYPT_KEY = b'iDJpljxUBBsacCZ50GpSBff6Xem0R-giqXXnBFGJ2Rs='

# index
def index(request):
    if request.method == "GET":
        #import pdb;pdb.set_trace()

        return render(request, 'index.html', {})


def encrypt(str_to_enc, str_key):
    try:
        salt='SlTKeYOpHygTYkP3'
        salt = salt.encode('utf8')
        enc_dec_method = 'utf-8'
        aes_obj = AES.new(str_key, AES.MODE_CFB, salt)
        hx_enc = aes_obj.encrypt(str_to_enc.encode('utf8'))
        mret = b64encode(hx_enc).decode(enc_dec_method)
        return mret
    except ValueError as value_error:
        if value_error.args[0] == 'IV must be 16 bytes long':
            raise ValueError('Encryption Error: SALT must be 16 characters long')
        elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
            raise ValueError('Encryption Error: Encryption key must be either 16, 24, or 32 characters long')
        else:
            raise ValueError(value_error)

def decrypt(enc_str, str_key):
    try:
        salt='SlTKeYOpHygTYkP3'
        salt = salt.encode('utf8')
        enc_dec_method = 'utf-8'
        aes_obj = AES.new(str_key.encode('utf8'), AES.MODE_CFB, salt)
        str_tmp = b64decode(enc_str.encode(enc_dec_method))
        str_dec = aes_obj.decrypt(str_tmp)
        mret = str_dec.decode(enc_dec_method)
        return mret
    except ValueError as value_error:
        if value_error.args[0] == 'IV must be 16 bytes long':
            raise ValueError('Decryption Error: SALT must be 16 characters long')
        elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
            raise ValueError('Decryption Error: Encryption key must be either 16, 24, or 32 characters long')
        else:
            raise ValueError(value_error)

#Mailgun Routes
def create_route(request):
  if request.method == "POST":
    # post_data = request.POST
    # markerID = post_data['id']
    # markers = Marker.objects.get(pk=markerID)
    # email = markers.email

    # N = 16
    # res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(N))
    # test_enc_text = encrypt(email, res)
    # test_dec_text = decrypt(test_enc_text, res)

    # mailgun_domain = "@mg.wordwideweb.info"
    # match_recipient =  test_enc_text+mailgun_domain
    # fakeEMail = 'thermic.arish@gmail.com'
    # print(f'Encrypted:{test_enc_text}  Decrypted:{test_dec_text} Domain: {match_recipient}')
    # resp = requests.put(
    #           "https://api.mailgun.net/v3/routes/5f89ecdf84e6f77ae7b5afe5",
    #            auth=("api", "ddab80f64ffe717494374abbc1284b7b-2fbe671d-d1e96897"),
    #            data={"priority": 0,
    #             "expression": "match_recipient('"+match_recipient+"')",
    #             "action": ["forward('"+fakeEMail+"')","stop()"]})


    # responseData = json.loads(resp.content)
    # reponseExp =  responseData['expression']
    # convertedEmail = re.search(r'\((.*?)\)',reponseExp).group(1)

    # responseEmail = convertedEmail.replace("'", "")

    # if responseEmail == match_recipient :
    #   data = {
    #     'responseEmail': responseEmail
    #   }

    # print(f'Encrypted:{test_enc_text}  Decrypted:{test_dec_text} Domain: {match_recipient} ResponseEmail: {responseEmail}' )
    #import pdb;pdb.set_trace()
    #################################PUT REQUEST################
      # resp = requests.put(
      #         "https://api.mailgun.net/v3/routes/5f89ecdf84e6f77ae7b5afe5",
      #         auth=("api", "ddab80f64ffe717494374abbc1284b7b-2fbe671d-d1e96897"),
      #         data={"priority": 0,
      #           "expression": "match_recipient('def@mg.wordwideweb.info')",
      #         })

      #json.loads(resp.content)
      #import pdb;pdb.set_trace()

    #################################GET REQUEST################
    # resp = requests.get("https://api.mailgun.net/v3/routes/5f89ecdf84e6f77ae7b5afe5",
    #                   auth=("api", "ddab80f64ffe717494374abbc1284b7b-2fbe671d-d1e96897"))
    # json.loads(resp.content)
    #routeData['route']['expression']


    #################################POST REQUEST################

    # post_data = request.POST
    # markerID = post_data['id']
    # markers = Marker.objects.get(pk=markerID)
    # email = markers.email
    # #conv_bytes = bytes(email, 'utf-8')
    # #encoded_str = base64.b64encode(conv_bytes)
    # #@mg.wordwideweb.info
    # #actual_email = base64.b64decode(encoded_str).decode()

    # # match = re.search('(?P<name>.*)', email)
    # # forw = re.search('(g<name>.*)', email)
    # #email = post_data['email']
    # match_recipient =  "abc@mg.wordwideweb.info"
    # resp = requests.post(
    #          "https://api.mailgun.net/v3/routes",
    #          auth=("api", "ddab80f64ffe717494374abbc1284b7b-2fbe671d-d1e96897"),
    #          data={"priority": 0,
    #                "description": "Sample route",
    #                "expression": "match_recipient('"+match_recipient+"')",
    #                "action": ["forward('"+email+"')",
    #                "stop()"]})
    # #import pdb;pdb.set_trace()
    # if(resp.status_code == 200) :
    #    responseData = json.loads(resp.content)
    #    route_id = responseData['route']['id']
    #    data = {
    #      'recipient': match_recipient
    #    }
       #5f89ecdf84e6f77ae7b5afe5
    data = {

    }
    return JsonResponse(data)

# def get_routes(request)
#   if request.method == "POST":
#   resp = requests.post("https://api.mailgun.net/v3/routes",
#                       auth=("api", "ddab80f64ffe717494374abbc1284b7b-2fbe671d-d1e96897"))




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
        markers = list(Marker.objects.filter(is_active=True).values('id', 'email', 'latitude', 'longitude', 'category__category', 'sub_category__sub_category', 'description'))
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
        if post_data['searchText'] is not '':
            or_lookup = (Q(description__icontains=post_data['searchText']) |
                         Q(category__category__icontains=post_data['searchText']) |
                         Q(sub_category__sub_category__icontains=post_data['searchText']) |
                         Q(category__category__icontains=post_data['categories']) |
                         Q(sub_category__sub_category__icontains=post_data['subcategories'])
                        )
            data = list(Marker.objects.filter(or_lookup).values('id', 'email', 'latitude', 'longitude', 'category__category', 'sub_category__sub_category', 'description'))

        elif post_data['subcategories'] != 'init':
            #import pdb;pdb.set_trace()
            data = list(Marker.objects.filter(category_id=post_data['categories'],
                                              sub_category_id=post_data['subcategories']).values('id', 'email', 'latitude', 'longitude', 'category__category', 'sub_category__sub_category', 'description'))
        else:
            data = {}
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
