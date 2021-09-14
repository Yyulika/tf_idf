from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import re

import pandas as pd

from .models import Files
import uuid


def upload(request):
    if request.method == "POST":
        upload_file = request.FILES['document']

        fs = FileSystemStorage()
        upload_file.name = str(uuid.uuid4())
        file = Files(name=upload_file.name)
        file.save()
        fs.save(upload_file.name, upload_file)
        return redirect('table/')

    return render(request, 'upload.html')


def table(request):
    number = Files.objects.all().count()
    path = 'media/' + str(Files.objects.order_by('id')[number - 1])
    f = open(path, encoding="utf-8")
    words = f.read()
    line_opt = re.sub(r'[^\w\s]', '', words).lower()

    word_list = line_opt.split()

    count = word_list.__len__()

    ulist = []
    [ulist.append(x) for x in word_list if x not in ulist]

    dict_w = {}
    for word in ulist:
        dict_w.update({word: {'tf': str(word_list.count(word)), 'idf': str(word_list.count(word) / count)}})

    y1 = pd.DataFrame(dict_w)
    y2 = y1.T
    y2['idf'] = pd.to_numeric(y2['idf'])
    df_sorted = y2.sort_values(["idf"], ascending=False)
    df = df_sorted.to_html
    return render(request, 'table.html', {'table': df})
