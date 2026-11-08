# 05. 모델 고르기와 추론(Thinking) 모델 다루기

> 프롬프트만큼 중요한 것이 **어떤 모델과 어떤 도구로** 묻느냐입니다.
> 그리고 2025~2026년 사이에 추론 모델이 보편화되면서, 예전 프롬프트 요령 중 상당수가 **필요 없어지거나 오히려 해로워졌습니다.**

---

## 1. Karpathy의 일상 사용 원칙

Andrej Karpathy가 "How I use LLMs"(2025) 강연과 이후 글에서 권한 습관을 정리하면 이렇습니다.

| 원칙 | 이유 |
|---|---|
| **지금 어떤 모델을 쓰고 있는지 확인한다** | 같은 서비스라도 무료/유료, 모드에 따라 모델이 다르다. 성능도 크게 다르다 |
| **모델은 마케팅이 아니라 비교로 고른다** | 리더보드와 직접 비교로 판단한다. 여러 모델에 같은 질문을 던져 보는 것도 방법 |
| **주제가 바뀌면 새 채팅** | 맥락 창(context window)은 작업 기억이다. 관계없는 내용이 쌓이면 방해가 되고 느려진다 |
| **필요한 자료는 직접 넣어 준다** | 모델의 기억에 기대지 말고 문서를 붙여 넣는다 (컨텍스트 엔지니어링) |
| **어려운 문제는 추론 모델로** | 수학, 코드, 복잡한 분석. 쉬운 질문에는 빠른 모델이면 충분 |
| **사실은 검색, 계산은 코드** | 최신 정보는 검색 도구, 숫자는 코드 실행 도구 |
| **중요한 것은 검증한다** | 모델은 사람이 하지 않을 실수를 한다 |

---

## 2. 작업별 도구 선택

| 작업 | 추천 설정 | 이유 |
|---|---|---|
| 아이디어, 초안, 번역, 말투 다듬기 | 빠른 모델 | 정답이 하나가 아니고 즉시 확인 가능 |
| 최신 뉴스, 통계, 제품 정보 | **검색 켜기** | 모델의 학습 데이터에는 마감 시점이 있다 |
| 계산, 표 분석, 그래프 | **코드 실행 켜기** | 언어 모델은 암산이 약하다 |
| 수학, 논리, 복잡한 코딩, 전략 분석 | **추론 모델 / 높은 추론 강도** | 스스로 여러 단계를 검토한다 |
| 여러 출처를 모은 조사 보고서 | 딥리서치 기능 + **출처 검증** | 편하지만 출처 품질을 가리지 않음 → [예제 3](../examples/03-research-with-sources.md) |
| 내 문서 기반 질의응답 | 파일 첨부 / 프로젝트 기능 | 근거를 내 자료로 제한 |
| 코드베이스 작업 | 코딩 에이전트 | 파일을 읽고 테스트를 실행할 수 있음 → [07. AI 코딩](07-ai-coding.md) |

---

## 3. 추론 모델은 "선배 동료"처럼 대한다

OpenAI는 두 종류의 모델을 이렇게 비유합니다.

- **일반 모델:** 지시를 하나하나 정확히 줘야 하는 **신입 동료**
- **추론 모델:** 목표만 주면 방법은 알아서 찾는 **노련한 선배 동료**

그래서 추론 모델에게는 다르게 써야 합니다.

| 예전 습관 (일반 모델용) | 추론 모델에게는 |
|---|---|
| "단계별로 생각해(think step by step)" | **빼세요.** 이미 스스로 생각합니다 |
| 풀이 절차를 1~10단계로 지시 | **목표와 성공 기준**만 분명히. Anthropic은 직접 쓴 단계보다 일반적인 지시("충분히 생각해서")가 나은 경우가 많다고 설명 |
| 예시를 많이 넣기 | **예시 없이 먼저** 시도 (OpenAI) |
| "생각 과정을 `<thinking>` 태그에 써" | 하지 마세요. 최신 Claude 모델은 거부할 수 있고, OpenAI·Microsoft는 내부 추론을 억지로 끌어내는 것을 지원하지 않는다고 명시 |
| "더 열심히 생각해", "think hard" | 문구보다 앱·API의 **추론 강도(effort) 설정**을 쓰세요. Claude Code 문서는 이런 문구를 "더 이상 할 필요 없는 것"으로 분류 (단, `ultrathink`는 한 턴에 한해 여전히 동작) |
| temperature 조정 | 추론 모델은 대부분 지원하지 않거나 무시. Google은 최신 Gemini에서 사용자 지정 값을 무시하며 앞으로 오류를 낼 예정이라고 안내 |

### 연구로 확인된 것

와튼 생성형 AI 연구소의 Prompting Science Report 2(2025)는 "단계별로 생각해" 지시의 효과를 측정했습니다.

