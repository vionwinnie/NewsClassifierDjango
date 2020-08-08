from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.urls import reverse

from .models import News,Category
from .forms import NameForm
from .serving import predict

# Create your views here.
def index(request):
    latest_news_list = News.objects.order_by('-pub_date')[:5]
    category = Category.objects.order_by('-category')[:5]
    ## Reading from template subdirectories 
    #template = loader.get_template('classifier/index.html')
    context = {
            'latest_question_list':latest_news_list,
            'latest_category_list':category
            }
    ## Create the http based on the response
    #return HttpResponse(template.render(context,request))
    
    ## Using render as shortcut
    return render(request,'classifier/index.html',context)

def results(request, news_id):

    try:
        news = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404("News does not exist")

    return render(request, 'classifier/results.html', {'news': news})

def enter_text(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            main_text = form.cleaned_data['enter_text']

            # Predict Model
            pred_category,pred_score,all_scores,viz = predict.predict(main_text)
            #pred_score = 0.5
            #pred_category = 'Sport'

            # Save News Data to Sqlite
            q = News(news_text=main_text, pub_date=timezone.now())
            q.save()
            q_id = q.id

            # Save Predict Category to Sqlite
            pred_category = Category(category=pred_category,
                    prob_score=pred_score,news_id=q_id)
            pred_category.save()
            return HttpResponseRedirect(reverse('results', args=(q.id,)))
#            return HttpResponseRedirect('{}/results'.format(q_id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'classifier/enter_text.html', {'form': form})


