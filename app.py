import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.parser import extract_text
from src.embedding import generate_embedding
from src.ranking import calculate_score
from src.ats import calculate_ats_score
from src.quality import resume_quality
from src.recommendations import suggestions
from src.career_paths import recommend_roles

st.set_page_config(
    page_title="AIResume Analyzer",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AIResume Analyzer")

st.markdown("""
Analyze your resume against a job description and receive:

✅ ATS Score

✅ Skill Match Analysis

✅ Missing Skills Detection

✅ Resume Quality Assessment

✅ Career Recommendations

✅ Learning Roadmap
""")

jd = st.text_area(
    "📋 Paste Job Description"
)

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

if st.button("Analyze Resume"):

    if uploaded_file and jd:

        with open(
            uploaded_file.name,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        resume_text = extract_text(
            uploaded_file.name
        )

        ats_score, matched, missing = (
            calculate_ats_score(
                resume_text,
                jd
            )
        )

        quality_score = (
            resume_quality(
                resume_text
            )
        )

        recommendations = (
            suggestions(
                missing
            )
        )

        roles = (
            recommend_roles(
                resume_text
            )
        )

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📄 Overview",
                "🎯 ATS Analysis",
                "🧠 Skill Gap",
                "🚀 Career Roadmap"
            ]
        )

        with tab1:

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "ATS Score",
                f"{ats_score}%"
            )

            c2.metric(
                "Resume Quality",
                f"{quality_score}%"
            )

            c3.metric(
                "Matched Skills",
                len(matched)
            )

        with tab2:

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=ats_score,
                    title={
                        "text":
                        "ATS Score"
                    },
                    gauge={
                        "axis":
                        {"range":[0,100]}
                    }
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with tab3:

            st.subheader(
                "Matched Skills"
            )

            for skill in matched:

                st.success(
                    f"✓ {skill}"
                )

            st.subheader(
                "Missing Skills"
            )

            for skill in missing:

                st.error(
                    f"✗ {skill}"
                )

            fig = px.pie(
                values=[
                    len(matched),
                    len(missing)
                ],
                names=[
                    "Matched",
                    "Missing"
                ],
                hole=0.6
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with tab4:

            st.subheader(
                "Recommended Roles"
            )

            for role in roles:

                st.info(role)

            st.subheader(
                "Improvement Suggestions"
            )

            for tip in recommendations:

                st.write(
                    f"• {tip}"
                )
