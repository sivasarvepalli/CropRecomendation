import streamlit as st
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

# Initialize history dataframe
history_df = pd.DataFrame(columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'Recommended Crop'])

# Streamlit application
def main():
    # Set background color
    background_color = """
    <style>
    body {
        background-color: ##000066;
    }
    </style>
    """
    st.markdown(background_color, unsafe_allow_html=True)

    st.title('Crop Recommendation System')

    # Display input fields for crop recommendation
    st.subheader('Input Fields for Crop Recommendation')
    N = st.number_input('Nitrogen (N)', min_value=0.0)
    P = st.number_input('Phosphorus (P)', min_value=0.0)
    K = st.number_input('Potassium (K)', min_value=0.0)
    temperature = st.number_input('Temperature')
    humidity = st.number_input('Humidity')
    ph = st.number_input('pH')
    rainfall = st.number_input('Rainfall')

    # Recommend crop button
    if st.button('Recommend Crop'):
        # Use the model to make recommendations for the user's inputs
        new_location = [[N, P, K, temperature, humidity, ph, rainfall]]
        recommended_crop = model.predict(new_location)[0]

        # Record the history
        history_df.loc[len(history_df)] = [N, P, K, temperature, humidity, ph, rainfall, recommended_crop]

        # Save history to Excel file
        history_df.to_excel( r'C:\Users\sivas\PycharmProjects\cropDP\history.xlsx', index=False)

        st.write(f'Recommended Crop: {recommended_crop}')

    # Display history
    st.subheader('Recommendation History')
    if st.checkbox('Show History'):
        history_data = pd.read_excel(r'C:\Users\sivas\PycharmProjects\cropDP\history.xlsx')
        st.write(history_data)

if __name__ == '__main__':
    main()
