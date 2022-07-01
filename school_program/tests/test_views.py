from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from school_program.models import School_ProgramModel
from course.models import CourseModel
from django.urls import reverse
from rest_framework import status

class School_ProgramTestCase(APITestCase):


    def setUp(self):
        self.password = 'admin123'
        self.my_admin = User.objects.create_superuser('admin', 'myemail@test.com', self.password)
        self.token = self.client.post('/rest-auth-token/', {'username': 'admin', 'password': 'admin123'})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.data["token"]}')

        self.list_url = reverse('School_Program-list')

        self.course_1 = CourseModel.objects.create(
            name = 'Curso 1',
            course_objective = 'Teste',
            curriculum = None,
            completion_profile = 'Teste',
            duration_time = 2400,
            occupation_area = 'Teste',
            course_image = None,
            is_activate = True,
        )

        self.school_program_1 = School_ProgramModel.objects.create(
            phase = 1,
            phase_time = 200,
            courses=self.course_1
        )
    
    def test_get_school_program_list(self):
        """Test to list all school programs / Teste para listar todas as fases"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_school_program_create(self):
        """Test to create school program / Teste para criar fase"""
        data = {
            "phase": 2,
            "phase_time": 100,
            "courses": str(self.course_1.id)
        }
        
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_school_program_update(self):
        """Test to edit school program / Teste para editar fase"""
        data = {
            "phase": 4,
            "phase_time": 150,
            "courses": str(self.course_1.id)
        }
        response = self.client.put(self.list_url + str(self.school_program_1.id) + '/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_school_program_delete(self):
        """Test to delete school program / Teste para deletar fase"""
        response = self.client.delete(self.list_url + str(self.school_program_1.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)