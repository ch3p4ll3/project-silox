import json


from string import Template


class Utils:
    @staticmethod
    def decode_payload(payload: str):
        """Decodes the payload from a string to a dictionary"""
        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            return {}