- **일반 모델:** 평균 성능이 올랐지만(최대 13.5%p), 원래 맞히던 **쉬운 문제에서 오히려 틀리는** 경우가 생겼습니다.
- **추론 모델:** 효과가 +3.1%p ~ −3.3%p로 **거의 없었고**, 답을 내는 시간만 20~80% 늘었습니다.
- 반대로 일반 모델에게 "답만 말해"라고 하면 성능이 떨어질 가능성이 높다고 경고했습니다.

> **정리:** 일반(즉답) 모델에게는 생각할 여지를 주고, 추론 모델에게는 생각하는 방법을 지시하지 마세요.

---

## 4. 추론 강도(Effort) 다루기

여러 서비스가 "추론 강도"를 선택하게 합니다 (예: 낮음 / 중간 / 높음, 또는 Thinking 모드 켜기).

- **기본값에서 시작**하고, 결과가 부족할 때 한 단계씩 올리세요.
- 추론 강도를 올리기 **전에** 먼저 확인할 것: 성공 기준을 썼는가? 자료를 줬는가? 검증 수단이 있는가? OpenAI는 강도를 올리기 전에 빠진 성공 기준이나 검증 루프가 없는지 먼저 보라고 권합니다.
- 너무 오래 고민한다면(overthinking) "한 가지 방법을 골라서 끝까지 진행해"라고 하거나 강도를 낮추세요 (Anthropic).

---

## 5. 2026년 기준: 버려야 할 예전 습관

세 회사의 최신 가이드가 공통으로 말하는 것은 **"새 요령을 더하라"가 아니라 "예전 요령을 덜어내라"**입니다.

| 버릴 습관 | 이유 |
|---|---|
| 대문자 강조, "절대!!!", "IMPORTANT" | 최신 모델이 과하게 따라서 융통성이 사라짐 |
| "게으름 피우지 마", "끝까지 다 해" | 최신 모델은 이미 끝까지 하려는 경향이 강함. 과잉 행동을 부름 |
| 과도한 검증 지시 | 최신 모델은 스스로 검토함. 예전 지시가 과잉 검증을 부름 |
| "간결하게" 반복 | 최신 모델은 이미 간결해지는 추세. 너무 짧아질 수 있음 |
| 길고 장황한 시스템 프롬프트 | OpenAI 내부 코딩 에이전트 테스트에서 군더더기를 덜어낸 프롬프트가 약 10~15% 높은 점수 (경향을 보여 주는 수치) |

### 모델을 바꾸면 프롬프트도 다시 맞춘다

같은 프롬프트라도 모델 버전이 바뀌면 결과가 달라집니다. 중요한 프롬프트는 모델을 바꿀 때마다 **같은 테스트 입력으로 다시 확인**하세요. OpenAI는 잘 작동하는 프롬프트에서 시작해 **한 묶음씩 덜어내며** 같은 평가를 다시 돌리라고 권합니다. → [08. 검증과 평가](08-verification-and-evals.md)

---

## 6. 같은 질문을 여러 모델에게

Karpathy가 만든 오픈소스 [llm-council](https://github.com/karpathy/llm-council)은 여러 모델이 각자 답하고, 서로의 답을 평가한 뒤, 의장 모델이 최종 답을 정리하는 구조입니다. 개인이 손으로 따라 하면 이렇습니다.

1. 같은 질문을 2~3개 서비스에 묻는다.
2. 답이 다른 부분을 표시한다. → 그 부분이 **가장 확인이 필요한 곳**입니다.
3. 한 모델에게 다른 모델들의 답을 보여 주고 차이를 분석하게 한다.

---

### 출처

- Karpathy, "How I use LLMs" (2025-02-27) — https://www.youtube.com/watch?v=EWvNQjAaOHw
- Karpathy, "Deep Dive into LLMs like ChatGPT" (2025-02-05) — https://www.youtube.com/watch?v=7xTGNNLPyMI
- Karpathy, llm-council — https://github.com/karpathy/llm-council
- OpenAI, Prompt engineering guide (추론 모델 = 선배 동료 비유) — https://developers.openai.com/api/docs/guides/prompt-engineering
- OpenAI, Reasoning best practices (o-series 기준, 일부 내용은 이전 세대 기준) — https://developers.openai.com/api/docs/guides/reasoning-best-practices
- OpenAI, 최신 모델 프롬프트 가이드 — https://developers.openai.com/api/docs/guides/prompt-guidance
- OpenAI, GPT-5.6 prompt guidance (군더더기 제거, effort 기준) — https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6
- Anthropic, Prompting best practices (일반 지시 > 단계 지시, effort, 과잉 검증) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Claude Code, Best practices ("더 이상 할 필요 없는 것") — https://code.claude.com/docs/en/best-practices
- Google, Prompt design strategies (thinking 모델, temperature) — https://aistudio.google.com/docs/prompting-strategies
- Microsoft, Prompt engineering techniques (추론 모델에는 비권장 배너) — https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering
- Meincke et al., Prompting Science Report 2 "The Decreasing Value of Chain of Thought in Prompting" (Wharton, 2025, 프리프린트) — https://arxiv.org/abs/2506.07142
