<p align="center">
  <img alt="🆚RMSProp_vs_ADAGrad" src="https://user-images.githubusercontent.com/62103572/183284601-5f2125ed-059a-4b0b-a566-72a912ef342a.png">
  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/y/EliaFantini/RMSProp-and-AMSGrad-for-MNIST-image-classification">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/EliaFantini/RMSProp-and-AMSGrad-for-MNIST-image-classification">
  <img alt="GitHub code size" src="https://img.shields.io/github/languages/code-size/EliaFantini/RMSProp-and-AMSGrad-for-MNIST-image-classification">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/EliaFantini/RMSProp-and-AMSGrad-for-MNIST-image-classification">
  <img alt="GitHub follow" src="https://img.shields.io/github/followers/EliaFantini?label=Follow">
  <img alt="GitHub fork" src="https://img.shields.io/github/forks/EliaFantini/RMSProp-and-AMSGrad-for-MNIST-image-classification?label=Fork">
  <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/EliaFantini/RMSProp-and-AMSGrad-for-MNIST-image-classification?label=Watch">
  <img alt="GitHub star" src="https://img.shields.io/github/stars/EliaFantini/RMSProp-and-AMSGrad-for-MNIST-image-classification?style=social">
</p>


Implementation of different first order (FO) stochastic methods: stochastic gradient descent (SGD), stochastic gradient descent with momentum (SGDw/Momentum) , Root Mean Squared Propagation (RMSProp), Adaptive Gradient Algorithm (Adagrad).  This project was made to test these different optimizers on a handwritten digit classifier using the well-known MNIST dataset. This dataset has 60000 training images, and 10000 test images. Each image is of size 28 × 28 pixels, and shows a digit from 0 to 9.


For a more detailed explanation of the algorithms mentioned above, please read *Exercise instructions.pdf*, it contains also some theoretical questions answered in *Answers.pdf* (handwritten). 

The project was part of an assignment for the EPFL course [EE-556 Mathematics of data: from theory to computation](https://edu.epfl.ch/coursebook/en/mathematics-of-data-from-theory-to-computation-EE-556). The backbone of the code structure to run the experiments was already given by the professor and his assistants, what I had to do was to implement the core theoretical concepts to actually make the experiments work. Hence, every code file is a combination of my personal code and the code that was given us by the professor.

The following table shows a summary of the training done by running **main.py** in the *code* folder. 



<p align="center">
<img width="692" alt="Immagine 2022-08-07 114348" src="https://user-images.githubusercontent.com/62103572/183285025-900ffee1-21a5-44c8-a5bb-fbb8f0ae5105.png">
</p>



The following image shows an example of the output figures of the code **main.py**. All plots show a comparison of convergence speed to the optimal loss and accuracy, for different learning rate's values.

<p align="center">
<img width="911" alt="Immagine 2022-08-07 114322" src="https://user-images.githubusercontent.com/62103572/183285022-65214817-7118-4cb7-ae52-84afe668a94a.png">
<img width="899" alt="Immagine 2022-08-07 114311" src="https://user-images.githubusercontent.com/62103572/183285023-0913378d-c894-444f-ad4e-0be3009d8117.png">
<img width="926" alt="Immagine 2022-08-07 114333" src="https://user-images.githubusercontent.com/62103572/183285026-5159305b-b60c-4357-b2ba-5329af10ae6f.png">
</p>



## Author
-  [Elia Fantini](https://github.com/EliaFantini)

## How to install and reproduce results
Download this repository as a zip file and extract it into a folder
The easiest way to run the code is to install Anaconda 3 distribution (available for Windows, macOS and Linux). To do so, follow the guidelines from the official
website (select python of version 3): https://www.anaconda.com/download/

Additional package required are: 
- matplotlib
- pytorch

To install them write the following command on Anaconda Prompt (anaconda3):
```shell
cd *THE_FOLDER_PATH_WHERE_YOU_DOWNLOADED_AND_EXTRACTED_THIS_REPOSITORY*
```
Then write for each of the mentioned packages:
```shell
conda install *PACKAGE_NAME*
```
Some packages might require more complex installation procedures (especially [pytorch](https://pytorch.org/)). If the above command doesn't work for a package, just google "How to install *PACKAGE_NAME* on *YOUR_MACHINE'S_OS*" and follow those guides.

Finally, run **main.py**. 
```shell
python main.py
```

## Files description

- **code/**: folder containing all the code to run the training and testing, included the optimization algorithms

-  **code/main.py**: main script to be run in order to do the training and output the plots.

- **Answers.pdf**: pdf with the answers and plots to the assignment of the course

- **Exercise instructions.pdf**: pdf with the questions of the assignment of the course

## 🛠 Skills
Python, Pytorch, Matplotlib. Machine learning, artificial neural networks, multilayer perceptron (MLP), implementation of optimization methods.

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://eliafantini.github.io/Portfolio/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/-elia-fantini/)

