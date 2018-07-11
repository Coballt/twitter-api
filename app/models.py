from datetime import datetime

class Tweet:
    def __init__(self,text):
        self.text = text
        self.created_at = datetime.now()
        self.id = None
