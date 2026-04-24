#resume_controller.py
from services.pipeline_service import ResumePipelineService

class ResumeController:

    def __init__(self):
        self.service = ResumePipelineService()

    def analyze_resume(self, resume, jd):
        if not resume or not jd:
            return {"status": "error", "message": "Missing input"}

        if len(resume) < 50:
            return {"status": "error", "message": "Resume too short"}

        return self.service.analyze(resume, jd)