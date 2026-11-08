# 02. 프롬프트의 6요소: 역할 · 맥락 · 지시 · 형식 · 제약 · 예시

> 좋은 프롬프트는 길이가 아니라 **AI가 추측해야 하는 부분이 얼마나 적은지**로 결정됩니다.
> 6요소는 그 추측을 줄이기 위한 점검표입니다. 매번 6개를 다 쓸 필요는 없지만, **빠뜨린 요소가 있다면 일부러 뺀 것이어야 합니다.**

---

## 한눈에 보기

| 요소 | 질문 | 효과가 큰 정도 | 빠지면 생기는 문제 |
|---|---|---|---|
| **맥락** (Context) | 왜, 누구를 위해, 어떤 상황에서? | ★★★ | 오해, 지어냄 |
| **지시** (Instruction) | 정확히 무엇을 하고, 언제 끝난 것인가? | ★★★ | 오해, 누락 |
| **형식** (Format) | 결과물이 어떤 모양이어야 하나? | ★★★ | 재작업, 누락 |
| **예시** (Example) | 좋은 결과물은 어떻게 생겼나? | ★★☆ | 스타일 불일치 |
| **제약** (Constraint) | 반드시 지키거나 피할 것은? | ★★☆ | 사고, 규칙 위반 |
| **역할** (Role) | 어떤 관점과 말투로? | ★☆☆ | 어조 불일치 (정확도와는 거의 무관) |

> ⚠️ 많은 강의가 "역할 부여"를 맨 앞에 두지만, 연구 결과로 보면 **정확도에 가장 영향이 적은 요소**가 역할입니다. 순서는 외우기 쉽게 "역할·맥락·지시·형식·제약·예시"로 두되, **시간을 쓸 곳은 맥락·지시·형식**입니다. (근거는 아래 1절)

### 다른 프레임워크와의 대응

이 저장소의 6요소는 여러 기관이 제시한 구성 요소를 합친 것입니다. 이름은 달라도 내용은 거의 같습니다.

| 이 저장소 | Google Gemini 가이드 (한국어판) | OpenAI 권장 순서 | MIT Sloan |
|---|---|---|---|
| 역할 | 페르소나(역할) | Identity | Context의 일부 (role/persona) |
| 맥락 | 맥락 | Context | Context |
| 지시 | 할 일 | Instructions | Task, Specificity |
| 형식 | 형식 | (Instructions에 포함) | Examples & constraints |
| 제약 | — | (Instructions에 포함) | Examples & constraints |
| 예시 | — | Examples | Examples & constraints |


---

## 1. 역할 (Role)

**무엇:** AI가 어떤 입장과 관점에서 답할지 정합니다. "너는 10년 차 HR 담당자야", "너는 초등학교 선생님이야".

**연구가 말하는 것**
- 와튼 생성형 AI 연구소의 2025년 보고서(Prompting Science Report 4)는 "물리학 전문가처럼 답해" 같은 전문가 페르소나가 **사실 정확도를 믿을 만하게 올려 주지 못했다**고 보고했습니다. 오히려 일부 조건에서는 정확도가 떨어졌고, "유아" 같은 낮은 지식 페르소나는 확실히 성능을 떨어뜨렸습니다.
- 162개 역할을 2,410개 질문으로 실험한 연구(Zheng et al., EMNLP Findings 2024)에서도 역할 부여가 정확도를 높이지 못했고, **가장 좋은 역할을 자동으로 골라도 무작위로 고른 것과 차이가 없었습니다.**

**그러면 언제 쓰나?**
- **말투, 관점, 어휘 수준**을 정할 때: "신입사원에게 설명하는 선배처럼", "법무팀 관점에서 위험 요소를 보는 검토자로"
- **반대 입장**에서 보게 할 때: "이 제안서를 거절하려는 심사위원으로서" → [아첨 방지](../templates/honest-critique.md)

| ❌ 효과 없음 | ✅ 효과 있음 |
|---|---|
| 너는 세계 최고의 마케팅 천재야. | 너는 B2B SaaS 마케터야. 독자는 기술을 잘 모르는 중소기업 대표라서 전문용어 대신 비용과 시간 절감으로 설명해. |

