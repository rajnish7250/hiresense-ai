#embeddings.py
import warnings
warnings.filterwarnings("ignore")

from typing import List, Union
from openai import OpenAI
import numpy as np
import os

#logging
import logging

#Local semantic model
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)


class EmbeddingGenerator:
    """
    Embedding generator with:
    - OpenAI primary embeddings
    - Semantic local fallback (SentenceTransformers)
    - Normalization for cosine similarity
    """

    #Singleton-like reuse (avoid reloading model repeatedly)
    _fallback_model_instance = None

    def __init__(self, model: str = "text-embedding-3-small"):
        api_key = os.getenv("OPENAI_API_KEY")

        #self.use_api = True if api_key else False
        
        # FORCE LOCAL MODE (no OpenAI calls)
        self.use_api = False#Do NOT call OpenAI at all. Always use local embeddings.

        if self.use_api:
            self.client = OpenAI(api_key=api_key)
            self.model = model
            self.embedding_dim = 1536
        else:
            logger.warning("No API key found. Using local embeddings.")

        #Load fallback model only once
        if EmbeddingGenerator._fallback_model_instance is None:
            EmbeddingGenerator._fallback_model_instance = SentenceTransformer(
                "all-MiniLM-L6-v2"
            )

        self.fallback_model = EmbeddingGenerator._fallback_model_instance
        self.fallback_dim = 384


    # Utility: Normalize vector
    def _normalize(self, vec: np.ndarray) -> np.ndarray:
        norm = np.linalg.norm(vec)
        return vec if norm == 0 else vec / norm

    # Single Embedding
    def get_embedding(self, text: str) -> np.ndarray:

        if not text or not text.strip():
            raise ValueError("Input text is empty.")

        if self.use_api:
            try:
                response = self.client.embeddings.create(
                    model=self.model,
                    input=text
                )
                embedding = np.array(response.data[0].embedding, dtype=np.float32)

                #Normalize
                return self._normalize(embedding)

            except Exception as e:
                logger.warning(f"API failed (single), switching to fallback: {e}")

        # Semantic fallback
        return self._fallback_embedding(text)

    # Batch Embeddings
    def get_embeddings_batch(self, texts: List[str]) -> np.ndarray:

        if not texts or not all(t.strip() for t in texts):
            raise ValueError("One or more input texts are empty.")

        if self.use_api:
            try:
                response = self.client.embeddings.create(
                    model=self.model,
                    input=texts
                )
                embeddings = [
                    self._normalize(np.array(item.embedding, dtype=np.float32))
                    for item in response.data
                ]
                return np.array(embeddings)

            except Exception as e:
                logger.warning(f"API failed (batch), switching to fallback: {e}")

        # Semantic fallback
        return self._fallback_batch_embeddings(texts)

    # Semantic Fallback
    def _fallback_embedding(self, text: str) -> np.ndarray:
        vec = self.fallback_model.encode(text)
        return self._normalize(np.array(vec, dtype=np.float32))

    def _fallback_batch_embeddings(self, texts: List[str]) -> np.ndarray:
        vecs = self.fallback_model.encode(texts)
        return np.array([self._normalize(np.array(v, dtype=np.float32)) for v in vecs])


# Wrapper function (optimized)
# UPDATED: reuse generator instead of recreating each call
_generator_instance = EmbeddingGenerator()
from functools import lru_cache

# Cached Single Embedding
@lru_cache(maxsize=1000)
def cached_embedding(text: str):
    return _generator_instance.get_embedding(text)


# Wrapper Function
def generate_embeddings(texts: Union[str, List[str]]):
    if isinstance(texts, list):
        return _generator_instance.get_embeddings_batch(texts)
    return cached_embedding(texts)
