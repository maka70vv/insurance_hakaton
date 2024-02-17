from datetime import datetime

import requests
from qreader import QReader
import cv2

from payments.parser import Parser


class ProcessQR:
    def process_receipt_image(self, image):
        try:

            qreader = QReader()

            image = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2RGB)

            decoded_text = qreader.detect_and_decode(image=image)
            self.process_qr(decoded_text[0])
        except Exception as e:
            return {'error': 'Error processing receipt image: {}'.format(str(e))}

    def process_qr(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            payment_data = response.json()
            inn = payment_data['tin']
            dateTime = datetime.strptime(payment_data['dateTime'], '%Y-%m-%dT%H:%M:%SZ')
            summ = int(payment_data['ticketTotalSum']) / 100
            parser = Parser()
            is_medical = bool(parser.parser(inn))
            return inn, dateTime, summ, is_medical



