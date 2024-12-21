# SFU CMPT 340 Project - EMOTIC - EEG Monitoring of Thoughts and Individual Conditions

A project using EEG to analyze and interpret users' emotional states through neural signal processing and machine learning.
- The collection of EEG data accredited to the authors of <em>A Large Finer-grained Affective Computing EEG Dataset</em>:
https://rdcu.be/d1TNW
- Chen, J., Wang, X., Huang, C. et al. A Large Finer-grained Affective Computing EEG Dataset. Sci Data 10, 740 (2023). https://doi.org/10.1038/s41597-023-02650-w

## Team Members
1. Maisha Supritee Chowdhury
2. Edan Stasiuk
3. Rashed Hadi
4. Zihao Xie
5. Daniel Kim

## Important Links

[Project report](Project_Report.pdf) | [Figma Designs](https://www.figma.com/design/07ebJ9bOish0JBql6CXDZY/EMOTIC?node-id=1-2&t=NrPhjqYzAK1cM2gP-1) |
|-----------|---------------|-------------------------|-------------------------|



## Table of Contents
1. [Demo](#demo)

2. [Installation](#installation)

3. [Reproducing this project](#repro)



<a name="demo"></a>
## 1. Demo video

[![Emotic Demo](https://img.youtube.com/vi/b06LVc8NDls/0.jpg)](https://www.youtube.com/watch?v=b06LVc8NDls&ab_channel=RashedHadi)

### What to find where

```bash
repository
├── backend                      ## Flask backend
    ├── app.py                   ## server
    ├── model.pkl                ## trained svm model
    ├── requirements.txt         ## required packages for project
├── frontend                     ## NextJS frontend
├── README.md                    ## You are here
├── GRU_model                    ## Gated Recurrent Unit model 
    ├── model.py                 ## model
    ├── process.py               ## processing data for model
    ├── predict.py               ## trying to predict with this model
├── KNN_model                    ## K Nearest Neighbors model
    ├── knn_model.py             ## model
    ├── process_data.py          ## processing data for model    
├── process_data.py              ## process data for main svm model
├── svm_model.py                 ## main model used for prediction
├── generate_sample.py           ## generates 1 sample for each emotion to try to predict


```

<a name="installation"></a>

## 2. Installation

### Clone the Repository

```bash
git clone https://github.com/sfu-cmpt340/EMOTIC_g3.git
cd EMOTIC_g3
```

### Install Dependencies

#### Frontend (Next.js)

```bash
cd frontend
npm install
npm i react-icons
```

Then navigate back to the main directory:

```bash
cd ..
```

#### Backend (Flask)

```bash
cd backend
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

<a name="repro"></a>
## 3. Reproduction

### (Optional) Running the Web Application and Server

To run the full-stack application locally, you need to start both the backend server and the frontend web application. Follow the steps below:

#### 1. Start the Backend Server

Navigate to the `backend` folder and run the Flask server with your virtual environment activated:

```bash
cd backend
flask --app app run
```

#### 2. Start the Frontend

Open a new terminal, navigate to the frontend folder, and start the Next.js development server:

```bash
cd frontend
npm run dev
```

Open your browser and navigate to http://localhost:3000/ to use the web application. Instructions to download data to use with the application can be found below.

### Running the ML Model Standalone

#### 1. Create the venv and install packages from the main directory:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install flask flask_cors pandas matplotlib seaborn scikit-learn tensorflow numpy
```

#### 2. Download sample data and run

```bash
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1DQPpjJIigouQEzcrkb9SQbCOPtSVbP5U' -O sample_data.zip
unzip sample_data.zip
python3 svm_model.py
>> Enter the name of the sample file: filename
```

`filename` should match any of the 9 csv files in Sample_data

#### Troubleshooting: wget does not work

Data can be found at https://drive.google.com/file/d/1DQPpjJIigouQEzcrkb9SQbCOPtSVbP5U/view?usp=sharing

- Download and unzip in the root directory of this project
- There should now exist a folder called Sample_data with 9 csv files 

#### 3. Output

Running the above python command should now display the predicted emotion of the selected csv data in the terminal
