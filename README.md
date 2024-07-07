# NeuroVID Predictor

NeuroVID Predictor is an AI-powered application for medical image analysis, specifically designed for neurological conditions and COVID-19 diagnosis using deep learning techniques.

Overview

NeuroVID Predictor integrates cutting-edge AI models to assist in the diagnosis of brain tumors and COVID-19 using medical imaging datasets. The application provides a user-friendly interface for uploading medical images and obtaining automated predictions.

Features

- Medical Image Upload: Easily upload brain MRI images for brain tumor detection or COVID-19 radiography images for diagnosis.
- **Automated Prediction: Obtain rapid predictions using advanced AI models trained on extensive datasets.
- **User Interface: Simple and intuitive interface designed for healthcare professionals and researchers.

Installation

To run NeuroVID Predictor locally, follow these steps:

1. Clone the Repository:
   ```bash
   git clone https://github.com/your_username/neurovid-predictor.git
   cd neurovid-predictor
   ```

2. Install Dependencies:
   ```bash
   npm install
   ```

3. Start the Application:
   ```bash
   npm start
   ```
   The application will run on `http://localhost:3000` by default.

4. Set Up Backend (Flask API):
   - Ensure Python 3.x and pip are installed.
   - Navigate to the `backend` directory.
   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Start the Flask server:
     ```bash
     python app.py
     ```
   The Flask server should run on `http://localhost:5000`.

Usage

1. Upload Images:
   - Navigate to the upload section on the web interface.
   - Select and upload medical images (PNG or JPG format).

2. Get Predictions:
   - Once uploaded, the AI model will process the images.
   - View predictions for brain tumor presence or COVID-19 diagnosis.

3. Interpret Results:
   - Results will be displayed indicating the predicted class and confidence level.

Model Accuracy

During training, the model achieved an accuracy of 91.42% on the training set and 77.50% on the validation set.

Technologies Used

Frontend: React.js, Axios, Bootstrap
Backend: Flask, Python
AI/ML Framework: TensorFlow, Keras
Dataset: Combined datasets of Brain MRI Images and COVID-19 Radiography Images

Contributing

Contributions are welcome! If you'd like to contribute to NeuroVID Predictor, please fork the repository and create a pull request. For major changes, please open an issue first to discuss what you would like to change.

License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

