from .forms import carrentalForm
from django.views.generic.edit import FormView
import amadeus
from amadeus.amadeus import Cars
class carrentalView(FormView):
    template_name = 'form.html'
    form_class = carrentalForm
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        pick_up_date = request.POST.get('pick_up_date',None)
        drop_off_date = request.POST.get('drop_off_date',None)
        location = request.POST.get('location',None)
        currency = request.POST.get('currency',None)
        language = request.POST.get('language',None)

        cars = Cars('jJo9Nv9JifWAIXFanTiV2tSAXRHFHEWc')
        resp = cars.search_airport(
            pick_up='2017-12-18',
            drop_off='2017-12-23',
            location='BLR',
            currency='USD',
            lang='EN')
        context['from']=resp
        return self.render_to_response(context)

