from django.test import TestCase
from university.models import UniversityModel

class UniversityModelTestCase(TestCase):

    def setUp(self):
        self.university = UniversityModel(
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
        )

    
    def test_check_university_attributes(self):
        """Test that checks university attributes with default value / Teste que verifica os atributos de universidade com valor padrão"""
        self.assertEqual(self.university.name, 'Nome Faculdade Teste')
        self.assertEqual(self.university.telephone, '(48) 3333-3333')
        self.assertEqual(self.university.phone_number, '(48) 95555-5555')
        self.assertEqual(self.university.attendance, 'Atendimento de segunda a sexta')
        self.assertEqual(self.university.email, 'teste@gmail.com')
        self.assertEqual(self.university.street, 'Rua de teste')
        self.assertEqual(self.university.neighborhood, 'Bairro de teste')
        self.assertEqual(self.university.city, 'Palhoça')
        self.assertEqual(self.university.state, 'Santa Catarina')
        self.assertEqual(self.university.zip_code, '88888-888')
        self.assertEqual(self.university.house_number, '100')
        self.assertEqual(self.university.university_image_local, None)
        self.assertEqual(self.university.is_activate, True)

