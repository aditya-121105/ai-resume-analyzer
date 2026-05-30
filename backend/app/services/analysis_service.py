from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.analysis.recommendation_engine import (
    generate_recommendations
)
from app.models.resume import Resume
from app.models.user import User
from app.models.analysis import Analysis
from app.analysis.skill_analyzer import (
    compare_skills
)


def analyze_resume_skills_service(

    resume_id: int,

    job_description: str,

    db: Session,

    current_user: User
):

    resume = db.query(Resume).filter(

        Resume.id == resume_id,

        Resume.owner_id == current_user.id

    ).first()

    if not resume:

        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    analysis_result = compare_skills(

        resume.resume_text,

        job_description
    )
    recommendations = generate_recommendations(

        analysis_result["missing_skills"]
    )
    analysis_result.update(
        recommendations
    )
    analysis = Analysis(
        resume_id=resume.id,
        job_description=job_description,
        match_percentage=analysis_result["match_percentage"],
        matched_skills=",".join(
            analysis_result["matched_skills"]
        ),
        missing_skills=",".join(
            analysis_result["missing_skills"]
        )
    )

    db.add(analysis)
    db.commit()
    analysis_result["analysis_id"] = analysis.id

    return analysis_result




def get_analysis_history_service(
    db: Session,
    current_user: User
):

    analyses = (

        db.query(Analysis)

        .join(Resume)

        .filter(
            Resume.owner_id ==
            current_user.id
        )

        .all()
    )

    return [

        {
            "analysis_id": analysis.id,

            "resume_id": analysis.resume_id,

            "resume_name": analysis.resume.file_name,

            "match_percentage":
                analysis.match_percentage,

            "created_at":
                analysis.created_at
        }

        for analysis in analyses
    ]

def get_analysis_detail_service(

    analysis_id: int,

    db: Session,

    current_user: User
):

    analysis = (

        db.query(Analysis)

        .join(Resume)

        .filter(

            Analysis.id == analysis_id,

            Resume.owner_id ==
            current_user.id

        )

        .first()
    )

    if not analysis:

        raise HTTPException(
            status_code=404,
            detail="Analysis not found"
        )

    return {

        "analysis_id":
            analysis.id,

        "resume_id":
            analysis.resume_id,

        "resume_name":
            analysis.resume.file_name,

        "job_description":
            analysis.job_description,

        "match_percentage":
            analysis.match_percentage,

        "matched_skills":
            analysis.matched_skills.split(","),

        "missing_skills":
            analysis.missing_skills.split(","),

        "created_at":
            analysis.created_at
    }