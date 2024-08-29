from django.db import models

class Questions(models.Model):
    QUESTION_CHOICES = [
        ("Text", "Text"),
        ("Bigtext", "Bigtext"),
        ("Radio", "Radio"),
        ("Checkbox", "Checkbox"),
    ]
    
    question = models.CharField(max_length=100)
    question_type = models.CharField(max_length=50, choices=QUESTION_CHOICES, default="Text")

    def __str__(self):
        return f"{self.question} ({self.question_type})"

class Options(models.Model):
    question = models.ForeignKey(Questions, related_name="options", on_delete=models.CASCADE)
    option_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.option_name

class CustomerFeedback(models.Model):
    question = models.ManyToManyField(Questions)
    feedback_text = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Feedback ID {self.id} on {self.question.count()} questions"

class Response(models.Model):
    feedback = models.ForeignKey(CustomerFeedback, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    response_text = models.TextField(null=True, blank=True)
    selected_options = models.ManyToManyField(Options, blank=True)
    
    def __str__(self):
        return f"Response for {self.question}"
