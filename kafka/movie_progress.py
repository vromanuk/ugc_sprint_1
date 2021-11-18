import faust

from kafka.main import app


class MovieProgress(faust.Record):
    id: str
    user: str


movie_progress_topic = app.topic('movie_progress', value_type=MovieProgress)


@app.agent(movie_progress_topic)
async def track_movie_progress(views):
    async for view in views.group_by(MovieProgress.id):
        await ClickhouseService.track_movie_progress(view)
