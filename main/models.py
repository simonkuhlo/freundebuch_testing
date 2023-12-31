from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return(str(self.name))

class Interview(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return(str(self.name))
    
class Entry(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    interview = models.ForeignKey(Interview, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', 'created']

    def __str__(self):
        return(str(self.author))
    

question_type_choices = [
("text" , "text"),
("longtext" , "longtext"),
("image" , "image"),
("boolean" , "boolean"),
]

class Question(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    value_de = models.CharField(max_length=200)
    value_en = models.CharField(max_length=200)
    description_de = models.CharField(max_length=500)
    description_en = models.CharField(max_length=500)
    type = models.CharField(max_length=100, choices=question_type_choices) #FileUpload, Interview, AboutMe
    sort_id = models.SmallIntegerField(null=True, blank=True)
    required = models.BooleanField(default=False)

    def __str__(self):
        return(str(self.name))
    
class Answer(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

    answer_text = models.TextField(null=True, blank=True)
    answer_image = models.ImageField(upload_to="upload/", default="no_image.jpg", blank=True)
    answer_boolean = models.BooleanField(null=True, blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return(str(self.entry))