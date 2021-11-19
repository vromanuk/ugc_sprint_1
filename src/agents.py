from src.db.clickhouse import ClickhouseClient
from src.main import get_faust_app
from src.records import MovieProgress

faust_app = get_faust_app()

movie_progress_topic = faust_app.topic("movie_progress", value_type=MovieProgress)


@faust_app.agent(movie_progress_topic)
async def track_movie_progress(movie_progress):
    async for progress in movie_progress.group_by(MovieProgress.movie_id_user_id):
        ClickhouseClient.track_movie_progress(
            progress.finished_at, progress.movie_id_user_id
        )
        print("ACK")
