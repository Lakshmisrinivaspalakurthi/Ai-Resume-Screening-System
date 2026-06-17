def suggestions(missing):

    tips = []

    mapping = {

        "power bi":
            "Build a Power BI Dashboard",

        "sql":
            "Practice SQL Window Functions",

        "python":
            "Complete Python Projects",

        "machine learning":
            "Build Churn Prediction Project",

        "nlp":
            "Build Resume Screening System"
    }

    for skill in missing:

        if skill in mapping:
            tips.append(
                mapping[skill]
            )

    return tips
