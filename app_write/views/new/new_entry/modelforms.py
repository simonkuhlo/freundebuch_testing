from django.forms import modelform_factory
from django.forms import ModelForm
from main import models


class RequiredForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequiredForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True


def get_answerform(question):
    answerform = modelform_factory(
        model = models.Answer,
        fields = [question.type],
        )
    answerform.instance.question = question
    return answerform