---
name: backlog-quality-gates
description: Двусторонний аудит KR↔epic↔story и готовности к разработке
---
# Backlog Quality Gates — адаптация для DeepSeek

Основа: Anthropic `sprint-planning`, PM Skills `capacity-planning`, `dependency-mapping`, Agile Story Skills `sprint-goal-writer`. Не копирует upstream.

## Вход
TOP→СРО→Product trace, инициативы, epics, stories, approved PRD, estimates, owner/RACI, run load, architecture source, other teams backlog.

## Проверяй в две стороны
TOP→СРО→Product KR→initiative→epic→story: у всех обязательных KR есть достаточные для эффекта deliverables, dependencies и measurement.
Story→epic→initiative→KR→СРО: любая story обоснована либо marked `ENABLER` + documented contribution.

## Gates
G1 Outcome coverage: сумма shipped epics достаточна для изменения метрики? Просто количество задач не доказательство.
G2 Ownership collision: единый accountable owner результата; shared APIs handled via integration contracts; нет двойного зачёта.
G3 Architecture reuse: проверить существующие сервисы, UI Kit, API, events до NEW service.
G4 Delivery DoR: AC покрыты, данные/API/NFR согласованы, тесты, observability, migration, rollback, audit.
G5 Role capacity: P50/P80 оценка, RUN/focus, bottleneck, uncertainty and cut order. Без подтверждённой оценки `CONDITIONAL`.
G6 KR metrics: numerator/denominator, baseline, source, cadence, evidence, direct-vs-contribution distinction.
G7 Slice coverage: для каждого epics AC есть story, у каждого story нет orphan/duplicated scope.

## Выход
`quality_report.md` (PASS/CONDITIONAL/FAIL с before→after, owner, источник, риск), `coverage_matrix.csv`, `dependency_register.csv`, `backlog_readiness.md` (commit/candidate/defer) и список решений к встрече с PO/тимлидом.
Пустая метрика, непроверенное обещание за внешнего смежника, capacity>100% без cut — FAIL.
