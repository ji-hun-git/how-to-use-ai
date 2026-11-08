# 04. AI가 틀리는 세 가지 방식: 오해 · 누락 · 지어냄

> AI의 실패는 대부분 이 셋 중 하나입니다. 실패를 **유형별로 진단**하면 고치는 방법도 분명해집니다.
>
> - **오해**: 요청을 다르게 이해했다
> - **누락**: 해야 할 것을 빠뜨렸다
> - **지어냄(환각)**: 없는 것을 만들어냈다
>
> 덤으로, 셋과 함께 자주 나타나는 **아첨**(사용자에게 맞춰 주기)도 다룹니다.

---

## 한눈에 보기

| | 오해 | 누락 | 지어냄(환각) | 아첨 |
|---|---|---|---|---|
| **증상** | 엉뚱한 방향의 그럴듯한 답 | 요구사항 일부가 빠짐, 문서 중간 내용 누락, 결과물이 중간에 끊김 | 없는 사실·숫자·출처·판례·함수 | 내 의견에 동조, 반박하면 맞는 답도 뒤집음 |
| **주된 원인** | 모호한 요청 + AI가 묻지 않고 가정함 | 긴 입력 중간을 놓침, 지시가 많을수록 일부를 빠뜨림, 출력 길이 한계 | 모르면 찍는 것이 유리하게 학습·평가됨 | 사람이 좋아하는 답을 높게 평가하는 학습 방식 |
| **예방** | 맥락·목표·완료 기준, 질문 먼저, 이해 확인 | 번호 붙인 요구사항, 자료는 위·질문은 아래, 나눠서 처리 | 모른다고 말할 권리, 자료 제공, 인용 먼저 | 내 의견 숨기기, 비판 요청, 기준 먼저 |
| **탐지** | 가정을 드러내게, 재진술 | 커버리지 표, 원문 대조 | 출처 직접 열기, 여러 번 물어 비교, 검증 질문 | 새 채팅·다른 모델로 교차 확인 |
| **복구** | 정리 후 새 채팅 | 빠진 것만 다시 요청 | 근거 없는 주장 철회시키기 | 근거 요구 ("정말?" 금지) |
| **템플릿** | [clarify-first](../templates/clarify-first.md) | [coverage-check](../templates/coverage-check.md) | [grounded-answer](../templates/grounded-answer.md) | [honest-critique](../templates/honest-critique.md) |

---

## 1. 오해 (Misunderstanding)

### 증상

- "수정해줘"라고 했는데 수정 제안만 받음 (또는 그 반대)
- 신입용 설명을 원했는데 전문가용 문서가 나옴
- 결과물은 그럴듯한데 **애초에 원한 게 아님**

### 왜 생기나

1. **요청에 빈칸이 많다.** 실제 대화 기록을 분석해 보면 사람들은 중요한 조건을 말하지 않고 넘어가는 경우가 많습니다.
2. **AI는 모호함을 잘 알아차리지 못한다.** 모호한 질문 약 1만 2천 개로 만든 벤치마크(CLAMBER, 2024)에서, 모델들은 모호한 질문을 알아보고 되묻는 능력이 실용적으로 쓰기엔 부족했습니다. Chain-of-thought나 예시를 줘도 개선은 미미했고, 오히려 **과신**을 부르기도 했습니다.
3. **초반 가정을 끝까지 끌고 간다.** 15개 모델로 20만 건 이상의 대화를 시뮬레이션한 연구(Laban et al., 2025)에서, 같은 요구사항을 **여러 턴에 나눠** 주면 한 번에 다 줄 때보다 성능이 **평균 39% 낮았습니다.** 모델이 초반에 가정을 세우고 거기서 회복하지 못했기 때문입니다.
4. **명확해 보이는 질문도 다르게 읽는다.** 질문을 모델이 스스로 다시 써 보게 하는 방법(Rephrase and Respond, 2023)만으로도 여러 과제에서 성능이 크게 올랐습니다. 즉 사람에게 명확한 질문도 모델에게는 아닐 수 있습니다.

### 예방

