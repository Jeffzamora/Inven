
from inventario.models import *
from django.shortcuts import render, HttpResponse, Http404
from django.contrib.auth.decorators import login_required


@login_required
def media(request):
    if not request.user.is_anonymous:
        app_label = request.POST.get('app_label', request.GET.get('app_label'))
        model_name = request.POST.get('model_name', request.GET.get('model_name'))
        primary_key = request.POST.get('primary_key', request.GET.get('primary_key'))
        model = ContentType.objects.get(app_label=app_label, model=model_name).model_class()
        obj = model.objects.get(id=primary_key)
        media_path = os.path.join(settings.BASE_DIR, 'media', obj.mediafile.name)
        if os.path.exists(media_path):
            if request.user.is_staff or request.user.is_active:
                with open(media_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type='application/pdf')
                    response['Content-Disposition'] = 'inline; filename=%s' % os.path.basename(media_path)
                    response['X-Sendfile'] = media_path
                    return response
    raise Http404
