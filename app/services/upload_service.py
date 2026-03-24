import os, string, random
from werkzeug.utils import secure_filename


class UploadService:
    def random_string():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def store_file(file):
        os.makedirs('uploads', exist_ok=True)
        extension = os.path.splitext(file.filename)[1]
        newname = secure_filename(random_string() + extension)
        file.save(os.path.join('uploads', newname))
        return newname


    def remove_file(filename):
        try:
            os.remove(os.path.join('app/uploads', filename))
        except:
            print('file already Deleted')