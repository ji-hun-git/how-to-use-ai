# 03. 예시로 지시하기 (Few-shot)

> 말로 열 줄 설명하는 것보다 **예시 하나를 보여 주는 것**이 더 정확할 때가 많습니다.
> 예시는 형식, 어조, 구조, 판단 기준을 맞추는 가장 믿을 만한 방법 중 하나입니다. (Anthropic, Google, OpenAI 공통)

---

## 1. 예시는 "평가 기준의 표본"이다

SKALA 강의 정리(수강생 블로그)에서는 예시를 **"평가 기준의 표본"**이라고 정의합니다. 좋은 정의입니다. 예시를 주는 목적은 내용을 베끼게 하려는 것이 아니라, **"이 정도면 합격"이라는 기준을 보여 주는 것**입니다.

그러니 예시를 고를 때는 이렇게 물어보세요.

> 이 예시들만 보고, 처음 보는 사람이 **합격 기준**을 추론할 수 있을까?

---

## 2. 공식 가이드가 말하는 규칙

| 규칙 | 출처 |
|---|---|
| **3~5개**가 적당하다 | Anthropic, Google 프롬프트 엔지니어링 백서, SKALA 강의 |
| 서로 **다양하게** 고른다 (경계 사례 포함) | Anthropic, OpenAI |
| `<example>` 태그로 감싸서 지시와 구분한다 | Anthropic |
| 모든 예시의 **형식을 똑같이** 맞춘다 (태그, 줄바꿈, 구분자) | Google |
| 너무 많으면 **과적합**된다 (예시에만 맞춘 답) | Google |
| 분류 작업은 6개 정도에서 시작하고 **정답 순서를 섞는다** | Google 백서 |
| 예시와 지시가 **서로 모순되면 안 된다** | OpenAI |
| 추론 모델은 **예시 없이 먼저** 시도하고, 필요할 때만 추가한다 | OpenAI |
| 효과가 없는 예시는 지운다 | OpenAI (최신 모델 가이드) |

---

## 3. 예시의 종류

### 3-1. 입력 → 출력 쌍 (가장 기본)

```xml
<examples>
<example>
입력: 배송이 너무 늦어요. 일주일째 안 와요.
출력: {"category": "배송", "sentiment": "부정", "urgency": "높음"}
</example>
<example>
입력: 포장이 꼼꼼해서 좋았어요!
출력: {"category": "포장", "sentiment": "긍정", "urgency": "낮음"}
</example>
<example>
입력: 사이즈 교환 되나요?
출력: {"category": "교환", "sentiment": "중립", "urgency": "중간"}
</example>
</examples>

이제 아래 리뷰를 같은 형식으로 분류해줘.
입력: {{리뷰}}
```

> 세 예시의 감정(부정/긍정/중립)과 긴급도(높음/낮음/중간)가 모두 다릅니다. 이렇게 **다양하게** 골라야 AI가 "다 부정으로 답하면 되겠다" 같은 엉뚱한 패턴을 배우지 않습니다.

### 3-2. 좋은 예와 나쁜 예 대비

판단 기준이 미묘할 때 효과적입니다.

```xml
<good_example>
제목: 3분기 매출 12% 증가, 신규 고객이 견인
→ 좋은 이유: 숫자와 원인이 제목에 다 있음
</good_example>
<bad_example>
제목: 3분기 실적 보고
→ 나쁜 이유: 읽기 전에는 아무것도 알 수 없음
</bad_example>
```

> **왜 좋은지/나쁜지 한 줄 설명**을 붙이면 AI가 표면이 아니라 원리를 배웁니다. Anthropic도 예시에 "왜 이 응답이 맞는지"를 함께 적으라고 권합니다.

### 3-3. 풀이 과정을 보여 주는 예시

추론이 필요한 작업이라면 **문제 → 풀이 방법 → 답** 순서로 예시를 보여 주세요. Anthropic은 이렇게 하면 모델의 사고 과정도 예시를 닮아 간다고 설명합니다.

### 3-4. 내 글을 예시로 (스타일 맞추기)

```text
아래는 내가 쓴 글 3편이야. 문장 길이, 어조, 자주 쓰는 표현을 분석해서 같은 스타일로 써줘.
내용과 주제는 참고하지 마.
<example>...</example>
<example>...</example>
<example>...</example>
```

