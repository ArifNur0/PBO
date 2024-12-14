import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

def read_data(file_name):
    try:
        df = pd.read_excel(file_name)
        print("Data successfully loaded.")
        return df
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

def show_missing_values(df):
    print("Missing values in each column:")
    print(df.isnull().sum())

def fill_missing_values(df):
    for column in df.columns:
        if df[column].dtype in ['float64', 'int64']:
            df[column].fillna(df[column].median(), inplace=True)
        elif df[column].dtype == 'object':
            df[column].fillna(df[column].mode()[0], inplace=True)
    print("Missing values filled.")

def train_model(X_train, y_train, model_type):
    if model_type == "RandomForest":
        model = RandomForestClassifier(n_estimators=100, random_state=42)
    elif model_type == "NaiveBayes":
        model = GaussianNB()
    elif model_type == "DecisionTree":
        model = DecisionTreeClassifier()
    else:
        print("Invalid model type.")
        return None

    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Model Accuracy:", accuracy)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

def main():
    df = None
    while True:
        print(" ==== ====  Analisis Data Air Quality  ==== ==== ")
        print("1. Membaca Data File XLSX")
        print("2. Parameter(Data Latih)")
        print("3. Analisis Dengan Algoritma")
        print("0. Keluar")

        pilihan = input("Masukkan Pilihan: ")
        
        if pilihan == "1":
            nama_file = input("Masukkan Nama File: ")
            df = read_data(nama_file)

        elif pilihan == "2":
            if df is None:
                print("Data belum dimuat. Silakan muat data terlebih dahulu.")
                continue
            
            print("=== Pilihan ===")
            print("1. Tunjukkan Missing Value")
            print("2. Isi Missing Value")
            print("3. Latih Data")

            parameter = input("Masukkan Parameter: ")
            if parameter == "1":
                show_missing_values(df)

            elif parameter == "2":
                fill_missing_values(df)
                print(df)

            elif parameter == "3":
                X = df.drop('Air Quality', axis=1)
                y = df['Air Quality']
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                print("Data siap untuk dilatih.")

            else:
                print("Error: Pilihan tidak valid.")

        elif pilihan == "3":
            if 'X_train' not in locals():
                print("Data belum dilatih. Silakan latih data terlebih dahulu.")
                continue
            
            print("Pilih Algoritma")
            print("1. Random Forest")
            print("2. Naive Bayesian")
            print("3. Tree Decision")

            algoritma = input("Masukkan Algoritma: ")
            model_type = ""
            if algoritma == "1":
                model_type = "RandomForest"
            elif algoritma == "2":
                model_type = "NaiveBayes"
            elif algoritma == "3":
                model_type = "DecisionTree"
            else:
                print("Error: Pilihan tidak valid.")
                continue

            model = train_model(X_train, y_train, model_type)
            evaluate_model(model, X_test, y_test)

        elif pilihan == "0":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()