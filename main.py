import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load the crop recommendation dataset
data = pd.read_csv(r"C:\Users\sivas\Downloads\Crop_recommendation.csv")

# Select relevant features
X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = data['label']

# Train a decision tree classifier
model = DecisionTreeClassifier()
model.fit(X, y)

# Get input from the user
N = float(input('Enter the value for Nitrogen (N): '))
P = float(input('Enter the value for Phosphorus (P): '))
K = float(input('Enter the value for Potassium (K): '))
temperature = float(input('Enter the value for temperature: '))
humidity = float(input('Enter the value for humidity: '))
ph = float(input('Enter the value for pH: '))
rainfall = float(input('Enter the value for rainfall: '))

# Use the model to make recommendations for the user's inputs
new_location = [[N, P, K, temperature, humidity, ph, rainfall]]
predicted_crop = model.predict(new_location)
print('Recommended crop:', predicted_crop[0])