> 두 번째 예시가 나은 이유는 "마케터"라는 역할 때문이 아니라 **독자와 설명 방식(맥락과 지시)**이 들어 있기 때문입니다.

---

## 2. 맥락 (Context): 가장 중요한 요소

**무엇:** 내 머릿속에만 있는 정보입니다. 목적, 독자, 상황, 배경 자료, 이미 시도한 것, 성공 기준.

**왜 가장 중요한가:** AI는 내 상황을 전혀 모릅니다. 맥락이 없으면 **가장 평균적인 답**을 내거나 빈칸을 **추측으로 채웁니다**(지어냄).

### 2-1. 목적(왜)을 알려 주면 AI가 스스로 응용한다

Anthropic 공식 가이드의 예입니다.

| ❌ 규칙만 | ✅ 이유까지 |
|---|---|
| 말줄임표(…)를 절대 쓰지 마. | 이 답변은 음성 합성(TTS) 엔진이 읽어 줄 거야. TTS는 말줄임표를 읽지 못하니까 쓰지 마. |

이유를 알려 주면 AI는 말줄임표뿐 아니라 **TTS가 읽기 어려운 다른 기호(이모지, 표 등)도 알아서 피합니다.** 규칙만 주면 정확히 그 규칙만 지킵니다.

### 2-2. 자료를 직접 주면 일반론이 사라진다

Google 공식 가이드의 예를 바꿔 옮기면 이렇습니다.

| ❌ 자료 없이 | ✅ 자료와 함께 |
|---|---|
| 공유기 불이 노란색으로 천천히 깜빡이는데 어떻게 해? | (공유기 매뉴얼의 문제 해결 부분을 붙여 넣고) 이 매뉴얼 내용만 근거로 답해줘. 공유기 불이 노란색으로 천천히 깜빡여. |
| → 어느 공유기에나 해당하는 일반적인 조치 | → 이 제품의 이 LED 상태에 맞는 조치 |

### 2-3. 맥락 점검 질문

- [ ] **목적:** 이 결과물로 무엇을 하려는가?
- [ ] **독자:** 누가 읽는가? 무엇을 이미 알고, 무엇을 모르는가?
- [ ] **상황:** 마감, 예산, 정치적 상황, 이미 정해진 것
- [ ] **자료:** AI가 알 수 없는 내부 자료, 최신 정보
- [ ] **이력:** 이미 해 봤는데 안 된 것

> **동료 테스트 (Anthropic 권장):** 이 프롬프트를 배경 지식이 없는 동료에게 그대로 보냈을 때 헷갈려 한다면, AI도 헷갈립니다.

### 2-4. 맥락은 "많이"가 아니라 "필요한 만큼"

맥락이 길수록 좋은 것은 아닙니다. Anthropic은 AI의 주의력을 **한정된 예산**에 비유하고, 입력이 길어질수록 앞의 정보를 놓치는 현상을 **맥락 부패(context rot)**라고 부릅니다. 목표는 **결과에 영향을 주는 정보를 가장 적은 분량으로** 주는 것입니다. → [06. 워크플로와 컨텍스트 엔지니어링](06-workflows.md)

---

## 3. 지시 (Instruction)

**무엇:** 무엇을 할지, 어떤 순서로 할지, 언제 끝난 것인지.

### 3-1. 원하는 수준을 분명히 말한다

최신 모델은 **시킨 것만 정확히** 하는 경향이 강해졌습니다. 기대 이상을 원하면 직접 말해야 합니다. Anthropic 공식 가이드의 예입니다.

| ❌ | ✅ |
|---|---|
| 분석 대시보드 만들어줘. | 분석 대시보드 만들어줘. 관련된 기능과 상호작용을 최대한 넣고, 기본 수준을 넘어 완성도 있게 구현해줘. |

### 3-2. 순서나 빠짐없음이 중요하면 번호를 붙인다

```text
1. 첨부한 고객 리뷰 200개를 긍정/부정/중립으로 분류
2. 부정 리뷰에서 반복되는 불만 주제 상위 5개 추출
3. 주제마다 대표 리뷰 1개 인용
```

### 3-3. 완료 기준(Done when)을 쓴다

"좋게 만들어줘"는 끝이 없습니다. **무엇이 되면 끝인지** 쓰세요.

```text
완료 기준: 비전공 임원이 1분 안에 읽고 "A안으로 가자"고 결정할 수 있으면 된다.
```

