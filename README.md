# Face Recognition

This project is on face recognition using PCA for dimentionality reduction and Milticlass SVM for classification. Effect of various hyperparameters are shown in the Jupyter Noebook.
 
Dataset is taken from MUCT Face database (http://www.milbo.org/muct/)

Faces folder contains sample dataset of 5 people.

# Preparing dataset
1. Download dataset from link provided above and extract it.
2. Move the file "data_preparation.py" to the directory "/faces/muct-master" where forders like "jpg-a", "jpg-b",...etc are present.
3. Choose number of people and change the variable "num_faces" in the python file.
4. A "Faces" forder will be created with "train" and "test" folders in it which is in the same format as the "Faces" folder in this repository.
5. Change vaiables in Jupyter Notebook file accordingly and run the program.