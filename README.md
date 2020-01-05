# DARPG Hackathon Solution
Predictive model solution for routing complaints to departments

 
Executive Summary

The project is of a predictive model used for predicting different departments which is dedicated for handling different complaints done by the people. In this project we are leveraging the capability of LSTM which uses a concept called gates used for remembering important things and forgetting unimportant things. By using this we are keeping only the important words from a complaint which is used for predicting the department required for handling that particular complaint. The predictive model created is able to identify the department for the complaints with test accuracy of 96-97 %.

Current State
Currently if a person posts a complaint and is unaware of which department is dedicated for handling his/her complaint and tag any random Ministry/Department then it takes near about 10-15 days for that complaint to reach the specific department and again it takes another 2-5 days for resolving and acknowledging the complaint.

Future State
In future by using the technology we can save up to 10-15 days of rerouting of the complaints and directly used the time for resolving the complaint.

Environment Used
•	OS: Linux
•	Python 3.6
•	Keras, Tensorflow, CUDA, CUDNN
•	12 GB DDR3 RAM
•	NVDIA 4 GB GPU
