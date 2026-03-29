from django.shortcuts import render, redirect
from django.contrib import messages

def report_leak(request):
    if request.method == "POST":
        location = request.POST.get('location')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        leak_type = request.POST.get('leak_type')
        details = request.POST.get('details')
        evidence = request.FILES.get('evidence')

        if not location or not full_name or not phone:
            return render(request, 'reports/report.html', {
                'error': 'Please fill in all required fields!'
            })

        # TODO: Save the report to database
        # TODO: Handle the file upload

        return redirect('success')

    return render(request, 'reports/report.html')


def success(request):
    return render(request, 'reports/success.html')