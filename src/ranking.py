from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(
    resume_embedding,
    jd_embedding
):

    score = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )

    return float(score[0][0]) * 100
