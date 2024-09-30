---

# MARINE SPECIES CLASSIFICATION USING MACHINE LEARNING

## Abstract

Classifying marine species is vital for biodiversity conservation and environmental monitoring. Traditional methods often rely on expert knowledge and manual observation, which can be time-consuming and prone to error. This project proposes an automated system that uses deep learning techniques to classify marine species from images. By employing advanced image recognition models, the system aims to facilitate accurate identification and monitoring of marine life, contributing to ecological research and conservation efforts. The project evaluates various convolutional neural network (CNN) architectures to identify the most effective model based on accuracy and performance metrics.

## Overview

This repository contains a web application that uses a trained model to classify marine species from uploaded images. The application is built with Flask, providing a user-friendly interface for interaction.

## Directory Structure

- **Marine Species Code/application/**: Contains the trained model and Flask API for the web application.
  - **marine_model.h5**: The saved model file.
  - **Flask/**: Contains the Flask app and static files.
    - **static/files/uploads/**: Directory for storing uploaded images.
    - **main.py**: Main entry point for running the Flask application.

- **Marine Species Code/codes/**: Contains Colab notebooks used for model training.
  - **marine_species_model.pynb**: Colab notebook for model training and evaluation.

## Getting Started

### Prerequisites

Ensure you have Python and the necessary libraries installed. Use `pip` to install the required packages.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install Dependencies**

   Install the required Python packages using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

### Steps for Executing the Application

1. **Extract the Application Folder**

   Extract the contents of the `application` folder to your local machine.

2. **Configure Model Path**

   Update the path for loading the model in `main.py` to match the directory on your machine:

   ```python
   model_path = 'path_to_your_model/marine_model.h5'
   ```

3. **Run the Flask Application**

   Start the Flask application by running:

   ```bash
   python main.py
   ```

   You will receive a URL where the app is hosted.

4. **Access the Web Application**

   Open your browser and navigate to the URL provided by the Flask app. The home page will be displayed.

5. **Upload Image**

   Click the "Add File" button to upload the image you want to classify.

6. **Submit for Prediction**

   Click the "Submit" button after uploading. The application will process the image and redirect you to the result page.

7. **View Results**

   On the result page, you will see the classification result, including the predicted marine species and confidence score based on the model’s prediction.

## Colab Notebooks

The `codes` directory contains Colab notebooks used for model training:

- **marine_species_model.pynb**: Contains the code for training and evaluating the classification model.

--- 
