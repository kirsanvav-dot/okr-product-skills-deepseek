# End-to-end: OKR → Jira-ready backlog

> Это маршрут выполнения в DeepSeek через portable Markdown skills. Требует человеческих решений, не автоматический Jira-бот.

| Step | Skill | Обязательный input | Output | Human gate |
|---|---|---|---|---|
| 00–02 | source-intake → questions → okr-design | Стратегия + исходные данные | OKR & metric passports | СРО/PO |
| 03–04 | traceability → collision-check | Все OKR коллег | Trace + collision matrix | СРО/владельцы команд |
| 05 | capacity-and-initiatives | velocity, RUN, backlog | Initiative register | PO/tech lead |
| 07 | product-roadmap | Approved KR / initiatives | Value milestones & roadmap | PO |
| 08 | epic-breakdown | Roadmap + AS-IS architecture | Epics | PO + tech lead |
| 09 | prd-write-spec | Approved Epic + code/API schemas | PRD with diagrams | Architect, DS, QA |
| 10–11 | story-writer → splitter | PRD + DoR + velocity | Stories + AC + split coverage | Team refinement |
| 12 | backlog-quality-gates | Full output + owner/RACI | Coverage, risk, capacity, readiness | PO + tech lead |
| 06 | audit-and-defense | All approved outputs | CPO-level final verdict | CPO/SRO |

## Replan loop
Любое изменение KR, периметра, роли или даты → **пересчёт 03,04,05,07,08,12**. PRD/stories обновлять только для затронутых epic IDs; сохранить связь с исходными артефактами и показать diff.

## Правила для маленькой команды
- Последовательная доставка, не параллельная фабрика микросервисов; максимум активных крупных инициатив — `X` до подтверждения velocity.
- Приоритет: business-effect evidence → обязательный MVP → optional → stretch; держать explicit scope cut.
- Не считать RUН и интеграционные согласования бесплатными; внешние госрегуляторы не заменяют внутренний RACI.
- Формулировки CPO на языке результатов, технические детали в epics/stories.

## Пилот (предлагается)
Один KR: **X% изменений критичных источников проверяются по DataContracts до production**.
Проверить: existing Registry/Stream Validator; наличие API согласования изменений; ответственность команды публикации контрактов; список stories, включая negative cases и telemetry; измерение изменений в обход процесса.

## Экспорт
Сгенерировать `epics.json`, `stories.json` по шаблонам, проверить локально `python scripts/validate_backlog.py --epics epics.json --stories stories.json`. Никакой записи в Jira без review и явного разрешения.
