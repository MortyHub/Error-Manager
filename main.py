Types = ["Error: ", "Warning: ", "Alert: "]


class Error:
    def __init__(self, name, text, typee):
        self.errorName = name
        self.errorText = text
        self.errorType = typee

    def printError(self):
        if self.errorType == "Error":
            colored(255, 51, 51, "Error: " + self.errorText)
        
        if self.errorType == "Warning":
            colored(235, 94, 94, "Warning: " + self.errorText)
        
        if self.errorType == "Alert":
            colored(255, 245, 84, "Alert: " + self.errorText)

def colored(r, g, b, text):
    print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text))


