# YoMo

Mole Skin Cancer Analysis usingLeNet Convolutional Neural Network and Machine Learning. YoMo classifies images as being "benign" or "malignant" along with a probability of that condition. 

The application works best if users use a clear and isolated photo of the mole, and the application should not be used for non-mole pictures. 

For mobile users, the application works best on Opera or FireFox browser. For mobile users on the Chrome browser, the camera feature may not be functional. 


## Getting Started

First, you will need to collect a dataset of "benign" and "malignant" moles. We used the dataset provided by The International Skin Imaging Collaboration and used atleast 700 benign and 700 malignant moles to train the model. The more images you can collect, the better, and ensure that the images are as clear and focused on the mole as possible. 

### Prerequisites

Create a new virtual environment, cd to the project folder and run

```
pip install -r requirements.txt
```

You should be using the 64bit version of Python 3 or TensorFlow will not install. 

### Training the model

Train the model in the command line using

```
python train_network.py --dataset images --model malignant_benign.model
```

The training will also return a training loss and accuracy plot. Your model is now ready to analyze and classify images.

## Testing the model
The model can be tested with either the command line or the front-end interface. If testing images using the command line, you will need to test each image one at a time and change the file name (or file location) such as below

```
python test_network.py --model malignant_benign.model --image images/test/b1.jpg

```

Image Analysis Results will be saved in

```
/static/results

```


## Acknowledgments
Design by: Johnny Dunn 
Developed with the PyImageSearch guide by Adrian Rosebrock