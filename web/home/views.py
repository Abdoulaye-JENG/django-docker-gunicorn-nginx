from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Context before 2: ", dir(context['view']))
        print("Context before 3: ", context['view'].get_template_names())  
        context["statement"] =  "Nice to meet you."
        print("Context after: ", context  )
        return context

    def print_me(self, *args, **kwargs):
        return "U're printed."
