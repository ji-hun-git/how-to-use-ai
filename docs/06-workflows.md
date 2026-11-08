# 06. 워크플로: 프롬프트 한 줄에서 일하는 방식으로

> 좋은 프롬프트 하나로 끝나는 일은 많지 않습니다. 실제 업무는 **여러 단계**이고, 단계마다 사람이 확인해야 합니다.
> 이 문서는 (1) 무엇을 AI에게 보여 줄지 정하는 **컨텍스트 엔지니어링**, (2) 일을 쪼개는 **5가지 패턴**, (3) 모든 작업에 통하는 **기본 루프**, (4) 업무별 **플레이북**을 다룹니다.

---

## 1. 컨텍스트 엔지니어링 (Context Engineering)

### 프롬프트 엔지니어링에서 컨텍스트 엔지니어링으로

2025년 6월, Shopify CEO Tobi Lütke와 Andrej Karpathy가 연달아 이 용어를 밀면서 널리 퍼졌습니다. Karpathy는 이를 **다음 단계에 필요한 정보를 맥락 창에 딱 알맞게 채우는 섬세한 기술**이라고 설명했습니다.

- **프롬프트 엔지니어링:** 지시문을 어떻게 **쓸지**
- **컨텍스트 엔지니어링:** 매번 AI가 **무엇을 보게 할지** (지시문, 자료, 대화 기록, 메모 파일, 도구 결과 전부)

Anthropic은 2025년 9월 글에서 맥락 창을 **한정된 주의력 예산**에 비유했습니다. 맥락이 쌓일수록 앞의 정보를 정확히 떠올리지 못하는 **맥락 부패(context rot)**가 생깁니다. 그래서 목표는 **원하는 결과를 낼 가능성을 가장 높이는, 가장 작은 양의 핵심 정보**입니다.

### 일상에서의 6가지 원칙

| 원칙 | 일반 채팅에서 | 코딩 에이전트에서 |
|---|---|---|
| **주제가 바뀌면 새로 시작** | 새 채팅 | `/clear` 또는 새 세션 |
| **필요한 자료만, 필요할 때** | 관련 문서만 첨부. 전부 넣지 않기 | 파일을 통째로 넣지 말고 에이전트가 필요할 때 읽게 하기 |
| **오래 쓰는 정보는 파일로** | 프로젝트(Projects) 기능의 지침, 커스텀 GPT 설정 | `AGENTS.md` / `CLAUDE.md` (짧게!) |
| **긴 작업은 메모로 넘긴다** | "지금까지 결정한 것 요약해줘" → 새 채팅에 붙여 넣기 | 진행 상황 파일(progress.md)에 기록, 압축(compaction) |
| **절차는 재사용 단위로** | 저장한 프롬프트 템플릿 | 스킬(Skills) |
| **꼭 지켜야 할 규칙은 글이 아니라 설정으로** | 회사가 허용한 도구만 쓰기 | 훅(hook), 권한 거부 규칙, CI |

> 2026년에는 맥락 창이 100만 토큰까지 커지고 자동 압축도 생겨서 맥락이 **부족한** 일은 드뭅니다. 그래도 맥락을 **좁게 유지하는 쪽이 답도 좋고 비용도 적다**는 것이 공통된 권고입니다.

---

## 2. 일을 쪼개는 5가지 패턴

Anthropic의 "Building effective agents"(2024-12)는 AI 작업을 구성하는 기본 패턴 5가지를 제시합니다. 원래 개발자를 위한 글이지만, **채팅창에서 그대로** 쓸 수 있습니다. 가장 중요한 원칙은 **가장 단순한 방법에서 시작하고, 효과가 확인될 때만 복잡하게 만드는 것**입니다.

