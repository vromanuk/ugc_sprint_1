from src.db.clickhouse import ClickhouseClient
from src.main import get_app
from src.records import MovieProgress

app = get_app()

movie_progress_topic = app.topic("movie_progress", value_type=MovieProgress)


@app.agent(movie_progress_topic)
async def track_movie_progress(movie_progress):
    async for progress in movie_progress.group_by(MovieProgress.movie_id_user_id):
        ClickhouseClient.track_movie_progress(
            progress.finished_at, progress.movie_id_user_id
        )
        print("ACK")
