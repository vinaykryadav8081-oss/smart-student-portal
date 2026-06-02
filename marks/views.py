from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import MarksForm
from .models import Marks


@login_required
def add_marks(request):

    if request.method == 'POST':

        form = MarksForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/marks/list/')

    else:

        form = MarksForm()

    return render(
        request,
        'marks/add_marks.html',
        {
            'form': form
        }
    )


@login_required
def marks_list(request):

    records = Marks.objects.filter(
        student__user=request.user
    )

    return render(
        request,
        'marks/marks_list.html',
        {
            'records': records
        }
    )