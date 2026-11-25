---
name: product-roadmap
description: OKR→value milestones→инициативы и roadmap
---
# Product Roadmap — адаптация для DeepSeek

Основа подхода: Anthropic Product Management `roadmap-update`, `product-brainstorming` и PM Skills `dependency-mapping`. Это **оригинальная адаптация**, не копия текста сторонних skills.

## Вход
Утверждённые TOP/СРО/Product OKR + KR passports, предыдущий roadmap, facts AS-IS, зависимости, реестр инициатив, оценки роли/спринт, правила RUN, ограничения. **Перед созданием нового backlog прочитать имеющиеся эпики**.

## Процедура
1. На каждый KR определи baseline, целевое изменение и минимальные observable signals. Не создавай инициативы, которые не меняют эти сигналы.
2. Сгенерируй альтернативы: reuse существующего решения, процессная мера, интеграция, новая разработка; сравни по impact, effort, зависимости, reversibility.
3. Сгруппируй гипотезы в **инициативы** (не сервисы, не stories), каждому KR достаточно минимального причинно-обоснованного набора.
4. Определи Q1–Q4 value milestones, на каких этапах появляется работающая ценность; различай выпуск capability и доказанный outcome.
5. Обозначь в каждой инициативе accountable owner, партнёра, decision owner, внешние gates, scope cuts, критерии отмены.
6. Для малого состава покажи последовательность с WIP limit; учитывай RUN, Q4 carry-over, неопределённости. Не обещай одновременно больше, чем вмещается в роль bottleneck.

## Выход: roadmap.md + initiative_register.csv
| Initiative ID | Parent KR ID | Problem / expected user change | Outcome metric | Value milestone | Q | Owner | Dependencies | Estimated role-days | Evidence | Confidence | Cut order |
Нельзя оставлять строку без родительского KR, метрики успеха или explicit label `ENABLER` с обоснованной связью.

## Gate ROADMAP
FAIL если результат KR зависит только от внешнего согласования; инициатива дублирует существующее; отсутствуют ownership/финансовые или ресурсные ограничения; нет основания причинной связи. Неизвестные значения — X/TBD с планом оценки.
