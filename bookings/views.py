from django.shortcuts import render
from django.db.models import Q
from accounts.models import Course
from accounts.constants import FACULTIES


def filter_courses(request):
    search_query = request.GET.get('q', '').strip()
    selected_faculty = request.GET.get('faculty', '').strip()
    selected_subject = request.GET.get('subject', '').strip()
    has_tutor_offering = request.GET.get('has_tutor', '').lower() in ['true', '1', 'on']

    courses = Course.objects.all()

    if selected_faculty and selected_faculty != 'all': 
        courses = courses.filter(course_faculty__iexact = selected_faculty)
        available_subjects = sorted([i for i, v in FACULTIES.items() if v.lower() == selected_faculty.lower()])
    else:
        available_subjects = sorted(FACULTIES.keys())
    
    if selected_subject and selected_subject != 'all': 
        courses = courses.filter(course_code__istartswith=selected_subject)
        
    
    if has_tutor_offering: 
        # To be added once available slots are implemented
        pass

    if search_query:
        courses = courses.filter(Q(course_code__icontains = search_query) | Q(course_name__icontains = search_query))
        
    available_faculties = sorted(set(FACULTIES.values()))

    context = {
        'courses': courses,
        'available_faculties': available_faculties,
        'available_subjects': available_subjects,
        'selected_faculty': selected_faculty,
        'selected_subject': selected_subject,
        'search_query': search_query,
        'has_tutor_offering': has_tutor_offering,
    }

    return render(request, 'bookings/search_results.html', context)
    

    