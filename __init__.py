from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder


class MirrorMirror(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.gender_value = self.translate_namedvalues('gender.value')

    @intent_handler(IntentBuilder("handlermirror").require("mirror").
                    one_of("beautiful", "bad").optionally("man").optionally("woman").optionally("location").build())
    def handle_mirror_mirror(self, message):
        if message.data.get("man", False):
            gender = "male"
        elif message.data.get("woman", False):
            gender = "female"
        else:
            gender = ""
        gender = self.gender_value[gender]
        if message.data.get("beautiful", False):
            self.speak_dialog('friendly', data={"gender":gender, "beautiful":self.translate("beautiful", data=None)})
        else:
            self.speak_dialog('unfriendly', data={"gender":gender, "bad" :self.translate("bad", data=None)})

    def shutdown(self):
        super(MirrorMirror, self).shutdown()

def create_skill():
    return MirrorMirror()

