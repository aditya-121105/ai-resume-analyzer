ROLE_KEYWORDS = {

    "Backend Engineer": [
        "fastapi",
        "flask",
        "django",
        "spring",
        "rest api",
        "backend"
    ],

    "Frontend Engineer": [
        "react",
        "angular",
        "vue",
        "javascript",
        "frontend"
    ],

    "Machine Learning Engineer": [
        "tensorflow",
        "pytorch",
        "machine learning",
        "deep learning",
        "nlp",
        "computer vision"
    ],

    "Data Analyst": [
        "power bi",
        "tableau",
        "data analysis",
        "excel",
        "sql"
    ],

    "DevOps Engineer": [
        "docker",
        "kubernetes",
        "terraform",
        "jenkins",
        "devops"
    ],

    "Cloud Engineer": [
        "aws",
        "azure",
        "gcp",
        "cloud"
    ]
}

def detect_role(
    job_description: str
):

    jd = job_description.lower()

    role_scores = {}

    for role, keywords in ROLE_KEYWORDS.items():

        score = 0

        for keyword in keywords:

            if keyword in jd:

                score += 1

        role_scores[role] = score

    max_score = max(
        role_scores.values()
    )

    if max_score == 0:

        return "Unknown"

    return max(
        role_scores,
        key=role_scores.get
    )