from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from university.models import UniversityModel
from django.urls import reverse
from rest_framework import status

class UniversityTestCase(APITestCase):


    def setUp(self):
        self.password = 'admin123'
        self.my_admin = User.objects.create_superuser('admin', 'myemail@test.com', self.password)
        self.token = self.client.post('/rest-auth-token/', {'username': 'admin', 'password': 'admin123'}, format="json")
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.data["token"]}')

        self.list_url = reverse('University-list')
        self.university_1 = UniversityModel.objects.create(
            name = 'Senac Palhoça',
            telephone = '(48) 3333-3333',
            phone_number = '(48) 99999-9999',
            attendance = 'Atendimento de segunda a sexta das 8h até 18h',
            email = 'senacteste@gmail.com',
            street = 'Rua João Pereira dos Santos',
            neighborhood = 'Ponte do Imaruim',
            city = 'Palhoça',
            state = 'SC',
            zip_code = '88130-475',
            house_number = '303',
            university_image_local = None,
            is_activate = True
        )
    
    def test_get_university_list(self):
        """Test to list all universities / Teste para listar todas as universidades"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_university_create(self):
        """Test to create university / Teste para criar universidade"""
        data = {
            "name": "Faculdade para Teste Post",
            "telephone": "(48) 3333-3333",
            "phone_number": "(48) 99999-9999",
            "attendance": "Teste Post",
            "email": "emailteste@gmail.com",
            "street": "Rua de Teste Post",
            "neighborhood": "Bairro de Teste Post",
            "city": "Palhoça",
            "state": 'SC',
            "zip_code": "88111-120",
            "house_number": "122",
            "is_activate": True,
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_university_update(self):
        """Test to edit university / Teste para editar universidade"""
        data = {
            "name": "Senac Palhoça",
            "telephone": "(48) 3333-3333",
            "phone_number": "(48) 99999-9999",
            "attendance": "Atendimento de segunda a sexta das 8h até 18h, aos sábados até 12h",
            "email": "senacteste@gmail.com",
            "street": "Rua João Pereira dos Santos",
            "neighborhood": "Ponte do Imaruim",
            "city": "Palhoça",
            "state": 'SC',
            "zip_code": "88130-475",
            "house_number": "303",
            "is_activate": False
        }
        response = self.client.put(self.list_url + str(self.university_1.id) + '/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_university_delete(self):
        """Test to delete university (must not delete) / Teste para deletar universidade (não deve deletar)"""
        response = self.client.delete(self.list_url + str(self.university_1.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)