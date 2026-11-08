# 08. 검증과 평가: "좋아 보인다"를 "좋다"로

> 검증(Verification)은 **답 하나**가 맞는지 확인하는 것이고, 평가(Evaluation, Evals)는 **프롬프트나 워크플로가** 꾸준히 잘 작동하는지 확인하는 것입니다.
> 둘 다 건너뛰기 쉽지만, AI 활용의 품질은 결국 여기서 갈립니다.

---

## Part 1. 답 하나를 검증하기

### 1. 검증의 기본 원칙

| 원칙 | 이유 |
|---|---|
| **AI의 말이 아니라 바깥의 증거로 확인한다** | 같은 모델에게 "맞아?"라고 묻는 것은 검증이 아니다 |
| **"정말 확실해?"는 쓰지 않는다** | 2023년 10개 모델 실험에서 46%가 답을 바꿨고 정확도가 평균 약 17%p 떨어짐 (FlipFlop) |
| **독립적으로 다시 하게 한다** | 앞의 답을 보지 않고 새로 풀어야 편향되지 않음 (Chain-of-Verification) |
| **실행할 수 있는 것은 실행한다** | 코드는 돌리고, 숫자는 재계산하고, 링크는 연다 |
| **검증 강도는 위험도에 비례한다** | 모든 답을 똑같이 검증할 수는 없다 |

> Anthropic도 공식 문서에서 환각 줄이는 기법들이 문제를 **완전히 없애지는 못한다**며, 판단의 무게가 큰 정보는 항상 직접 확인하라고 말합니다.

### 2. 검증 사다리

| 위험도 | 예 | 해야 할 것 |
|---|---|---|
| **낮음** | 아이디어, 초안, 개인 메모 | 훑어보기 + "빠뜨리거나 확신 없는 부분이 뭐야?" |
| **중간** | 사내 문서, 보고서, 코드 리뷰 | + 요구사항 커버리지 표 + 내 자료 기준으로 인용 확인 + **새 채팅**에서 2차 의견 |
| **높음** | 법률·의료·재무, 외부 공개, 배포 코드 | + **모든 출처 열기** + 핵심 주장마다 옆으로 읽기 + 숫자 직접 재계산 + 테스트 실행 + 사실 단위로 쪼개 확인 |

### 3. 검증 도구 상자

**① 옆으로 읽기 (Lateral reading)**
전문 팩트체커들은 한 페이지 안에서 깊이 읽는 대신, **페이지를 벗어나 다른 독립적인 출처가 뭐라고 하는지** 확인합니다. AI 답변도 마찬가지입니다. AI가 준 출처만 보지 말고 **다른 경로로** 같은 사실을 찾아보세요.

**② 사실 단위로 쪼개기 (Atomic facts)**
긴 글은 "OO는 2023년에 설립됐다", "매출은 12% 늘었다"처럼 **한 문장에 사실 하나**로 쪼갠 뒤 하나씩 확인합니다. 연구(FActScore, 2023)에서 쓰는 표준 방법입니다.

```text
위 답변을 확인 가능한 사실 단위로 쪼개서 번호를 붙여줘.
각 사실 옆에 [출처 있음 / 기억에 의존 / 추론]을 표시해줘.
```

**③ 검증 질문 체인 (Chain-of-Verification)**
1. 초안 → 2. 검증 질문 만들기 → 3. **앞 답을 보지 않고** 독립적으로 답하기 → 4. 차이를 반영해 수정

**④ 여러 번, 여러 모델**
새 채팅 2~3개, 또는 다른 회사 모델에 같은 질문. **답이 다른 부분**이 가장 의심스러운 곳입니다. (같다고 증명되는 것은 아님)

**⑤ 스스로 비판하게 (Red team)**
작성한 채팅과 **다른 채팅**에서 "이 답변의 문제점을 찾아줘"라고 요청합니다. 확인이 아니라 **문제 찾기**를 시키세요.

**⑥ 실행**
- 코드: 실행하고 테스트를 돌린다
- 숫자: 엑셀이나 코드로 재계산
- 링크: 직접 클릭
- 인용: 원문에서 Ctrl+F

---

## Part 2. 프롬프트와 워크플로를 평가하기 (Evals)

자주 쓰는 프롬프트, 팀이 함께 쓰는 템플릿, 직접 만든 에이전트라면 **평가셋**을 만들어 두세요. 그래야 프롬프트를 고쳤을 때 **정말 나아졌는지** 알 수 있습니다.

### 1. 먼저 할 것: 성공 기준

Anthropic은 프롬프트를 다듬기 **전에** 세 가지가 있어야 한다고 말합니다.

1. **성공 기준**의 명확한 정의
2. 그 기준으로 **시험해 볼 방법**
3. 첫 번째 **초안 프롬프트**

