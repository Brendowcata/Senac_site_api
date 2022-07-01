from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from subject.models import SubjectModel
from django.urls import reverse
from rest_framework import status

class SubjectTestCase(APITestCase):


    def setUp(self):
        self.password = 'admin123'
        self.my_admin = User.objects.create_superuser('admin', 'myemail@test.com', self.password)
        self.token = self.client.post('/rest-auth-token/', {'username': 'admin', 'password': 'admin123'}, format="json")
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.data["token"]}')

        self.list_url = reverse('Subject-list')
        self.subject_1 = SubjectModel.objects.create(
            name = 'Desenvolvimento Web',
            description = 'Teste descrição',
        )
    
    def test_get_subject_list(self):
        """Test to list all subjects / Teste para listar todas as matérias"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_subject_create(self):
        """Test to create subject / Teste para criar matéria"""
        data = {
            "name": "Materia de Teste",
            "description": "Testando post",
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_subject_update(self):
        """Test to edit subject / Teste para editar matéria"""
        data = {
            "name": "Alterando Nome",
            "description": "Alterando descrição"
        }
        response = self.client.put(self.list_url + str(self.subject_1.id) + '/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_subject_delete(self):
        """Test to delete subject  / Teste para deletar matéria"""
        response = self.client.delete(self.list_url + str(self.subject_1.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)