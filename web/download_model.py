# import the necessary packages
from keras.applications import ResNet50


print("* Loading model...")
_ = ResNet50(weights="imagenet")
print("* Model loaded")
