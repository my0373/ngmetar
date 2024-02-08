import unittest
from metarng.metar import get_metar
import os
from dotenv import load_dotenv
import httpx
import json

class TestMetar(unittest.TestCase):
    def setUp(self):
        load_dotenv(dotenv_path="metarng/config.env")

        self.ICAO = os.environ.get("METAR_ICAO")
        self.API_KEY = os.environ.get("METAR_API_KEY")
        self.API_URI = os.environ.get("METAR_SERVICE_URI")

    def test_api_key_length(self):

        # Same request, but without an API key.
        self.assertEqual(len(self.API_KEY),26)

    def test_get_metar(self):

        good_metardata = get_metar(uri=self.API_URI, api_key=self.API_KEY)

        # Assert the response code is 200 successful as long as we supply a valid key.
        self.assertEqual(good_metardata.status_code,200)


    def test_get_metar_error(self):

        # Same request, but without an API key.
        bad_metardata = get_metar(uri=self.API_URI, api_key="")

        # Assert the response code is 401 unauthorized as we don't supply a key.
        self.assertEqual(bad_metardata.status_code,401)


if __name__ == "__main__":
    unittest.main()




if __name__ == '__main__':
    unittest.main()
