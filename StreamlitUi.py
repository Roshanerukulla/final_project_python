# StreamlitUI.py
import streamlit as st
from ModelTrainer import ModelTrainer

class StreamlitUI:
    def __init__(self, model_trainer):
        self.model_trainer = model_trainer
        self.query = st.text_input("Enter keyword to search comments by topic:")
        self.score_option = st.radio("Select Comments by Score", ["All", "Positive (>= 4)", "Neutral (3)", "Negative (<= 2)"])
        self.num_comments = st.sidebar.slider("Select the number of comments to display", min_value=1, max_value=100, value=5)

    def _display_comments(self, query, score_indicator, num_comments):
        comments_to_display = []
        for idx, row in self.model_trainer.df.iterrows():
            if query.lower() in row['Text'].lower() and (row['Score'] == score_indicator if score_indicator is not None else True):
                comments_to_display.append((row['ProfileName'], row['OriginalComment'], row['Score']))

        # Display the selected number of comments
        st.subheader(f"Top {num_comments} Comments:")
        for i in range(min(num_comments, len(comments_to_display))):
            username, original_comment, comment_score = comments_to_display[i]
            st.write(f"Username: {username}")
            st.write(f"Original Comment: {original_comment}")
            st.write(f"Score: {comment_score}")
            st.write("----")

    def run_app(self):
       st.markdown("<h1 style='text-align: center;'>Topic Search App</h1>", unsafe_allow_html=True)

        # Add a button to trigger the display when the slider value changes
        if st.button("Display Comments"):
            # Add radio buttons for selecting helpfulness criteria
            if self.score_option == "Positive (>= 4)":
                score_indicator = 4
            elif self.score_option == "Neutral (3)":
                score_indicator = 3
            elif self.score_option == "Negative (<= 2)":
                score_indicator = 2
            else:
                score_indicator = None  # Show all comments

            # Display the comments based on the current slider value
            self._display_comments(self.query, score_indicator, self.num_comments)

if __name__ == "__main__":
    # Training the model
    model_trainer = ModelTrainer("./Reviews.csv")  # Adjust the path based on your actual project structure

    # Creating the Streamlit app
    streamlit_ui = StreamlitUI(model_trainer)

    # Running the Streamlit app
    streamlit_ui.run_app()
