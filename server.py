from flask import Flask, render_template, url_for, request, redirect
from werkzeug.utils import secure_filename
import cv2
import os
from test_network import read_image, test_image
from binascii import a2b_base64
import datetime

application = Flask(__name__, static_url_path='/static')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@application.route('/')
def index(): 
    return render_template('index.html')

# Upload from file browse
@application.route('/upload', methods=['POST'])
def upload_file():
    print("Uploading file..")
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            error = "No file part"
            return redirect('/')
        file = request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename
        if file.filename == '':
            error = "No selected file"
            return redirect('/')
        if file and allowed_file(file.filename):
            print("Sucessful upload")
            filename = secure_filename(file.filename)
            file.save(os.path.join("images/test/uploaded", filename))
            image = "images/test/uploaded/" + filename
            print("File path to pass: " +  image)
            original_image, processed_image = read_image(filename)
            label = test_image(processed_image, original_image, filename)
            return filename

# Upload from camera
@application.route('/upload_snap', methods=['POST'])
def upload_snap():
    print("Uploading file from camera..")
    if request.method == 'POST':
      result = request.data
    new_result = str(result)
    new_result = new_result.replace("b'data:image/jpeg;base64,", "")
    new_result = new_result[:-1]
    print(new_result)
    ts = datetime.datetime.now().timestamp()
    binary_data = a2b_base64(new_result)
    fd = open("images/test/uploaded/" + str(ts) + '.jpg', 'wb')
    fd.write(binary_data)
    fd.close()
    filename = str(ts) + ".jpg"
    print("Sucessful upload. Now processing..")
    original_image, processed_image = read_image(filename)
    label = test_image(processed_image, original_image, filename)
    return filename


# Functions below are linked to hardcoded example image results 
@application.route('/upload_ex_1', methods=['GET'])
def upload_ex_1():
    print("Uploading file..")
    filename = "b2.jpg"
    image = "images/test/example/" + filename
    print("File path to pass: " +  image)
    original_image, processed_image = read_image_example(filename)
    label = test_image(processed_image, original_image, filename)
    return filename

@application.route('/upload_ex_2', methods=['GET'])
def upload_ex_2():
    print("Uploading file..")
    filename = "b3.jpg"
    image = "images/test/example/" + filename
    print("File path to pass: " +  image)
    original_image, processed_image = read_image_example(filename)
    label = test_image(processed_image, original_image, filename)
    return filename

@application.route('/upload_ex_3', methods=['GET'])
def upload_ex_3():
    print("Uploading file..")
    filename = "m1.jpg"
    image = "images/test/example/" + filename
    print("File path to pass: " +  image)
    original_image, processed_image = read_image_example(filename)
    label = test_image(processed_image, original_image, filename)
    return filename

@application.route('/upload_ex_4', methods=['GET'])
def upload_ex_4():
    print("Uploading file..")
    filename = "b6.jpg"
    image = "images/test/example/" + filename
    print("File path to pass: " +  image)
    original_image, processed_image = read_image_example(filename)
    label = test_image(processed_image, original_image, filename)
    return filename

@application.route('/upload_ex_5', methods=['GET'])
def upload_ex_5():
    print("Uploading file..")
    filename = "m6.jpg"
    image = "images/test/example/" + filename
    print("File path to pass: " +  image)
    original_image, processed_image = read_image_example(filename)
    label = test_image(processed_image, original_image, filename)
    return filename

# run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = False
    application.run()