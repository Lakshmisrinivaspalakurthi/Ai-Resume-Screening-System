from src.skills import extract_skills

def recommend_roles(text):

    skills = extract_skills(text)

    roles = []

    if "power bi" in skills:
        roles.append(
            "Data Analyst"
        )

    if "machine learning" in skills:
        roles.append(
            "ML Engineer"
        )

    if "nlp" in skills:
        roles.append(
            "AI Engineer"
        )

    return roles
