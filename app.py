import streamlit as st
from backend.parser import extract_text_from_pdf, extract_text_from_txt
from backend.logic import summarize_text, embed_and_index, answer_question, generate_questions, evaluate_response

st.set_page_config(page_title="Smart Research Assistant")
st.title("Smart Research Summarizer")
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_txt(uploaded_file)

    st.subheader("Auto Summary")
    summary = summarize_text(text)
    st.write(summary)

    index, chunks = embed_and_index(text)

    mode = st.radio("Choose a mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        query = st.text_input("Ask a question about the document")
        if query:
            answer, context = answer_question(query, index, chunks)
            st.write(f"**Answer:** {answer}")
            st.info(f"Justified from context: {context[:200]}...")

    elif mode == "Challenge Me":
        questions = generate_questions(text)
        for i, q in enumerate(questions):
            st.write(f"**Q{i+1}:** {q}")
            user_ans = st.text_input(f"Your Answer to Q{i+1}", key=f"q{i+1}")
            if user_ans:
                _, context = answer_question(q, index, chunks)
                evaluation = evaluate_response(q, context, user_ans)
                st.write(f"**Evaluation:** {evaluation}")
