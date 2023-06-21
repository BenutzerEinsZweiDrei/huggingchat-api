class Message:
    def __init__(self, conversation_id: str, web_search_enabled: bool):
        self.text: str = ""
        self.final_text: str = None
        self.web_search_steps = None
        self.done: bool = False
        self.web_search_enabled = web_search_enabled
        self.error: Exception = None
        self.conversation_id: str = conversation_id
    
    def getConversation(self) -> str:
        return self.conversation_id
    
    def setError(self, error: Exception):
        self.error = error
        
    def setWebSearchSteps(self, process):
        self.web_search_steps = process
    
    def getWebSearchSteps(self):
        if self.error:
            raise self.error
        return self.web_search_steps
    
    def setText(self, text, done: bool = False):
        self.text += text
        if done:
            self.done = True
    
    def getText(self) -> str:
        if self.error:
            raise Exception(self.error)
        return self.text
    
    def setFinalText(self, text):
        self.final_text = text
        self.done = True
    
    def getFinalText(self) -> str:
        if self.error:
            raise Exception(self.error)
        return self.final_text
    
    def isDone(self) -> bool:
        return self.done
