ROLE_PROJECT_RECOMMENDATIONS = {

    "Backend Engineer": {

        "docker": [
            "Dockerized FastAPI API"
        ],

        "fastapi": [
            "JWT Authentication REST API"
        ],

        "aws": [
            "Deploy FastAPI Application on AWS EC2"
        ]
    },

    "Machine Learning Engineer": {

        "nlp": [
            "Resume Classification System",
            "Sentiment Analysis Application"
        ],

        "tensorflow": [
            "Image Classification Project"
        ],

        "deep learning": [
            "CNN Image Classification System"
        ]
    },

    "DevOps Engineer": {

        "docker": [
            "Containerized Microservice Deployment"
        ],

        "kubernetes": [
            "Kubernetes Cluster Deployment"
        ],

        "terraform": [
            "AWS Infrastructure as Code Project"
        ]
    }
}

ROLE_CERTIFICATION_RECOMMENDATIONS = {

    "Backend Engineer": {

        "aws": [
            "AWS Cloud Practitioner"
        ],

        "docker": [
            "Docker Foundations"
        ]
    },

    "Machine Learning Engineer": {

        "nlp": [
            "Natural Language Processing Specialization"
        ],

        "tensorflow": [
            "TensorFlow Developer Certificate"
        ]
    }
}

def generate_recommendations(
    missing_skills,
    target_role
):

    recommended_projects = []

    recommended_certifications = []

    role_projects = (
        ROLE_PROJECT_RECOMMENDATIONS.get(
            target_role,
            {}
        )
    )

    role_certifications = (
        ROLE_CERTIFICATION_RECOMMENDATIONS.get(
            target_role,
            {}
        )
    )

    for skill in missing_skills:

        recommended_projects.extend(

            role_projects.get(
                skill,
                []
            )
        )

        recommended_certifications.extend(

            role_certifications.get(
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