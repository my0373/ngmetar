import os
from dotenv import load_dotenv
import httpx
import sys




def main():

    load_dotenv(dotenv_path="./config.env")
    ICAO = os.environ.get("METAR_ICAO")
    API_KEY = os.environ.get("METAR_API_KEY")
    API_URI = os.environ.get("METAR_SERVICE_URI")

    if not ICAO:
        print("No ICAO Provided. Exiting.")
        sys.exit(1)
    if not API_KEY:
        print("No API Key Provided. Exiting")
        sys.exit(1)
    if not API_URI:
        print("No API URI found. Exiting")
        sys.exit(1)

    metardata = get_metar(uri=API_URI, api_key=API_KEY)

    if metardata.status_code != 200:
        print(f"Something failed when making the request to {API_URI}")

    print(f"JSON Result: {metardata.text}")


def get_metar(uri, api_key):
    response = httpx.get(url=uri, headers={'X-API-Key': api_key}, verify=False)
    return response


if __name__ == "__main__":
    main()
