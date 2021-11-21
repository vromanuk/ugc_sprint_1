#!/bin/bash
set -e

clickhouse client -n <<-EOSQL
    CREATE DATABASE IF NOT EXISTS movies_db ON CLUSTER project_cluster;
    CREATE TABLE IF NOT EXISTS movies_db.views (
      user_id String,
      movie_id String,
      finished_watching_at String,
      event_datetime DateTime
    ) Engine=MergeTree() ORDER BY event_datetime;
EOSQL