import os
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv
import logging
from typing import Optional, Dict, Any

# Configura logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

class FreelancerDataSystem:
    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        self.client = self._initialize_client()

    def _initialize_client(self):
        try:
            from gotrue import SyncMemoryStorage
            from supabase.lib.client_options import ClientOptions

            options = ClientOptions(
                auto_refresh_token=False,
                storage=SyncMemoryStorage()
            )

            client = create_client(self.url, self.key, options)
            logger.info("Conexión a Supabase establecida")

            client.table("freelancers").select("*").limit(1).execute()
            return client

        except Exception as e:
            logger.error(f"Error inicializando Supabase: {str(e)}")
            raise RuntimeError("No se pudo conectar a Supabase")

    def get_filtered_freelancers(self, habilidad: str, disponibilidad: str) -> Optional[list]:
        try:
            result = self.client.table("freelancers").select("*").execute()
            rows = result.data

            filtrados = [
                row for row in rows
                if habilidad.lower() in [h.lower() for h in row.get("habilidades", [])]
                and row.get("disponibilidad", "").lower() == disponibilidad.lower()
            ]
            return filtrados

        except Exception as e:
            logger.error(f"Error obteniendo freelancers: {str(e)}")
            return []

class SafeFreelancerDataSystem:
    def __enter__(self):
        self.system = FreelancerDataSystem()
        return self.system

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self.system.client, 'auth'):
            self.system.client.auth.close()