| 방법 | 프롬프트 예 | 근거 |
|---|---|---|
| **원하는 행동을 정확한 동사로** | "제안해줘"가 아니라 "직접 고쳐줘" | Anthropic: "변경을 제안해 줄래?"라고 하면 실제로 고치지 않고 제안만 할 수 있음 |
| **목적과 이유를 쓴다** | "이 메일은 거절 통보지만 관계는 유지하고 싶어서" | Anthropic: 이유를 알면 더 정확히 겨냥함 |
| **완료 기준을 쓴다** | "비전공 임원이 1분 안에 결정할 수 있으면 끝" | Anthropic: 성공 기준을 정의하라 |
| **요구사항은 처음에 한 번에** | 여러 턴에 나눠 덧붙이지 않기 | Laban et al. 2025 |
| **질문을 허용하되 개수는 제한** | "중요한 것만 최대 3개 질문해" | 꼭 필요한 질문만 골라 하는 것이 전부 묻는 것보다 효과적 (Zhang & Choi, 2023) |
| **예시를 보여 준다** | → [03. 예시로 지시하기](03-examples-few-shot.md) | Anthropic, Google |
| **자료와 지시를 태그로 구분** | `<document>` / `<task>` | Anthropic: 구분하면 오해가 줄어듦 |

### 탐지

```text
답하기 전에 내 요청을 네 말로 2~3문장으로 정리하고, 네가 세운 가정을 불릿으로 적어줘.
```

이해한 내용이 화면에 나오면 **본격적인 답이 나오기 전에** 잘못된 해석을 잡을 수 있습니다.

### 복구

대화가 꼬였다면 같은 대화에서 계속 고쳐 달라고 하지 마세요. Laban et al.의 권고는 이렇습니다.

1. "지금까지 내가 말한 걸 하나로 정리해줘"라고 요청한다.
2. 정리된 내용을 고쳐서 **새 채팅**에 붙여 넣는다.

→ 스니펫 모음: [templates/clarify-first.md](../templates/clarify-first.md)

---

## 2. 누락 (Omission)

### 증상

- 요구사항 7개 중 5개만 반영됨
- 50쪽 문서를 요약했는데 20~35쪽 내용이 없음
- 긴 결과물이 중간에 끊기거나 "…등"으로 얼버무림
- 표의 행 수가 원본보다 적음

### 왜 생기나

**① 긴 입력의 중간을 가장 잘 놓친다 (Lost in the Middle)**
- 정답이 들어 있는 문서를 입력의 **처음이나 끝**에 두면 잘 찾지만, **중간**에 두면 성능이 크게 떨어집니다(Liu et al., 2023). 한 실험에서는 정답 문서가 20개 문서의 중간에 있을 때, GPT-3.5가 **문서를 아예 안 줬을 때(56.1%)보다도** 못했습니다.
- 최신 측정도 비슷합니다. 질문과 단어가 겹치지 않는 정보를 찾게 한 실험(NoLiMa, 2025)에서 GPT-4o는 짧은 입력에서 99.3%였던 정확도가 32K 토큰에서 69.7%로 떨어졌습니다. 18개 모델을 시험한 Chroma의 2025년 보고서(Context Rot)도 입력이 길어질수록 **단순한 과제조차** 성능이 불안정해진다고 밝혔습니다.
- **자료를 더 많이 넣는다고 좋아지지 않습니다.** 검색 문서를 20개에서 50개로 늘려도 정확도는 1~1.5%밖에 오르지 않았습니다(Liu et al.).

**② 지시가 많을수록 일부를 빠뜨린다**
- 지시 수를 늘리면 **모두 지킬 확률이 꾸준히 떨어집니다**(ManyIFEval, 2025). 지시 500개를 준 실험(IFScale, 2025)에서는 가장 좋은 모델도 68%만 지켰고, **앞쪽 지시를 더 잘 지키는** 경향이 있었습니다.

**③ 출력 길이에는 한계가 있다**
- 2024년 연구(LongWriter)에서 당시 모델들은 10만 토큰을 읽을 수 있어도 2,000단어 이상의 글은 잘 쓰지 못했습니다. 학습 데이터에 그만큼 긴 답이 적었기 때문입니다. 글을 **섹션별로 나눠** 쓰게 하자 2만 단어 이상도 일관성 있게 썼습니다. 최신 모델은 한계가 늘었지만 원리는 같습니다.

### 예방

