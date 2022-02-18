from django import forms
from mrd.widgets import *
from django.contrib.auth.forms import UserChangeForm
from datetime import datetime
from mrd.models import *
from inventario.widgets import *


# class ProcesoForm(forms.ModelForm):
#     Sede = forms.CharField(max_length=300, label="Sede", required=False, widget=forms.TextInput(
#         attrs={
#             'readonly': 'readonly'
#         }
#     ))
#
#     class Meta:
#         model = Proceso
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         instance = kwargs.get('instance', None)
#         updated_initial = {}
#         if instance:
#             updated_initial['Sede'] = instance.Sede
#             updated_initial['Area'] = instance.Area
#         kwargs.update(initial=updated_initial)
#         super().__init__(*args, **kwargs)
#
#
# class SerieForm(forms.ModelForm):
#     Sede = forms.CharField(max_length=300, label="Sede", required=False, widget=forms.TextInput(
#         attrs={
#             'readonly': 'readonly'
#         }
#     ))
#
#     Area = forms.CharField(max_length=300, label="Area", required=False, widget=forms.TextInput)
#
#     Proceso = forms.ModelChoiceField(queryset=Proceso.objects.all(),
#                                         label="Departamento",
#                                         widget=AreaWidget({
#                                             'customer_selector': '#id_customer'
#                                         }))
#
#     class Meta:
#         model = Serie
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         instance = kwargs.get('instance', None)
#         updated_initial = {}
#         if instance:
#             updated_initial['Sede'] = instance.Sede
#             updated_initial['Area'] = instance.Area
#         kwargs.update(initial=updated_initial)
#         super().__init__(*args, **kwargs)
#
#
# class sub_SerieForm(forms.ModelForm):
#     Sede = forms.CharField(max_length=300, label="Sede", required=False, widget=forms.TextInput(
#         attrs={
#             'readonly': 'readonly'
#         }
#     ))
#
#     Area = forms.CharField(max_length=300, label="Area", required=False, widget=forms.TextInput(
#         attrs={
#             'readonly': 'readonly'
#         }
#     ))
#
#     Proceso = forms.CharField(max_length=300, label="Proceso", required=False, widget=forms.TextInput(
#         attrs={
#             'readonly': 'readonly'
#         }
#     ))
#
#     class Meta:
#         model = Serie
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         instance = kwargs.get('instance', None)
#         updated_initial = {}
#         if instance:
#             updated_initial['Sede'] = instance.Sede
#             updated_initial['Area'] = instance.Area
#             updated_initial['Proceso'] = instance.Proceso
#         kwargs.update(initial=updated_initial)
#         super().__init__(*args, **kwargs)
