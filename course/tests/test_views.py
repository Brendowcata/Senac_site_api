from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from course.models import CourseModel
from django.urls import reverse
from rest_framework import status

class CourseTestCase(APITestCase):


    def setUp(self):
        self.password = 'admin123'
        self.my_admin = User.objects.create_superuser('admin', 'myemail@test.com', self.password)
        self.token = self.client.post('/rest-auth-token/', {'username': 'admin', 'password': 'admin123'}, format="json")
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.data["token"]}')

        self.list_url = reverse('Course-list')
        self.course_1 = CourseModel.objects.create(
            name = 'Curso teste',
            course_type = 'GRADUACAO',
            course_objective = 'Teste',
            curriculum = None,
            completion_profile = 'Teste',
            duration_time = 2400,
            occupation_area = 'Teste',
            course_image = None,
            is_activate = True,
            modality = 'EAD',
            mec_score = 'MEC4'
        )
    
    def test_get_course_list(self):
        """Test to list all courses / Teste para listar todas as cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_course_create(self):
        """Test to create course / Teste para criar curso"""
        data = {
            "name": 'Curso teste',
            "course_type": 'POS_GRADUACAO',
            "course_objective": 'Teste111',
            "curriculum": '',
            "completion_profile": 'Teste23',
            "duration_time": 1200,
            "occupation_area": 'Teste',
            "course_image": '',
            "is_activate": True,
            "modality": 'PRESENCIAL',
            "mec_score": 'MEC5',
            "enrollments": []
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_course_update(self):
        """Test to edit course / Teste para editar curso"""
        data = {
            "name": 'Curso atualizando',
            "course_type": 'POS_GRADUACAO',
            "course_objective": 'Testando',
            "curriculum": '',
            "completion_profile": 'testando12',
            "duration_time": 1450,
            "occupation_area": 'testando',
            "course_image": '',
            "is_activate": False,
            "modality": 'PRESENCIAL',
            "mec_score": 'MEC5',
            "universities": [],
            "enrollments": []

        }
        response = self.client.put(self.list_url + str(self.course_1.id) + '/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_course_delete(self):
        """Test to delete course (must not delete) / Teste para deletar curso (não deve deletar)"""
        response = self.client.delete(self.list_url + str(self.course_1.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)