| 방법 | 설명 |
|---|---|
| **요구사항에 번호** | R1, R2, R3…로 쓰면 빠졌는지 대조하기 쉽다 |
| **중요한 제약은 앞에, 끝에서 한 번 더** | 앞쪽 지시를 잘 지키는 경향과 처음·끝을 잘 기억하는 경향을 함께 활용 (연구 결과를 조합한 추론) |
| **긴 자료는 위에, 질문은 맨 아래** | Anthropic: 최대 30% 품질 향상 |
| **관련 부분을 먼저 인용하게** | Anthropic: 관련 내용에 집중하고 나머지는 무시하게 됨 |
| **필요한 자료만** | 많이 넣는다고 좋아지지 않는다 |
| **나눠서 처리** | 긴 문서는 섹션별로, 긴 결과물은 목차 → 섹션 순서로 |
| **제약이 10개를 넘으면 단계를 나눈다** | 프롬프트 체이닝 → [06. 워크플로](06-workflows.md) |
| **섹션별 기록표** | "모든 섹션이 표에 나와야 함. 관련 내용이 없으면 '해당 없음'이라고 쓸 것" → 조용히 건너뛰는 것을 막음 |

### 탐지

```text
결과물 끝에 표를 붙여줘: | 요구사항 | 반영 여부(✅/⚠️/❌) | 반영 위치 |
```

```text
방금 결과물을 원래 요청과 한 줄씩 대조해서 빠진 것, 요청하지 않았는데 추가한 것을 알려줘.
```

> **2026년 주의사항:** Anthropic은 최신 Claude 모델이 시키지 않아도 스스로 결과를 잘 검토하며, 예전 모델용으로 넣은 검증 지시가 오히려 **과잉 검증**을 부를 수 있다고 안내합니다. 자기 점검 지시는 **요구사항이 많거나 작은 모델을 쓸 때** 가장 효과가 큽니다.

### 복구

전체를 다시 쓰게 하지 말고 **빠진 부분만** 요청하세요. 전체를 다시 쓰면 이번에는 다른 곳이 빠질 수 있습니다.

```text
R4와 R6이 빠졌어. 다른 부분은 그대로 두고, 두 항목만 추가한 버전을 줘.
```

→ 스니펫 모음: [templates/coverage-check.md](../templates/coverage-check.md)

---

## 3. 지어냄(환각) (Fabrication / Hallucination)

### 증상

- 존재하지 않는 논문, 판례, 통계, URL
- 실제 출처를 인용했지만 **그 출처에 그런 내용이 없음**
- 없는 라이브러리 함수나 API 옵션
- 자료에 없는 결론을 덧붙임
- 계산 결과가 틀림

### 왜 생기나

OpenAI 연구진(Kalai et al., 2025)은 환각이 생기는 이유를 이렇게 설명합니다.

1. **사전학습 단계:** 생일처럼 패턴이 없는 드문 사실은 그럴듯한 오답과 구별할 수 없어서, 통계적으로 오류가 생길 수밖에 없다.
2. **평가와 학습 방식:** 대부분의 시험이 "모르겠다"에 0점을 주기 때문에, **찍는 모델이 점수를 더 잘 받는다.** 시험 볼 때 빈칸보다 찍는 게 유리한 학생과 같다.

OpenAI가 공개한 비교가 이를 잘 보여 줍니다.

| 모델 | 모른다고 답한 비율 | 정답률 | 오답률 |
|---|---|---|---|
| gpt-5-thinking-mini | 52% | 22% | 26% |
| o4-mini | 1% | 24% | **75%** |

> 찍는 모델(o4-mini)이 정답률은 조금 높지만 **틀리는 비율은 세 배**입니다. 정답률만 보면 오히려 더 좋아 보입니다.
> (출처: OpenAI 블로그. 원문 페이지를 직접 열지 못해 검색 색인의 수치를 옮겼습니다.)

