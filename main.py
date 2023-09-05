# IMPORTS
import requests
from bs4 import BeautifulSoup


# SETUP
URL = r'http://aws.imd.gov.in:8091/state.php?id=TAMIL_NADU'
r = requests.get(URL)


# HELPER FUNCTIONS


# MAIN FUNCTION
if __name__ == "__main__":
    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup.prettify())