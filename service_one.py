from flask import Flask, request, Response, send_file, make_response
from rabbit import RabbitHelper
from database import DatabaseHelper
from s3 import S3Helper
import os
import cv2

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    db = DatabaseHelper()
    s3 = S3Helper()
    rabbit = RabbitHelper()

    if request.method == 'POST':  # Advertisement registration
        print("here1")
        image = request.files['image']
        email = request.form['email']
        description = request.form['description']
        print("here")
        print(db.select_from_db('email', 18))
        image_id = db.insert_to_db(description, email)

        s3.upload_file(image, image_id)

        rabbit.insert_to_queue(image_id)
        response_message = f'your advertisement registered with ID: {image_id}'
        # response_message = 'foo'
    if request.method == 'GET':
        image_id = request.form['id']
        # ad_status = db.select_from_db('status', image_id)
        # if ad_status == 'accepted':
        # TODO return image and ...
        object_name = 'car.jpg'
        download_path = os.path.join(os.getcwd(), 'images', object_name)
        image_binary = cv2.imread('ff.jpg', 2)
        response = make_response(image_binary)
        response.headers.set('Content-Type', 'image/jpeg')
        response.headers.set(
            'Content-Disposition', 'attachment', filename='%s.jpg' % pid)
        return response

        return send_file(download_path, mimetype='image/gif'), Response(response="des", status=200, mimetype="application/json")
        response_message = ad_status


    return Response(response=response_message, status=200, mimetype="application/json")
