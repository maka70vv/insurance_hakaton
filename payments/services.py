from datetime import datetime

import requests
from pyzbar.pyzbar import decode
from PIL import Image
import cv2

class ProcessQR:
    def process_receipt_image(self, image):
        try:
            img = cv2.imread(image)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
                if len(approx) == 4:
                    x, y, w, h = cv2.boundingRect(approx)
                    roi = img[y:y + h, x:x + w]
                    decoded_objects = decode(roi)
                    if decoded_objects:
                        qr_data = decoded_objects[0].data.decode('utf-8')
                        self.process_qr(qr_data)
                        # return {'qr_data': qr_data}

            return {'error': 'No QR code found on the receipt image'}

        except Exception as e:
            return {'error': 'Error processing receipt image: {}'.format(str(e))}

    def process_qr(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            payment_data = response.json()
            inn = payment_data['tin']
            dateTime = datetime.strptime(payment_data['dateTime'], '%Y-%m-%dT%H:%M:%SZ')
            summ = int(payment_data['ticketTotalSum']) / 100
        return inn, dateTime, summ

