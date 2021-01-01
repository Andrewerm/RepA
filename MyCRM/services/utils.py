from crmApp.models import AvangardStock
import re

def handle_avangard_file(file):
    AvangardStock.objects.all().delete()
    file_data=file.read().decode('utf-8')
    lines=file_data.split('\n')
    lines=map(lambda x:AvangardStock(item=re.search('\d{6}', x)[0]), lines )
    AvangardStock.objects.bulk_create(lines)


