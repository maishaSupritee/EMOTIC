import os
import numpy as np
import pandas as pd
from process_data import preprocess, get_labels
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Function for training the model
def train_svm_model(eeg_data, labels):
    # Training: Split data into training and test sets:
    # Utilize a training to testing ratio of 80:20 as discussed by the group
    X_train, X_valid, y_train, y_valid = train_test_split(eeg_data, labels, test_size=0.20, random_state=59)

    # Standardize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_valid = scaler.transform(X_valid)

    # Create the Support-Vector-Machine model
    # Kernel: Complicated, 'linear' seems to work best with the format of our data
    # C: Tradeoff between maximizing margins and minimizing misclassifications
    svm = SVC(kernel='linear', C=2.0)
    svm.fit(X_train, y_train)

    # Testing: Make a prediction using the test set
    y_predict = svm.predict(X_valid)
    print("\nClassification Report:\n", classification_report(y_valid, y_predict))
    print("\nAccuracy:", accuracy_score(y_valid, y_predict))

    return svm, scaler

# Function to preprocess and classify a single input CSV file
def classify(svm_model, scaler, csv_path, downsample_factor):
    # Load the input CSV file
    input_data = pd.read_csv(csv_path, header=None).values  # Shape: (32, 7500)

    # Downsample the data
    downsampled_data = input_data[:, ::downsample_factor]  # Shape: (32, reduced_timepoints)

    # Flatten the data (32 channels * reduced_timepoints)
    flattened_data = downsampled_data.flatten().reshape(1, -1)

    # Standardize the input data using the scaler from training
    standardized_data = scaler.transform(flattened_data)

    # Perform classification
    prediction = svm_model.predict(standardized_data)

    return prediction

# Prepare model for training
if __name__ == "__main__":
    directory = "Processed_data_train"
    emotions = ["Anger", "Anger", "Anger",
                "Disgust", "Disgust", "Disgust",
                "Fear", "Fear", "Fear",
                "Sadness", "Sadness", "Sadness", 
                "Neutral", "Neutral", "Neutral", "Neutral",
                "Amusement", "Amusement", "Amusement",
                "Inspiration", "Inspiration", "Inspiration",
                "Joy", "Joy", "Joy",
                "Tenderness", "Tenderness", "Tenderness"]

    # Preprocess data (adjust second parameter to control downsampling)
    downsample = 10
    eeg_data = preprocess(directory, downsample)
    labels = get_labels(eeg_data.shape[0], emotions)

    # Reshape data (flatten from 3D to 2D)
    num_subjects, num_videos, num_channels, num_timepoints = eeg_data.shape
    reshaped_eeg_data = eeg_data.reshape(-1, num_channels * num_timepoints)

    # Call function to train the Support-Vector-Machine model
    svm_model, scaler = train_svm_model(reshaped_eeg_data, labels)

    # Example: Classify a single input CSV file
    sample_file = "neutral.csv"
    sample_path = os.path.join("Sample_data", sample_file)
    prediction = classify(svm_model, scaler, sample_path, downsample)

    print("\nPredicted emotion:", prediction)