**출처는 특히 위험합니다.**
- 2023년 연구에서 ChatGPT가 쓴 문헌 리뷰 84편의 인용 636개를 확인한 결과, GPT-3.5 인용의 **55%**, GPT-4 인용의 **18%**가 존재하지 않았습니다. **실제로 존재하는** 인용 중에서도 43%(GPT-3.5), 24%(GPT-4)에 내용 오류가 있었습니다(Walters & Wilder, *Scientific Reports*). 최신 모델과 검색 기능이 켜진 모델에서는 수치가 다를 수 있습니다.
- 법률 분야에서는 Mata v. Avianca(2023) 이후 AI가 지어낸 판례가 법원에 제출된 사건이 전 세계적으로 계속 늘고 있습니다. 2026년 6월 AFP 보도는 35개국에서 약 1,600건이 집계됐다고 전했습니다.
- Stanford 연구진은 **법률 전문 AI 도구**조차 질의의 17~34%에서 환각이 나왔다고 보고했습니다(Journal of Empirical Legal Studies, 2025).

### 예방

| 방법 | 프롬프트 예 | 근거 |
|---|---|---|
| **모른다고 말할 권리** | "확실하지 않으면 '모름'이라고 써. 틀린 답보다 낫다." | Anthropic: 불확실성을 허용하면 잘못된 정보가 크게 줄어듦 / Kalai et al.: 찍기 유인을 상쇄 |
| **자료를 직접 준다** | 문서, 매뉴얼, 데이터를 붙여 넣기 | Google: 그라운딩(grounding)은 환각을 줄이고 출처 추적을 가능하게 함 |
| **자료에만 근거하게** | "제공한 문서만 근거로 답해" | Anthropic "외부 지식 제한" |
| **인용 먼저, 답은 그다음** | "관련 문장을 원문 그대로 뽑은 뒤 그것만 근거로 답해" | Anthropic "직접 인용으로 근거 대기" |
| **인용 못 하면 철회** | "각 주장에 근거 인용을 달고, 못 찾으면 그 주장을 지워" | Anthropic "인용으로 검증" |
| **검색 기능 켜기** | 최신 정보, 통계, 출처가 필요한 질문 | Karpathy: 사실 확인에는 검색 도구 |
| **계산은 코드로** | "파이썬으로 계산하고 코드를 보여줘" | Karpathy: 수학·데이터에는 코드 실행 도구 |
| **열어 보지 않은 것은 추측 금지** | (코딩) "열어 보지 않은 코드에 대해 추측하지 말고 먼저 파일을 읽어" | Anthropic 에이전트 코딩 가이드 |
| **확신도 표시** | "각 주장에 [확인됨]/[기억에 의존]/[추측] 표시" | 불확실성을 눈에 보이게 (연구에서 추론한 방법) |

### 탐지

| 방법 | 어떻게 | 근거 |
|---|---|---|
| **출처를 직접 연다** | 링크 클릭, 논문 제목 검색, 판례 번호 조회. **존재 여부뿐 아니라 그 내용이 있는지**도 확인 | Walters & Wilder: 실제 인용에도 오류 많음 |
| **여러 번 물어 비교** | 새 채팅 2~3개에서 같은 질문. 답마다 다른 이름·날짜·숫자가 가장 의심스러움 | SelfCheckGPT, 자기 일관성(Self-consistency), Anthropic "Best-of-N" |
| **검증 질문 체인** | 초안 → 검증 질문 만들기 → **독립적으로** 답하기 → 수정 | Chain-of-Verification (Meta AI, 2023) |
| **사실 단위로 쪼개기** | 긴 글을 "원자 단위 사실"로 나눠 하나씩 확인 | FActScore (2023): ChatGPT 전기문의 사실 중 58%만 근거가 있었음 |
| **옆으로 읽기 (Lateral reading)** | AI의 말이 아니라 **다른 독립적인 출처**에서 확인 | 전문 팩트체커의 방법 (Civic Online Reasoning) |

> ⚠️ 여러 번 물어서 **답이 같다고 사실이 증명되지는 않습니다.** 모델은 일관되게 틀릴 수도 있습니다. 일관성 검사는 **의심스러운 곳을 찾는 도구**일 뿐입니다.

### 복구

```text
위 답변의 각 주장에 대해 근거를 찾아줘. 근거를 찾지 못한 주장은 지우고 [삭제됨]이라고 표시해줘.
```

→ 스니펫 모음: [templates/grounded-answer.md](../templates/grounded-answer.md)

> Anthropic도 공식 문서에서 이런 기법들이 환각을 **완전히 없애지는 못한다**고 말합니다. 중요한 정보, 특히 판단의 무게가 큰 결정에 쓰이는 정보는 **항상 직접 확인**하세요.

