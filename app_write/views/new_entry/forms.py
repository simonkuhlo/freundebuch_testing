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
        models.Answer,
        fields = [question.type],
        )
    print(answerform.fields)
    return answerform

class create_author(ModelForm):
    class Meta:
        model = models.Author
        fields = "__all__"
