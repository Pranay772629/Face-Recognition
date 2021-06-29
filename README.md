# Face Recognition

This project is on face recognition using PCA for dimentionality reduction and Milticlass SVM for classification. Effect of various hyperparameters are shown in the Jupyter Noebook.

The images are resized to a 100x100 pixels which gives 10,000 imputs for our Multiclass SVM. PCA is used to reduce the dimension of input from 10,000 to <100 (can be changed according to the size of dataset). This reduced dataset is used to train a Multiclass SVM which is made from scratch using python's cvxopt library.
 
Dataset is taken from MUCT Face database (http://www.milbo.org/muct/)

Faces folder contains sample dataset of 5 people.

# Preparing dataset
1. Download dataset from link provided above and extract it.
2. Move the file "data_preparation.py" to the directory "/faces/muct-master" where forders like "jpg-a", "jpg-b",...etc are present.
3. Choose number of people and change the variable "num_faces" in the python file.
4. A "Faces" forder will be created with "train" and "test" folders in it which is in the same format as the "Faces" folder in this repository.
5. Change vaiables in Jupyter Notebook file accordingly and run the program.