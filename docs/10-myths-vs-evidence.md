# 10. 프롬프트 신화 vs 근거

> 인터넷에는 "이 문구 하나로 GPT 성능 2배!" 같은 요령이 넘쳐납니다.
> 이 문서는 널리 퍼진 요령들을 **통제된 실험 결과**와 **공식 가이드**에 비춰 정리합니다.
> 핵심 교훈: **요령보다 과제 정의, 맥락, 형식, 예시, 검증이 훨씬 중요합니다.**

---

## 요약표

| 흔한 요령 | 판정 | 근거 |
|---|---|---|
| "팁 줄게", "안 하면 큰일 나" (보상·협박) | ❌ 효과 없음 | 와튼 Report 3 (2025) |
| "부탁해요"처럼 정중하게 / 반대로 명령조로 | ➖ 전체적으로 차이 없음 | 와튼 Report 1 (2025) |
| "너는 세계 최고의 전문가야" (전문가 역할) | ❌ 정확도 향상 없음, 때로 하락 | 와튼 Report 4 (2025), Zheng et al. (2024) |
| "단계별로 생각해" (추론 모델에) | ❌ 거의 효과 없고 시간만 증가 | 와튼 Report 2 (2025), OpenAI, Microsoft |
| "단계별로 생각해" (일반 모델에) | ⚠️ 평균은 오르지만 쉬운 문제를 틀리기도 | 와튼 Report 2 (2025) |
| 대문자, "절대!!!", "IMPORTANT" 강조 | ❌ 최신 모델에선 과잉 반응 | Anthropic, OpenAI, Google 최신 가이드 |
| "정말 확실해?"로 검증 | ❌ 맞는 답을 뒤집음 | FlipFlop (2023) |
| 프롬프트는 길고 자세할수록 좋다 | ❌ 군더더기는 해로움 | OpenAI 최신 모델 가이드, Anthropic 컨텍스트 엔지니어링 |
| 자료는 많이 넣을수록 좋다 | ❌ 중간 내용을 놓치고 효과는 미미 | Lost in the Middle (2023), Context Rot (2025) |
| 출력 형식 지정은 사소하다 | ❌ **형식 지시는 성능 요소** | 와튼 Report 1 (2025) |
| 한두 번 해 보고 잘 되면 된 것 | ❌ 같은 질문도 매번 다름 | 와튼 Report 1 (2025) |
| AI가 출처를 달면 믿을 만하다 | ❌ 출처 자체를 지어내기도 | Walters & Wilder (2023), Stanford (2025) |
| AI를 쓰면 무조건 빨라진다 | ⚠️ 상황에 따라 더 느리거나 더 틀림 | METR (2025), HBS/BCG (2023) |
| 예시는 많을수록 좋다 | ⚠️ 3~5개 적당, 추론 모델엔 예시 없이 먼저 | Anthropic, Google, OpenAI |
| 모른다고 하면 성능이 나쁜 모델이다 | ❌ 모른다고 하는 모델이 덜 틀림 | OpenAI (2025) |

---

## 1. 보상과 협박: 효과 없음

와튼 생성형 AI 연구소의 **Prompting Science Report 3**("I'll pay you or I'll kill you — but will you care?", 2025)은 1,000달러 팁, 1조 달러 팁, 위협 같은 문구를 체계적으로 실험했습니다.

- 전체적으로 **성능을 믿을 만하게 올리지 못했습니다.**
- 다만 **개별 질문** 단위에서는 정답률이 최대 +36%p, −35%p까지 크게 흔들렸고, 방향은 **예측할 수 없었습니다.**

> 이것이 "팁 주니까 잘 되더라"는 경험담이 계속 나오는 이유입니다. 한두 개 질문에서는 우연히 좋아질 수 있지만, 평균적으로는 효과가 없습니다.

2023년의 "26가지 원칙" 논문은 팁과 벌칙 문구가 효과가 있다고 주장했지만, 이 주장은 이후 와튼 연구로 **반박**되었습니다. 그 논문의 결과는 원칙마다 20개 질문으로 평가한 것이었습니다.

