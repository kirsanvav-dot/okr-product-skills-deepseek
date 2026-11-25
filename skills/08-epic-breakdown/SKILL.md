---
name: epic-breakdown
description: Инициативы→поставляемые эпики по вертикальным срезам
---
# Epic Breakdown — адаптация для DeepSeek

Основа: `epic-breakdown` Vsank PM-Skills, Anthropic roadmap & write-spec. Не воспроизводит их текст.

## Вход
Approved initiative register, KR trace, реестр существующих эпиков, архитектура AS-IS, code map, интеграции, NFR, role capacity, ограничения.

## Алгоритм
1. Проанализируй текущие эпики и сервисы: EXISTING / EXTEND / NEW. Не генерируй повторно существующее.
2. На инициативу предложи 1–5 **vertical outcome epics**: каждый поставляет тестируемую способность пользователя или системы end-to-end, а не только компонент backend/UI/DB.
3. Для каждого эпика выпиши trigger, actor, вход/выход, in/out scope, бизнес-проверку, measurable acceptance, NFR (security, perf, audit, monitoring), integration owners.
4. Построй dependencies DAG. Ранее существующие договорённости и внешние решения не считай готовыми без evidence.
5. Проверь укладывание в квартальный milestone и capacity по ролям. Зафиксируй `MVP`, `OPTIONAL`, `DEFER`, `SPIKE`.
6. Для сложной архитектуры укажи варианты embed existing vs new service; отдели техническую гипотезу от утверждённой архитектуры.
7. Не создавать story до human gate техлида и PO по границам эпика.

## Выход: epics.md / epics.json
Обязательные поля: `epic_id`, `initiative_id`, `kr_ids`, `problem`, `deliverable`, `business_acceptance`, `scope`, `excluded`, `owner`, `dependencies`, `reuse_decision`, `role_estimate_range`, `quarter`, `confidence`, `risk`, `evidence`.

## Gate EPIC
FAIL если эпик равен названию микросервиса без результата; зависит от несуществующей интеграции без mitigation; нет KR/инициативы; не включены тесты и эксплуатация; estimation=0 для unknown.
