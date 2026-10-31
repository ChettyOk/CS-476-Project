from django.urls import reverse
from django.test import TestCase
from accounts.models import Course
from django.test import Client
from django.urls import reverse


class test_filter_courses_system(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.course1 = Course.create_course('CS 101', 'Introduction to Computer Science')
        self.course2 = Course.create_course('CS 202', 'Data Structures')
        self.course3 = Course.create_course('ENER 101', 'Energy Systems')
        self.course4 = Course.create_course('CS476', 'Software Development Project')

    def test_search_query_all_courses(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.context['courses'].count(), 4)
        available_faculties = response.context['available_faculties']
        self.assertIn('Science', available_faculties)
        self.assertIn('Engineering', available_faculties)

    def test_search_query_selcect_subject(self):
        response = self.client.get(reverse('search'), {'q': 'CS'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['courses'].count(), 3)
    
    def test_search_query_selcect_course(self):
        response = self.client.get(reverse('search'), {'q': 'CS 476'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['courses'].count(), 1) 
        self.assertEqual(response.context['courses'][0].course_code, "CS 476")   

    def test_search_course_name(self):
        response = self.client.get(reverse('search'), {'q': 'Software Development Project'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['courses'].count(), 1) 
        self.assertEqual(response.context['courses'][0].course_name, "Software Development Project")  

    def test_filter_faculty(self):
        response = self.client.get(reverse('search'), {'faculty': 'Science'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['courses'].count(), 3) 
        available_subjects = response.context['available_subjects']
        self.assertNotIn('ENER', available_subjects)
        self.assertIn('CS', available_subjects)

    def test_faculty_and_search_query(self):
        response = self.client.get(reverse('search'), {'faculty': 'Science', 'q': '476'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['courses'].count(), 1)
        self.assertEqual(response.context['courses'][0].course_code, "CS 476")

    def test_no_search_results(self):
        response = self.client.get(reverse('search'), {'q': '676767676767'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['courses'].count(), 0)
        
        
        