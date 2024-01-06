
def get_fields_for_question_type(question_type):
    match question_type:
        case "text":
            fields = ['answer_text']
        case "longtext":
            fields = ['answer_longtext']
        case "image":
            fields = ['answer_image']
        case "boolean":
            fields = ['answer_boolean']
        case _:
            return
    return fields