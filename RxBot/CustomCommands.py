from Settings import *
from Initialize import *




commands_CustomCommands = {
    "!enabledrops": ("STREAMER", 'customcmds.enable', 'cmdArguments', 'user'),
    "!disabledrops": ("STREAMER", 'customcmds.disable', 'cmdArguments', 'user'),
    "!dropnow": ("STREAMER", 'tock.dropNow', 'cmdArguments', 'user'),
}

class resources:
    def __init__(self):
        pass

    def sendMessageFromText(self):
        with open("../Config/Messages.txt", "r") as f:
            data = f.read().splitlines(True)

            if not data:
                print("MESSAGES FILE IS EMPTY!")
                return

            line = data[0]


        with open("../Config/Messages.txt", "w") as f:
            f.writelines(data[1:])  # Write everything back except for the top line


            return line



class CustomCommands:
    def __init__(self):
        self.enabled = True

    def enable(self, args, user):
        self.enabled = True
        return "Enabled drops!"

    def disable(self, args, user):
        self.enabled = False
        return "Disabled drops!"




customcmds = CustomCommands()
resources = resources()