## 2. 정중함: 평균적으로 차이 없음

**Report 1**("Prompt Engineering is Complicated and Contingent", 2025)에서 "부탁드립니다"와 "명령한다"는 **전체적으로 믿을 만한 차이를 만들지 않았습니다.** 개별 질문에서는 차이가 날 수 있습니다.

> 정중하게 쓰는 건 자유지만 **성능 요령은 아닙니다.** 반대로 무례하게 쓴다고 좋아지지도 않습니다.

## 3. 전문가 역할: 정확도를 올리지 않음

**Report 4**("Playing Pretend: Expert Personas Don't Improve Factual Accuracy", 2025)
- 전문가 페르소나는 사실 정확도를 **믿을 만하게 올리지 못했고**, 일부 조건에서는 유의하게 **떨어뜨렸습니다.**
- "유아"처럼 지식이 낮은 페르소나는 성능을 떨어뜨렸습니다.
- 질문과 **맞지 않는 전문가** 역할을 주자 한 Gemini 모델은 질문당 25번 중 평균 약 10.6번 답을 **거부**했습니다.

**Zheng et al.** (EMNLP Findings 2024): 162개 역할, 2,410개 사실 질문으로 실험한 결과 역할 부여가 성능을 높이지 못했고, 최적의 역할을 자동으로 골라도 **무작위 선택과 차이가 없었습니다.**

