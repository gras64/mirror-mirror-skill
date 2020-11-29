from mycroft import MycroftSkill, intent_file_handler


class MirrorMirror(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mirror.mirror.intent')
    def handle_mirror_mirror(self, message):
        self.speak_dialog('mirror.mirror')


def create_skill():
    return MirrorMirror()

