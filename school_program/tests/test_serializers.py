from uuid import UUID
from django.test import TestCase
from school_program.models import School_ProgramModel
from school_program.serializers import School_ProgramSerializer


class School_ProgramSerializerTestCase(TestCase):

    def setUp(self):
        self.school_program = School_ProgramModel(
            phase = 1,
            phase_time = 1400,
        )

        self.school_program_error = School_ProgramModel(
            phase = 2,
            phase_time = 2000,
        )
        self.serializer_error = School_ProgramSerializer(instance=self.school_program_error)
        self.serializer = School_ProgramSerializer(instance=self.school_program)
    
    def test_check_serialized_fields(self):
        """Test that checks the fields being serialized / Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'phase', 'phase_time', 'courses', 'subjects']))

    def test_check_contents_of_serialized_fields(self):
        """Test that checks the contents of serialized fields / Teste que verifica o conteúdo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(UUID(data['id']), self.school_program.id)
        self.assertEqual(data['phase'], self.school_program.phase)
        self.assertEqual(data['phase_time'], self.school_program.phase_time)
    
    def test_check_wrong_serialized_content(self):
        """Test that checks the serialized contents that are wrong / Teste que verifica o conteúdo serializado que estão errados"""
        data = self.serializer_error.data
        self.assertNotEqual(data['phase'], self.school_program.phase)
        self.assertNotEqual(data['phase_time'], self.school_program.phase_time)