import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")

st.title("🤖 FAQ Chatbot")
st.write("Ask a question and get the most relevant FAQ answer.")

faqs = {
    "What is artificial intelligence?": "Artificial Intelligence is a technology that allows machines to think, learn, and make decisions like humans.",
    "What is machine learning?": "Machine Learning is a branch of AI where computers learn from data without being directly programmed.",
    "What is deep learning?": "Deep Learning uses neural networks to solve complex problems like image recognition and speech processing.",
    "What is natural language processing?": "NLP helps computers understand and process human languages.",
    "What is computer vision?": "Computer Vision allows computers to understand images and videos.",
    "What is data science?": "Data Science is the process of collecting, analyzing, and using data to make decisions.",
    "What is Python used for?": "Python is used for web development, AI, machine learning, automation, and data analysis.",
    "What is chatbot?": "A chatbot is a software application that can communicate with users and answer their questions.",
    "What is Streamlit?": "Streamlit is a Python framework used to build simple and interactive web apps.",
    "How are you?": "I am fine and ready to help you.",
"What is your name?": "I am an AI FAQ chatbot.",
"Who created you?": "I was created using Python and Streamlit.",
"Hello": "Hello! How can I help you today?",
"Hi": "Hi! Ask me any AI-related question.",
    "What is TF-IDF?": "TF-IDF is a technique used to find the importance of words in a document."
}

questions = list(faqs.keys())

user_question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if user_question.strip():
        all_questions = questions + [user_question]

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(all_questions)

        similarity = cosine_similarity(vectors[-1], vectors[:-1])
        best_match_index = similarity.argmax()
        best_score = similarity[0][best_match_index]

        st.subheader("Bot Response")

        if best_score > 0.2:
            st.success(faqs[questions[best_match_index]])
            st.caption(f"Matched FAQ: {questions[best_match_index]}")
        else:
            st.warning("Sorry, I could not find a suitable answer.")
    else:
        st.warning("Please enter a question.")