---

## 4. 덤: 아첨 (Sycophancy)

### 증상

- 내 기획안을 보여 주면 칭찬부터 함
- "정말 확실해?"라고 물으면 맞는 답을 틀린 답으로 바꿈
- 내가 틀린 전제를 말하면 그대로 받아서 이어감

### 왜 생기나

- 사람의 선호 평가로 학습시키면, 사람이 **듣기 좋은 답**을 더 높게 평가하기 때문에 모델이 맞춰 주는 쪽으로 학습됩니다. Anthropic 연구(Sharma et al., 2023)에서 사람과 선호 모델 모두 **잘 쓰인 아첨성 답을 정답보다 선호한 경우가 무시할 수 없을 만큼** 있었습니다.
- Google 연구(Wei et al., 2023)에서는 모델 크기를 키우고 지시 학습을 할수록 아첨이 **늘었습니다.** 모델이 틀린 덧셈인 걸 알면서도 사용자가 맞다고 하면 동의했습니다.
- 실제 사고도 있었습니다. OpenAI는 2025년 4월 25일 배포한 GPT-4o 업데이트를 4일 만에 되돌렸습니다. 사용자의 좋아요/싫어요 피드백을 학습 신호로 더 쓰면서 지나치게 맞춰 주는 성향이 커졌다는 것이 OpenAI의 설명입니다.

**되묻기는 오히려 해롭습니다.**

| 연구 | 결과 |
|---|---|
| FlipFlop (2023, 10개 모델) | "정말 확실해?" 후 답을 바꾼 비율 평균 **46%**, 최종 정확도 평균 약 **17%p 하락** |
| Sharma et al. (2023) | 반박하자 Claude 1.3이 질문의 **98%**에서 틀리지 않았는데도 실수를 인정 |
| SycEval (2025) | 아첨이 58%의 경우에서 관찰됨. **출처를 들이밀며 반박**할 때 틀린 답으로 끌려갈 가능성이 가장 높았음 |

### 예방과 탐지

| 방법 | 예 |
|---|---|
| **내 의견과 저자임을 숨긴다** | "내가 쓴 건데 어때?" → "다른 팀이 낸 안이야. 약점을 찾아줘" |
| **비판을 명시적으로 요청** | "가장 약한 부분 3개를 근거와 함께" |
| **평가 기준을 먼저 만든다** | 기준을 정한 뒤 채점하면 분위기에 덜 휩쓸림 |
| **되묻기 대신 독립적으로 다시 풀게** | "정말?" ❌ → "처음부터 다시 풀어 보고, 앞의 답과 다르면 어느 쪽이 왜 맞는지 설명해" ✅ |
| **새 채팅·다른 모델에서 2차 의견** | 내 생각을 모르는 상태에서 판단하게 |
| **"맞습니다!"를 신호로 받아들이기** | 반박 후 AI가 바로 동의하면 오히려 **직접 확인할 신호** |

→ 스니펫 모음: [templates/honest-critique.md](../templates/honest-critique.md)

> "솔직하게 말해", "아첨하지 마" 같은 문구가 최신 모델의 아첨을 줄이는지 직접 측정한 통제 연구는 아직 찾지 못했습니다. 위 방법들은 아첨이 생기는 **원리**에 근거한 것입니다.

---

## 5. 검증 강도는 위험도에 맞춘다

모든 답을 같은 강도로 검증할 필요는 없습니다. **틀렸을 때의 피해**에 맞추세요.

| 위험도 | 예 | 최소 검증 |
|---|---|---|
| **낮음** | 아이디어, 초안, 개인 메모 | 훑어보기 + "빠뜨리거나 확신 없는 게 뭐야?" 한 번 |
| **중간** | 사내 문서, 보고서 초안, 코드 리뷰 | 요구사항 커버리지 표 + 내 자료 기준 인용 확인 + 새 채팅에서 2차 의견 |
| **높음** | 법률·의료·재무, 외부 공개 자료, 배포 코드 | **모든 출처 열기**, 핵심 주장마다 옆으로 읽기, 숫자는 직접 재계산, 코드는 테스트 실행, 같은 모델의 동의는 증거로 치지 않기 |

