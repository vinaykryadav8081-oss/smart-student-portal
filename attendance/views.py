from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Attendance
from accounts.models import CustomUser


@login_required
def attendance_list(request):

    records = Attendance.objects.all()

    return render(
        request,
        'attendance/attendance_list.html',
        {
            'records': records
        }
    )


@login_required
def mark_attendance(request):

    students = CustomUser.objects.filter(
        role='student'
    )

    if request.method == 'POST':

        student_id = request.POST.get('student')

        status = request.POST.get('status')

        student = CustomUser.objects.get(
            id=student_id
        )

        Attendance.objects.create(
            student=student,
            date=request.POST.get('date'),
            status=status
        )

        return redirect('attendance_list')

    return render(
        request,
        'attendance/mark_attendance.html',
        {
            'students': students
        }
    )