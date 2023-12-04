
from ModelTrainer import ModelTrainer
from StreamlitUi import StreamlitUI

if __name__ == "__main__":
    # Training the model
    model_trainer = ModelTrainer("./Reviews.csv")  # Adjust the path based on your actual project structure

    # Creating the Streamlit app
    streamlit_ui = StreamlitUI(model_trainer)

    # Running the Streamlit app
    streamlit_ui.run_app()
