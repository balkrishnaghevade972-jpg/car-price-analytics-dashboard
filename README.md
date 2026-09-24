# Car Price Analytics Dashboard

An interactive **Car Price Analytics and Prediction Dashboard** built using Python, Machine Learning, and Streamlit.

The project combines **data analysis, visualization, machine learning, and an interactive web dashboard** to explore car specifications, understand pricing patterns, compare vehicles, and predict car prices using a trained Machine Learning model.

---

## Project Overview

The **Car Price Analytics Dashboard** provides an interactive platform for analyzing automobile data.

Users can explore different cars based on:

* Manufacturer
* Fuel Type
* Horsepower
* Top Speed
* 0–100 km/h Performance
* Engine CC / Battery Capacity
* Number of Seats
* Torque
* Price

The project also includes a **Machine Learning-based price prediction system** that estimates the price of a car based on its specifications.

The complete project workflow is:

```text
Dataset
   ↓
Data Cleaning & Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Machine Learning Model
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Streamlit Dashboard
   ↓
Deployment
```

---

##  Objectives

The main objectives of this project are:

1. To analyze automobile specifications and pricing data.
2. To identify relationships between car features and prices.
3. To visualize important patterns in the dataset.
4. To compare cars based on performance and pricing.
5. To analyze different automobile manufacturers.
6. To develop a Machine Learning model for price prediction.
7. To create an interactive dashboard using Streamlit.
8. To deploy the dashboard so that it can be accessed online.

---

##  Technologies Used

| Technology      | Purpose                             |
| --------------- | ----------------------------------- |
| Python          | Main programming language           |
| Google Colab    | Data analysis and model development |
| Pandas          | Data manipulation                   |
| NumPy           | Numerical operations                |
| Plotly          | Interactive visualizations          |
| Scikit-learn    | Machine Learning                    |
| Joblib          | Saving and loading ML model         |
| Streamlit       | Dashboard development               |
| GitHub          | Source-code management              |
| Streamlit Cloud | Dashboard deployment                |

---

##  Dataset

The project uses a car dataset containing information about automobile specifications and prices.

### Important Features

| Feature                     | Description                         |
| --------------------------- | ----------------------------------- |
| `Company Names`             | Manufacturer/company of the car     |
| `Cars Names`                | Name/model of the car               |
| `Fuel Types`                | Type of fuel used                   |
| `HorsePower`                | Engine power                        |
| `Total Speed`               | Maximum speed                       |
| `Performance(0 - 100 )KM/H` | Acceleration performance            |
| `CC_Battery`                | Engine capacity or battery capacity |
| `Seats_Clean`               | Number of seats                     |
| `Torque_Nm`                 | Torque produced by the vehicle      |
| `Engines`                   | Engine information                  |
| `Price`                     | Price of the car                    |

---

##  Project Development

### 1. Data Collection

The automobile dataset was collected and loaded into **Google Colab** for analysis.

The dataset was examined to understand:

* Number of records
* Number of features
* Data types
* Missing values
* Duplicate records
* Numerical and categorical variables

---

### 2. Data Preprocessing

The dataset was prepared before applying Machine Learning.

The preprocessing stage includes operations such as:

* Handling missing values
* Checking duplicate records
* Cleaning inconsistent data
* Converting data into appropriate formats
* Selecting relevant features
* Preparing categorical and numerical features

This ensures that the data is suitable for analysis and model training.

---

### 3. Exploratory Data Analysis

Exploratory Data Analysis was performed to understand relationships within the automobile dataset.

Different visualizations were used to analyze:

* Car price distribution
* Horsepower distribution
* Top speed
* Manufacturer-wise pricing
* Fuel-type distribution
* Horsepower vs price
* Performance vs price
* Other relationships between car specifications

Interactive visualizations are also available in the Streamlit dashboard.

---

##  Machine Learning

A Machine Learning model was developed to predict car prices.

### Model Used

**Random Forest Regression**

Random Forest combines multiple decision trees to generate a prediction.

The model uses car specifications such as:

* Manufacturer
* Fuel Type
* Horsepower
* Top Speed
* 0–100 km/h Performance
* CC/Battery
* Seats
* Torque

to estimate the car price.

### Model Workflow

```text
Input Car Specifications
          ↓
Data Preprocessing
          ↓
Feature Transformation
          ↓
Random Forest Model
          ↓
Predicted Car Price
```

