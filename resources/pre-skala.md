# SKALA · Pre-SKALA 학습자를 위한 연결 안내

> 이 문서는 SKALA / Pre-SKALA 학습자가 이 저장소를 **수업 흐름에 맞춰** 쓸 수 있도록 연결해 둔 안내입니다.
>
> ⚠️ **비공식 자료입니다.** SK AX나 SKALA 운영진과 관계가 없으며, 강의 자료를 옮기거나 재배포하지 않습니다.
> 아래 내용은 **공개된 정보**(공식 사이트, 보도자료, 공개 블로그)만으로 작성했습니다.

---

## 1. SKALA와 Pre-SKALA는 무엇인가 (공개 정보 기준)

| | SKALA | Pre-SKALA |
|---|---|---|
| 공식 명칭 | SK AI Leader Academy (스칼라) | Pre-SKALA |
| 운영 | SK AX (2024년 SK C&C가 시작) | 주최 SK AX, 후원 SK하이닉스 |
| 형식 | 약 5개월, 전일제 대면, 채용 연계형 | 3주 자기주도 온라인 부트캠프 + 1박 2일 해커톤 |
| 대상 | 만 19~34세 | 500명 선발, 온라인 과정 상위 100명이 해커톤 진출 |
| 2026 일정 | 4기: 2026년 7~12월, 판교·광주·울산 | 온라인 10월 말~11월 중순, 해커톤 11/28~29 (판교) |
| 핵심 영역 | 데이터 분석·AIOps, Cloud Native AI, 생성형 AI 서비스 개발 | 아래 2절 참고 |

