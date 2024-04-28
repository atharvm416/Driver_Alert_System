# Driver Alert System

## Objective
1. To design a system that will alert the driver about distracted behaviours.
2. To classify each driver's behaviour and determine if they are driving attentively, or doing any irrelevant activity
3. To ring alarm if driver is indulging in any irrelevant behaviour

## Scope and Limitations
* The scope of the system in real-time is to continuously monitor the driver's behavior and alert them in case of any distractions while driving. The system's real-time capabilities make it highly effective in detecting distractions as they occur and providing timely alerts, which can help prevent accidents.

* In addition, the system can be used in various real-world scenarios, such as commercial fleets, personal vehicles, and public transportation systems. This system can also be integrated with other safety features such as lane departure warning systems and automatic emergency braking systems to further improve overall safety.

* Overall, the real-time scope of the system can help reduce the number of accidents caused by distracted driving, thus saving lives and reducing the economic burden of accidents.

* However, there are also some limitations to this project. Firstly, the system relies on the accuracy of the self-trained model, which can be affected by factors such as lighting and camera angle. Secondly, the system may not be able to detect all instances of distracted behavior, as it is limited to the behaviors it has been trained to recognize. Thirdly, the system may not be compatible with all types of vehicles or driving situations. Lastly, the system may be affected by false alarms, which could potentially cause driver distraction and reduce the effectiveness of the system.

## Related Work
Many studies show that driving while talking on hand-held phone increases the risk of accident. Other studies have shown that almost 70% of fatal traffic accidents are attributed to driver’s distraction, and hand-held phone using is one of the major reasons of the distraction.

D. Wang. et al. [1] present a novel method to detect the driver use mobile phone based on an in-car camera. Author’s use AoG (And-Or Graph) to model the driver’s phoning activity and employ an parsing algorithm to detect the phoning activity. They found that created system achieved high positive detection rate and the results are only related to the driver, could not be affected by passengers. The only focus of this paper is about mobile phone usage of a person in a car. But in reality the mobile phone is not the only culprit. The false detection rate is a little high which may disturb the driver with unnecessary alerts.

Published by C. Huang. et al. [3] propose a hybrid CNN framework (HCF) to recognize distracted driver behaviours. Features are extracted by pretrained CNN model then, the features are concatenated to obtain the feature maps. Author’s train 8 the fully connected layer to classify each distracted driving behaviour. The results show that the proposed HCF achieves good performance for recognizing distracted driver behaviours, reaching a classification accuracy of 96.74%. The dataset in this paper only provides the images from the right-hand side. In addition, the HCF is greatly influenced by the light, which indicates that the HCF cannot detect the distracted driving behaviour accurately at night.

## Requirement Gathering
To develop an effective distracted driver detection system, we began by conducting a thorough analysis of the problem. This involved studying accident reports and statistics, identifying common distracted driving behaviors, and understanding the factors that contribute to these behaviors.

We also conducted a literature review to explore existing research on similar projects, including their limitations and potential areas for improvement. This helped us identify the most promising technologies and techniques to incorporate into our own system.

Based on our research, we identified the following requirements for our system:

* Ability to detect and classify a range of distracted driving behaviors, including texting, phone use, eating and drinking, and grooming.
* Real-time monitoring of the driver's behavior, with immediate alerts if any distracting behavior is detected.
* Accuracy and reliability in detecting distracted behavior, while minimizing false alarms.
* A user-friendly interface that provides clear and actionable alerts to the driver.
* Compatibility with a range of vehicles and driving conditions.
* Integration of the components.
* High resolution camera for capture live video.
* Stable internet connection for the detection.

These requirements guided our design and development process, ensuring that we developed a system that met the needs of our stakeholders and effectively addressed the problem of distracted driving.

##  Validation Criteria

| Sr. No | Test Case Title           | Description                                                      | Expected Output |
|--------|---------------------------|------------------------------------------------------------------|-----------------|
| 1      | Safe Driving              | Driver should be in ideal state of driving for drinking. This state detected here. | No alarm        |
| 2      | Right-handed texting      | When driver is using mobile phone and he is texting while mobile at right hand. | Alarm rings     |
| 3      | Right-handed phone use    | When driver is talking on mobile phone and phone at right side. | Alarm rings     |
| 4      | Left-handed texting       | When driver is using mobile phone and he is texting while mobile at left hand. | Alarm rings     |
| 5      | Left-handed phone use     | When driver is talking on mobile phone and phone at left side. | Alarm rings     |
| 6      | Operating the radio       | When driver is operating radio and he loses his concentration. | Alarm rings     |
| 7      | Drinking                  | Driver started drinking something. | Alarm rings     |
| 8      | Glancing behind           | Driver is glancing behind and talking with another person. | Alarm rings     |
| 9      | Hair and makeup           | Driver is doing hair and makeup which makes him/her less concentrated. | Alarm rings     |
| 10     | Talking with the passengers | Driver is talking with another person. | Alarm rings     |

## Environmental Setup

Before running the project on our device, we need to install the Python 3.10 version. We have used the Python 3.10 version because it has more stable libraries than 3.11, which was recently released. After that, we need to install all the libraries required for our project. We have used libraries as follows: opencv, numpy, imutils, pyttsx3, pillow, pandas, pickle, shutil, and keras.

