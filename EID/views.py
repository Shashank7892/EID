from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from EID.models import UserProfileInfo,Docstatus,adhardocument,passportdocument,dldocument,pancarddocument,voteriddocument,rationcarddocument,buspassdocument
from pathlib import Path
import os
import qrcode
import qrcode.image.svg
from io import BytesIO

BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    return render(request,'EID/index.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def signup(request):
    if request.method=='POST':
        print("POST")
        if UserProfileInfo.objects.filter(phoneno=request.POST['phoneno']).exists() or UserProfileInfo.objects.filter(gmailid=request.POST['gmail']).exists():
            return redirect('EID:signup')
            print("POST1")
        else:
            print("POST2")
            if len(request.POST['username'])>0 and len(request.POST['gmail'])>0 and len(request.POST['dob'])>0 and len(request.POST['phoneno'])==10 and len(request.POST['password'])>=7:
                us=UserProfileInfo(username=request.POST['username'],gmailid=request.POST['gmail'],dob=request.POST['dob'],phoneno=request.POST['phoneno'],password=request.POST['password'])
                us.save()
                da=Docstatus(phoneno=request.POST['phoneno'],vstat="0",addharstatus="notuploaded",passportstatus="notuploaded",dlstatus="notuploaded",pancardstatus="notuploaded",voteridstatus="notuploaded",rationcardstatus="notuploaded",buspassstatus="notuploaded")
                da.save()
                print("POST3")
                return redirect('EID:login')
            else:
                print("POST4")
                return redirect('EID:signup')
    else:
        print("POST5")
        return render(request,'EID/register.html')

def login(request):
    request.session['vst']=""
    if request.method=='POST':
        if UserProfileInfo.objects.filter(gmailid=request.POST['gmail'],password=request.POST['password']).exists():
            dp=UserProfileInfo.objects.filter(gmailid=request.POST['gmail'])
            request.session['currentuser']=dp[0].phoneno
            return redirect('EID:upload')
        else:
            print("please enter valid Email and password")
            return redirect('EID:login')
    else:
        return render(request,'EID/login.html')

def upload(request):
    if request.session['currentuser']:
        return render(request,'EID/upload.html')
    else:
        return redirect('EID:login')

def logout(request):
    request.session['currentuser']=""
    return redirect('EID:login')
def alogout(request):
    request.session['currentuser']=""
    return redirect('EID:adminlog')
def success(request):
    request.session['currentuser']=""
    return HttpResponse('successfully')

def viewstatus(request):
    context={}
    if request.method=="POST":
        request.session['vst']=request.POST['btn']
        return redirect('EID:viewstatus')
    data=Docstatus.objects.filter(phoneno=request.session['currentuser'])
    a=UserProfileInfo.objects.filter(phoneno=request.session['currentuser'])
    username=a[0].username
    print(username)
    if request.session['vst']:
        if request.session['vst']=='aadhaar':
            a=adhardocument.objects.filter(phoneno=request.session['currentuser'])
            factory = qrcode.image.svg.SvgImage
            text="This is a Verified Aadhaar Document by the EID\n Username :- "+username+"\n Phoneno :- "+request.session['currentuser']+"\n Aadhhar No:- "+a[0].adhaarno
            img = qrcode.make(text, image_factory=factory, box_size=20)
            stream = BytesIO()
            img.save(stream)
            context['svg'] = stream.getvalue().decode()
            context['data']=data[0]
            return render(request,'EID/viewstatus.html',context)
        elif request.session['vst']=='passport':
            a=passportdocument.objects.filter(phoneno=request.session['currentuser'])
            factory = qrcode.image.svg.SvgImage
            text="This is a Verified Aadhaar Document by the EID\n Username :- "+username+"\n Phoneno :- "+request.session['currentuser']+"\n Passport No:- "+a[0].passportno
            img = qrcode.make(text, image_factory=factory, box_size=20)
            stream = BytesIO()
            img.save(stream)
            context['svg'] = stream.getvalue().decode()
            context['data']=data[0]
            return render(request,'EID/viewstatus.html',context)
        elif request.session['vst']=='dl':
            a=dldocument.objects.filter(phoneno=request.session['currentuser'])
            factory = qrcode.image.svg.SvgImage
            text="This is a Verified Aadhaar Document by the EID\n Username :- "+username+"\n Phoneno :- "+request.session['currentuser']+"\n DL No:- "+a[0].dlno
            img = qrcode.make(text, image_factory=factory, box_size=20)
            stream = BytesIO()
            img.save(stream)
            context['svg'] = stream.getvalue().decode()
            context['data']=data[0]
            return render(request,'EID/viewstatus.html',context)
        elif request.session['vst']=='pancard':
            a=pancarddocument.objects.filter(phoneno=request.session['currentuser'])
            factory = qrcode.image.svg.SvgImage
            text="This is a Verified Aadhaar Document by the EID\n Username :- "+username+"\n Phoneno :- "+request.session['currentuser']+"\n Pan Card No:- "+a[0].pancardno
            img = qrcode.make(text, image_factory=factory, box_size=20)
            stream = BytesIO()
            img.save(stream)
            context['svg'] = stream.getvalue().decode()
            context['data']=data[0]
            return render(request,'EID/viewstatus.html',context)
        elif request.session['vst']=='voterid':
            a=voteriddocument.objects.filter(phoneno=request.session['currentuser'])
            factory = qrcode.image.svg.SvgImage
            text="This is a Verified Aadhaar Document by the EID\n Username :- "+username+"\n Phoneno :- "+request.session['currentuser']+"\n Voter ID No:- "+a[0].voteridno
            img = qrcode.make(text, image_factory=factory, box_size=20)
            stream = BytesIO()
            img.save(stream)
            context['svg'] = stream.getvalue().decode()
            context['data']=data[0]
            return render(request,'EID/viewstatus.html',context)
        elif request.session['vst']=='rationcard':
            a=rationcarddocument.objects.filter(phoneno=request.session['currentuser'])
            factory = qrcode.image.svg.SvgImage
            text="This is a Verified Aadhaar Document by the EID\n Username :- "+username+"\n Phoneno :- "+request.session['currentuser']+"\n Ration Card No:- "+a[0].rationcardno
            img = qrcode.make(text, image_factory=factory, box_size=20)
            stream = BytesIO()
            img.save(stream)
            context['svg'] = stream.getvalue().decode()
            context['data']=data[0]
            return render(request,'EID/viewstatus.html',context)
        elif request.session['vst']=='buspass':
            a=buspassdocument.objects.filter(phoneno=request.session['currentuser'])
            factory = qrcode.image.svg.SvgImage
            text="This is a Verified Aadhaar Document by the EID\n Username :- "+username+"\n Phoneno :- "+request.session['currentuser']+"\n Bus Pass No:- "+a[0].buspassno
            img = qrcode.make(text, image_factory=factory, box_size=20)
            stream = BytesIO()
            img.save(stream)
            context['svg'] = stream.getvalue().decode()
            context['data']=data[0]
            return render(request,'EID/viewstatus.html',context)


    return render(request,'EID/viewstatus.html',{'data':data[0]})

def uploadfiles(request,value=None):
    if request.method=="POST":
        if value=='Aadhaar':
            if request.FILES['myfile']:
                print(request.session['currentuser'])
                ad=adhardocument(phoneno=request.session['currentuser'],adhaar=request.FILES['myfile'],adhaarno=request.POST['idno'])
                ad.save()
                Docstatus.objects.filter(phoneno=request.session['currentuser']).update(addharstatus="Pending",vstat="1")
                return redirect('EID:viewstatus')
            else:
                return redirect('EID:uploadfiles')
        elif value=='Passport':
            if request.FILES['myfile']:
                print(request.session['currentuser'])
                ad=passportdocument(phoneno=request.session['currentuser'],passport=request.FILES['myfile'],passportno=request.POST['idno'])
                ad.save()
                Docstatus.objects.filter(phoneno=request.session['currentuser']).update(passportstatus="Pending",vstat="1")
                return redirect('EID:viewstatus')
            else:
                return redirect('EID:uploadfiles')

        elif value=='Dl':
            if request.FILES['myfile']:
                print(request.session['currentuser'])
                ad=dldocument(phoneno=request.session['currentuser'],dl=request.FILES['myfile'],dlno=request.POST['idno'])
                ad.save()
                Docstatus.objects.filter(phoneno=request.session['currentuser']).update(dlstatus="Pending",vstat="1")
                return redirect('EID:viewstatus')
            else:
                return redirect('EID:uploadfiles')
        elif value=='Pancard':
            if request.FILES['myfile']:
                print(request.session['currentuser'])
                ad=pancarddocument(phoneno=request.session['currentuser'],pancard=request.FILES['myfile'],pancardno=request.POST['idno'])
                ad.save()
                Docstatus.objects.filter(phoneno=request.session['currentuser']).update(pancardstatus="Pending",vstat="1")
                return redirect('EID:viewstatus')
            else:
                return redirect('EID:uploadfiles')
        elif value=='Rationcard':
            if request.FILES['myfile']:
                print(request.session['currentuser'])
                ad=rationcarddocument(phoneno=request.session['currentuser'],rationcard=request.FILES['myfile'],rationcardno=request.POST['idno'])
                ad.save()
                Docstatus.objects.filter(phoneno=request.session['currentuser']).update(rationcardstatus="Pending",vstat="1")
                return redirect('EID:viewstatus')
            else:
                return redirect('EID:uploadfiles')
        elif value=='Voterid':
            if request.FILES['myfile']:
                print(request.session['currentuser'])
                ad=voteriddocument(phoneno=request.session['currentuser'],voterid=request.FILES['myfile'],voteridno=request.POST['idno'])
                ad.save()
                Docstatus.objects.filter(phoneno=request.session['currentuser']).update(voteridstatus="Pending",vstat="1")
                return redirect('EID:viewstatus')
            else:
                return redirect('EID:uploadfiles')
        elif value=='Buspass':
            if request.FILES['myfile']:
                print(request.session['currentuser'])
                ad=buspassdocument(phoneno=request.session['currentuser'],buspass=request.FILES['myfile'],buspassno=request.POST['idno'])
                ad.save()
                Docstatus.objects.filter(phoneno=request.session['currentuser']).update(buspassstatus="Pending",vstat="1")
                return redirect('EID:viewstatus')
            else:
                return redirect('EID:uploadfiles')
    else:
        return render(request,'EID/uploadfiles.html',{'value':value})

def adminlog(request):
    if request.method=="POST":
        if request.POST['username']=='admin' and request.POST['password']=='admin':
            request.session['admusr']='1'
            return redirect('EID:adminz')
        else:
            return redirect('EID:adminlog')
    return render(request,'EID/adminlog.html')

def adminz(request):
    if request.session['admusr']:
        return render(request,'EID/adminz.html')
    else:
        return redirect('EID:adminlog')

def adminupdate(request):
    if request.session['admusr']:
        data=Docstatus.objects.filter(vstat="1")
        return render(request,'EID/adminupdate.html',{'data':data})
    else:
        return redirect('EID:adminlog')

def vd(request,value=None):
    print("OMG")
    if request.session['admusr']:
        print("PECAS")
        context={}
        data=Docstatus.objects.filter(phoneno=value)
        context['data']=data[0]
        if adhardocument.objects.filter(phoneno=value).exists():
            adh=adhardocument.objects.filter(phoneno=value)
            context['adh']=adh[0].adhaar.url
        if passportdocument.objects.filter(phoneno=value).exists():
            ppt=passportdocument.objects.filter(phoneno=value)
            context['ppt']=ppt[0].passport.url
        if dldocument.objects.filter(phoneno=value).exists():
            dld=dldocument.objects.filter(phoneno=value)
            context['dld']=dld[0].dl.url
        if pancarddocument.objects.filter(phoneno=value).exists():
            pdc=pancarddocument.objects.filter(phoneno=value)
            context['pdc']=pdc[0].pancard.url
        if voteriddocument.objects.filter(phoneno=value).exists():
            vid=voteriddocument.objects.filter(phoneno=value)
            context['vid']=vid[0].voterid.url
        if rationcarddocument.objects.filter(phoneno=value).exists():
            rcd=rationcarddocument.objects.filter(phoneno=value)
            context['rcd']=rcd[0].rationcard.url
        if buspassdocument.objects.filter(phoneno=value).exists():
            bpd=buspassdocument.objects.filter(phoneno=value)
            context['bpd']=bpd[0].buspass.url
        return render(request,'EID/verifydata.html',context)
    else:
        return redirect('EID:adminlog')

def aproaadhaar(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(addharstatus="approved")
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def aprpassport(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(passportstatus="approved")
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def aprdl(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(dlstatus="approved")
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def aprpancard(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(pancardstatus="approved")
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def aprvoterid(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(voteridstatus="approved")
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def aprrationcard(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(rationcardstatus="approved")
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def aprbuspass(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(buspassstatus="approved")
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def disaadhaar(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(addharstatus="notuploaded")
            adhardocument.objects.filter(phoneno=value).delete()
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def dispassport(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(passportstatus="notuploaded")
            passportdocument.objects.filter(phoneno=value).delete()
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def disdl(request,value=None):
    if request.session['admusr']:
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(dlstatus="notuploaded")
            dldocument.objects.filter(phoneno=value).delete()
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def dispancard(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(pancardstatus="notuploaded")
            pancarddocument.objects.filter(phoneno=value).delete()
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def disvoterid(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(voteridstatus="notuploaded")
            voteriddocument.objects.filter(phoneno=value).delete()
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def disrationcard(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(rationcardstatus="notuploaded")
            rationcarddocument.objects.filter(phoneno=value).delete()
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')

def disbuspass(request,value=None):
    if request.session['admusr']:
        print("PEACES")
        if Docstatus.objects.filter(phoneno=value).exists() and Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
            Docstatus.objects.filter(phoneno=value).update(buspassstatus="notuploaded")
            buspassdocument.objects.filter(phoneno=value).delete()
            if Docstatus.objects.filter(phoneno=value)[0].addharstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].passportstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].dlstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].pancardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].voteridstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].rationcardstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            elif Docstatus.objects.filter(phoneno=value)[0].buspassstatus=="Pending":
                Docstatus.objects.filter(phoneno=value).update(vstat="1")
                return redirect('EID:vd',value)
            else:
                Docstatus.objects.filter(phoneno=value).update(vstat="0")
                return redirect('EID:adminupdate')
        else:
            return redirect('EID:adminupdate')
    else:
        return redirect('EID:adminlog')
