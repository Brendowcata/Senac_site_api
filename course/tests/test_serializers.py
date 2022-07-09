from uuid import UUID
from django.test import TestCase
from course.models import CourseModel
from course.serializers import CourseSerializer


class CourseSerializerTestCase(TestCase):

    def setUp(self):
        self.course = CourseModel(
            name = 'Curso 1',
            course_type = 'GRADUACAO',
            course_objective = 'Teste',
            curriculum = None,
            completion_profile = 'Teste',
            duration_time = 2400,
            occupation_area = 'Teste',
            course_image = None,
            is_activate = True,
            modality = 'EAD',
            mec_score = 'MEC4'
        )

        self.course_error = CourseModel(
            name = 'Curso 2',
            course_type = 'POS_GRADUACAO',
            course_objective = 'Teste12',
            curriculum = None,
            completion_profile = 'Teste121',
            duration_time = 1000,
            occupation_area = 'Teste12',
            course_image = None,
            is_activate = False,
            modality = 'PRESENCIAL',
            mec_score = 'MEC5'
        )
        self.serializer_error = CourseSerializer(instance=self.course_error)
        self.serializer = CourseSerializer(instance=self.course)
    
    def test_check_serialized_fields(self):
        """Test that checks the fields being serialized / Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'course_type', 'course_objective', 'curriculum', 'completion_profile', 'duration_time', 
        'occupation_area', 'course_image', 'is_activate','modality','mec_score', 'enrollments', 'school_programs']))

    def test_check_contents_of_serialized_fields(self):
        """Test that checks the contents of serialized fields / Teste que verifica o conteúdo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(UUID(data['id']), self.course.id)
        self.assertEqual(data['name'], self.course.name)
        self.assertEqual(data['course_type'], self.course.course_type)
        self.assertEqual(data['course_objective'], self.course.course_objective)
        self.assertEqual(data['curriculum'], self.course.curriculum)
        self.assertEqual(data['completion_profile'], self.course.completion_profile)
        self.assertEqual(data['duration_time'], self.course.duration_time)
        self.assertEqual(data['occupation_area'], self.course.occupation_area)
        self.assertEqual(data['course_image'], self.course.course_image)
        self.assertEqual(data['is_activate'], self.course.is_activate)
        self.assertEqual(data['modality'], self.course.modality)
        self.assertEqual(data['mec_score'], self.course.mec_score)
    
    def test_check_wrong_serialized_content(self):
        """Test that checks the serialized contents that are wrong / Teste que verifica o conteúdo serializado que estão errados"""
        data = self.serializer_error.data
        self.assertNotEqual(data['name'], self.course.name)
        self.assertNotEqual(data['course_type'], self.course.course_type)
        self.assertNotEqual(data['course_objective'], self.course.course_objective)
        self.assertNotEqual(data['completion_profile'], self.course.completion_profile)
        self.assertNotEqual(data['duration_time'], self.course.duration_time)
        self.assertNotEqual(data['occupation_area'], self.course.occupation_area)
        self.assertNotEqual(data['is_activate'], self.course.is_activate)
        self.assertNotEqual(data['modality'], self.course.modality)
        self.assertNotEqual(data['mec_score'], self.course.mec_score)