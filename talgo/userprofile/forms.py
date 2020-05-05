from django import forms
from django.core.exceptions import ValidationError

from .models import User


class CheckAnketaForm(forms.Form):
    name = forms.CharField(max_length=25)
    lastname = forms.CharField(max_length=50)
    age = forms.IntegerField(min_value=1)
    activity = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    social = forms.CharField(max_length=100, required=False)

    def clean(self):
        check = self.checkExistUser(self.cleaned_data)
        if check['status']:
            print('\nERROR %s' % check['msg'])
            raise ValidationError(check['msg'])
        return self.cleaned_data

    def checkExistUser(self, data):
        """
        Проверка на существование пользователя.
        Проверяется отсутствие/совпадение обязательных полей
        :param data:
        :return:
        """
        out = {}
        users = User.objects.all().values()
        if not users:
            return {'status': False, 'msg': ''}
        for user in users:
            vals = ('name', 'lastname', 'age', 'activity')
            out = {'status': True, 'msg': 'Пользователь уже существует'}
            for el in vals:
                el1 = el
                if el == 'activity': el1 = 'activity_id'

                if not (str(data.get(el, None)) == str(user[el1])):
                    out = {'status': False, 'msg': ''}

                if data.get(el, None) is None:
                    return {'status': True, 'msg': f'''Параметр "{el}" не задан!'''}
        return out