### 3-4. 추론 모델에게는 절차보다 목표를

최신 추론(Thinking) 모델은 단계를 하나하나 지시하는 것보다 **목표와 성공 기준을 분명히** 주는 편이 낫다고 OpenAI와 Anthropic 모두 권합니다. → [05. 모델과 추론](05-models-and-reasoning.md)

---

## 4. 형식 (Format)

**무엇:** 결과물의 모양. 구조(표, 불릿, 섹션), 분량, 어조, 파일 형식(JSON, 마크다운, CSV).

**연구가 말하는 것:** 와튼 Prompting Science Report 1(2025)에서 출력 형식 지시를 **뺐더니** 정확도가 GPT-4o에서 8.6%p, GPT-4o-mini에서 12.1%p 떨어졌습니다. 형식 지시는 꾸밈이 아니라 **성능 요소**입니다.

### 4-1. 구체적으로

| ❌ | ✅ |
|---|---|
| 간단히 정리해줘. | 3줄 요약 + 표(항목/현황/위험도) + 다음 할 일 불릿 3개 |
| 짧게 써줘. | 200자 이내로 |
| 보기 좋게 | 섹션 제목(##)을 쓰고, 문단은 3문장을 넘기지 마 |

### 4-2. "하지 마" 대신 "이렇게 해"

Anthropic과 Google 모두 **부정형보다 긍정형 지시**를 권합니다.

| ❌ | ✅ |
|---|---|
| 마크다운 쓰지 마. | 문단으로 이어지는 일반 텍스트로 써줘. |
| 너무 길게 쓰지 마. | 5문장 이내로 써줘. |
| 전문용어 쓰지 마. | 중학생이 이해할 수 있는 단어로 써줘. |

### 4-3. 프로그램이 읽을 결과는 구조화 출력 기능을 쓴다

결과를 코드에서 바로 읽어야 한다면 프롬프트로 "JSON으로 줘"라고 부탁하기보다, API의 **구조화 출력(Structured Outputs) 기능**으로 스키마를 지정하세요. OpenAI는 이 기능을 쓰면 스키마 준수를 보장한다고 밝힙니다.

### 4-4. 프롬프트의 모양이 답의 모양을 닮는다

마크다운으로 가득 찬 프롬프트를 주면 답도 마크다운이 되기 쉽습니다. 원하는 결과물과 비슷한 스타일로 프롬프트를 쓰세요.

---

## 5. 제약 (Constraint)

**무엇:** 반드시 지킬 규칙과 경계. 근거 규칙, 금지 사항, 범위, 정책.

### 5-1. 제약은 적을수록 잘 지켜진다

지시가 많아질수록 **모두 지킬 확률은 떨어집니다.** 여러 연구(ManyIFEval 2025, IFScale 2025)에서 지시 수가 늘수록 성능이 꾸준히 떨어졌고, 지시 500개를 준 실험에서는 가장 좋은 모델도 68%만 지켰습니다. **정말 중요한 제약만 남기세요.**

### 5-2. 대문자와 "절대!!!" 강조는 빼라 (2026년 기준)

예전에는 `IMPORTANT`, `반드시`, `절대` 같은 강조가 효과가 있었지만, Anthropic·OpenAI·Google의 최신 가이드는 공통으로 **최신 모델은 이런 강조를 지나치게 따른다**고 경고합니다. 그 결과 다른 지시를 무시하거나 융통성 없이 행동합니다.

| ❌ | ✅ |
|---|---|
| 절대로!!! 고객 이름을 쓰지 마!!! | 고객 이름 대신 "고객님"이라고 써줘. 이 답변은 다른 고객에게도 공유될 수 있어서야. |

> `항상`/`절대`는 **정말 예외가 없는 규칙**에만 쓰세요.

### 5-3. 꼭 넣을 만한 제약: 근거 규칙

```text
제공한 자료에 없는 내용은 추측하지 말고 "자료에 없음"이라고 써줘.
```

이 한 줄이 지어냄(환각)을 가장 싸게 줄여 줍니다. → [04. 오해 · 누락 · 지어냄](04-failure-modes.md)

---

## 6. 예시 (Example)

**무엇:** 원하는 결과물의 견본. 말로 설명하기 어려운 스타일, 형식, 판단 기준을 **보여 주는** 방법입니다.

핵심만 요약하면 다음과 같습니다. 자세한 내용은 [03. 예시로 지시하기](03-examples-few-shot.md)에 있습니다.

- **3~5개**, 서로 **다양하게**, `<example>` 태그로 감싸기 (Anthropic, Google)
- 예시가 1개면 그대로 베낍니다
- 추론 모델에는 **예시 없이 먼저** 해 보고, 필요할 때 추가하기 (OpenAI)

---

## 7. 배치와 구분: 어디에 무엇을 둘까

### 7-1. 구분자로 칸을 나눈다

맥락, 자료, 지시가 한 문단에 섞이면 AI가 **자료 속 문장을 지시로 착각**하기도 합니다. XML 태그나 마크다운 제목으로 나누세요. 네 회사 모두 같은 권고를 합니다. 한 프롬프트 안에서는 **한 가지 방식만** 쓰세요.

```xml
<context>...</context>
<document>...</document>
<task>...</task>
<format>...</format>
```

### 7-2. 긴 자료는 위에, 질문은 아래에

자료가 길면(수십 쪽 이상) 자료를 **앞에** 두고 질문과 지시를 **맨 끝에** 두세요. Anthropic은 이렇게 하면 응답 품질이 **최대 30%** 좋아졌다고 밝혔습니다. 여러 문서를 넣을 때는 문서마다 출처를 붙이세요.

```xml
<documents>
  <document index="1"><source>2026_사업계획.pdf</source><content>...</content></document>
  <document index="2"><source>경쟁사_분석.xlsx</source><content>...</content></document>
</documents>

위 두 문서를 비교해서 ...  ← 질문은 맨 끝에
```

---

## 8. 최종 점검표

보내기 전에 10초만 확인하세요.

- [ ] **맥락:** 목적과 독자를 썼다
- [ ] **지시:** 무엇을 하는지, 언제 끝나는지 분명하다
- [ ] **형식:** 구조와 분량을 정했다
- [ ] **제약:** 정말 중요한 규칙만 남겼고, 근거 규칙을 넣었다
- [ ] **예시:** 스타일이 중요하면 2~3개를 넣었다
- [ ] **역할:** 말투나 관점이 중요할 때만 넣었다
- [ ] **구분:** 자료와 지시를 태그로 나눴고, 긴 자료는 위에 뒀다
- [ ] **동료 테스트:** 맥락 없는 동료가 읽어도 이해할 수 있다

→ 바로 쓸 수 있는 템플릿: [templates/universal-prompt.md](../templates/universal-prompt.md)
→ 단계별로 좋아지는 예제: [examples/01-email-step-by-step.md](../examples/01-email-step-by-step.md)

---

### 출처

- Anthropic, Prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic, Prompt engineering overview — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Anthropic, Effective context engineering for AI agents (2025-09-29) — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- OpenAI, Prompt engineering guide — https://developers.openai.com/api/docs/guides/prompt-engineering
- OpenAI, Structured outputs — https://developers.openai.com/api/docs/guides/structured-outputs
- Google, Prompt design strategies — https://aistudio.google.com/docs/prompting-strategies
- Google, Gemini for Google Workspace 프롬프트 가이드 101 (한국어판) — https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101_ko.pdf
- Microsoft, Prompt engineering techniques — https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering
- MIT Sloan Teaching & Learning Technologies, Effective Prompts for AI: The Essentials — https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/
- Meincke et al., Prompting Science Report 1 "Prompt Engineering is Complicated and Contingent" (Wharton, 2025, 프리프린트) — https://arxiv.org/abs/2503.04818
- Basil et al., Prompting Science Report 4 "Playing Pretend: Expert Personas Don't Improve Factual Accuracy" (Wharton, 2025, 프리프린트) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5879722
- Zheng et al., "When 'A Helpful Assistant' Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models" (EMNLP Findings 2024) — https://arxiv.org/abs/2311.10054
- ManyIFEval / StyleMBPP: 지시 수에 따른 성능 저하 연구 (2025) — https://arxiv.org/abs/2509.21051
- IFScale: 최대 500개 지시 동시 준수 실험 (2025) — https://arxiv.org/abs/2507.11538
