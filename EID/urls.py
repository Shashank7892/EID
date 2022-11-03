from django.conf.urls import url
from EID import views
app_name='EID'

urlpatterns=[
url(r'^register/$',views.signup,name='register'),
url(r'^login/$',views.login,name='login'),
url(r'^logout/$',views.logout,name='logout'),
url(r'^alogout/$',views.alogout,name='alogout'),
url(r'^upload/$',views.upload,name='upload'),
url(r'^success/$',views.success,name='success'),
url(r'^adminz/$',views.adminz,name='adminz'),
url(r'^adminlog/$',views.adminlog,name='adminlog'),
url(r'^viewstatus/$',views.viewstatus,name='viewstatus'),
url(r'^uploadfiles/(?P<value>\w+)$',views.uploadfiles,name='uploadfiles'),
url('vd/(?P<value>\w+)$',views.vd,name='vd'),
url(r'^adminupdate/$',views.adminupdate,name='adminupdate'),
url(r'^aproaadhaar/(?P<value>\w+)$',views.aproaadhaar,name='aproaadhaar'),
url(r'^aprpassport/(?P<value>\w+)$',views.aprpassport,name='aprpassport'),
url(r'^aprdl/(?P<value>\w+)$',views.aprdl,name='aprdl'),
url(r'^aprpancard/(?P<value>\w+)$',views.aprpancard,name='aprpancard'),
url(r'^aprvoterid/(?P<value>\w+)$',views.aprvoterid,name='aprvoterid'),
url(r'^aprrationcard/(?P<value>\w+)$',views.aprrationcard,name='aprrationcard'),
url(r'^aprbuspass/(?P<value>\w+)$',views.aprbuspass,name='aprbuspass'),
url(r'^disaadhaar/(?P<value>\w+)$',views.disaadhaar,name='disaadhaar'),
url(r'^dispassport/(?P<value>\w+)$',views.dispassport,name='dispassport'),
url(r'^disdl/(?P<value>\w+)$',views.disdl,name='disdl'),
url(r'^dispancard/(?P<value>\w+)$',views.dispancard,name='dispancard'),
url(r'^disvoterid/(?P<value>\w+)$',views.disvoterid,name='disvoterid'),
url(r'^disrationcard/(?P<value>\w+)$',views.disrationcard,name='disrationcard'),
url(r'^disbuspass/(?P<value>\w+)$',views.disbuspass,name='disbuspass'),

]
