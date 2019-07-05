import random
from collections import namedtuple
from django.shortcuts import render
from datetime import datetime, timedelta


def list(request):

    return redirect('lesson-list')

    Issue = namedtuple('Issue', 'id name cost created_at')
    rand = lambda: random.randint(1, random.randint(1, random.randint(1, 4)))
    randdate = lambda: datetime.now() - timedelta(seconds=random.randint(1, 86400 * 30))

    issues = [
            Issue(2,  'Test', rand(), randdate()),
        ]

    context = {
            'issues': issues,
        }
    return render(request, 'issues/list.html', context)
