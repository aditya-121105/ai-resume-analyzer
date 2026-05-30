from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from app.services.analysis_service import (
    analyze_resume_skills_service,
    get_analysis_history_service, get_analysis_detail_service
)
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.auth.dependencies import (
    get_current_user

)
from app.models.user import User
from app.models.resume import Resume
from app.analysis.skill_analyzer import (
    compare_skills
)
from pydantic import BaseModel


class JobDescriptionRequest(BaseModel):

    resume_id: int

    job_description: str

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)
@router.post("/skills")
def analyze_resume_skills(

    request: JobDescriptionRequest,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    return analyze_resume_skills_service(

        resume_id=request.resume_id,

        job_description=request.job_description,

        db=db,

        current_user=current_user
    )

@router.get("/history")
def get_analysis_history(

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    return get_analysis_history_service(

        db=db,

        current_user=current_user
    )
@router.get("/{analysis_id}")
def get_analysis_detail(

    analysis_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    return get_analysis_detail_service(

        analysis_id=analysis_id,

        db=db,

        current_user=current_user
    )