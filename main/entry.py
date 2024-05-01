from main import models

class Entry():
    db_object:models.Entry = None
    author_db_object:models.Author = None
    
    
    name:str = None
    description:str = None
    image:models.Answer.answer_image = None
    
    interview_elements_db = {}
    
    created = None
    last_edit =  None
    
    def __init__(self, entry_id) -> None:
        db_connection = EntryDB(entry_id)
        
        self.db_object = db_connection.entry
        self.author_db_object = db_connection.author
        self.image= db_connection.get_imagepath()
        self.name = db_connection.get_name()
        self.description = db_connection.get_description()
        
        self.interview_elements_db = db_connection.get_interview_elements()
        
        self.created = db_connection.get_created()
        self.last_edit = db_connection.get_last_edit()
    
    def print_interview_elements(self):
        print(self.interview_elements)


class EntryDB():
    entry:models.Entry = None
    author:models.Author = None
    
    def __init__(self, entry_id):
        self.entry = models.Entry.objects.get(id=entry_id)
        self.author = self.entry.author
    def get_author_id(self):
        return self.author.id
    def get_name(self):
        return self.author.name
    def get_description(self):
        description = None
        description_question = models.Question.objects.get(name = "about_me")
        db_object = models.Answer.objects.filter(entry = self.entry, question = description_question.id).first()
        if db_object:
            description = db_object.answer_text
        return description
    def get_imagepath(self):
        image = None
        image_question = models.Question.objects.get(name = "profile_picture")
        db_object = models.Answer.objects.filter(entry = self.entry, question = image_question.id).first()
        if db_object:
            image = db_object.answer_image
        return image
    def get_interview_elements(self):
        interview_elements = {}
        all_questions = models.Question.objects.filter(interview_element = True)
        for question in all_questions:
            answer = models.Answer.objects.filter(entry=self.entry.id, question=question.id).first()
            if answer:
                interview_elements[question] = answer
        return interview_elements
    def get_created(self):
        return self.entry.created
    def get_last_edit(self):
        return self.entry.updated