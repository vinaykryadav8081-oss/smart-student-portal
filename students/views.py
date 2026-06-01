from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from attendance.models import Attendance
from marks.models import Marks


@login_required
def student_dashboard(request):

    attendance_records = Attendance.objects.filter(
        student__user=request.user
    )

    marks_records = Marks.objects.filter(
        student__user=request.user
    )

    # Attendance Analytics

    total_attendance = attendance_records.count()

    present_count = attendance_records.filter(
        status=True
    ).count()

    absent_count = attendance_records.filter(
        status=False
    ).count()

    if total_attendance > 0:
        attendance_percentage = round(
            (present_count / total_attendance) * 100,
            2
        )
    else:
        attendance_percentage = 0

    # Marks Analytics

    total_marks = 0

    for mark in marks_records:
        total_marks += mark.marks

    total_marks_obtained = total_marks

    if marks_records.count() > 0:
        average_marks = round(
            total_marks / marks_records.count(),
            2
        )
    else:
        average_marks = 0

    return render(
        request,
        'students/dashboard.html',
        {
            'attendance_records': attendance_records,
            'marks_records': marks_records,

            'total_attendance': total_attendance,
            'present_count': present_count,
            'absent_count': absent_count,
            'attendance_percentage': attendance_percentage,

            'average_marks': average_marks,
            'total_marks_obtained': total_marks_obtained,

            'user': request.user,
        }
    )