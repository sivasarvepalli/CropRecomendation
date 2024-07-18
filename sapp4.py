import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load the crop recommendation dataset
data = pd.read_csv(r"C:\Users\sivas\OneDrive\Pictures\Crop_recommendation.csv")

# Select relevant features
X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'previous_crop']]
y = data['label']

# Train a decision tree classifier
model = DecisionTreeClassifier()
model.fit(X, y)

# Streamlit application
def main():
    st.title('Crop Recommendation System')

    # Initialize history dataframe or create it if not exists
    try:
        history_df = pd.read_excel(r'C:\Users\sivas\PycharmProjects\cropDP\history.xlsx')
    except FileNotFoundError:
        history_df = pd.DataFrame(columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'previous_crop', 'Recommended Crop'])

    # Display input fields for crop recommendation
    st.subheader('Input Fields for Crop Recommendation')
    N = st.number_input('Nitrogen (N)', min_value=0.0)
    P = st.number_input('Phosphorus (P)', min_value=0.0)
    K = st.number_input('Potassium (K)', min_value=0.0)
    temperature = st.number_input('Temperature')
    humidity = st.number_input('Humidity')
    ph = st.number_input('pH')
    rainfall = st.number_input('Rainfall')
    previous_crop = st.selectbox('Previous Crop', options=['Maize', 'Rice', 'Wheat', 'Cotton'])

    # Recommend crop button
    if st.button('Recommend Crop'):
        # Use the model to make recommendations for the user's inputs
        new_location = [[N, P, K, temperature, humidity, ph, rainfall, previous_crop]]
        recommended_crop = model.predict(new_location)[0]

        # Create a new DataFrame with the new data
        new_data = pd.DataFrame({'N': [N], 'P': [P], 'K': [K], 'temperature': [temperature],
                                 'humidity': [humidity], 'ph': [ph], 'rainfall': [rainfall],
                                 'previous_crop': [previous_crop], 'Recommended Crop': [recommended_crop]})

        # Concatenate the new data with the existing history DataFrame
        history_df = pd.concat([history_df, new_data], ignore_index=True)

        # Save history to Excel file
        history_df.to_excel(r'C:\Users\sivas\PycharmProjects\cropDP\history.xlsx', index=False)

        st.write(f'Recommended Crop: {recommended_crop}')

    # Display history
    st.subheader('Recommendation History')
    if st.checkbox('Show History'):
        st.write(history_df)

if __name__ == '__main__':
    main()
