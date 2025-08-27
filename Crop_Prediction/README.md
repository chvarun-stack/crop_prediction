🌱 Smart Crop Prediction using Machine Learning

This project is a Django-based web application that predicts the most suitable crop for farming based on soil and environmental parameters.
It leverages machine learning models such as Naive Bayes, Logistic Regression, SVM, Decision Tree, and Voting Classifier to provide accurate predictions.

📌 Features

✅ User-friendly web interface built with Django + Bootstrap

✅ Takes input of soil & environmental parameters (N, P, K, Temperature, Humidity, pH, Rainfall)

✅ Trains multiple ML models and selects the best performing one

✅ Provides real-time crop prediction

✅ Clean UI with prediction results displayed instantly

📂 Project Structure
Crop_Prediction/
│── Crop_Prediction/        # Main Django project folder
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routes
│   ├── wsgi.py             # WSGI application
│   └── asgi.py             # ASGI application
│
│── crop/                   # Core application
│   ├── views.py            # ML model integration & prediction logic
│   ├── models.py           # Django models (if needed)
│   ├── templates/          # HTML templates
│   └── static/             # CSS, JS, images
│
│── manage.py               # Django entry point
│── Crop_Datasets.csv       # Dataset used for training/testing
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
│── .gitignore              # Git ignore file

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/chvarun-stack/crop-prediction.git
cd crop-prediction

2️⃣ Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run the server
python manage.py runserver


Visit http://127.0.0.1:8000/
 in your browser 🎉

📊 Dataset

The project uses Crop_Datasets.csv, which contains information on:

N (Nitrogen), P (Phosphorus), K (Potassium)

Temperature, Humidity, pH, Rainfall

Target variable: Crop Label

🤖 Machine Learning Models

The following models are trained & compared:

Naive Bayes

Logistic Regression

Support Vector Machine (SVM)

Decision Tree

Voting Classifier

The best-performing model (KNN/Voting Classifier) is used for final predictions.



🚀 Future Enhancements

Add real-time weather API integration

Improve UI/UX with modern frontend frameworks

Deploy on Heroku / AWS / Render

👨‍💻 Author

Varun Chandubatla – GitHub
 | LinkedIn

✨ This project is built as part of learning Machine Learning + Django and can be extended for real-world applications in Smart Agriculture.