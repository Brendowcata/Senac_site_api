from uuid import UUID
from django.test import TestCase
from university.models import UniversityModel
from university.serializers import UniversitySerializer


class UniversitySerializerTestCase(TestCase):

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
            is_activate = True,
        )

        self.university_error = UniversityModel(
             name = '123',
            telephone = '333',
            phone_number = '(48) 95555-5555',
            attendance = 'Atendimento de segunda a sexta',
            email = 'teste',
            street = '',
            neighborhood = '',
            city = '155',
            state = '27',
            zip_code = '88888888',
            house_number = 'numer',
            university_image_local = 'Teste',
            is_activate = False,
        )
        self.serializer_error = UniversitySerializer(instance=self.university_error)
        self.serializer = UniversitySerializer(instance=self.university)
    
    def test_check_serialized_fields(self):
        """Test that checks the fields being serialized / Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'telephone', 'phone_number', 'attendance', 'email', 'street', 
        'neighborhood', 'city', 'state','zip_code','house_number', 'localization', 'university_image_local', 'is_activate', 'courses']))

    def test_check_contents_of_serialized_fields(self):
        """Test that checks the contents of serialized fields / Teste que verifica o conteúdo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(UUID(data['id']), self.university.id)
        self.assertEqual(data['name'], self.university.name)
        self.assertEqual(data['telephone'], self.university.telephone)
        self.assertEqual(data['phone_number'], self.university.phone_number)
        self.assertEqual(data['attendance'], self.university.attendance)
        self.assertEqual(data['email'], self.university.email)
        self.assertEqual(data['street'], self.university.street)
        self.assertEqual(data['neighborhood'], self.university.neighborhood)
        self.assertEqual(data['city'], self.university.city)
        self.assertEqual(data['state'], self.university.state)
        self.assertEqual(data['zip_code'], self.university.zip_code)
        self.assertEqual(data['house_number'], self.university.house_number)
        self.assertEqual(data['university_image_local'], self.university.university_image_local)
        self.assertEqual(data['is_activate'], self.university.is_activate)
    
    def test_check_wrong_serialized_content(self):
        """Test that checks the serialized contents that are wrong / Teste que verifica o conteúdo serializado que estão errados"""
        data = self.serializer_error.data
        self.assertNotEqual(data['name'], self.university.name)
        self.assertNotEqual(data['telephone'], self.university.telephone)
        self.assertNotEqual(data['email'], self.university.email)
        self.assertNotEqual(data['street'], self.university.street)
        self.assertNotEqual(data['neighborhood'], self.university.neighborhood)
        self.assertNotEqual(data['city'], self.university.city)
        self.assertNotEqual(data['state'], self.university.state)
        self.assertNotEqual(data['zip_code'], self.university.zip_code)
        self.assertNotEqual(data['house_number'], self.university.house_number)
        self.assertNotEqual(data['university_image_local'], self.university.university_image_local)
        self.assertNotEqual(data['is_activate'], self.university.is_activate)