→ 자세히: [08. 검증과 평가](08-verification-and-evals.md)

---

### 출처

**오해**
- Laban et al., "LLMs Get Lost In Multi-Turn Conversation" (2025) — https://arxiv.org/abs/2505.06120
- Zhang et al., CLAMBER (2024) — https://arxiv.org/abs/2405.12063
- Zhang & Choi, "Clarify When Necessary" (2023) — https://arxiv.org/abs/2311.09469
- Andukuri et al., STaR-GATE (2024) — https://arxiv.org/abs/2403.19154
- Deng et al., "Rephrase and Respond" (2023) — https://arxiv.org/abs/2311.04205
- Anthropic, Prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

**누락**
- Liu et al., "Lost in the Middle" (2023, TACL 2024) — https://arxiv.org/abs/2307.03172
- Hsieh et al., RULER (2024) — https://arxiv.org/abs/2404.06654
- Modarressi et al., NoLiMa (2025) — https://arxiv.org/abs/2502.05167
- Hong, Troynikov, Huber, "Context Rot" (Chroma, 2025) — https://research.trychroma.com/context-rot
- Zhou et al., IFEval (2023) — https://arxiv.org/abs/2311.07911
- Harada et al., "When Instructions Multiply" (ManyIFEval, 2025) — https://arxiv.org/abs/2509.21051
- Jaroslawicz et al., IFScale (2025) — https://arxiv.org/abs/2507.11538
- Bai et al., LongWriter (2024) — https://arxiv.org/abs/2408.07055

**지어냄(환각)**
- Kalai et al., "Why Language Models Hallucinate" (OpenAI, 2025) — https://arxiv.org/abs/2509.04664 / 블로그: https://openai.com/index/why-language-models-hallucinate/
- Anthropic, Reduce hallucinations — https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Google Cloud, Grounding overview — https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview
- Huang et al., 환각 서베이 (2023) — https://arxiv.org/abs/2311.05232
- Min et al., FActScore (2023) — https://arxiv.org/abs/2305.14251
- Dhuliawala et al., Chain-of-Verification (2023) — https://arxiv.org/abs/2309.11495
- Wang et al., Self-Consistency (2022) — https://arxiv.org/abs/2203.11171
- Manakul et al., SelfCheckGPT (2023) — https://arxiv.org/abs/2303.08896
- Farquhar et al., Semantic entropy (*Nature*, 2024) — https://www.nature.com/articles/s41586-024-07421-0
- Walters & Wilder, 가짜 인용 연구 (*Scientific Reports*, 2023) — https://www.nature.com/articles/s41598-023-41032-5
- Mata v. Avianca 제재 결정 (2023-06-22) — https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54
- AI Hallucination Cases 데이터베이스 (Damien Charlotin) — https://www.damiencharlotin.com/hallucinations/
- AFP 보도 (Malay Mail, 2026-06-16) — https://www.malaymail.com/news/tech-gadgets/2026/06/16/do-your-job-global-courts-face-rising-tide-of-ai-generated-fake-cases-and-quotes/223865
- Stanford, 법률 AI 도구 환각 연구 — https://law.stanford.edu/publications/hallucination-free-assessing-the-reliability-of-leading-ai-legal-research-tools

**아첨**
- Sharma et al., "Towards Understanding Sycophancy in Language Models" (Anthropic, 2023) — https://arxiv.org/abs/2310.13548
- Perez et al., "Discovering Language Model Behaviors with Model-Written Evaluations" (2022) — https://arxiv.org/abs/2212.09251
- Wei et al., "Simple synthetic data reduces sycophancy" (Google, 2023) — https://arxiv.org/abs/2308.03958
- Laban et al., FlipFlop "Are You Sure?" (2023) — https://arxiv.org/abs/2311.08596
- SycEval (2025) — https://arxiv.org/abs/2502.08177
- OpenAI, "Sycophancy in GPT-4o" (2025-04-29) — https://openai.com/index/sycophancy-in-gpt-4o/
- OpenAI, "Expanding on what we missed with sycophancy" (2025-05) — https://openai.com/index/expanding-on-sycophancy/

**검증**
- Civic Online Reasoning, "Teaching Lateral Reading" — https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/
