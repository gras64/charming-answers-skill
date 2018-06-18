from mycroft import MycroftSkill, intent_file_handler


class CharmingAnswers(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('answers.charming.intent')
    def handle_answers_charming(self, message):
        self.speak_dialog('answers.charming')


def create_skill():
    return CharmingAnswers()

