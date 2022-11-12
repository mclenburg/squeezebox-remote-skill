from mycroft import MycroftSkill, intent_file_handler


class SqueezeboxRemote(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('remote.squeezebox.intent')
    def handle_remote_squeezebox(self, message):
        self.speak_dialog('remote.squeezebox')


def create_skill():
    return SqueezeboxRemote()

