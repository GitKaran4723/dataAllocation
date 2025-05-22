import requests
import pandas as pd

def getdata(query):
    # Replace with the correct query string (e.g., ?q=zones, ?q=colleges)
    url = "https://script.google.com/macros/s/AKfycbxRp57h21hbO_vcUvCeZ2MgXmC7A7RcksaQqo9yKuEnvp-fH_j2X24MSXY1rqvtQPxx/exec?q="+query

    # Step 1: Fetch data
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