> **그래도 역할은 쓸모가 있습니다.** 정확도가 아니라 **말투, 관점, 독자 수준**을 맞출 때입니다. → [02. 프롬프트의 6요소](02-prompt-anatomy.md#1-역할-role)

## 4. "단계별로 생각해": 모델에 따라 다름

**Report 2**("The Decreasing Value of Chain of Thought in Prompting", 2025)

| 모델 종류 | 효과 | 부작용 |
|---|---|---|
| 일반(즉답) 모델 | 평균 최대 13.5%p 향상 | 원래 맞히던 쉬운 문제를 틀리기도 |
| 추론 모델 | +3.1%p ~ −3.3%p (거의 없음) | 응답 시간 20~80% 증가 |

OpenAI는 추론 모델에 chain-of-thought 프롬프트를 쓰지 말라고 하고, Microsoft의 프롬프트 기법 문서에는 "이 기법들은 GPT-5, o-시리즈 같은 추론 모델에는 권장하지 않는다"는 배너가 붙어 있습니다.

## 5. 대문자와 강조: 최신 모델에선 역효과

Anthropic, OpenAI, Google의 2026년 가이드는 공통으로, 예전 모델을 위해 넣던 강조(`IMPORTANT`, `반드시`, `절대`)와 "게으름 피우지 마" 같은 문구를 **빼라**고 권합니다. 최신 모델은 이런 지시를 **과하게** 따라서 다른 지시를 무시하거나 과잉 행동을 합니다. 대신 **이유를 한 줄** 설명하세요.

## 6. "정말 확실해?": 검증이 아니라 흔들기

- FlipFlop 실험(2023, 10개 모델): "정말 확실해?" 후 답을 바꾼 비율 평균 **46%**, 정확도 평균 **17% 하락**
- Anthropic 연구(2023): 반박하자 Claude 1.3이 **98%**의 질문에서 (틀리지 않았는데도) 실수를 인정

→ 대신 **근거를 요구**하거나, **새 채팅에서 독립적으로** 다시 풀게 하세요. → [templates/honest-critique.md](../templates/honest-critique.md)

## 7. 길고 자세한 프롬프트가 좋다? 

- **필요한 맥락**은 자세할수록 좋지만, **군더더기**는 해롭습니다.
- OpenAI 최신 가이드: 내부 코딩 에이전트 테스트에서 덜어낸 프롬프트가 약 10~15% 높은 점수를 냈고 토큰은 41~66% 줄었습니다 (방향을 보여 주는 수치).
- Anthropic: 맥락은 한정된 주의력 예산이다. **가장 작은 양의 핵심 정보**를 목표로.
- 지시가 늘어날수록 모두 지킬 확률은 떨어집니다 (ManyIFEval, IFScale).

## 8. 형식 지정은 사소하다? → 오히려 중요

**Report 1**: 출력 형식 지시를 **뺐더니** 정확도가 GPT-4o 8.6%p, GPT-4o-mini 12.1%p 떨어졌습니다. 요령처럼 보이는 것 중 **실제로 효과가 확인된** 몇 안 되는 것입니다.

## 9. 한 번 잘 되면 된 것이다? → 매번 다르다

**Report 1**은 같은 질문을 100번씩 물었습니다. "100번 모두 맞혀야 통과"라는 엄격한 기준에서 GPT-4o는 **무작위 추측보다 약 5%p 높은 수준**(통계적으로 유의하지 않음)이었습니다. 연구진의 결론은 프롬프트 엔지니어링이 **"복잡하고 상황에 따라 다르다"**는 것입니다.

→ 중요한 프롬프트는 **여러 입력, 여러 번** 시험하세요. [08. 검증과 평가](08-verification-and-evals.md)

## 10. 모른다고 하는 모델은 나쁜 모델이다? → 반대

OpenAI가 공개한 비교에서 "모른다"고 52% 답한 모델의 오답률은 26%, 1%만 모른다고 한 모델의 오답률은 **75%**였습니다. 정답률은 비슷했습니다. **모른다고 말하는 것은 기능입니다.** 프롬프트에서도 그 권리를 주세요.

---

## 그러면 무엇이 효과가 있나

와튼 연구진과 공식 가이드들이 공통으로 가리키는 것:

1. **과제를 명확히 정의한다** (무엇을, 왜, 언제 끝나는지)
2. **맥락과 자료를 준다**
3. **출력 형식을 정한다**
4. **예시를 보여 준다** (추론 모델은 예시 없이 먼저)
5. **결과를 검증한다** (여러 번, 바깥 증거로)

MIT Sloan 가이드는 Acar(2023)를 인용해, 장기적으로는 프롬프트 문구를 다듬는 기술보다 **문제를 정의하고 범위와 경계를 정하는 능력**이 더 중요할 수 있다고 말합니다.

---

### 출처

- Meincke, Mollick, Mollick, Shapiro, Prompting Science Report 1 (2025, 프리프린트) — https://arxiv.org/abs/2503.04818
- Meincke et al., Prompting Science Report 2 (2025, 프리프린트) — https://arxiv.org/abs/2506.07142
- Meincke et al., Prompting Science Report 3 (2025, 프리프린트) — https://arxiv.org/abs/2508.00614
- Basil et al., Prompting Science Report 4 (2025, 프리프린트) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5879722 / 해설: https://knowledge.wharton.upenn.edu/article/why-you-shouldnt-ask-chatbots-to-act-like-an-expert/
- Zheng et al., Personas in System Prompts (EMNLP Findings 2024) — https://arxiv.org/abs/2311.10054
- Bsharat et al., "Principled Instructions Are All You Need" (26가지 원칙, 2023, 프리프린트) — https://arxiv.org/abs/2312.16171
- Laban et al., FlipFlop (2023) — https://arxiv.org/abs/2311.08596
- Sharma et al., Towards Understanding Sycophancy (Anthropic, 2023) — https://arxiv.org/abs/2310.13548
- OpenAI, Why language models hallucinate (2025) — https://openai.com/index/why-language-models-hallucinate/
- OpenAI, GPT-5.6 prompt guidance — https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6
- OpenAI, Reasoning best practices — https://developers.openai.com/api/docs/guides/reasoning-best-practices
- Microsoft, Prompt engineering techniques — https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering
- Anthropic, Prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic, Effective context engineering for AI agents — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Liu et al., Lost in the Middle (2023) — https://arxiv.org/abs/2307.03172
- Chroma, Context Rot (2025) — https://research.trychroma.com/context-rot
- Walters & Wilder, 가짜 인용 연구 (*Scientific Reports*, 2023) — https://www.nature.com/articles/s41598-023-41032-5
- METR (2025) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- MIT Sloan, Effective Prompts for AI (Problems over prompts) — https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/
