import joblib

def load_trained_svm_model():
    return joblib.load('/Cell_quality/models/trained_model.pkl')

def predict_svm(X_test):
    clf = load_trained_svm_model()  # Load the SVM model
    yhat = clf.predict(X_test)  # Make predictions
    return yhat

