from datetime import date
import hashlib

class NukeActivator:
    """
    Hanterar laddning av hemliga nycklar och aktiveringskoder för ubåts-drönare,
    samt tillhandahåller funktionalitet för att försöka aktivera en mini-nuke.

    Programmet använder två filer:
    - SecretKEY.txt -> innehåller varje ubåts unika hemliga nyckel
    - ActivationCodes.txt -> innehåller varje ubåts unika aktiveringskod

    En aktivering lyckas endast om både ubåtens ID, nyckel och kod matchar filerna.
    """
    def __init__(self, secret_file="Secrets/SecretKEY.txt", activation_file="Secrets/ActivationCodes.txt"):
        self.secret_keys = self._read_file_to_dict(secret_file)
        self.activation_codes = self._read_file_to_dict(activation_file)

    def _read_file_to_dict(self, filename):
        """Läser en fil i format ID: värde och returnerar som dictionary"""
        data = {}
        with open(filename, "r") as f:
            for line in f:
                if ":" in line:
                    key, value = line.strip().split(":", 1)
                    data[key.strip()] = value.strip()
        return data

    def activate_nuke(self, submarine_id, user_key, user_code):
        """Försöker aktivera en ubåt med given input"""
        if submarine_id not in self.secret_keys or submarine_id not in self.activation_codes:
            return {"status": "error", "message": "ACCESS DENIED"}

        if (self.secret_keys[submarine_id] != user_key 
                or self.activation_codes[submarine_id] != user_code):
            return {"status": "error", "message": "ACCESS DENIED"}

        today = date.today().strftime("%Y-%m-%d")
        raw = today + user_key + user_code
        hash_value = hashlib.sha256(raw.encode()).hexdigest()

        return {
            "status": "success",
            "message": f"Ubåt {submarine_id} AKTIVERAD!",
            "hash": hash_value
        }

 