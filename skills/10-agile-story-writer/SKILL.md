---
name: agile-story-writer
description: PRD/Epic→stories с независимыми AC и техническими границами
---
# Agile Story Writer — адаптация для DeepSeek

Основа: `agile-story-writer`, `problem-framing` из Agile Story Skills; Anthropic `write-spec`. Не копирует их текст.

## Вход
Approved epic+PRD, UX kit and architecture, API & data deltas, release constraints, team Definition of Ready, historical velocity. Existing Jira stories to deduplicate.

## Правила
1. Разбивай **вертикально**: каждая story даёт проверяемый end-to-end срез; не генерируй backend/frontend/QA stories как отдельные фазы, если не обосновано.
2. Story формат: «Для [роль/система] нужно [поведение], чтобы [результат]»; для внутренних платформных работ допускается capability statement вместо искусственного пользователя.
3. Acceptance criteria 3–8 Given/When/Then, с нормальным сценарием, валидацией, негативным вариантом, аудитом/наблюдаемостью, границами ошибок.
4. Для каждого изменения явно: данные и схема, API/event contract, backwards compatibility, доступы, тесты и мониторинг.
5. Привязки: parent epic, initiative, KR, dependency, expected measurable outcome; stories без бизнес-родителя допустимы только как маркированный ENABLER.
6. Убедись, что story оценима и ≤ 1 спринт целевой команды; если больше — вызови 11-story-splitter, НЕ придумывай velocity.
7. Исходный Jira тикет при наличии не перезаписывать, только diff/new proposed acceptance.

## Выход: stories.json + jira_draft.md
Поля: `story_id`, `epic_id`, `initiative_id`, `kr_ids`, `title`, `value`, `description`, `acceptance_criteria[]`, `technical_notes`, `api_data_impact`, `negative_cases`, `nfr`, `test_evidence`, `dependencies[]`, `owner_role`, `estimate_range`, `readiness_status`, `source_refs[]`.

## Gate STORY
FAIL если story оторвана от эпика, AC невозможно проверить, нет негативных сценариев для рискованной функции, нужна незадокументированная интеграция или story превышает спринт.
