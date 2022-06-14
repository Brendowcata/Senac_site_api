from os import stat
from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework.test import APITestCase
from university.models import UniversityModel
from django.urls import reverse
from rest_framework import status

class UniversityTestCase(APITestCase):

    def setUp(self):
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
            university_image_local = '',
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
            "telephone": "",
            "phone_number": "(48) 99999-9999",
            "attendance": "Teste Post",
            "email": "emailteste@gmail.com",
            "street": "Rua de Teste Post",
            "neighborhood": "Bairro de Teste Post",
            "city": "Palhoça",
            "state": 'SC',
            "zip_code": "88111-120",
            "house_number": "122",
            "university_image_local": '',
            "is_activate": True,
            "courses": []
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
            "university_image_local": '',
            "is_activate": False
        }
        response = self.client.put('/cursos//', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)