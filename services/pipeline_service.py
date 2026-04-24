#pipeline_service.py
from core.preprocessing import clean_text
from core.embeddings import generate_embeddings
from core.similarity import SimilarityEngine
from core.scoring import calculate_match_score
from services.llm_feedback_service import LLMFeedbackService



class ResumePipelineService:

    def __init__(self):
        self.similarity_engine = SimilarityEngine()

        #cache dictionary for Job Description embeddings
        self._jd_cache = {}
        
        self.feedback_service = LLMFeedbackService()


    def analyze(self, resume_text: str, job_desc: str) -> dict:
        try:
            
            # 1. Preprocess
            cleaned_resume = clean_text(resume_text)
            cleaned_jd = clean_text(job_desc)

            # -------------------------
            # 2. Resume Embedding (always compute)
            # -------------------------
            resume_embedding = generate_embeddings(cleaned_resume)

            # JD Embedding with caching
            if cleaned_jd in self._jd_cache:
                job_embedding = self._jd_cache[cleaned_jd]
            else:
                job_embedding = generate_embeddings(cleaned_jd)
                self._jd_cache[cleaned_jd] = job_embedding

            # -------------------------
            # 3. Similarity
            # -------------------------
            similarities = self.similarity_engine.batch_similarity(
                resume_embedding,
                [job_embedding]
            )

            best_match = similarities[0]

            # 4. Keyword Analysis
            keyword_data = self.similarity_engine.keyword_overlap(
                cleaned_resume,
                cleaned_jd
            )
            
            #5. Final Score
            final_score = calculate_match_score(best_match)

            # 5.1 Feedback
            
            filtered_missing = [
                w for w in keyword_data["missing_keywords"]
                if w not in {"engineer", "developer", "role"}
            ]
            feedback = self.feedback_service.generate_feedback(
                cleaned_resume,
                cleaned_jd,
                final_score,
                filtered_missing,
                keyword_data["matched_keywords"] 
            )

            # 6. Response
            return {
                "status": "success",
                "match_score": final_score,

                "confidence": (
                    "High" if final_score > 80 else
                    "Moderate" if final_score > 60 else
                    "Low"
                ),

                "matched_keywords": keyword_data["matched_keywords"],
                "missing_keywords": keyword_data["missing_keywords"],
                "keyword_overlap_score": keyword_data["overlap_score"],
                "llm_feedback": feedback
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
