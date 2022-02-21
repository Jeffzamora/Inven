from django.forms import Widget, modelform_factory
from inventario.models import *
from etiqueta.models import *
from user.models import *


# class FormWidget(Widget):
#     template_name = 'widgets/form_template.html'
#
#     def format_value(self, value):
#         return value
#
#
# class AreaWidget(Widget):
#     template_name = 'widgets/department.html'
#
#     def format_value(self, value):
#         if value:
#             return Area.objects.get(id=value)
#         return value
#
#
# class FormBoxWidget(Widget):
#     template_name = 'widgets/form-box.html'
#
#     def format_value(self, value):
#         if value:
#             return FormBox.objects.get(id=value)
#         return value
#
#
# class FormFileWidget(Widget):
#     template_name = 'widgets/form-file.html'
#
#     def format_value(self, value):
#         if value:
#             return FormFile.objects.get(id=value)
#         return value
#
#
# class FormDocWidget(Widget):
#     template_name = 'widgets/form-doc.html'
#
#     def format_value(self, value):
#         if value:
#             return FormDoc.objects.get(id=value)
#         return value
#
#
# class CajaWidget(Widget):
#     template_name = 'widgets/box.html'
#
#     def format_value(self, value):
#         if value:
#             return Caja.objects.get(id=value)
#         return value
#
#
# class FolderWidget(Widget):
#     template_name = 'widgets/file.html'
#
#     def format_value(self, value):
#         if value:
#             return Folder.objects.get(id=value)
#         return value
#
#
# class GrpTableWidget(Widget):
#     template_name = "widgets/grp-table.html"
#
#     def _form(self):
#         return modelform_factory(self.attrs['model'], fields=self.attrs['fields'])
#
#     def format_value(self, value):
#         return value
#
#     def build_attrs(self, base_attrs, extra_attrs=None):
#         extra_attrs.update({'form': self._form()})
#         return super().build_attrs(base_attrs, extra_attrs=extra_attrs)
#
#
# class GrpSimpleTableWidget(Widget):
#     template_name = "widgets/grp-simple-table.html"
#
#     def format_value(self, value):
#         return value


class ImagePreviewWidget(Widget):
    template_name = "widgets/grp-image-preview.html"

    def format_value(self, value):
        return value


