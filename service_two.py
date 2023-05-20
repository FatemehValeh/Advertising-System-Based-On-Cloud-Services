from rabbit import RabbitHelper
from s3 import S3Helper
from image_tagging import ImageTagging
from database import DatabaseHelper
from email_helper import Email


def main():
    rabbit = RabbitHelper()
    s3 = S3Helper()
    image_tagging = ImageTagging()
    db = DatabaseHelper()

    rabbit.read_from_queue()
    image_id = rabbit.get_id()
    print("image_id:", image_id)
    s3.download_file(image_id)
    image_category = image_tagging.find_category(image_id)
    s3.remove_file(image_id)  # not to store images in local
    db.update_in_db('category', image_id, image_category)
    send_mail(image_category, image_id, db)
    update_status(image_category, image_id, db)


def send_mail(category, _id, db: DatabaseHelper):
    if category == 'not_vehicle':
        email_text = 'Your ad is rejected. Not a picture of a vehicle'
    else:
        email_text = 'Your add accepted'
    email = db.select_from_db('email', _id)
    Email().send_email(email, 'Your ad status', email_text)


def update_status(category, image_id, db: DatabaseHelper):
    if category == 'not_vehicle':
        status = 'rejected'
    else:
        status = 'accepted'
    db.update_in_db('status', image_id, status)


if __name__ == '__main__':
    main()
