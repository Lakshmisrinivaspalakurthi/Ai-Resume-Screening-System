from src.skills import extract_skills

def calculate_ats_score(
    resume_text,
    jd_text
):

    resume_skills = set(
        extract_skills(resume_text)
    )

    jd_skills = set(
        extract_skills(jd_text)
    )

    matched = resume_skills & jd_skills

    missing = jd_skills - resume_skills

    if len(jd_skills) == 0:
        score = 0
    else:
        score = (
            len(matched)
            /
            len(jd_skills)
        ) * 100

    return (
        round(score,2),
        list(matched),
        list(missing)
    )
