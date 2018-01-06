# CLI example
# python test_network.py --model malignant_benign.model --image images/test/b1.jpg
# Image analysis results saved in /static/results

from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

def prepare_file(filepath):
    print("\nTesting image from: " + filepath)
    image = cv2.imread(filepath)
    return image

def read_image(filename):
    image = "images/test/uploaded/" + filename
    print("\nFile path passed: " + str(image))
    image = cv2.imread(str(image))
    original_image = image.copy()
    processed_image = cv2.resize(image, (128, 128))
    processed_image = processed_image.astype("float") / 255.0
    processed_image = img_to_array(processed_image)
    processed_image = np.expand_dims(processed_image, axis=0)
    print("\nFinished image processing.")
    print("\t" + str(processed_image))
    return original_image, processed_image


def read_image_example(filename):
    image = "images/test/example/" + filename
    print("\nFile path passed: " + str(image))
    image = cv2.imread(str(image))
    original_image = image.copy()
    processed_image = cv2.resize(image, (128, 128))
    processed_image = processed_image.astype("float") / 255.0
    processed_image = img_to_array(processed_image)
    processed_image = np.expand_dims(processed_image, axis=0)
    print("\nFinished image processing.")
    print("\t" + str(processed_image))
    return original_image, processed_image

def test_image(processed_image, original_image, filename):
    print("\nClassifiying image..")
    model = load_model('malignant_benign.model') # Model should be already trained and saved    
    (benign, malignant) = model.predict(processed_image)[0]
    classified = "Malignant" if malignant > benign else "Benign"
    probability = malignant if malignant > benign else benign
    print("\nImage classified: " + classified)
    label = "{}: {:.2f}%".format(classified, probability * 100)
    res = show_results(label, original_image, filename)
    return label

def show_results(label, original_image, filename):
    output = imutils.resize(original_image, width=400)
    cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_DUPLEX,
    0.7, (0, 255, 0), 2)
    # cv2.imshow("Output", output)
    cv2.waitKey(0)
    # _filename = filename.replace('.jpg', 'bmp') # OpenCV has some trouble saving to JPG sometimes
    cv2.imwrite('static/results/' + filename, output)
    print("\nWrote result image to file: " + filename + ".")

if __name__ == '__main__':
    # Running as a script
    # Command line arguments
    print("\nTesting model with CLI..")
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--model", required=True,
        help="path to trained model model")
    ap.add_argument("-i", "--image", required=True,
        help="path to input image")
    args = vars(ap.parse_args())
    # model = load_model(args["model"])
    image = args["image"]
    processed_image = read_image(image)
else:
    print("\nImporting model as a module..")
    # model = load_model('malignant_benign.model') # For some reason TensorFlow throws an error when we load the model here?? 