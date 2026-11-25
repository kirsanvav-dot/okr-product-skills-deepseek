---
name: prd-write-spec
description: Эпик→PRD/спецификация с API/данными/NFR
---
# Write Spec / PRD — адаптация для DeepSeek

Основа: Anthropic Product Management `write-spec`; дополнено требованиями к бэкенду, данным и anti-fraud latency. Не копирует upstream.

## Вход
Approved epic, пользовательский сценарий, UI Kit из репозитория, исходный код API, схемы Kafka/DB, data contracts, ошибки и incident RUN.

## Процедура
1. Problem & user benefit: почему необходима capability, как доказывает KR, что не входит.
2. Current-state vs target-state с точными компонентами, API и контрактами. Не выдумывай существующие endpoints.
3. Функциональные сценарии normal / unhappy / fallback; actor, triggers, permissions, audit.
4. Data mapping: source field → transform → validation → target → retention/privacy, backfill, idempotency, duplicates.
5. API delta: create/change/remove; request/response/events/status codes/versioning; migration/rollout/rollback; compatibility.
6. Sequence/flow diagrams **Mermaid source** (редактируемые), альтернативные варианты; качество диагностики и алертинга.
7. NFR performance, fault isolation, observability, DQ, IAM, security, SLA. Для нагруженных контуров указать impact on latency, not invented figures.
8. Метрики результата: `capability shipped` ≠ `KR improved`. Measurement and instrumentation plan отдельно.
9. Open questions: топ-5 блокирующих вопросов; неизвестные данные маркировать `TBD`; owner и trigger для решения.

## Выход: PRD.md
Структура: Metadata, Business context, KR & evidence, AS-IS, TO-BE flows, functional requirements, data & APIs, failure scenarios, NFR, telemetry, test strategy, migration/rollback, DoD, dependencies, open questions. Нельзя переходить к stories при unresolved blocker по критичному интерфейсу.

## Gate SPEC
Проверить соответствие архитектуре, отсутствие дублирования, тестируемость, полноту data/API/NFR и связь с родительским epic.
