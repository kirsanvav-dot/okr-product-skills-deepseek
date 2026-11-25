---
name: story-splitter
description: Крупные stories→минимальные ценные вертикальные срезы
---
# Story Splitter — адаптация для DeepSeek

Основа: `agile-story-splitter` из Agile Story Skills. Не копирует сторонний исходный текст.

## Когда
Story не входит в один спринт, AC >8, много независимых workflows, смешано несколько акторов/контрактов/отчётов, либо недопустимая неопределённость.

## Шаги
1. Определи главный value slice, который можно выкатить безопасно и проверить отдельно.
2. Предложи 2–5 вариантов разреза: по бизнес-сценариям, типам данных, правилам, source/sink, happy→edge, permissions, risk exposure, batch→stream. Сравни, не ломают ли срезы жизнеспособность.
3. Выбери минимальный **vertical** split. Нельзя делить по слоям `backend`, `frontend`, `QA` как независимый value, если это всего лишь этапы одной capability.
4. Отобрази coverage оригинальных AC: у каждого требования есть новая story или explicit deferred reason.
5. Повтори оценки с tech lead; если нет оценки, `TBD`, а не придуманное число.
6. Сохрани идентичность parent epic/KR и исходной story `split_from`.

## Выход: story_split_map.md + stories.json
Таблица: source story, reason, target story IDs, AC coverage %, dependencies, unaddressed requirements, scope cut, signoff.

## Gate SPLIT
FAIL если потеряны AC; новые куски непроверяемы по отдельности; исчезла трассировка; split требует бессмысленных отдельных релизов.