| 패턴 | 무엇 | 채팅에서 따라 하기 | 사람이 확인하는 지점 |
|---|---|---|---|
| **프롬프트 체이닝** (Prompt chaining) | 일을 순서대로 나눠 단계마다 처리 | ① 개요 → 확인 → ② 초안 → ③ 기준표로 비평 → ④ 수정 | 단계마다 결과를 보고 넘어감 |
| **라우팅** (Routing) | 종류에 따라 다른 도구·모델로 보냄 | 간단한 질문은 빠른 모델, 어려운 분석은 추론 모델, 조사는 딥리서치 | 내가 모드를 고름 |
| **병렬화** (Parallelization) | ⓐ 독립적인 부분을 동시에 ⓑ 같은 일을 여러 번 | ⓐ 보고서 장(章)별로 다른 채팅 ⓑ 같은 질문을 2~3번 / 여러 모델에 | 합치기, 다른 부분 확인 |
| **오케스트레이터-워커** | 총괄이 나누고, 일꾼들이 하고, 총괄이 합침 | 딥리서치 기능, 코딩 에이전트의 하위 에이전트 | 최종 결과 검증 |
| **평가자-최적화자** (Evaluator-optimizer) | 하나가 만들고 다른 하나가 평가하며 반복 | 작성은 채팅 A, 평가는 새 채팅 B에서 기준표로 | 기준표를 내가 만듦 |

> Anthropic의 2026년 문서는 최신 모델이 여러 단계 추론을 **내부에서** 대부분 처리한다고 설명합니다. 그래도 **중간 결과를 직접 보고 싶을 때**는 체이닝이 여전히 유용합니다. 가장 흔한 체인은 **초안 → 기준에 따라 검토 → 수정**입니다.

> 여러 에이전트를 쓰는 방식은 비쌉니다. Anthropic의 리서치 시스템 사례에서 다중 에이전트는 일반 채팅의 약 **15배** 토큰을 썼습니다. 독립적으로 나눌 수 있는 큰 조사에는 효과가 크지만, 서로 맥락을 공유해야 하는 일(대부분의 코딩)에는 잘 맞지 않습니다.

---

## 3. 모든 작업에 통하는 기본 루프

2026년의 공식 가이드들(Anthropic, OpenAI)과 실무자들(Karpathy, Simon Willison)의 조언은 결국 같은 루프로 모입니다.

```
① 명세 (Specify)   목표 · 맥락 · 제약 · 완료 기준을 쓴다. 막막하면 AI에게 인터뷰를 받는다
      ↓
② 계획 (Plan)      여러 단계짜리 일은 실행 전에 계획을 받고 승인한다
      ↓
③ 실행 (Execute)   AI가 스스로 확인할 수 있는 기준(테스트, 체크리스트, 원문)을 함께 준다
      ↓
④ 검증 (Verify)    결과를 증거로 확인한다. 가능하면 새 채팅이나 다른 사람·모델이 본다
      ↓
⑤ 반영 (Learn)     반복되는 실수는 템플릿, 메모 파일, 체크리스트에 한 줄 추가한다
```

| 단계 | 건너뛰면 생기는 일 |
|---|---|
| ① 명세 | **오해**. AI가 빈칸을 추측으로 채움 |
| ② 계획 | 큰 방향이 틀린 것을 다 만든 뒤에 발견 |
| ③ 확인 기준 | AI가 "다 했습니다"라고 하지만 실제로는 **누락** |
| ④ 검증 | **지어냄**이 그대로 밖으로 나감 |
| ⑤ 반영 | 같은 실수가 매번 반복 |

---

## 4. 업무별 플레이북

### 4-1. 글쓰기 (보고서, 기획서, 블로그)

```
1. [나]   핵심 주장 3줄을 먼저 직접 쓴다 (생각을 맡기지 않기)
2. [AI]   독자·목적을 주고 개요를 받는다 → 내가 고친다
3. [AI]   개요대로 섹션별 초안 (긴 글은 섹션 하나씩)
4. [AI*]  새 채팅에서 평가 기준표로 비평 (*작성한 채팅과 분리)
5. [AI]   비평을 반영해 수정
6. [나]   사실·숫자·인용 확인, 내 말투로 다듬기
```

### 4-2. 조사·리서치

```
1. 질문과 출처 기준을 정한다 (1차 자료 우선, 기간, 지역)
2. 검색 또는 딥리서치로 자료를 모은다
3. 주장마다 출처를 달게 하고, 확인 못 한 것은 [미확인] 표시
4. 핵심 주장은 원문을 직접 열어 확인 (옆으로 읽기)
5. "반대 증거만 찾아줘"로 한쪽 치우침 점검
```
→ [예제 3](../examples/03-research-with-sources.md)

