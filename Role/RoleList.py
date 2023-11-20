from .Role import Role
from GPT.ChatGPT import ChatGPT
import os


_MEETING_SECRETARY_FILE = "MeetingSecretaryPrompt.md"
_SUMMARY_WRITER_FILE = "SummaryPrompt.md"
_MEETING_MINUTES_EDITOR_FILE = "MeetingMinutesEditor.md"


class MeetingSecretary(Role):
    def __init__(self, model, template: str=None) -> None:
        super().__init__(_MEETING_SECRETARY_FILE, model)
        self.raw_prompt = self.role_prompt
        self.set_template(template if template is not None else self._get_default_template())


    def set_template(self, template: str) -> str:
        self.role_prompt = self.raw_prompt.replace("${template}", template)

    
    def _get_default_template(self):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(f"{path}/prompt/DefaultMinutesTemplate.md", "r", encoding='utf-8') as f:
            return f.read() 


class SummaryWriter(Role):
    def __init__(self, model: ChatGPT) -> None:
        super().__init__(_SUMMARY_WRITER_FILE, model)


class MeetingMinutesEditor(Role):
    def __init__(self, model, template: str=None) -> None:
        super().__init__(_MEETING_MINUTES_EDITOR_FILE, model)
        self.raw_prompt = self.role_prompt
        self.set_template(template if template is not None else self._get_default_template())


    def set_template(self, template: str) -> str:
        self.role_prompt = self.raw_prompt.replace("${template}", template)

    
    def _get_default_template(self):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(f"{path}/prompt/DefaultMinutesTemplate.md", "r", encoding='utf-8') as f:
            return f.read() 
