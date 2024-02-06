from . import models


class Static():
    def gettext(language:str, textname:str):
        textobject = models.SystemMessage.objects.get(name = textname)
        language_attr = f"value_{language}"
        text = getattr(textobject, language_attr)
        return text
        
class Write():
    class NewEntry():
        class Interview():
            
            def heading(language):
                text = Static.gettext(language, "write.new_entry.interview.heading")
                return text

            def question_text(language, question):
                language_attr = f"value_{language}"
                text = getattr(question, language_attr)
                return text
            
            def question_desc(language, question):
                language_attr = f"description_{language}"
                text = getattr(question, language_attr)
                return text
            
        class ConfirmMail():

            def text_1(language):
                text = Static.gettext(language, "write.new_entry.confirm_mail.text1")
                return text