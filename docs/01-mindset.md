# 01. 마음가짐: AI를 어떻게 대할 것인가

> 프롬프트 기술보다 먼저 정해야 할 것은 **AI를 어떤 존재로 대할지**입니다.
> 이 관점이 정해지면 좋은 프롬프트의 대부분은 저절로 따라옵니다.

---

## 1. AI는 "유능하지만 맥락이 전혀 없는 신입"이다

세 회사의 공식 가이드와 Karpathy가 같은 비유를 씁니다.

| 출처 | 비유 | 의미 |
|---|---|---|
| Anthropic | 맥락이 전혀 없는 뛰어난 신입 직원 | 내 상황, 목적, 기준을 **말해 주지 않으면 모른다** |
| OpenAI (추론 모델 가이드) | 노련한 선배 동료 | 목표를 주면 **방법은 알아서** 찾는다. 단계를 일일이 지시할 필요가 없다 |
| Andrej Karpathy | 유능하지만 실수가 잦은 인턴 | 결과물은 **반드시 검토**해야 한다 |

이 세 비유를 합치면 이렇게 됩니다.

> **목표와 맥락은 자세히 주고, 방법은 맡기고, 결과는 확인한다.**

---

## 2. AI의 능력은 들쭉날쭉하다 (Jagged Frontier)