---

## 4. 흔한 실패와 해결

| 실패 | 원인 | 해결 |
|---|---|---|
| 예시 문장을 **그대로 베낌** | 예시가 1개뿐이거나 지시가 없음 | 예시를 늘리고 "패턴만 참고하고 표현은 새로 써"라고 쓰기 |
| 모든 답이 **같은 라벨** | 예시의 라벨이 한쪽으로 쏠림 | 라벨을 고르게, 순서도 섞기 |
| 마지막 예시만 닮음 | 최근 예시에 끌리는 경향 | 순서를 바꿔 가며 시험해 보기 |
| 예시에 없는 경우를 **이상하게 처리** | 경계 사례 예시 부족 | 애매한 경우, 빈 입력, 예외 예시 추가 |
| 지시와 예시가 **충돌** | 예시는 길게, 지시는 "짧게" | 예시를 지시에 맞게 고치기 |
| 추론 모델 성능이 **오히려 떨어짐** | 예시가 모델의 자체 추론을 방해 | 예시 없이 시도 후 비교 |

> 예시의 라벨 분포나 순서에 결과가 끌리는 현상은 오래전부터 연구됐습니다(Zhao et al., "Calibrate Before Use", 2021). 최신 모델에서는 덜하지만, **분류 작업**이라면 여전히 확인할 가치가 있습니다.

> 마이크로소프트 연구진의 프리프린트(2024)에서는 추론 모델(o1)에 few-shot 예시를 주자 **성능이 오히려 떨어졌습니다.** 그래서 추론 모델에는 "예시 없이 먼저"가 기본입니다.

---

## 5. 예시가 없을 때: AI에게 예시를 만들게 하기

```text
이 작업에 쓸 예시 5개를 만들어줘. 쉬운 경우 2개, 애매한 경우 2개, 예외 1개로.
각 예시마다 정답과 그 이유를 적어줘.
```

AI가 만든 예시를 **내가 검토하고 고친 뒤** 프롬프트에 넣으세요. 고치는 과정에서 내 기준도 분명해집니다. Anthropic도 Claude에게 예시를 평가하거나 새로 만들게 하는 방법을 소개합니다.

---

## 6. 점검표

- [ ] 예시가 2개 이상이고, 서로 충분히 다르다
- [ ] 경계 사례(애매한 경우)가 하나 이상 있다
- [ ] 모든 예시의 형식이 똑같다
- [ ] 예시가 지시와 모순되지 않는다
- [ ] "무엇을 참고하고 무엇은 참고하지 말지"를 적었다
- [ ] 추론 모델이라면 예시 없이도 시도해 봤다

---

### 출처

- Anthropic, Prompting best practices (예시 3~5개, 다양성, 태그) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic, Effective context engineering (규칙 나열보다 대표 예시) — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- OpenAI, Prompt engineering guide — https://developers.openai.com/api/docs/guides/prompt-engineering
- OpenAI, Reasoning best practices (추론 모델은 zero-shot 먼저) — https://developers.openai.com/api/docs/guides/reasoning-best-practices
- OpenAI Cookbook, GPT-4.1 Prompting Guide (예시 문구 반복 문제, 보관 문서) — https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide
- Google, Prompt design strategies (형식 일관성, 과적합) — https://aistudio.google.com/docs/prompting-strategies
- Google/Kaggle, Prompt Engineering 백서 (Lee Boonstra) — https://www.kaggle.com/whitepaper-prompt-engineering
- Microsoft, Prompt engineering techniques (few-shot 전후 비교) — https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering
- Nori et al., "From Medprompt to o1" (Microsoft Research, 2024, 프리프린트) — https://arxiv.org/abs/2411.03590
- Zhao et al., "Calibrate Before Use: Improving Few-Shot Performance of Language Models" (ICML 2021) — https://arxiv.org/abs/2102.09690
- Schulhoff et al., "The Prompt Report" (2024~2025) — https://arxiv.org/abs/2406.06608
- SKALA 4기 수강생 블로그, "Prompt 설계와 Context" (비공식) — https://stellacustodis.github.io/posts/skala-prompt-engineering/
