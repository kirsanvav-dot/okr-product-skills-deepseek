# OKR → Product Delivery Skills (DeepSeek-compatible)

**13 переносимых skills для продуктовых команд:** от целей руководителя до инициатив, эпиков, PRD, User Stories и проверки бэклога. Работают как Markdown-инструкции для LLM; **не являются нативным плагином DeepSeek**.

> Репозиторий содержит **промпты, сценарии и локальные валидаторы**. Он не подключается к Jira, не публикует результаты и не гарантирует корректность OKR без проверки человеком.

## Зачем

Типичная проблема: OKR красиво каскадируются по названиям, но не по причинно-следственной связи. Несколько команд заявляют один результат, метрики подменяются инициативами, а эпики не соотносятся с доступной ёмкостью. Эти навыки предлагают управляемый процесс с остановками на согласование и понятными артефактами.

## Все skills

| Этап | Skill | Результат |
|---|---|---|
| 00 | [`source-intake`](skills/00-source-intake/SKILL.md) | Реестр источников, факты/планы/гипотезы |
| 01 | [`discovery-questions`](skills/01-discovery-questions/SKILL.md) | Уточняющие вопросы, решения и неизвестные |
| 02 | [`okr-design`](skills/02-okr-design/SKILL.md) | Годовые OKR руководителя и команды, паспорта метрик |
| 03 | [`cascade-traceability`](skills/03-cascade-traceability/SKILL.md) | Трассировка TOP → руководитель → команда |
| 04 | [`collision-check`](skills/04-collision-check/SKILL.md) | Пересечения KR, ownership, двойной зачёт |
| 05 | [`capacity-and-initiatives`](skills/05-capacity-and-initiatives/SKILL.md) | Инициативы, приоритеты, зависимости, capacity |
| 06 | [`audit-and-defense`](skills/06-audit-and-defense/SKILL.md) | Аудит PASS / CONDITIONAL / FAIL |
| 07 | [`product-roadmap`](skills/07-product-roadmap/SKILL.md) | Квартальный roadmap и инициативы |
| 08 | [`epic-breakdown`](skills/08-epic-breakdown/SKILL.md) | Эпики с outcome и связями с KR |
| 09 | [`prd-write-spec`](skills/09-prd-write-spec/SKILL.md) | PRD, API/data changes, error cases, диаграммы |
| 10 | [`agile-story-writer`](skills/10-agile-story-writer/SKILL.md) | User Stories и acceptance criteria |
| 11 | [`story-splitter`](skills/11-story-splitter/SKILL.md) | Небольшие stories с сохранением ценности |
| 12 | [`backlog-quality-gates`](skills/12-backlog-quality-gates/SKILL.md) | DoR, трассировка до stories, проверка конфликтов |

## Быстрый запуск

### Вариант A — DeepSeek Chat / любой LLM-чат

1. Возьмите файл `skills/01-discovery-questions/SKILL.md` и вставьте в инструкцию беседы (или приложите как контекст, если клиент поддерживает).
2. Приложите **обезличенный** стратегический контекст, TOP OKR, список команд и факт прошлого периода.
3. Попросите: «Выполни этап 01; задай только блокирующие вопросы, не придумывай данные, закончи списком решений для подтверждения».
4. После ответов запустите `02-okr-design`, затем `03-cascade-traceability` и `04-collision-check`.
5. Подтвердите результат человеком, прежде чем запускать `07-product-roadmap` и следующие этапы.

Полный сценарий: [`workflows/manual-run.md`](workflows/manual-run.md) и [`workflows/end-to-end-product-delivery.md`](workflows/end-to-end-product-delivery.md).

### Вариант B — DeepSeek API

```bash
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export DEEPSEEK_API_KEY='...'          # Windows PowerShell: $env:DEEPSEEK_API_KEY='...'
python scripts/run_api.py \
  --source examples/fictional-service-case.md \
  --stage 01-discovery-questions \
  --out /tmp/okr_questions.md \
  --confirm-external-upload
```

**Важно:** `--confirm-external-upload` означает, что вы проверили разрешённость передачи данных во внешний API. Для корпоративных документов используйте разрешённый контур. Скрипт выполняет только выбранный этап, не обходит согласование и не интегрируется с Jira.

### Вариант C — агентный IDE-клиент

Положите `skills/*/SKILL.md` в предусмотренную вашим клиентом структуру. Если клиент умеет обнаруживать skills, используйте его механизм; формат каталогов и автоматическое выполнение зависят **от клиента**, а не от DeepSeek как модели.

## Что проверяет агент

- **Причинность, а не сходство названий.** «Мониторинг» не становится вкладом в надёжность без понятного механизма.
- **Два вида пересечения.** Общая интеграция ≠ конфликт KR; общий owner одного результата требует разделения.
- **KR ≠ инициатива.** KR описывает измеримый outcome; инициатива — действия для его достижения.
- **Нет выдуманных чисел.** Неизвестный baseline — `н/и`, target — `X` с планом измерения.
- **Внешние обязательства — не свои KR.** Не обещать процент согласованных партнёров без полномочий.
- **Связь события не равна причинности.** Сопутствующее событие и подтверждённая причина считаются раздельно.
- **Проверка capacity.** Нельзя превращать каждый KR в неограниченный набор эпиков.

## Структура репозитория

```text
skills/          # 13 portable SKILL.md
workflows/       # последовательность и ручные approval gates
scripts/         # вызов DeepSeek API и структурные валидаторы
examples/        # исключительно синтетические данные
references/      # источники методик, атрибуция
templates/      # traceability, epics, stories
 docs/           # подробное руководство и публикация
```

## Проверка

```bash
python scripts/validate_trace.py examples/sample_trace.json
python -m compileall -q scripts
```

Локальная структурная проверка не доказывает причинность KR и не заменяет экспертный аудит.

## Источники и лицензирование

Инструкции написаны как самостоятельные адаптации практик Product Management. Оригинальные сторонние SKILL.md в репозиторий не включены. Ссылки: [`references/upstream-catalog.md`](references/upstream-catalog.md). Для собственного кода и текста автор репозитория должен выбрать лицензию перед публикацией. Не добавляйте лицензию третьих сторон, если не владеете правами на их материалы.

## Безопасность

Не публикуйте рабочие OKR, внутренние схемы, клиентские события, идентификаторы и примеры антифрода. Синтетический пример включён; исходные корпоративные демонстрации намеренно исключены.

## Contributing

Ошибки, сценарии и улучшения приветствуются. Правила в [`CONTRIBUTING.md`](CONTRIBUTING.md). Для обсуждения дефектов прикладывайте только обезличенные или синтетические кейсы.

---

Подробнее: [`docs/DETAILED_GUIDE.md`](docs/DETAILED_GUIDE.md). Публичная версия README подготовлена для репозитория, но не свидетельствует о прохождении end-to-end испытания на DeepSeek API.