하버드 경영대학원과 BCG가 컨설턴트 758명을 대상으로 한 실험(Dell'Acqua et al., 2023, GPT-4 기준)은 AI 능력의 경계가 **매끈한 선이 아니라 들쭉날쭉한 톱니 모양**이라는 것을 보여 주었습니다.

- **AI가 잘하는 과제**에서는 AI를 쓴 그룹이 과제를 12.2% 더 많이, 25.1% 더 빨리, 약 40% 더 높은 품질로 끝냈습니다.
- **AI의 능력 밖 과제**에서는 AI를 쓴 그룹이 정답을 맞힐 확률이 **19%p 낮았습니다.** AI의 그럴듯한 오답을 그대로 믿었기 때문입니다.
- 연구진은 이를 **"운전대에서 잠드는(falling asleep at the wheel)"** 현상이라고 불렀습니다.

어려워 보이는 일은 잘하는데 쉬워 보이는 일에서 틀리기도 합니다. 그래서 **"이 정도는 맞겠지"라는 감으로 판단하면 안 됩니다.** 직접 써 보면서 내 업무에서 AI가 어디까지 믿을 만한지 경계를 익혀야 합니다.

연구진은 AI를 잘 쓰는 사람을 두 유형으로 나눴습니다.

- **켄타우로스(Centaur):** 일을 나눠서, AI가 잘하는 부분만 맡긴다.
- **사이보그(Cyborg):** 작업 전체에서 AI와 계속 주고받으며 함께 한다.

둘 다 결과는 좋았습니다. 공통점은 **어디서 AI를 믿고 어디서 의심할지 알고 있었다**는 것입니다.

---

## 3. 책임은 사람에게 있다

- 미국에서는 변호사가 ChatGPT가 지어낸 판례를 법원에 냈다가 5,000달러 제재를 받았습니다(Mata v. Avianca, 2023). 법원은 AI를 쓴 것이 아니라 **확인하지 않은 것**을 문제 삼았습니다.
- MIT Sloan의 AI 가이드는 인용과 출처 확인을 **타협할 수 없는 것(non-negotiable)**이라고 표현합니다.
- 카네기멜런대와 마이크로소프트의 지식노동자 319명 조사(CHI 2025)에서는 **AI를 더 신뢰할수록 비판적 사고를 덜 하고**, 자기 능력에 자신감이 있을수록 비판적 사고를 더 하는 경향이 나타났습니다.

> AI가 만든 결과물을 내 이름으로 내보내는 순간, 그것은 **내 결과물**입니다.

---

## 4. 생각은 맡겨도 이해는 맡길 수 없다

Karpathy는 2026년 글에서 이렇게 정리했습니다. 생각은 외주할 수 있어도 **이해는 외주할 수 없다.**

- 와튼(펜실베이니아대) 연구진이 튀르키예 고등학생 약 1,000명을 대상으로 한 실험(Bastani et al., *PNAS*, 2025)에서, 답을 바로 주는 AI로 공부한 학생들은 연습 점수가 크게 올랐지만 **AI 없이 본 시험에서는 17% 낮았습니다.** 반면 힌트만 주는 튜터형 AI는 시험 점수를 떨어뜨리지 않았습니다.
- 즉, 문제는 AI를 쓰느냐가 아니라 **어떻게 쓰느냐**입니다. → [예제 6: AI로 공부하기](../examples/06-learning-with-ai.md)

**실천법:** 중요한 일은 **내가 먼저 생각하거나 초안을 쓴 다음** AI에게 보여 주세요. 순서를 바꾸면 AI의 답이 내 생각의 틀이 되어 버립니다.

---

## 5. 자율성은 슬라이더처럼 조절한다

Karpathy는 2025년 YC 강연에서 AI를 **"로봇이 아니라 아이언맨 슈트"**처럼 쓰자고 말했습니다. 완전 자동화보다, 사람이 통제권을 쥔 채 AI가 능력을 키워 주는 방식입니다. 그는 이를 **자율성 슬라이더(autonomy slider)**라고 불렀습니다.

| 단계 | AI의 역할 | 사람의 역할 | 예 |
|---|---|---|---|
| 1 | 질문에 답한다 | 모든 것을 판단 | 개념 설명, 아이디어 |
| 2 | 초안을 만든다 | 고쳐서 쓴다 | 메일, 보고서 초안 |
| 3 | 작업을 수행한다 | 단계마다 승인 | 코딩 에이전트 (계획 승인 → 구현) |
| 4 | 여러 작업을 알아서 한다 | 결과만 검토 | 테스트가 잘 갖춰진 반복 작업 |

**처음에는 낮은 단계에서 시작하고, 결과를 확인할 수단(테스트, 체크리스트, 원문 대조)이 생길 때마다 한 단계씩 올리세요.**

---

## 6. 이럴 때는 AI를 쓰지 않거나 조심해서 쓴다

| 상황 | 이유 |
|---|---|
| 결과를 **검증할 방법이 없는데** 틀리면 피해가 큰 일 | 들쭉날쭉한 경계 밖일 수 있다 |
| 지금 **배우고 있는 핵심 기술** | 이해를 외주하게 된다 |
| 회사가 허용하지 않은 도구에 **기밀이나 개인정보**를 넣는 일 | [09. 보안과 개인정보](09-security-privacy.md) |
| 내가 직접 하는 게 더 빠른 짧은 일 | 설명하는 시간이 더 든다 |

> "AI를 쓰면 무조건 빨라진다"도 사실이 아닙니다. 비영리 연구기관 METR의 2025년 실험에서, 숙련 개발자들은 AI를 쓰면 20% 빨라질 거라고 **느꼈지만** 실제로는 19% **느려졌습니다.** METR 스스로 이 결과는 2025년 초 도구 기준이라 지금은 달라졌을 수 있다고 밝혔습니다. 그래도 교훈은 남습니다. **체감 속도와 실제 속도는 다를 수 있습니다.**

---

## 핵심 정리

1. 목표와 맥락은 자세히, 방법은 맡기고, 결과는 확인한다.
2. AI의 능력은 들쭉날쭉하다. 감으로 믿지 말고 내 업무에서 직접 경계를 익힌다.
3. 결과에 대한 책임은 사람에게 있다.
4. 중요한 일은 내가 먼저 생각하고 AI를 부른다.
5. 자율성은 검증 수단이 생기는 만큼만 올린다.

---

### 출처

- Anthropic, Prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- OpenAI, Reasoning best practices — https://developers.openai.com/api/docs/guides/reasoning-best-practices
- Karpathy, Sequoia Ascent 2026 요약 (2026-04-30) — https://karpathy.bearblog.dev/sequoia-ascent-2026/
- Karpathy, "Software Is Changing (Again)" YC AI Startup School (2025-06-18) — https://www.youtube.com/watch?v=LCEmiRjPEtQ (강연 요약: https://ikyle.me/blog/2025/andrej-karpathy-software-is-changing-again)
- Dell'Acqua et al., "Navigating the Jagged Technological Frontier" (HBS Working Paper, 2023) — 공저자 Ethan Mollick의 해설: https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged
- Mata v. Avianca 제재 결정 (2023-06-22) — https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54
- MIT Sloan Teaching & Learning Technologies, "Addressing AI Hallucinations and Bias" — https://mitsloanedtech.mit.edu/ai/basics/addressing-ai-hallucinations-and-bias/
- Lee et al., "The Impact of Generative AI on Critical Thinking" (CHI 2025) — https://advait.org/files/lee_2025_ai_critical_thinking_survey.pdf
- Bastani et al., "Generative AI without guardrails can harm learning" (*PNAS*, 2025) — https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/
- METR, Early-2025 AI 숙련 개발자 연구 (2025-07-10) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
