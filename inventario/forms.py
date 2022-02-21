from django import forms
from inventario.widgets import *
from django.contrib.auth.forms import UserChangeForm
from datetime import datetime
from inventario.models import *
from mrd.models import *


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class CajaForm(forms.ModelForm):
    template_data = forms.CharField(required=False, label="Datos de la etiqueta",
                                    widget=FormWidget)

    total_folders = forms.IntegerField(label="Total de folderes en la caja", initial="0", required=False,
                                       widget=forms.NumberInput(
                                           attrs={
                                               'readonly': 'readonly'
                                           }
                                       ))
    total_in = forms.IntegerField(label="Total de folderes status IN", initial="0", required=False,
                                  widget=forms.NumberInput(
                                      attrs={
                                          'readonly': 'readonly'
                                      }
                                  ))
    total_out = forms.IntegerField(label="Total de folderes status OUT", initial="0", required=False,
                                   widget=forms.NumberInput(
                                       attrs={
                                           'readonly': 'readonly'
                                       }
                                   ))
    total_delete = forms.IntegerField(label="Total de folderes status DELETE", initial="0", required=False,
                                      widget=forms.NumberInput(
                                          attrs={
                                              'readonly': 'readonly'
                                          }
                                      ))
    rc = forms.CharField(required=False, label="Número RC", widget=forms.TextInput(
        attrs={
            'readonly': 'readonly'
        }
    ))

    class Meta:
        model = Caja
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        updated_initial = {}
        if instance:
            updated_initial['template_data'] = instance
            updated_initial['Sede'] = instance.Sede
            updated_initial['Area'] = instance.Area
            updated_initial['template'] = instance.template
            updated_initial['folders'] = instance.folders()
            updated_initial['total_folders'] = instance.total_folders
            updated_initial['total_in'] = instance.total_in
            updated_initial['total_out'] = instance.total_out
            updated_initial['total_delete'] = instance.total_delete
        kwargs.update(initial=updated_initial)
        super().__init__(*args, **kwargs)
        self.fields['rc'].widget.attrs['readonly'] = 'readonly'


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'


class DocForm(forms.ModelForm):
    image_preview = forms.Field(label="", required=False, widget=ImagePreviewWidget(
        attrs={
            'mediafile': 'mediafile',
            'modelname': 'document',
        }
    ))

    class Meta:
        model = Document
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        updated_initial = {}
        if instance:
            updated_initial['template_data'] = instance
            updated_initial['image_preview'] = instance
        kwargs.update(initial=updated_initial)
        super().__init__(*args, **kwargs)
