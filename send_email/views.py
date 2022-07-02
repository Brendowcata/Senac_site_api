from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from course.models import CourseModel
from send_email.models import Send_EmailModel
from django.core.mail import send_mail
from datetime import datetime

from send_email.serializers import Send_EmailSerializer
from university.models import UniversityModel

class Send_EmailViewSet(viewsets.ModelViewSet):
    queryset = Send_EmailModel.objects.all()
    serializer_class = Send_EmailSerializer
    http_method_names = ['post',]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = {
            "name":serializer.data['name'],
            "phone_number":serializer.data['phone_number'],
            "email":serializer.data['email'],
            "email_university":serializer.data['email_university'],
            "message":serializer.data['message'],
            "courses":serializer.data['courses'],
            "universities":serializer.data['universities']
        }
        obj_university = get_object_or_404(UniversityModel, pk=data["universities"])
        message =  f'Faculdade: {obj_university}\nNome: {data["name"]}\nE-mail: {data["email"]}\nTelefone: {data["phone_number"]}'
        if(serializer.data['courses'] != None): 
            obj_course = get_object_or_404(CourseModel, pk=data['courses'])
            send_mail(f'{data["name"]} - {datetime.today().strftime("%d-%m-%y")} Senac SC - Interesse/Dúvidas Curso {obj_course}',
           f'{message}\nCurso: {obj_course}\n\n{data["message"]}', 'adsgrupoapi@gmail.com', [data['email_university']])
        else:
            send_mail(f'{data["name"]} - {datetime.today().strftime("%d-%m-%y")} Senac SC',
            f'{message}\n\n{data["message"]}', 'adsgrupoapi@gmail.com', [data['email_university']])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

