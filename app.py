import streamlit as st
import pandas as pd

from src.parser import extract_text
from src.embedding import generate_embedding
from src.ranking import calculate_score

st.title("AI Resume Screening System")

jd = st.text_area(
    "Paste Job Description"
)

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Rank Candidates"):

    if jd and uploaded_files:

        results = []

        jd_embedding = generate_embedding(jd)

        for file in uploaded_files:

            with open(file.name, "wb") as f:
                f.write(file.getbuffer())

            resume_text = extract_text(file.name)

            resume_embedding = generate_embedding(
                resume_text
            )

            score = calculate_score(
                resume_embedding,
                jd_embedding
            )

            results.append(
                {
                    "Resume": file.name,
                    "Match Score": round(score, 2)
                }
            )

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="Match Score",
            ascending=False
        )

        st.dataframe(df)
