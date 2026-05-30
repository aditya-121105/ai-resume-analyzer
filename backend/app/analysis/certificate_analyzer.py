CERTIFICATIONS = [

    "aws cloud practitioner",

    "aws solutions architect",

    "google cloud associate",

    "tensorflow developer",

    "docker foundations",

    "kubernetes for developers",

    "microsoft azure fundamentals",

    "oracle java certification",

    "google data analytics"
]

def extract_certifications(
    resume_text: str
):

    text = resume_text.lower()

    detected_certifications = []

    for certification in CERTIFICATIONS:

        if certification in text:

            detected_certifications.append(
                certification
            )

    return detected_certifications