import json


from string import Template


class Utils:
    @staticmethod
    def decode_payload(payload: str):
        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            return {}
