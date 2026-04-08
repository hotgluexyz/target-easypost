import base64

from hotglue_singer_sdk.target_sdk.auth import Authenticator


class EasypostAuthenticator(Authenticator):
    """HTTP Basic auth: `api_key` is the username, password is empty (EasyPost convention)."""

    @property
    def auth_headers(self) -> dict:
        api_key = self._config["api_key"]
        token = base64.b64encode(f"{api_key}:".encode()).decode()
        return {"Authorization": f"Basic {token}"}
