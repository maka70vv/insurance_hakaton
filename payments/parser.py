import re
import requests
from bs4 import BeautifulSoup as BS
from gked_check import CheckGKED


class Parser:
    URL = 'https://www.osoo.kg'

    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0'
    }

    def get_html(self, url, params=''):
        req = requests.get(url, headers=self.HEADERS)
        return req


    def get_data(self, html):
        soup = BS(html, 'html.parser')
        table = soup.find('div', {'class': 'row profile-section py-3'}).find('table')

        gked = table.find_all('tr')[6].find_all('td')[1].get_text(strip=True)
        match = re.search(r'([\d.]+):', gked)

        if match:
            gked_code = match.group(1)
            checkGKED = CheckGKED()
            result = checkGKED.check_gked_medical(gked_code)
            return result
        else:
            return "Not found"

    def parser(self, inn):
        html = self.get_html(self.URL+f"/inn/{inn}/")
        if html.status_code == 200:
            gked = self.get_data(html.text)
            return gked
        else:
            raise Exception('Error in parser func........')

