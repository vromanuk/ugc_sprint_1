from dataclasses import dataclass

from clickhouse_driver import Client

from src.core.config import get_settings

settings = get_settings()


@dataclass
class ClickhouseClient:
    client: Client = Client(host="localhost")

    @classmethod
    def track_movie_progress(cls, finished_at: int, movie_id_user_id: str):
        cls.client.execute(
            f"INSERT INTO {settings.clickhouse_config.CLICKHOUSE_DB} (finished_at, movie_id_user_id) VALUES ('{finished_at}', '{movie_id_user_id}')"
        )
