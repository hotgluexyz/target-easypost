from hotglue_singer_sdk.target_sdk.client import HotglueSink

from target_easypost.auth import EasypostAuthenticator

class EasypostStream(HotglueSink):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.authenticator = EasypostAuthenticator(self._target, self._state)

    @property
    def base_url(self) -> str:
        return "https://api.easypost.com/v2"
    
    @property
    def name(self) -> str:
        return self.stream_name

    def preprocess_record(self, record: dict, context: dict) -> dict:
        return record
