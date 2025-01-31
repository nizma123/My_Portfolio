# Bike Rentals - Final Project Data Analytics

This is a final project from Dicoding in the "Belajar Analisis Data dengan Python" course to make analysis and create a dashboard from the bike sharing dataset. In the notebook file, I attached the way I did the analysis from Data Wrangling, Cleaning Data, Exploratory Data Analysis (EDA), and Data Visualization. I also make the dashboard using Streamlit as you can check in [here].

## File Structures
Here is the directory and file structure of this project:
```
Bike_Sharing
├───dashboard
│       dashboard.py
│       day.csv
└───data
│       day.csv
│       hour.csv
├───notebook.ipynb
├───requirements.txt
├───README.md
└───url.txt

```

* **dashboard/** : Contains the main files for data visualization.
  * ```day.csv``` : The main dataset used in the project.
  * ```dashboard.py``` : Python script for the dashboard or analysis.
* **data/** : Contains additional datasets used.
  * ```day.csv``` : First dataset.
  * ```hour.csv``` : Second dataset.
* **notebook.ipynb** : Jupyter Notebook containing data exploration and analysis.
* **README.md** : Documentation of this project.
* **requirements.txt** : List of dependencies required to run the project.
* **url.txt** : A text file that may contain reference source or related URLs.

## How to Use
1. Clone this repository:
   ```
   git clone https://github.com/nizma123/My_Portfolio.git
   ```
2. Navigate to the project directory:
   ```
   cd Bike_Sharing
   ```
3. Install depedencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the Jupyter Notebook:
   ```
   jupyter notebook notebook.ipynb
   ```
5. To run the dashboard, execute the following command:
   ```
   python streamlit run dashboard.py
   ```
