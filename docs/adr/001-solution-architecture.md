## Solution architecture
Дата: 2021-11-15
## Статус
Принят
## Контекст
Отдел маркетинга пришёл к вам с новой задачей: «Нам нужно добавить больше активности сайту. 
Мы планируем добавить пользовательский рейтинг фильмов, поэтому нам нужны лайки и отзывы. 
К тому же пользовательская активность продвинет нас в выдаче поисковых движков. 
Сделайте пользователю историю просмотров. И пусть добавляют фильмы в закладки, чтобы у них была мотивация вернуться на сайт. 
Потом добавим список недосмотренных фильмов, информацию о работе с плеером вроде переключения языков и отдадим аналитикам. 
В общем, нам нужен инструмент для аналитики пользовательского поведения.

Основная задача сводиться к тому, чтобы собирать данные пользователей.

## Решение
Решили применить подход `Client -> Async API -> UGC`, т.к. `Async API` разрабатывался с целью быть производительным,
таким образом мы не потеряем в производительности, но не будем дублировать / писать заново логику проверки токенов.

## Рассмотренные варианты
Сервис должен справляться с высокими нагрузками и выдерживать запись большого количества событий, 
постоянно поступающих от каждого пользователя. Полученные данные должны быть удобны для команды аналитиков. 
Так как каждый запрос должен быть однозначно соотнесён c пользователем, который его сделал, сервису понадобится аутентификация.

- `Client -> UGC`
Если запросы от клиента будут приходить напрямую в сервис UGC, потребуется дублировать код проверки актуальности токена, написанный в AsyncAPI. 
  При изменении его формата придётся вносить изменения в оба сервиса.
- `Client -> Async API -> UGC`
Убрать UGC за AsyncAPI, чтобы к нему проходили только валидные запросы — тоже не лишён недостатков: быстродействие системы снизится из-за сетевых взаимодействий, 
  а большая нагрузка на UGC обернётся нагрузкой и на AsyncAPI.
  