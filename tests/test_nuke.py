import unittest
from Funktioner.nuke_activator import NukeActivator
from pathlib import Path
from datetime import date
import hashlib


class Testing(unittest.TestCase):


    def setUp(self):
        self.folder = Path("test_nuke")
        self.folder.mkdir(exist_ok=True)
        file = self.folder / f"ActivationCodes.txt"
        file.write_text(f"78532111-11:v6wkxY9siR3ZtWueIIAHbx2")
        file = self.folder / f"SecretKEY.txt"
        file.write_text(f"78532111-11:yTjocWZkFj9cCeeJQxfnCyB")
        self.activator = NukeActivator(secret_file="test_nuke/SecretKEY.txt",activation_file="test_nuke/ActivationCodes.txt")



    def test_nuke_aktivation(self):
        today = date.today().strftime("%Y-%m-%d")
        
        submarine_id = "78532111-11"
        secret_key = "yTjocWZkFj9cCeeJQxfnCyB"
        activation_code = "v6wkxY9siR3ZtWueIIAHbx2"
        user_date = today
        result = self.activator.activate_nuke(submarine_id, secret_key, activation_code,user_date)
        raw = user_date + secret_key + activation_code
        hash_value = hashlib.sha256(raw.encode()).hexdigest()
        self.assertEqual(result,{
            "status": "success",
            "message": f"Ubåt {submarine_id} AKTIVERAD!",
            "hash": hash_value
        }
        )
    

    def test_nuke_fail(self):
        result = self.activator.activate_nuke("1111", "secret_key", "activation_code","user_date")

        self.assertEqual(result, {"status": "error", "message": "ACCESS DENIED"})