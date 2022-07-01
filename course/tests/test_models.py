from django.test import TestCase
from course.models import CourseModel

class CourseModelTestCase(TestCase):

    def setUp(self):
        self.course = CourseModel(
            name = 'Curso 1',
            course_objective = 'Teste',
            curriculum = None,
            completion_profile = 'Teste',
            duration_time = 2400,
            occupation_area = 'Teste',
            course_image = None,
        )

    
    def test_check_course_attributes(self):
        """Test that checks course attributes with default value / Teste que verifica os atributos de curso com valor padrão"""
        self.assertEqual(self.course.name, 'Curso 1')
        self.assertEqual(self.course.course_type, 'GRADUACAO')
        self.assertEqual(self.course.course_objective, 'Teste')
        self.assertEqual(self.course.curriculum, None)
        self.assertEqual(self.course.completion_profile, 'Teste')
        self.assertEqual(self.course.duration_time, 2400)
        self.assertEqual(self.course.occupation_area, 'Teste')
        self.assertEqual(self.course.course_image, None)
        self.assertEqual(self.course.is_activate, True)
        self.assertEqual(self.course.modality, 'PRESENCIAL')
        self.assertEqual(self.course.mec_score, 'MEC5')

