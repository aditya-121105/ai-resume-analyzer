PROJECT_RECOMMENDATIONS = {

    "docker": [
        "Dockerized FastAPI Resume Analyzer"
    ],

    "aws": [
        "Deploy FastAPI Application on AWS EC2"
    ],

    "fastapi": [
        "JWT Authentication REST API"
    ],

    "redis": [
        "FastAPI Redis Cache Project"
    ],

    "kubernetes": [
        "Microservices Deployment Project"
    ]
}


CERTIFICATION_RECOMMENDATIONS = {

    "aws": [
        "AWS Cloud Practitioner"
    ],

    "docker": [
        "Docker Foundations"
    ],

    "kubernetes": [
        "Kubernetes for Developers"
    ]
}

def generate_recommendations(
    missing_skills: list
):

    recommended_projects = []

    recommended_certifications = []

    for skill in missing_skills:

        recommended_projects.extend(

            PROJECT_RECOMMENDATIONS.get(
                skill,
                []
            )
        )

        recommended_certifications.extend(

            CERTIFICATION_RECOMMENDATIONS.get(
                skill,
                []
            )
        )

    return {

        "recommended_projects":
            list(set(recommended_projects)),

        "recommended_certifications":
            list(set(recommended_certifications))
    }