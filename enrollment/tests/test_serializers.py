from uuid import UUID
from django.test import TestCase
from enrollment.models import EnrollmentModel
from course.models import CourseModel
from university.models import UniversityModel
from enrollment.serializers import EnrollmentSerializer


class EnrollmentSerializerTestCase(TestCase):

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

        self.enrollment = EnrollmentModel(
            title_enrollment = "teste12",
            date_initial = '2022-06-30',
            date_final = '2022-07-20',
            courses = self.course_1,
            universities = self.university
        )

        self.enrollment_error = EnrollmentModel(
            title_enrollment = "teste",
            date_initial = '2022-08-10',
            date_final = '2022-09-25',
            courses = self.course_1,
            universities = self.university
        )
        self.serializer_error = EnrollmentSerializer(instance=self.enrollment_error)
        self.serializer = EnrollmentSerializer(instance=self.enrollment)
    
    def test_check_serialized_fields(self):
        """Test that checks the fields being serialized / Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title_enrollment', 'date_initial', 'date_final', 'courses', 'universities']))

    def test_check_contents_of_serialized_fields(self):
        """Test that checks the contents of serialized fields / Teste que verifica o conteúdo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(UUID(data['id']), self.enrollment.id)
        self.assertEqual(data['title_enrollment'], self.enrollment.title_enrollment)
        self.assertEqual(data['date_initial'], self.enrollment.date_initial)
        self.assertEqual(data['date_final'], self.enrollment.date_final)
        self.assertEqual(data['courses'], self.enrollment.courses.id)
        self.assertEqual(data['universities'], self.enrollment.universities.id)
    
    def test_check_wrong_serialized_content(self):
        """Test that checks the serialized contents that are wrong / Teste que verifica o conteúdo serializado que estão errados"""
        data = self.serializer_error.data
        self.assertNotEqual(data['title_enrollment'], self.enrollment.title_enrollment)
        self.assertNotEqual(data['date_initial'], self.enrollment.date_initial)
        self.assertNotEqual(data['date_final'], self.enrollment.date_final)