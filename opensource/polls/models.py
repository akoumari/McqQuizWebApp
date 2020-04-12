from django.db import models

class Test(models.Model):
    test_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.test_text

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    total_votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote_percent = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    isCorrect = models.BooleanField(default=False)
    def __str__(self):
        return self.choice_text