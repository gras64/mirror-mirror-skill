from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder
import random


class MirrorMirror(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.gender_value = self.translate_namedvalues('gender.value')
        

    @intent_handler(IntentBuilder("handlermirror").require("mirror").
                    one_of("beautiful", "bad").optionally("man").optionally("woman").optionally("location").build())
    def handle_mirror_mirror(self, message):
        location = ""
        bad = ""
        beautiful = ""
        if message.data.get("location", False):
            for word in message.data['utterance'].split(" "):
                if self.voc_match(word, "location"):
                    location = word
                    break
                location = ""
        if message.data.get("beautiful", False):
            for word in message.data['utterance'].split(" "):
                if self.voc_match(word, "beautiful"):
                    beautiful = word
                    break
        if message.data.get("bad", False):
            for word in message.data['utterance'].split(" "):
                if self.voc_match(word, "beautiful"):
                    bad = word
                    break        
        if message.data.get("man", False):
            gender = "male"
        elif message.data.get("woman", False):
            gender = "female"
        else:
            gender = ""
        gender = self.gender_value[gender]
        if message.data.get("beautiful", False):
            l = ["friendly"]
            if self.settings.get('random', True):
                l = ["friendly", "the.second"]
            self.speak_dialog(random.choice(l), data={"gender":gender, "beautiful":beautiful, "location":location})
        else:
            self.speak_dialog('unfriendly', data={"gender":gender, "bad":bad, "location":location})

    def shutdown(self):
        super(MirrorMirror, self).shutdown()

def create_skill():
    return MirrorMirror()

