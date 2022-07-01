from uuid import UUID
from django.test import TestCase
from subject.models import SubjectModel
from subject.serializers import SubjectSerializer


class SubjectSerializerTestCase(TestCase):

    def setUp(self):
        self.subject = SubjectModel(
            name = 'Desenvolvimento Web',
            description = 'teste',
        )

        self.subject_error = SubjectModel(
            name = 'Desenvolvimento Desktop',
            description = 'teste123',
        )

        self.serializer_error = SubjectSerializer(instance=self.subject_error)
        self.serializer = SubjectSerializer(instance=self.subject)
    
    def test_check_serialized_fields(self):
        """Test that checks the fields being serialized / Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'description']))

    def test_check_contents_of_serialized_fields(self):
        """Test that checks the contents of serialized fields / Teste que verifica o conteúdo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(UUID(data['id']), self.subject.id)
        self.assertEqual(data['name'], self.subject.name)
        self.assertEqual(data['description'], self.subject.description)
    
    def test_check_wrong_serialized_content(self):
        """Test that checks the serialized contents that are wrong / Teste que verifica o conteúdo serializado que estão errados"""
        data = self.serializer_error.data
        self.assertNotEqual(data['name'], self.subject.name)
        self.assertNotEqual(data['description'], self.subject.description)