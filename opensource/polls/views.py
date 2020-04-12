from django.shortcuts import get_object_or_404, render

from .models import Question, Choice, Test
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

def index(request):
    latest_test_list = Test.objects.order_by('-pub_date')[:10]
    context = {'latest_test_list': latest_test_list}
    return render(request, 'polls/index.html', context)

def detail(request, test_id):
    try:
        test = Test.objects.get(pk=test_id)
    except Test.DoesNotExist:
        raise Http404("Quiz was not found...")
    return render(request, 'polls/detail.html', {'test': test})

def results(request, test_id ,score):
    print(score)
    test = get_object_or_404(Test, pk=test_id)
    return render(request, 'polls/results.html', {'test': test, 'score': score})
    
def vote(request, test_id):
    # print(request.POST['choice'])
    test = get_object_or_404(Test, pk=test_id)
    try:
        questions = Question.objects.filter(test=test.id)
        selected_choice = []
        for question in questions:
            key = request.POST[str(question.id)]
            selected_choice.append(test.choice_set.get(pk=key))
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'test': test,
            'error_message': "You didn't select a choice.",
        })
    else:
        score = 0
        print(selected_choice)
        numQuestions = len(test.question_set.all())
        for choice in selected_choice:
            print(choice.question)
            question = Question.objects.get(pk=choice.question.id)
            choice.votes += 1
            question.total_votes += 1
            choice.save()
            question.save()
            if choice.isCorrect == True:
                print(choice.question)
                score += 1
            choices = question.choice_set.all()
            for choice in choices:
                choice.vote_percent = ((choice.votes/question.total_votes)*100)
                choice.save()
        print(score)
        score = round((score/numQuestions)*100)
                
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(test.id, score)))