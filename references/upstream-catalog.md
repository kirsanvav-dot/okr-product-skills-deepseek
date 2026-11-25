# Каталог источников и адаптаций

Мы **не включаем код или текст третьесторонних SKILL.md**. Следующие skill-названия и подходы послужили отправной точкой; правила для DeepSeek написаны заново и расширены  Quality Gates. Репозитории следует изучить перед отдельной установкой, проверить лицензии и актуальные версии.

| Источник | Конкретные upstream skills | В нашем пакете | Доверие / оговорки |
|---|---|---|---|
| [Anthropic Product Management](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management) | `roadmap-update`, `write-spec`, `sprint-planning`, `product-brainstorming` | 07,09,12 | Официальный Anthropic, но не нативный DeepSeek |
| [Vsank PM-Skills Epic Breakdown](https://github.com/Vsank/PM-Skills/blob/main/skills/epic-breakdown/SKILL.md) | `epic-breakdown` | 08 | Community: нужна ручная валидация |
| [Agile Story Skills](https://github.com/alwyndsouza/agile-story-skills) | `agile-story-writer`, `agile-story-splitter`, `problem-framing`, `sprint-goal-writer` | 10,11,12 | Community: адаптация не равна сертифицированному результату |
| [Program Management PM Skills](https://github.com/janellecipriano/pm-skills) | `capacity-planning`, `dependency-mapping`, `okr-tracking` | 05,07,12 | Community: сверять с фактической velocity |
| [Product on Purpose](https://github.com/product-on-purpose/pm-skills) | Альтернатива полному PM workflow | Optional only | Не дублировать в базовом пакете |

## Реальные различия

- Официальная команда Anthropic поддерживает **Claude tools and commands**; DeepSeek получает только portable prompts.
- Community skills не становятся «проверенными» от того, что доступны на GitHub. Нужны тестовые кейсы и ручная проверка качества.
- Наши scripts — самостоятельный адаптер, не upstream CLI. Не использовать Claude plugin install для установки этих переносимых DeepSeek инструкций.
