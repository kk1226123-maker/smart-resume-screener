import streamlit as st
from resume_parser import extract_text
from scorer import rank_resumes

st.set_page_config(page_title="Smart Resume Screener", layout="centered")

st.title("Smart Resume Screening System")

job_desc = st.text_area("Paste Job Description")

uploaded_files = st.file_uploader(
    " Upload Resumes (TXT files)", 
    accept_multiple_files=True, 
    type=["txt"]
)

if st.button(" Rank Candidates") and uploaded_files:
    resumes = []
    names = []

    for file in uploaded_files:
        text = file.read().decode("utf-8")
        resumes.append(extract_text(text))
        names.append(file.name)

    scores = rank_resumes(job_desc, resumes)

    results = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)

    st.subheader(" Ranking Results")

    for name, score in results:
        st.write(f" {name}: **{round(score * 100, 2)}%** match")

