from mycroft import MycroftSkill, intent_file_handler


class CharmingAnswers(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('answers.stupid.intent')
    def handle_answers_stupid(self, message):
        self.speak_dialog('answers.stupid')

    @intent_file_handler('who.thebest.intent')
    def handle_answers_thebest(self, message):
        self.speak_dialog('who.thebest')


def create_skill():
    return CharmingAnswers()