### 4-3. 데이터 분석

```
1. 데이터 점검부터 (결측, 중복, 단위) → 처리 방법을 내가 결정
2. 지표 정의를 내가 쓴다
3. 계산은 코드 실행으로, 코드 공개
4. 숫자 1~2개를 직접 재계산
5. 해석은 "데이터로 알 수 있는 것"과 "추측"을 구분
```
→ [예제 4](../examples/04-data-analysis.md)

### 4-4. 긴 문서 요약·회의록

```
1. 문서는 위, 질문은 아래
2. 관련 문장을 원문 그대로 먼저 뽑게 한다
3. 인용만 근거로 요약, 근거 없는 주장은 삭제
4. "문서에서 확인되지 않은 것" 섹션을 따로 둔다
```
→ [예제 2](../examples/02-document-summary.md)

---

## 5. 메타 프롬프팅과 재사용

### AI에게 프롬프트를 쓰게 한다

- **인터뷰 받기:** "빠진 정보를 하나씩 질문해서 프롬프트를 완성해줘"
- **개선 받기:** "이 프롬프트로 생길 수 있는 오해·누락·지어냄을 예상하고 고쳐줘"
- **최소 수정:** OpenAI는 이미 쓰고 있는 프롬프트를 고칠 때, 원하는 행동을 끌어내는 **최소한의 수정**이 무엇인지 모델에게 물어보라고 권합니다.

→ 템플릿: [templates/meta-prompt.md](../templates/meta-prompt.md)

### 잘 되는 프롬프트는 저장한다

한 번 잘 된 프롬프트는 다음에도 씁니다. 여러 서비스가 저장 기능을 제공합니다.

| 기능 | 무엇 |
|---|---|
| 프로젝트 (Projects) | 지침과 자료를 묶어 두고 그 안에서 대화 |
| 커스텀 GPT / 젬 (Gems) | 지침이 들어간 나만의 챗봇 |
| 스킬 (Skills) | 지침 + 스크립트 + 자료를 묶은 폴더. AI가 필요할 때 불러 씀 |
| 프로젝트 메모리 파일 | 코딩 에이전트가 매번 읽는 `AGENTS.md` / `CLAUDE.md` |

> 저장한 프롬프트도 모델이 바뀌면 **다시 시험**하세요.

---

## 6. 긴 작업: 여러 세션에 걸친 일

하루 이상 걸리는 큰 작업은 한 대화로 끝까지 갈 수 없습니다. Anthropic의 장기 실행 에이전트 사례(2025-11)는 이렇게 합니다.

1. **첫 세션:** 전체 작업 목록(체크리스트)과 진행 상황 파일을 만든다.
2. **이후 세션마다:** 진행 상황 파일을 읽고 → **항목 하나만** 처리하고 → 확인하고 → 기록을 남긴다.
3. **버전 관리(git)**로 언제든 되돌릴 수 있게 한다.

채팅에서도 똑같이 할 수 있습니다. 대화가 길어지면 "지금까지 결정한 것, 남은 일, 주의할 점을 정리해줘"라고 한 뒤 새 채팅에 붙여 넣으세요.

---

### 출처

- Karpathy, "context engineering" 게시물 (2025-06-25) — https://x.com/karpathy/status/1937902205765607626
- Tobi Lütke, "context engineering" 게시물 (2025-06) — https://twitter.com/tobi/status/1935533422589399127
- Simon Willison, "Context engineering" (2025-06-27) — https://simonwillison.net/2025/Jun/27/context-engineering/
- Anthropic, Effective context engineering for AI agents (2025-09-29) — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic, Building effective agents (2024-12-19) — https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, How we built our multi-agent research system (2025-06-13) — https://www.anthropic.com/engineering/multi-agent-research-system
- Anthropic, Effective harnesses for long-running agents (2025-11-26) — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic, Equipping agents for the real world with Agent Skills — https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Anthropic, Prompting best practices (체이닝, 하위 에이전트) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Claude Code, Best practices — https://code.claude.com/docs/en/best-practices
- OpenAI Cookbook, GPT-5 prompting guide (메타 프롬프팅, 보관 문서) — https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide
- Chroma, Context Rot (2025) — https://research.trychroma.com/context-rot
