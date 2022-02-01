from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone

from django.views import View
# Create your views here.

class IndexView(View):
	def get(self,request,*args,**kwargs):
		latest_question_list = Question.objects.order_by('-pub_date')[:5]
		template_name = 'polls/index.html'
		context_object_name = {'latest_question_list': latest_question_list}
		return render(request,template_name,context_object_name)
				
class DetailView(View):
    def get(self,request,*args,**kwargs):
    	question = get_object_or_404(Question, pk=self.kwargs['question_id'])
    	template_name = 'polls/detail.html'
    	context_object_name = {'question':question}
    	return render(request,template_name,context_object_name)
	   	
class ResultsView(View):
	def get(self,request,*args,**kwargs):
		question = get_object_or_404(Question, pk=self.kwargs['question_id'])
		template_name = 'polls/results.html'
		context_object_name = {'question':question}
		return render(request,template_name,context_object_name)
		
'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
'''

'''def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")'''
'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)'''
'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))'''

'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
'''
 
'''def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)'''
'''def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})'''


 

def vote(request, question_id):
    '''return HttpResponse("You're voting on question %s." % question_id)'''
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        
