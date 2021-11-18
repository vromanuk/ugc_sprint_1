from dataclasses import dataclass

import faust
from clickhouse_driver import Client
from pydantic import BaseSettings

app = faust.App(
    "movie_progress",
    broker="//localhost:9092",
    topic_partitions=4,
)


class ClickhouseConfig(BaseSettings):
    CLICKHOUSE_DB: str = "example.test"


@dataclass
class ClickhouseClient:
    client: Client = Client(host="localhost")
    config: ClickhouseConfig = ClickhouseConfig()

    @classmethod
    def track_movie_progress(cls, finished_at: int, movie_id_user_id: str):
        cls.client.execute(
            f"INSERT INTO {cls.config.CLICKHOUSE_DB} (finished_at, movie_id_user_id) VALUES ('{finished_at}', '{movie_id_user_id}')"
        )


class MovieProgress(faust.Record):
    finished_at: int
    movie_id_user_id: str


movie_progress_topic = app.topic("movie_progress", value_type=MovieProgress)


@app.agent(movie_progress_topic)
async def track_movie_progress(movie_progress):
    async for progress in movie_progress.group_by(MovieProgress.movie_id_user_id):
        ClickhouseClient.track_movie_progress(
            progress.finished_at, progress.movie_id_user_id
        )