##  Detailed Description of Methods

### 1. Create a pickle file:

A dictionary is created where each label name is mapped to a unique integer ID. The enumerate function is used to assign a unique ID to each label in the 'labels_list' starting from 0. We then replace the class names in the 'ClassName' column of the 'data_train' dataset with their corresponding integer IDs using the dictionary. Now we create a pickle file (.pkl), namely 'labels_list.pkl'. The 'labels_id' dictionary converts the dictionary to a binary format and stores 'labels_list.pkl'. In summary, the code converts the class names in the 'ClassName' column of the 'data_train' dataset from strings to integers, which is often necessary for machine learning algorithms to work properly.

### 2. Create preprocessed training and validation data in the form of 4D tensors:

For creating a 4D numpy array, we convert our RGB image to 4D tensor. This resulting numpy array has shape (num_samples, height, width, and channels), where num_samples is the number of images in the input list and height, width, and channels represent the dimensions of each image. Now we add these 4D tensor images by passing training and testing sets. ‘train_tensors’ for the train set and ‘valid_tensors’ for the test set. By doing this, we pre-process the image data to prepare it for use with Keras by converting the image file paths to a tensor of image data, casting the tensor to the appropriate data type, and normalizing the pixel values.

### 3. Split of training and testing dataset:

The test_size parameter we set it to 0.2, which means that 20% of the data will be reserved for testing, and the remaining 80% will be used for training the model. The 19 random_state parameter is set to 42, which ensures that the same random splits will be generated each time the code is executed.

### 4. Configure the model:
To configure the model we require optimizer, loss, and metrics:
For the optimizer, we have used the RMSprop optimizer, which restricts the oscillations in the vertical direction. Therefore, we can increase our learning rate, and our algorithm could take larger steps in the horizontal direction, converging faster.
For loss, we have used categorical_crossentropy, which is used as a loss function for multi-class classification models where there are two or more output labels. The output label is assigned a one-hot category encoding value in the form of 0s and 1. The output label, if present in integer form, is converted into categorical encoding using Keras.
For metrics, we have used accuracy, which is used to calculate how often predictions equal labels.

### 5. Fit the model:
We have specified that the model be in HDF5 format. HDF5 format, which is used for general-purpose libraries and file formats for storing scientific data. The call model.fit() is used to test the result of the images stored in ‘train_tensors’ and ‘valid_tensors’. After completion of the epoch, we will get a self-trained model with the file name "distracted-{epoch:02d}-{val_accuracy:.2f}.hdf5".

### 6. Real-time capturing:
We have obtained real-time data by using mobile phones cameras. With the help of the app known as "IP Webcam", which is available on the Play Store. Live images are taken by cv2.VideoCapture(url) from the library CV2, where the url is provided by the app, and we require a laptop to connect to the same network as our mobile phone.

### 7. Detection:
After capturing the image file, we call the function from driver_prediction.py and store the returned string value in a variable named "Label".
The image is converted to a 4D tensor array from RGB. By using pickle and a selftrained model, specify the notation for which the image is captured. Then it returns a string to the main file.

### 8. Display and Alert:
We highlight the notation on our screen, and after 3 seconds, if the same activity is present without "safe_driving", then the system makes the sound of the notation that has been detected for the last 3 seconds.


## Implementation Detail 
We have implemented 3 files in total from which 2 are .py and 1 is .ipyb file.

### 1. Implementation of ipyb file –
For this we have used anaconda containing jupyter notebook. In the file we have used a bunch of libraries so that we can get the desired self-trained model. The time required for the implementation of the entire code is around 4 hours and 30 minutes.

### 2. Implementation of py file –
For this we have used IDLE python 3.10 (64 bit). To get access with the libraries in our code, we have used command prompt.

## Description of the Integration Modules
In our system we have only Integrated mobile phone as any external resource to capture higher resolution image. This connection is done by the connecting the laptop and the mobile phone physically and with the use of the IP Webcam app we started capturing the images from our mobile phone.

## Future Scope
Firstly, improving the system's performance in low-light conditions, such as during nighttime or in dark mode, can significantly enhance its accuracy. This can be achieved by incorporating night vision cameras specifically designed to capture clear images in challenging lighting environments. By leveraging such advanced camera technology, the system will be better equipped to detect and recognize faces, ultimately improving its performance and accuracy during nighttime operations.

Another potential area for future expansion is the incorporation of motion detection capabilities. Currently, the system is unable to determine whether the driver's vehicle is in motion or stationary. By integrating motion detection algorithms and techniques into the existing model, the system can gain the ability to identify the movement of the vehicle. This feature could be valuable for assessing driver behavior and detecting potentially dangerous situations, such as when a driver falls asleep or loses control of the vehicle while in motion.

Furthermore, the project could be extended to include the detection of Bluetooth headphones and other electronic devices. As the usage of Bluetooth devices, including headphones, continues to rise, it becomes increasingly important to monitor their presence and usage while driving. By training the model to identify Bluetooth devices, the system can alert the driver if they are using such devices, which could contribute to distracted driving. This expansion would enhance the overall effectiveness of the Driver Alert System, ensuring a comprehensive approach to promoting safe driving practices.
