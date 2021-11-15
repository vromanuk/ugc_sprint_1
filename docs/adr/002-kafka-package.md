## Solution architecture
Дата: 2021-11-15
## Статус
Принят
## Контекст
В Python экосистеме существует много клиентов для Kafka. Нужно выбрать наиболее оптимальный.

## Решение
Используем пакет `aiokafka`.

## Рассмотренные варианты

- `kafka-python`
  синхронный
- `confluent-kafka-python`
  синхронный
- `pykafka`
  мертвый проект, последний коммит был в 2019 году
- `aiokafka`
  представитель aio-libs, построен поверх `kafka-python`
- `faust`
  мини-фреймворк, слишком много лишней функциональности, идея Kafka Streams в Python.