from django.contrib.auth.forms import UserChangeForm
from user.models import *


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        updated_initial = {}
        if instance and instance.Sede:
            self.base_fields['Area'].choices = instance.Sede.Area
        kwargs.update(initial=updated_initial)
        super().__init__(*args, **kwargs)
