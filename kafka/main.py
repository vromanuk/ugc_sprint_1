import faust as faust

app = faust.App(
    'movie_progress',
    broker='kafka://localhost:9092',
    topic_partitions=4,
)