The trained model was saved using **Joblib**.

```text
car_price_model_v2.pkl
```

This allows the Streamlit application to load the trained model without retraining it every time.

---

##  Streamlit Dashboard

The Streamlit application provides an interactive interface for exploring the automobile dataset.

### Dashboard Sections

The dashboard contains the following major sections:

####  Summary

Provides an overview of the project and the automobile dataset.

####  Overview

Displays important statistics and visualizations related to the dataset.

####  Performance

Allows users to analyze vehicle performance characteristics such as:

* Horsepower
* Top speed
* Acceleration
* Torque

####  Pricing

Provides analysis of automobile prices and their relationship with different features.

####  Compare

Allows users to compare different cars based on their specifications.

#### Brands

Provides manufacturer-wise analysis and comparison.

####  Explorer

Allows users to explore individual cars and their specifications.

####  Predict Price

Allows users to enter vehicle specifications and obtain an estimated car price using the trained Machine Learning model.

---

##  Interactive Filters

The dashboard provides filters that allow users to customize their analysis.

Available filters include:

* Car search
* Manufacturer
* Fuel type
* Price range
* Horsepower range
* Top speed range

The charts and statistics update according to the selected filters.

---

##  Key Performance Indicators

The dashboard provides important summary metrics such as:

* **Total Cars**
* **Average Price**
* **Average Horsepower**
* **Average Top Speed**

These metrics provide a quick overview of the currently selected dataset.

---

##  Project Structure

```text
Car-Price-Analytics/
│
├── README.md
├── final_car_dataset.csv
├── car_price_model_v2.pkl
├── app.py
└── requirements.txt
```

### File Description

**`app.py`**

Main Streamlit dashboard application.

**`final_car_dataset.csv`**

Dataset containing automobile specifications and prices.

**`car_price_model_v2.pkl`**

Trained Random Forest Machine Learning model.

**`requirements.txt`**

Contains the Python libraries required to run the project.

**`README.md`**

Project documentation.

---

##  How to Run the Project Locally

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Step 2: Open the Project Folder

```bash
cd Car-Price-Analytics
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

```bash
streamlit run app.py
```

The dashboard will open in your browser.

Usually it will be available at:

```text
http://localhost:8501
```

---

##  Deployment

The dashboard can be deployed using **Streamlit Community Cloud**.

Deployment workflow:

```text
GitHub Repository
        ↓
Streamlit Community Cloud
        ↓
Install Dependencies
        ↓
Run app.py
        ↓
Live Dashboard
```

### Live Dashboard

**Car Price Analytics Dashboard**

https://car-price-analytics-dashboard-dgx7vmvcjrkqohimxns2ap.streamlit.app/

---

##  Future Scope

The project can be further enhanced with:

* Advanced Machine Learning model comparison
* Multiple price prediction algorithms
* Car recommendation system
* Used-car price prediction
* Depreciation analysis
* Advanced brand comparison
* User-uploaded datasets
* Automated PDF reports
* More advanced car visualizations
* Real-time automobile market data
* Mobile-friendly dashboard improvements

---

##  Advantages

* Interactive and user-friendly interface
* Easy exploration of automobile data
* Interactive charts and visualizations
* Machine Learning-based price prediction
* Car comparison functionality
* Manufacturer analysis
* Filter-based data exploration
* Online accessibility through deployment

---

##  Limitations

* Prediction accuracy depends on the quality and coverage of the dataset.
* The model is trained using the available historical dataset.
* Market prices can change over time.
* The dashboard does not represent real-time automobile market prices unless the dataset is updated.

---

##  Conclusion

The **Car Price Analytics Dashboard** combines data analytics, visualization, Machine Learning, and web application development into a single project.

The project demonstrates how automobile data can be analyzed to discover pricing and performance patterns and how Machine Learning can be used to estimate car prices based on vehicle specifications.

The Streamlit dashboard makes the analysis interactive and easier for users to explore, compare, and understand automobile data.

---

##  Project

**Project:** Car Price Analytics Dashboard
**Domain:** Data Analytics & Machine Learning
**Language:** Python
**Dashboard:** Streamlit
**Model:** Random Forest Regression
**Development Environment:** Google Colab + Streamlit

---

##  References

* Python Documentation
* Pandas Documentation
* NumPy Documentation
* Scikit-learn Documentation
* Plotly Documentation
* Streamlit Documentation
* Google Colab Documentation
