import pprint

import requests
import os


class ImageTagging:
    def __init__(self):
        self.api_key = 'acc_df160781bc7c92c'
        self.api_secret = 'bc9647c8fa8b1d15c0a7e03eaa306309'

    def get_tags(self, image_id):
        image_file = f'{image_id}.jpg'
        image_path = os.path.join(os.getcwd(), 'images', image_file)
        response = requests.post(
            'https://api.imagga.com/v2/tags',
            auth=(self.api_key, self.api_secret),
            files={'image': open(image_path, 'rb')})
        return response.json()['result']['tags']

    def find_category(self, image_id):
        tags = self.get_tags(image_id)
        for item in tags:
            if item['tag']['en'] == 'vehicle':
                if item['confidence'] > 50:
                    return tags[0]['tag']['en']
        return 'not_vehicle'