없으면 그것부터 만드세요.

### 2. 가장 가벼운 평가 루프

```
1. 실제 사례 20개 모으기        특히 AI가 실패했던 사례 위주로 (Anthropic 권장 20~50개)
2. 결과를 직접 읽기             실패마다 짧은 메모 → 비슷한 것끼리 묶기 → 개수 세기
3. 통과/실패 기준 만들기         5점 척도 대신 통과/실패 (Hamel Husain 권장)
4. 프롬프트 수정 → 전체 다시 실행  하나를 고치면 다른 게 깨질 수 있음
5. 통과한 사례는 회귀 테스트로    다음 수정 때도 계속 확인
```

### 3. 실무자들의 핵심 조언

**Hamel Husain & Shreya Shankar (평가 FAQ)**
- **오류 분석이 먼저다.** 실제 결과물(trace)을 읽고, 실패 유형을 분류하고, 개수를 센다. 이것이 평가에서 **가장 중요한 활동**이다.
- **통과/실패로만 채점한다.** 5점 척도보다 결정이 분명해지고 일관성이 높아진다.
- 약 100개를 검토하되, 처음 30개 이상은 **직접** 주석을 단다. 새로운 실패 유형이 더 이상 안 나오면 멈춘다.
- ROUGE나 BERTScore 같은 범용 지표는 대부분의 LLM 앱에 맞지 않는다.

**Anthropic ("Demystifying evals for AI agents", 2026-01)**
- **과정이 아니라 결과를 채점한다.** "예약했습니다"라고 말했는지가 아니라 실제로 예약이 DB에 있는지.
- **능력 평가**(처음엔 통과율 낮음, 오를 언덕)와 **회귀 평가**(거의 100% 유지)를 구분한다. 능력 평가를 통과한 과제는 회귀 평가로 "졸업"시킨다.
- **pass@k vs pass^k:** k번 중 **한 번이라도** 성공할 확률과 k번 **모두** 성공할 확률은 다르다. 한 번 성공률이 75%면 3번 모두 성공할 확률은 약 42%다. 매번 믿을 수 있어야 하는 일이라면 pass^k를 봐야 한다.
- **기록(transcript)을 읽어라.**

### 4. AI에게 채점을 맡길 때 (LLM-as-judge)

- 판단이 필요한 기준에만 쓰고, 코드로 확인할 수 있는 것은 코드로 확인한다.
- **사람이 채점한 결과와 비교해서** 판정 AI가 믿을 만한지 먼저 확인한다 (참 양성률·참 음성률).
- 실패 유형마다 판정 프롬프트를 따로 만든다.
- 기준표(rubric) 예: 사실 정확도, 인용 정확도, 완결성, 출처 품질 (Anthropic 리서치 시스템이 쓴 기준).

```text
너는 채점자야. 아래 기준 하나만 보고 통과/실패를 판정해.
기준: 답변의 모든 숫자가 <source> 문서에 실제로 있는가?
출력: {"pass": true/false, "reason": "실패라면 어떤 숫자가 문서에 없는지"}
```

### 5. 같은 질문도 매번 다르다

와튼 Prompting Science Report 1(2025)은 같은 질문을 100번씩 물었습니다. "100번 모두 맞혀야 통과"라는 엄격한 기준을 적용하자, GPT-4o의 성적은 **무작위로 찍는 것보다 약 5%p 높은 수준**에 그쳤습니다(통계적으로 유의하지 않음). 한두 번 해 보고 "잘 되네"라고 판단하면 안 되는 이유입니다.

---

### 출처

- Laban et al., FlipFlop "Are You Sure?" (2023) — https://arxiv.org/abs/2311.08596
- Dhuliawala et al., Chain-of-Verification (2023) — https://arxiv.org/abs/2309.11495
- Min et al., FActScore (2023) — https://arxiv.org/abs/2305.14251
- Civic Online Reasoning, Teaching Lateral Reading — https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/
- Anthropic, Reduce hallucinations — https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Anthropic, Prompt engineering overview (성공 기준 먼저) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Anthropic, Demystifying evals for AI agents (2026-01-09) — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Anthropic, How we built our multi-agent research system (채점 기준표) — https://www.anthropic.com/engineering/multi-agent-research-system
- Hamel Husain & Shreya Shankar, LLM Evals FAQ — https://hamel.dev/blog/posts/evals-faq/
- OpenAI, Prompt optimizer (좁게 정의된 채점자) — https://developers.openai.com/api/docs/guides/prompt-optimizer
- Simon Willison, "Here's how I use LLMs to help me write code" (테스트는 사용자의 몫) — https://simonwillison.net/2025/Mar/11/using-llms-for-code/
- Meincke et al., Prompting Science Report 1 (Wharton, 2025, 프리프린트) — https://arxiv.org/abs/2503.04818