출처: [SK AX 뉴스룸 (2026-05-07)](https://www.skax.co.kr/company/news-room/sk-ax-skala-%EA%B4%91%EC%A3%BC%C2%B7%EC%9A%B8%EC%82%B0%EC%9C%BC%EB%A1%9C-%ED%99%95%EB%8C%80%ED%95%B4-ai%EC%9D%B8%EC%9E%AC-%EC%9C%A1%EC%84%B1%ED%95%9C%EB%8B%A4), [SKALA 공식 사이트](http://2026skala.co.kr/), [Pre-SKALA 공식 페이지](https://2026pre-skala.co.kr/), [서울대 컴퓨터공학부 공지](https://cse.snu.ac.kr/en/community/notice/25679)

---

## 2. Pre-SKALA 공개 커리큘럼 ↔ 이 저장소

Pre-SKALA 공식 페이지에 공개된 것은 **모듈 제목**뿐입니다. 각 모듈에서 실제로 무엇을 가르치는지는 공개되지 않았으므로, 아래 표는 **주제가 겹치는 이 저장소의 문서**를 연결한 것일 뿐 강의 내용과 같다는 뜻이 아닙니다.

| Pre-SKALA 모듈 (공개 제목) | 함께 보면 좋은 문서 |
|---|---|
| **Agent 이해와 업무 분석** | [01. 마음가짐](../docs/01-mindset.md) (자율성 슬라이더, AI를 쓰지 말아야 할 때) · [예제 7 1단계: 업무 분석](../examples/07-build-your-own-agent.md#1단계-업무-분석-무엇을-ai에게-맡길지-정하기) |
| **바이브코딩 입문** | [07. AI 코딩](../docs/07-ai-coding.md) (바이브 코딩 vs 에이전틱 엔지니어링) · [예제 5](../examples/05-coding-agent.md) |
| └ AI 지시 및 결과 검증 | [02. 프롬프트의 6요소](../docs/02-prompt-anatomy.md) · [04. 오해·누락·지어냄](../docs/04-failure-modes.md) · [08. 검증과 평가](../docs/08-verification-and-evals.md) |
| └ Agent 디버깅 및 설계 | [07. AI 코딩 §2 실패의 4가지 원인](../docs/07-ai-coding.md#2-세션이-실망스러운-4가지-이유) · [템플릿: 코딩 작업 지시](../templates/coding-task.md) |
| **에이전트 구성 및 실행** (도구 연결·업무지식 설계·자동화·테스트 및 개선) | [06. 워크플로](../docs/06-workflows.md) · [templates/AGENTS.template.md](../templates/AGENTS.template.md) · [09. 보안](../docs/09-security-privacy.md) |
| **최종과제: 나만의 Agent 만들기** | [예제 7. 나만의 에이전트 설계하기](../examples/07-build-your-own-agent.md) (업무 분석 → 지시문 → 평가셋 → 보안 점검) |

> 💡 공식 커리큘럼에서 프롬프트와 가장 가까운 표현은 **"AI 지시 및 결과 검증"**입니다. 이 저장소 전체가 결국 이 한 줄, 즉 **잘 지시하고(02~03) 결과를 검증하는 것(04, 08)**을 다룹니다.

---

## 3. SKALA 본과정의 프롬프트 수업 (공개된 수강생 기록)

SKALA 4기 수강생 한 명이 공개 블로그에 정리한 "Prompt 설계와 Context" 수업 기록(2026-07-15)이 유일하게 상세한 공개 자료입니다. **비공식 기록이며, 캠퍼스나 강사에 따라 다를 수 있습니다.**

기록에 따르면 수업의 중심 틀은 **RICE**였습니다.

| RICE | 수업에서의 설명 (기록 요약) | 이 저장소의 6요소 |
|---|---|---|
| **R**ole | 누구처럼 생각할지 | 역할 |
| **I**nstruction | 어떤 절차로 판단할지 | 지시 |
| **C**ontext | 사고가 허용되는 경계 조건 | 맥락 |
| **E**xample | 출력 견본이 아니라 **평가 기준의 표본** (3~5개 권장) | 예시 |
| (추가) Policy / Style / Constraints | | 제약 |
| (추가) Format / Structure | | 형식 |

그 밖에 기록된 주제: 환각의 원인(다음 토큰 예측), few-shot, CoT, Step-back, Self-Consistency, 소크라테스식 프롬프팅(모델이 먼저 질문하게), 반대 논증자(Devil's Advocate)와 다중 페르소나, 컨텍스트 엔지니어링, 하네스 엔지니어링.

| 수업 기록의 주제 | 이 저장소에서 |
|---|---|
| RICE + 형식·제약 | [02. 프롬프트의 6요소](../docs/02-prompt-anatomy.md) |
| Example = 평가 기준의 표본 | [03. 예시로 지시하기](../docs/03-examples-few-shot.md) |
| 환각 | [04 §3 지어냄(환각)](../docs/04-failure-modes.md#3-지어냄환각-fabrication--hallucination) |
| 소크라테스식 프롬프팅 | [templates/clarify-first.md](../templates/clarify-first.md) |
| Devil's Advocate, 다중 페르소나 | [templates/honest-critique.md](../templates/honest-critique.md) |
| CoT, Self-Consistency | [05. 모델과 추론](../docs/05-models-and-reasoning.md) · [04 §3](../docs/04-failure-modes.md#3-지어냄환각-fabrication--hallucination) |
| 컨텍스트·하네스 엔지니어링 | [06. 워크플로](../docs/06-workflows.md) · [07. AI 코딩](../docs/07-ai-coding.md) |

> 📌 수업 기록의 CoT 관련 내용은 2026년 기준으로 업데이트가 필요할 수 있습니다. 추론 모델에는 "단계별로 생각해"가 거의 효과가 없다는 연구가 있습니다. → [10. 신화 vs 근거 §4](../docs/10-myths-vs-evidence.md#4-단계별로-생각해-모델에-따라-다름)

출처: [SKALA 4기 수강생 블로그, "Prompt 설계와 Context"](https://stellacustodis.github.io/posts/skala-prompt-engineering/)

---

## 4. 이 저장소의 용어에 대해

| 이 저장소의 틀 | 출처 |
|---|---|
| **역할 · 맥락 · 지시 · 형식 · 제약 · 예시** (6요소) | 연구소 가이드, SKALA RICE, Google 한국어 가이드의 공통 요소를 합쳐 이 저장소가 정리한 것 |
| **오해 · 누락 · 지어냄** (3가지 실패) | 이 저장소의 **학습용 분류 틀**입니다. 이 세 단어가 한 묶음으로 쓰인 공개 출처는 찾지 못했습니다. 다만 각 실패의 원인과 대처는 모두 연구 근거에 연결했습니다 → [04](../docs/04-failure-modes.md) |
| **지어냄(환각)** | 한국어에서는 보통 **환각**(할루시네이션)이라고 부릅니다. 이 저장소에서는 "지어냄(환각)"으로 함께 씁니다 |

### 다른 한국어 자료와 용어 대응

| 이 저장소 | Google 한국어 가이드 | 프롬프트 엔지니어링 가이드 한국어판 |
|---|---|---|
| 역할 | 역할 (페르소나) | — |
| 맥락 | 맥락 | 문맥, 입력 데이터 |
| 지시 | 할 일 | 지시 |
| 형식 | 형식 | 출력 지시자 |
| 제약 | — | — |
| 예시 | — | — |

---

## 5. 해커톤·최종과제를 위한 체크리스트

에이전트를 만들 때 이 저장소에서 가장 바로 쓸 만한 것만 모았습니다.

- [ ] **업무 분석:** 어느 단계를 AI에게 맡기고, 어디서 사람이 승인할지 표로 정했다 ([예제 7](../examples/07-build-your-own-agent.md))
- [ ] **지시문:** 역할·맥락·지시·형식·제약·예시를 채웠고, "없는 정보는 만들지 말 것"을 넣었다 ([템플릿](../templates/universal-prompt.md))
- [ ] **출력 형식:** 다음 단계가 읽을 수 있게 JSON 등 구조화된 형식으로 정했다
- [ ] **평가셋:** 실패하기 쉬운 경우를 포함한 테스트 입력 20개를 만들고 통과/실패로 채점했다 ([08](../docs/08-verification-and-evals.md))
- [ ] **실패 분석:** 실패를 오해/누락/지어냄으로 분류해서 고쳤다 ([04](../docs/04-failure-modes.md))
- [ ] **보안:** 신뢰할 수 없는 입력 + 개인정보 + 외부 전송이 한 에이전트에 다 있지 않다 ([09](../docs/09-security-privacy.md))
- [ ] **코드:** 내가 설명할 수 없는 코드는 제출하지 않는다 ([07](../docs/07-ai-coding.md))

---

> 이 문서는 공개 정보가 늘어나면 업데이트합니다. Pre-SKALA 강의 내용이 공개되면 다시 대조할 예정입니다.
