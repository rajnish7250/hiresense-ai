##similarity.py
from typing import List, Dict
import numpy as np

STOP_WORDS = {
    "the", "is", "and", "for", "to", "of", "in", "on",
    "a", "an", "with", "looking", "we", "are", "you"
}

GENERIC_WORDS = {
    "experience", "developer", "engineer", "role", "work", "team"
}

IMPORTANT_SHORT_WORDS = {"ml", "ai", "cv", "nlp"}

TECH_SKILLS = {
    "python", "sql", "docker", "aws", "kubernetes",
    "tensorflow", "pytorch", "scikit-learn",
    "pandas", "numpy", "nlp", "computer", "vision",
    "machine", "learning", "deep", "learning",
    "api", "apis", "flask", "fastapi",
    "mlflow", "airflow", "kubeflow",
    "git", "linux", "embedding", "embeddings",
    "llm", "openai", "transformers"
}


class SimilarityEngine:
    """
    Computes similarity between resume embeddings and job description embeddings.
    Enhanced with normalization, stability fixes, and explainability.
    """

    def __init__(self):
        pass

    #  safer cosine similarity
    @staticmethod
    def cosine_similarity(vector_a: np.ndarray, vector_b: np.ndarray) -> float:
        vector_a = np.array(vector_a)
        vector_b = np.array(vector_b)

        # Add epsilon for numerical stability
        epsilon = 1e-10

        norm_a = np.linalg.norm(vector_a) + epsilon
        norm_b = np.linalg.norm(vector_b) + epsilon

        similarity = np.dot(vector_a, vector_b) / (norm_a * norm_b)

        # CHANGE 2: Clip values to valid cosine range
        similarity = np.clip(similarity, -1.0, 1.0)

        return float(similarity)

    # safer batch similarity
    def batch_similarity(
        self,
        resume_embedding: np.ndarray,
        job_embeddings: List[np.ndarray]
    ) -> List[float]:

        resume_embedding = np.array(resume_embedding)
        job_embeddings = np.array(job_embeddings)

        epsilon = 1e-10

        # Safe normalization (avoid divide by zero)
        resume_norm = resume_embedding / (np.linalg.norm(resume_embedding) + epsilon)
        job_norms = job_embeddings / (
            np.linalg.norm(job_embeddings, axis=1, keepdims=True) + epsilon
        )

        similarities = np.dot(job_norms, resume_norm)

        # Normalize to 0–1 range (better for UI/ATS)
        similarities = (similarities + 1) / 2

        return similarities.tolist()

    # keyword overlap for explainability
    def keyword_overlap(
        self,
        resume_text: str,
        job_text: str
    ) -> Dict:

        
        IMPORTANT_SHORT_WORDS = {"ml", "ai", "cv", "nlp"}

        resume_words = {
            word for word in resume_text.lower().split()
            if word not in STOP_WORDS
            and word not in GENERIC_WORDS
            and (len(word) > 2 or word in IMPORTANT_SHORT_WORDS)
        }

        job_words = {
            word for word in job_text.lower().split()
            if word not in STOP_WORDS
            and word not in GENERIC_WORDS
            and (len(word) > 2 or word in IMPORTANT_SHORT_WORDS)
        }
        # Skill-based filtering
        resume_skills = resume_words.intersection(TECH_SKILLS)
        job_skills = job_words.intersection(TECH_SKILLS)
        
        common = resume_skills.intersection(job_skills)
        missing = job_skills - resume_skills

        return {
            "matched_keywords": sorted(list(common))[:20],
            "missing_keywords": list(missing)[:20],
            "overlap_score": round(len(common) / (len(job_skills) + 1e-10), 4)
        }

    # Richer ranking output
    def rank_jobs(
        self,
        similarities: List[float],
        job_texts: List[str]
    ) -> List[Dict]:

        results = []

        for idx, score in enumerate(similarities):
            results.append({
                "job_id": idx,
                "job_description": job_texts[idx],
                "similarity_score": round(score, 4),

                # Add confidence label (for UI)
                "confidence": self._confidence_label(score)
            })

        ranked_results = sorted(
            results,
            key=lambda x: x["similarity_score"],
            reverse=True
        )

        return ranked_results

    # confidence helper
    def _confidence_label(self, score: float) -> str:
        if score > 0.8:
            return "High Match"
        elif score > 0.6:
            return "Moderate Match"
        else:
            return "Low Match"

    # end-to-end with explainability
    def find_best_match(
        self,
        resume_embedding: np.ndarray,
        job_embeddings: List[np.ndarray],
        job_texts: List[str],
        resume_text: str = None
    ) -> Dict:

        similarities = self.batch_similarity(resume_embedding, job_embeddings)
        ranked_jobs = self.rank_jobs(similarities, job_texts)

        best = ranked_jobs[0]

        result = {
            "best_match": best,
            "all_matches": ranked_jobs
        }

        # Add explainability
        if resume_text:
            result["keyword_analysis"] = self.keyword_overlap(
                resume_text,
                best["job_description"]
            )

        return result
