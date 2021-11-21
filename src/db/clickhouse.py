import asyncio
import logging
import multiprocessing
from concurrent.futures.thread import ThreadPoolExecutor
from dataclasses import dataclass

import backoff as backoff
from clickhouse_driver import Client

from src.db.models import Event

logger = logging.getLogger()


@dataclass
class ClickhouseClient:
    client: Client = Client(host="localhost")

    @classmethod
    async def track_movie_progress(cls, finished_at: int, movie_id_user_id: str):
        event = Event(finished_at=finished_at, movie_id_user_id=movie_id_user_id)
        executor = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(executor, cls.track_event, event)

    @classmethod
    @backoff.on_exception(
        backoff.expo,
        Exception,
        max_tries=3,
        jitter=backoff.random_jitter,
    )
    def track_event(cls, event: Event):
        try:
            cls.client.execute(
                f"INSERT INTO {event._tablename} (finished_at, movie_id_user_id, event_datetime) VALUES",
                [event.dict()],
            )
            logger.info("ack")
        except Exception as e:
            logger.error(e)
