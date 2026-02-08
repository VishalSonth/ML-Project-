# 🚀 End-to-End Machine Learning Project: Student Performance Prediction

This project implements a comprehensive, industry-standard **Machine Learning Pipeline**. It covers everything from data ingestion and transformation to model training, hyperparameter tuning, and deployment on **AWS Elastic Beanstalk** using **CI/CD pipelines**.

## 🌟 Key Features
- **Modular Code Structure**: Follows best practices by separating concerns into `components` (Data Ingestion, Transformation, Model Trainer) and `pipelines` (Training, Prediction).
- **Automated Workflows**: Implements a full CI/CD pipeline for seamless updates and deployment.
- **Custom Exception Handling & Logging**: Robust error tracking and activity logging for production-level reliability.
- **Web Interface**: A Flask-based web application to interact with the model and get real-time predictions.

## 🛠️ Technology Stack
- **Language**: Python 3.8+
- **Machine Learning**: Scikit-learn, Pandas, NumPy, XGBoost, CatBoost.
- **Web Framework**: Flask
- **Deployment**: AWS Elastic Beanstalk
- **Version Control & CI/CD**: Git, GitHub, AWS CodePipeline.

## 🏗️ Project Architecture
The project is structured to be generic and scalable:
1. **Data Ingestion**: Reading data from local or remote databases and splitting into train/test sets [00:43:04].
2. **Data Transformation**: Handling missing values, categorical encoding, and feature scaling using Scikit-learn Pipelines [00:00:52].
3. **Model Trainer**: Testing multiple regression algorithms (Linear Regression, Random Forest, etc.) and selecting the best performer based on R2 Score [00:45:52].
4. **Prediction Pipeline**: A specialized module that takes web input, transforms it, and returns the model's prediction.

## 🚀 How to Run Locally

### 1. Clone the repository
bash
git clone [https://github.com/VishalSonth/langchain-project.git](https://github.com/VishalSonth/langchain-project.git)
cd langchain-project
2. Create and Activate Environment
Bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate # Mac/Linux
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Run the Application
Bash
python application.py
Open your browser and navigate to http://127.0.0.1:5000/predictdata.

☁️ Deployment on AWS
The application is hosted on AWS Elastic Beanstalk. The deployment is automated via GitHub Actions and AWS CodePipeline. Any change pushed to the main branch triggers a new build and deployment automatically [04:16:47].

📂 Project Structure
src/components/: Contains modules for Data Ingestion, Transformation, and Model Training.

src/pipeline/: Contains Training and Prediction pipelines.

src/logger.py & src/exception.py: Custom logging and error handling scripts.

application.py: The entry point for the Flask web app.

setup.py: Allows the project to be installed as a package [00:22:52].

