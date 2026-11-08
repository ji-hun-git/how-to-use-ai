# how-to-use-ai

AI에게 일을 잘 맡기는 방법을 정리한 한국어 가이드입니다. 지시를 어떻게 쓰고, 결과를 어떻게 확인하는지에 집중합니다.

Anthropic · OpenAI · Google · Microsoft의 공식 문서, 공개된 연구, Andrej Karpathy 같은 실무자의 글을 바탕으로 정리했습니다. 출처는 각 문서 끝에 있고, 2차 자료로만 확인한 수치나 논쟁 중인 연구는 [근거 보고서](research/evidence-report.md#8-검증된-것과-검증되지-않은-것)에 따로 표시했습니다. 연구 결과는 대부분 조사 당시 모델 기준이라, 최신 모델에서 같은 크기로 나타난다고 보장하지 않습니다.

[English](README.en.md) · [한 장 치트시트](CHEATSHEET.md) · [근거 보고서](research/evidence-report.md)

---

## 30초 요약

> **AI 활용의 단위는 "좋은 문장"이 아니라 "좋은 지시 + 좋은 검증"이다.**

### 1. 이렇게 지시한다: 6요소

| 역할 | 맥락 | 지시 | 형식 | 제약 | 예시 |
|---|---|---|---|---|---|
| 어떤 관점·말투로 | 왜, 누구를 위해, 어떤 상황에서 | 무엇을, 언제 끝나면 완료인지 | 결과물의 구조·분량 | 꼭 지킬 규칙 | 좋은 결과의 견본 3~5개 |

연구로 보면 시간을 쓸 곳은 맥락 · 지시 · 형식입니다. "세계 최고의 전문가" 같은 역할 설정은 통제 실험에서 정확도를 올리지 못했습니다. → [02. 프롬프트의 6요소](docs/02-prompt-anatomy.md)

### 2. 이렇게 진단한다: AI가 틀리는 세 가지 방식

| 오해 | 누락 | 지어냄(환각) |
|---|---|---|
| 요청을 다르게 이해했다 | 해야 할 것을 빠뜨렸다 | 없는 것을 만들어냈다 |
| 맥락·완료 기준을 주고, 질문을 먼저 받고, 꼬이면 정리해서 **새 채팅** | 요구사항에 번호, 자료는 위·질문은 아래, **커버리지 표** | **모른다고 말할 권리**, 자료에만 근거, 인용 먼저, **출처 직접 확인** |

여기에 **아첨**(내 말에 맞춰 주기)도 있습니다. 2023년 실험(10개 모델)에서 "정말 확실해?"라고 되묻자 모델은 평균 46%의 경우 답을 바꿨고, 정확도는 평균 약 17%p 떨어졌습니다. → [04. 오해 · 누락 · 지어냄](docs/04-failure-modes.md)

### 3. 이렇게 일한다: 기본 루프

```
명세 → 계획 → 실행 → 검증 → 반영
```

목표와 완료 기준을 먼저 쓰고, 큰 일은 계획부터 승인하고, AI가 스스로 확인할 수단을 주고, **바깥 증거로** 검증하고, 반복되는 실수는 템플릿에 반영합니다. → [06. 워크플로](docs/06-workflows.md)

---

## 바로 쓰기: 복사해서 붙여 넣는 템플릿

| 상황 | 템플릿 |
|---|---|
| 어떤 작업이든 | [만능 프롬프트 템플릿](templates/universal-prompt.md) (3줄 버전 / 전체 버전) |
| AI가 내 말을 자꾸 다르게 이해할 때 | [오해 방지: 질문 먼저](templates/clarify-first.md) |
| 요구사항이나 문서 내용이 빠질 때 | [누락 방지: 커버리지 점검](templates/coverage-check.md) |
| 사실·숫자·출처가 중요할 때 | [지어냄(환각) 방지: 근거 기반 답변](templates/grounded-answer.md) |
| 솔직한 피드백이 필요할 때 | [아첨 방지: 정직한 비평](templates/honest-critique.md) |
| 프롬프트 자체를 개선하고 싶을 때 | [메타 프롬프트](templates/meta-prompt.md) |
| 코딩 에이전트에게 일을 맡길 때 | [코딩 작업 지시](templates/coding-task.md) · [AGENTS.md 템플릿](templates/AGENTS.template.md) |

---

## 목차

### 가이드 (docs)

| # | 문서 | 핵심 질문 |
|---|---|---|
| 01 | [마음가짐](docs/01-mindset.md) | AI를 어떤 존재로 대해야 하나? 언제 쓰지 말아야 하나? |
| 02 | [프롬프트의 6요소](docs/02-prompt-anatomy.md) | 역할 · 맥락 · 지시 · 형식 · 제약 · 예시를 어떻게 쓰나? |
| 03 | [예시로 지시하기](docs/03-examples-few-shot.md) | 예시는 몇 개, 어떻게 골라야 하나? |
| 04 | [오해 · 누락 · 지어냄](docs/04-failure-modes.md) | AI는 왜 틀리고, 어떻게 막고, 어떻게 잡아내나? |
| 05 | [모델과 추론](docs/05-models-and-reasoning.md) | 어떤 모델·도구를 쓰나? 추론 모델은 어떻게 다르게 다루나? |
| 06 | [워크플로](docs/06-workflows.md) | 컨텍스트 엔지니어링, 5가지 패턴, 업무별 플레이북 |
| 07 | [AI 코딩](docs/07-ai-coding.md) | 바이브 코딩에서 에이전틱 엔지니어링으로 |
| 08 | [검증과 평가](docs/08-verification-and-evals.md) | 답 하나는 어떻게 검증하고, 프롬프트는 어떻게 평가하나? |
| 09 | [보안과 개인정보](docs/09-security-privacy.md) | 무엇을 넣으면 안 되나? 프롬프트 인젝션은? |
| 10 | [신화 vs 근거](docs/10-myths-vs-evidence.md) | "팁 줄게", "전문가처럼", "단계별로 생각해"는 정말 효과가 있나? |

### 예제 (examples): 나쁜 프롬프트가 좋은 프롬프트로 바뀌는 과정

| # | 예제 | 배우는 것 |
|---|---|---|
| 1 | [업무 메일: 한 요소씩 더해 보기](examples/01-email-step-by-step.md) | 6요소가 결과를 어떻게 바꾸는지 |
| 2 | [긴 문서 요약](examples/02-document-summary.md) | 누락과 지어냄을 동시에 막기 |
| 3 | [조사·리서치](examples/03-research-with-sources.md) | 가짜 출처 걸러내기 |
| 4 | [데이터 분석](examples/04-data-analysis.md) | 계산은 코드로, 가정은 드러나게 |
| 5 | [코딩 에이전트로 버그 고치기](examples/05-coding-agent.md) | 탐색 → 계획 → 테스트 → 구현 → 검증 |
| 6 | [AI로 공부하기](examples/06-learning-with-ai.md) | 답이 아니라 이해를 얻는 법 |
| 7 | [나만의 에이전트 설계하기](examples/07-build-your-own-agent.md) | 업무 분석 → 지시문 → 평가셋 → 보안 |

### 자료 (resources)

- [참고 자료 모음 (Awesome List)](resources/awesome.md): 공식 가이드, Karpathy의 영상·글·저장소, MIT · Harvard · Wharton · Stanford 자료, 유명 GitHub 저장소(별 수·상태 확인)
- [SKALA · Pre-SKALA 학습자를 위한 연결 안내](resources/pre-skala.md): 공개 커리큘럼과 이 저장소 문서 연결, 해커톤 체크리스트

### 근거 (research)

- [근거 보고서](research/evidence-report.md): 이 저장소의 모든 권고가 기대고 있는 조사 보고서. 출처 288개, 주장별 확인 수준 표 포함

---

## 학습 경로

| 시간 | 대상 | 순서 |
|---|---|---|
| **30분** | 처음 시작하는 사람 | [치트시트](CHEATSHEET.md) → [02. 6요소](docs/02-prompt-anatomy.md) → [예제 1](examples/01-email-step-by-step.md) → [만능 템플릿](templates/universal-prompt.md) |
| **2시간** | 업무에 제대로 쓰려는 사람 | 위 + [01. 마음가짐](docs/01-mindset.md) → [04. 오해·누락·지어냄](docs/04-failure-modes.md) → [08. 검증](docs/08-verification-and-evals.md) → [10. 신화 vs 근거](docs/10-myths-vs-evidence.md) → 예제 2~4 |
| **하루** | 개발자, 에이전트를 만드는 사람 | 위 + [05](docs/05-models-and-reasoning.md) → [06](docs/06-workflows.md) → [07](docs/07-ai-coding.md) → [09](docs/09-security-privacy.md) → 예제 5, 7 → [Karpathy "How I use LLMs"](https://www.youtube.com/watch?v=EWvNQjAaOHw) |

---

## 용어에 대해

"역할 · 맥락 · 지시 · 형식 · 제약 · 예시"는 여러 기관 가이드의 공통 요소를 합친 것이고, "오해 · 누락 · 지어냄"은 이 저장소가 만든 학습용 분류입니다. 효과가 없다고 나온 요령(팁·협박·전문가 역할·추론 모델에 "단계별로 생각해")은 [10. 신화 vs 근거](docs/10-myths-vs-evidence.md)에 따로 정리했습니다. SKALA / Pre-SKALA와의 관계는 [resources/pre-skala.md](resources/pre-skala.md)를 참고하세요 (비공식).

---

## 핵심 출처

| 분류 | 대표 자료 |
|---|---|
| 연구소 공식 가이드 | [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) · [OpenAI](https://developers.openai.com/api/docs/guides/prompt-engineering) · [Google](https://aistudio.google.com/docs/prompting-strategies) · [Microsoft](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering) · [Claude Code](https://code.claude.com/docs/en/best-practices) · [Codex](https://learn.chatgpt.com/guides/best-practices) |
| Andrej Karpathy | [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) · [Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI) · [Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/) · [nanochat](https://github.com/karpathy/nanochat) · [llm-council](https://github.com/karpathy/llm-council) |
| 대학·연구 | [MIT Sloan](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/) · [Wharton Prompting Science Reports](https://arxiv.org/abs/2503.04818) · [Harvard/BCG Jagged Frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged) · [Stanford 법률 AI 환각](https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries) · [The Prompt Report](https://arxiv.org/abs/2406.06608) |
| 실패 연구 | [Lost in the Middle](https://arxiv.org/abs/2307.03172) · [Why LMs Hallucinate](https://arxiv.org/abs/2509.04664) · [LLMs Get Lost in Multi-Turn](https://arxiv.org/abs/2505.06120) · [Sycophancy](https://arxiv.org/abs/2310.13548) · [Chain-of-Verification](https://arxiv.org/abs/2309.11495) |
| GitHub | [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) · [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) · [openai/openai-cookbook](https://github.com/openai/openai-cookbook) · [github/spec-kit](https://github.com/github/spec-kit) · [agents.md](https://agents.md/) |

전체 목록: [resources/awesome.md](resources/awesome.md) · 전체 출처: [research/evidence-report.md](research/evidence-report.md#참고문헌)

---

## 업데이트 정책

AI 도구와 공식 가이드는 몇 달마다 바뀝니다. 이 저장소는 **조사 기준일(현재 2026-11-09)**을 밝히고, 모델 세대가 바뀌어 낡은 조언은 표시하거나 고칩니다. 모델 이름처럼 빨리 바뀌는 정보는 가능한 한 일반적인 표현(일반 모델 / 추론 모델)으로 썼습니다.

## 만든 사람

**Jihun Chae** ([@ji-hun-git](https://github.com/ji-hun-git))

잘못된 내용이나 깨진 링크를 발견하면 [이슈](https://github.com/ji-hun-git/how-to-use-ai/issues)로 알려 주세요.

## 라이선스

[MIT](LICENSE). 각 문서에서 인용·요약한 외부 자료의 권리는 원저작자에게 있습니다.
