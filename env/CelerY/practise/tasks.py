from templated_email import send_templated_mail
from practise.models import Info
import datetime

def timediff(a,b):
    date_format1 = "%Y-%m-%d"
    a_new  = datetime.datetime.strptime(str(a), date_format1)
    b_new = datetime.datetime.strptime(str(b), date_format1)
    diff = a_new - b_new
    return diff.days

def send_invitation():
    curr = datetime.date.today()
    res = curr + datetime.timedelta(days = 2)
    ob = Info.objects.all()
    for object in ob:
        if timediff(res,object.date_visit) == 0:
            info_u = object.Username
            info_org = object.Organisation
            send_templated_mail(
                        template_name='info',
                        from_email='hreddy281@gmail.com',
                        recipient_list=['sumanthminupala1974@gmail.com'],
                        context = {
                                'info_u':info_u,
                                'info_org':info_org,
                        }
                    )
