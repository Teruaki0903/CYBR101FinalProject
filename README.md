Design documents
Author Teruaki Murakami
The member of the project.

Teruaki Murakami

1.	*Purpose Purpose of this software
The purpose of this project is to develop software that predicts crime rates based on several factors in a specific state.

2.	*Background Background and history of developing this software, etc.
 Currently in the United States, crimes such as shoplifting are on the rise, so finding and implementing methods to effectively control crimes has become an urgent issue. There is also the view that one of the reasons for the increase in crime is that economic problems such as inflation and rising unemployment rates are affecting people's lives.
We started this project because we believe that more effective crime prevention can be achieved by predicting the scale of crime and allocating personnel and budget based on these social issues.

3.	Requirements specifications Links to requirements specifications, functional specifications, etc. (sometimes the main points of the requirements specifications are written)
 Predict crime by inputting economic conditions, population, labor rate, etc.
Outputting the input data and crime prediction results to separate files
Create two programs: an AI model learning program and an AI model usage program.
 
4.	*Overview of each part (module/class) Overview, responsibilities, purpose, etc. of each part
 This project is roughly divided into two programs, one dataset, one result file, and one AI model.
5.	*Overview of each part (module/class) Overview, responsibilities, purpose, etc. of each part
Dataset: CSV format file, GDP, population (under 20 years old, 20-65 years old, 65 years old) (male, female),Labor rate (under 20 years old, 20-65 years old, 65 years old) (male, female), number of crimes
Tensorflow ML Module In the section for performing machine learning in Tensorflow, various variables are read from the dataset and machine learning is performed.
ML save Module Outputs the AI model when learning is completed.
AI model AI model created by Tensorflow
Tensorflow Module(For use AI model) A module for using AI model by Tensorflow, input data and predict the number of crimes.
Data Output Part that outputs the predicted number of crimes and input data to a CSV file

