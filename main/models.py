from django.db import models
import colorfield.fields as colorfield

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
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
    preview_image = models.ImageField(upload_to="upload", default="no_image.webp", blank=True)
    bg_color = colorfield.ColorField(default='#FF0000')
    language = models.CharField(max_length=50)
    visible = models.BooleanField(default = False)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', 'created']
        
    def __str__(self):
        return(str(self.author))
    

question_type_choices = [
("answer_text", "text"),
("answer_image", "image"),
("answer_color", "color"),
("answer_boolean", "boolean"),
]

class Question(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    
    value_de = models.CharField(max_length=200)
    description_de = models.CharField(max_length=500)
    
    value_en = models.CharField(max_length=200)
    description_en = models.CharField(max_length=500)
    
    type = models.CharField(max_length=100, choices=question_type_choices) #FileUpload, Interview, AboutMe
     
    sort_id = models.SmallIntegerField()
    
    special = models.BooleanField(default=False)# clarify if special field like name, fav color, etc.
    show_in_friendbook = models.BooleanField(default=True)
    required = models.BooleanField(default=False)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['interview', 'sort_id', 'name'], name='unique_question')
        ]

    def __str__(self):
        return(str(self.name))
    
class Answer(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

    answer_text = models.TextField(null=True, blank=True)
    answer_image = models.ImageField(upload_to="upload", default="no_image.webp", blank=True)
    answer_boolean = models.BooleanField(null=True, blank=True)
    answer_color = colorfield.ColorField(default=None, format="rgb", null=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return(str(self.entry))

class SystemMessage(models.Model):
    name = models.CharField(max_length=100, unique = True)

    value_en = models.TextField()
    value_de = models.TextField(blank=True)
    
    def __str__(self):
        return(str(self.name))
    
    def save(self, *args, **kwargs):
        if not self.value_de:
            self.value_de = self.value_en
        super().save(*args, **kwargs)