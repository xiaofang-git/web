from django.shortcuts import render
from django.core.paginator import Paginator
from notice.models import Gupiao
from django.core.mail import send_mail


# Create your views here.

def index(request):
    arti_info = Gupiao.objects.all()
    pageinator = Paginator(arti_info, 6)
    page = request.GET.get('page',1)
    info = pageinator.page(page)
    context = {
        'meta':info
    }
    return render(request, '../templates/index.html',context)

def email(request):
    """
    实现发送邮件
    :param request:
    :return:
    """
    try:
        email_id = request.POST.get('id')
        info = request.POST.get('email')
        send_mail('Subject here', info, '15732633601@163.com',
                  [email_id], fail_silently=False)
        context = {
            'mess':'发送成功！'
        }
    except:
        context = {
            'mess':'发送失败！'
        }
    return render(request, '../templates/mail.html',context)
