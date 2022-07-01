from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from enrollment.models import EnrollmentModel
from course.models import CourseModel
from university.models import UniversityModel
from django.urls import reverse
from rest_framework import status

class EnrollmentTestCase(APITestCase):


    def setUp(self):
        self.password = 'admin123'
        self.my_admin = User.objects.create_superuser('admin', 'myemail@test.com', self.password)
        self.token = self.client.post('/rest-auth-token/', {'username': 'admin', 'password': 'admin123'})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.data["token"]}')

        self.list_url = reverse('Enrollment-list')

        self.university = UniversityModel.objects.create(
            name = 'Nome Faculdade Teste',
            telephone = '(48) 3333-3333',
            phone_number = '(48) 95555-5555',
            attendance = 'Atendimento de segunda a sexta',
            email = 'teste@gmail.com',
            street = 'Rua de teste',
            neighborhood = 'Bairro de teste',
            city = 'Palhoça',
            state = 'Santa Catarina',
            zip_code = '88888-888',
            house_number = '100',
            university_image_local = None,
            is_activate = True,
        )

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

        self.enrollment_1 = EnrollmentModel.objects.create(
            title_enrollment = "teste12",
            date_initial = '2022-06-30',
            date_final = '2022-07-20',
            courses = self.course_1,
            universities = self.university
        )
    
    def test_get_enrollment_list(self):
        """Test to list all enrollments / Teste para listar todas as inscrições"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_enrollment_create(self):
        """Test to create enrollment / Teste para criar inscrição"""
        data = {
            "title_enrollment": "Criado Test",
            "date_initial": '2022-01-27',
            "date_final": '2022-03-13',
            "courses": self.course_1.id,
            "universities": self.university.id
        }
        
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_enrollment_update(self):
        """Test to edit enrollment / Teste para editar inscrição"""
        data = {
            "title_enrollment": "Alterado",
            "date_initial": '2022-02-15',
            "date_final": '2022-04-07',
            "courses": self.course_1.id,
            "universities": self.university.id
        }
        response = self.client.put(self.list_url + str(self.enrollment_1.id) + '/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_enrollment_delete(self):
        """Test to delete enrollment (must not delete) / Teste para deletar inscrição (não deve deletar)"""
        response = self.client.delete(self.list_url + str(self.enrollment_1.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)