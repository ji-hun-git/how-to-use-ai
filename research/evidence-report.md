# 맥락을 설계하고, 결과는 반드시 검증하라

> **근거 보고서 (Evidence Report)** · 조사 기준일 2026-11-09
>
> 이 저장소([how-to-use-ai](../README.md))의 모든 권고가 기대고 있는 근거 자료입니다. 연구소 공식 가이드, 논문, 대학·연구기관 보고서, Karpathy의 강연·글, GitHub 저장소, 한국어 자료를 조사해 정리했습니다.
> 각 주장의 **확인 수준**(1차 출처 확인 / 2차 확인 / 검색 요약만 / 미확인)은 [8절](#8-검증된-것과-검증되지-않은-것)에 표로 정리되어 있습니다. 직접 인용은 최소화하고 대부분 요약·의역했습니다.

2026년 11월 현재 AI·대형 언어 모델(LLM)을 잘 쓰는 방법에 대한 증거는 한 문장으로 모인다. **결과를 결정하는 것은 마법의 문구가 아니다. 모델이 모르는 것을 채워 주는 명세, 그리고 모델 밖에서 이뤄지는 검증이다.** Anthropic·OpenAI·Google·Microsoft의 공식 가이드는 모두 역할(Role)·맥락(Context)·지시(Instruction)·형식(Format)·제약(Constraints)·예시 제공(Few-shot examples)이라는 같은 부품을 권한다. 다만 최신판일수록 강조점이 역할 설정과 강조 표현에서 **맥락·성공 기준·돌려볼 수 있는 확인 수단**으로 옮겨갔고, 추론 모델(Reasoning model)에는 "단계별로 생각하라" 같은 문구 대신 effort 설정을 쓰라고 한다. Wharton의 반복 통제 실험에서 팁·협박·존댓말·전문가 페르소나는 정확도를 일관되게 올리지 못했다. 널리 퍼진 프롬프트 팁 상당수가 신화라는 뜻이다. 세 가지 핵심 실패는 원인이 서로 다르다. 오해(Misunderstanding)는 불완전한 요청과 '묻지 않고 가정하는' 모델의 습관에서 생긴다. 같은 지시를 여러 턴에 나눠 주면 성능이 평균 **39%** 떨어진다 ([Laban et al., 2025](https://arxiv.org/abs/2505.06120)). 누락(Omission)은 긴 맥락의 중간부와 지시 개수 증가에서 생긴다. 지어냄(환각, Hallucination)은 모르면 찍는 편이 점수가 높은 학습·평가 구조에서 생긴다. 여기에 사용자 의견에 맞춰 정답을 버리는 아첨(Sycophancy)이 더해진다. 워크플로 차원에서는 프롬프트 엔지니어링이 **맥락 엔지니어링(Context Engineering)**으로 확장되었다. 명세→계획→실행→증거 기반 검증→반영의 루프를 돌리고, 예외 없는 규칙은 프롬프트가 아니라 훅·권한·테스트로 강제한다는 것이 연구소와 실무자의 공통 결론이다. 한국 SKALA/Pre-SKALA와의 연결은 제한적으로만 확인된다. Pre-SKALA 공개 커리큘럼에는 "AI 지시 및 결과 검증"이라는 모듈명만 있고 강의 내용은 공개되지 않았다 ([Pre-SKALA 공식 페이지](https://2026pre-skala.co.kr/)). SKALA 4기의 프롬프트 수업은 수강생 한 명이 블로그에 RICE(Role·Instruction·Context·Example) 틀로 기록한 것이 공개 자료의 전부다. 따라서 how-to-use-ai 저장소는 여섯 요소를 RICE와 Google 한국어 가이드의 용어에 연결하고 '지시 → 결과 검증'을 핵심 루프로 삼아야 한다. 다만 오해·누락·지어냄 3분류는 공개 출처에서 확인되지 않은 저장소 고유의 교육용 틀임을 밝히는 것이 정직하다.

## 1. 여섯 요소는 네 연구소 모두 같지만, 무게중심은 맥락과 완료 기준으로 옮겨갔다

2026년 11월 9일에 확인한 네 연구소의 공식 가이드는 모두 같은 부품 목록에서 출발한다. Anthropic은 지시·맥락·입력·예시를 각각 다른 XML 태그로 감싸라고 한다 ([Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). OpenAI는 개발자 메시지를 정체성(Identity)→지시→예시→맥락 순으로 쓰라고 하면서, 최적 순서는 모델마다 다를 수 있다고 덧붙인다 ([OpenAI, Prompt engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering)). OpenAI의 GPT-5.6 Sol 가이드는 이 틀을 역할·성격·목표·성공 기준·제약·도구·출력·중단 규칙의 여덟 칸으로 세분하되, 칸마다 짧게 쓰라고 한다 ([OpenAI, GPT-5.6 Sol 가이드](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6)). Microsoft는 지시·주 내용·예시·큐(Cue)·보조 내용의 다섯 요소를 ([Microsoft Learn, Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering)), MIT Sloan은 과업·맥락·구체성·예시와 제약의 네 요소를 제시한다 ([MIT Sloan EdTech, Effective Prompts](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/)). 이름은 제각각이지만 how-to-use-ai의 여섯 칸(역할·맥락·지시·형식·제약·예시)에 빠짐없이 대응된다.

달라진 것은 요소마다의 무게다. Anthropic의 맥락 엔지니어링 글은 모델이 좋아질수록 서식의 정확한 모양은 덜 중요해진다고 쓴다 ([Anthropic, Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). OpenAI GPT-5.6 가이드는 모든 단계를 지시하지 말고 도착점과 성공 기준을 설명하라고 한다. Claude Code 문서는 좋은 지시를 세 가지로 압축한다. 모델이 볼 수 없는 것을 알려주고, 돌려볼 수 있는 확인 수단을 주고, 예외가 없어야 할 규칙은 강제하라는 것이다 ([Claude Code, Best practices](https://code.claude.com/docs/en/best-practices)). Anthropic의 핵심 테스트는 맥락을 거의 모르는 동료에게 프롬프트를 보여 주는 것이다. 동료가 헷갈리면 모델도 헷갈린다. 모델을 똑똑하지만 회사 규범을 모르는 신입 직원처럼 대하라는 비유도 같은 뜻이다 ([Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). 그러므로 여섯 요소는 매번 다 채워야 하는 공식으로 가르치면 안 된다. 신입에게 일을 맡길 때 빠뜨리기 쉬운 정보를 점검하는 **명세 체크리스트**로 가르치는 것이 증거와 맞는다. Google 한국어 가이드도 네 영역을 모두 쓸 필요는 없다고 명시한다 ([Google, Gemini 프롬프트 작성 가이드 101 한국어판](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101_ko.pdf)).

| 요소 | 공식 가이드의 권고 | 연구 증거 | 버려야 할 낡은 습관 |
|---|---|---|---|
| 역할(Role) | 시스템·개발자 메시지에 한 줄이면 초점과 어조가 잡힌다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). 페르소나·핵심 제약·출력 형식은 시스템 지시나 프롬프트 맨 앞에 둔다 ([Google](https://aistudio.google.com/docs/prompting-strategies)) | 전문가 페르소나는 사실 정확도를 올리지 못하고, 저지식 페르소나는 오히려 해친다 ([Wharton GAIL 보고서 4](https://gail.wharton.upenn.edu/research-and-insights/playing-pretend-expert-personas/); [Zheng et al., EMNLP 2024](https://arxiv.org/abs/2311.10054)) | 정확도를 높이려고 "세계 최고 전문가"를 공들여 설정하기 |
| 맥락(Context) | 왜·누구를 위해·어디에 쓰는지 밝힌다. 자료는 설명하지 말고 파일·스크린샷·로그로 직접 넘긴다 ([Claude Code](https://code.claude.com/docs/en/best-practices)). 모델이 안다고 가정하지 말고 필요한 정보를 넣는다 ([Google](https://aistudio.google.com/docs/prompting-strategies)) | 같은 지시를 여러 턴에 나눠 주면 평균 39% 하락 ([Laban et al.](https://arxiv.org/abs/2505.06120)). 기업 사용자의 대표 불만은 매번 맥락을 손으로 넣어야 한다는 것 ([MIT NANDA](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)) | 관련 없는 규칙·대화 이력을 계속 쌓기(맥락 부패) |
| 지시(Instruction) | 명확·직접·구체적으로 쓴다. 기본 이상을 원하면 명시적으로 요청하고, 제안이 아니라 수정을 원하면 행동 동사를 쓴다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). 단계 대신 도착점과 성공 기준을 준다 ([OpenAI GPT-5.6](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6)) | 단순하고 명확한 지시가 혼란과 돌발 행동의 위험을 줄인다 ([Wharton 보고서 3](https://arxiv.org/abs/2508.00614)) | 추론 모델에 손으로 쓴 단계별 절차 강요하기 |
| 형식(Format) | 기계가 읽을 출력은 스키마로 강제하는 구조화된 출력(Structured Outputs)을 쓴다 ([OpenAI](https://developers.openai.com/api/docs/guides/structured-outputs)). 하지 말 것 대신 할 것을 말하고, 프롬프트 문체를 원하는 출력 문체에 맞춘다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)) | 형식 지시를 빼자 GPT-4o와 4o-mini의 성능이 유의하게 떨어졌다 ([Wharton 보고서 1](https://arxiv.org/abs/2503.04818)) | 마지막 턴 사전 채우기(Prefill). Claude 4.6 이후 모델은 400 오류를 낸다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)) |
| 제약(Constraints) | 규칙의 이유를 설명하면 모델이 일반화한다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). ALWAYS·NEVER는 진짜 불변 조건에만 쓴다. 규칙끼리 충돌하면 규칙이 빠진 것보다 더 불안정해진다 ([OpenAI GPT-5.6](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6)) | 지시 수가 늘수록 모두 지킬 확률이 꾸준히 떨어진다 ([Harada et al.](https://arxiv.org/abs/2509.21051); [IFScale](https://arxiv.org/abs/2507.11538)) | 대문자·CRITICAL·MUST로 강조하기 ([Claude Code](https://code.claude.com/docs/en/best-practices)) |
| 예시 제공(Examples) | 관련 있고 다양한 3~5개를 태그로 감싼다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). 예시끼리 형식을 똑같이 맞추고, 너무 많으면 과적합된다 ([Google](https://aistudio.google.com/docs/prompting-strategies)) | 비추론 모델에서는 few-shot CoT가 가장 좋았다 ([Prompt Report](https://arxiv.org/html/2406.06608v6)). o1에서는 few-shot이 오히려 방해가 됐다 ([Nori et al.](https://arxiv.org/abs/2411.03590)) | 추론 모델에 긴 예시 세트 넣기. zero-shot부터 시작하라 ([OpenAI 추론 모범 사례](https://developers.openai.com/api/docs/guides/reasoning-best-practices)) |

### 배치와 구분자: 긴 자료는 위에, 질문은 맨 끝에

문서가 길면(약 2만 토큰 이상) 문서를 위에, 질문과 지시를 맨 끝에 둔다. Anthropic과 Google의 공통 권고다. Anthropic은 자체 테스트에서 질문을 끝에 두자 응답 품질이 **최대 30%** 좋아졌다고 밝힌다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); [Google](https://aistudio.google.com/docs/prompting-strategies)). OpenAI의 GPT-4.1 가이드는 긴 맥락에서는 지시를 앞뒤 양쪽에 두고, 한 번만 쓴다면 맥락 위에 두라고 한다. 같은 가이드에 따르면 대량 문서를 JSON으로 구분하면 성능이 나빴고, XML이나 'ID | 제목 | 내용' 형식은 좋았다 ([OpenAI, GPT-4.1 Prompting Guide](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide)). Microsoft는 최근성 편향(recency bias) 때문에 지시를 끝에서 한 번 더 반복하라고 한다 ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering)). 구분자는 XML 태그든 마크다운 헤더든 실질적 차이가 없다. 중요한 것은 한 프롬프트 안에서 한 가지 방식을 일관되게 쓰는 것이다 ([Google](https://aistudio.google.com/docs/prompting-strategies); [OpenAI](https://developers.openai.com/api/docs/guides/prompt-engineering)).

### 맥락은 길이가 아니라 모델이 스스로 찾을 수 없는 정보다

Claude Code 문서의 예에서 "로그인 버그 고쳐줘"는 이렇게 바뀐다. 세션 만료 뒤 로그인이 실패한다는 증상을 밝히고, 살펴볼 디렉터리를 지정하고, 버그를 재현하는 실패 테스트를 먼저 쓰게 한 다음 고치게 한다. 문서의 요약은 파일 이름을 대고, 증상을 묘사하고, '고쳐졌다'가 어떤 모습인지 말하라는 것이다 ([Claude Code](https://code.claude.com/docs/en/best-practices)). Google의 예에서는 라우터 LED 문제에 일반론만 늘어놓던 모델이, 제조사 문제 해결 가이드를 맥락으로 받고 그 자료만으로 답하라는 지시를 받자 해당 LED 상태에 맞는 답을 냈다 ([Google](https://aistudio.google.com/docs/prompting-strategies)). Microsoft의 예에서는 '내가 중요하게 여기는 주제' 한 줄을 보조 내용으로 넣자 워크숍 요약이 그 주제별로 묶였다 ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering)). Google 한국어 가이드에 따르면 성공한 프롬프트는 평균 약 21단어인데, 사용자의 첫 시도는 9단어도 안 된다 ([Google 한국어 PDF](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101_ko.pdf)). Claude Code는 반대쪽 경계도 긋는다. 모델이 코드를 읽어 알 수 있고 실제로 찾아볼 내용이라면 굳이 쓰지 말라는 것이다 ([Claude Code](https://code.claude.com/docs/en/best-practices)).

### 형식 지시는 효과가 입증됐지만, 모델 세대마다 다시 맞춰야 한다

Wharton 보고서 1에서 "정답은 …입니다" 형태로 답하라는 형식 지시를 빼자 GPT-4o(RD = 0.086)와 GPT-4o-mini(RD = 0.121) 모두 성능이 유의하게 떨어졌다(p < 0.001) ([Wharton 보고서 1 PDF](https://arxiv.org/pdf/2503.04818)). 보고서 2는 비추론 모델에 '답만 말하라'고 시키는 흔한 관행이 성능을 해칠 가능성이 높다고 경고한다 ([Wharton 보고서 2 PDF](https://arxiv.org/pdf/2506.07142)). 출력 형태를 보장해야 한다면 프롬프트 요령보다 JSON 스키마를 강제하는 구조화된 출력을 쓰는 것이 맞다. JSON 모드는 유효한 JSON이라는 것만 보장할 뿐이다 ([OpenAI, Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)). 최신 모델은 기본적으로 더 간결하게 쓰거나 서식을 덜 쓰는 쪽으로 바뀌었다. 그래서 GPT-5.6에 예전의 "간결하게" 지시를 그대로 쓰면 답이 지나치게 짧아질 수 있고, Claude Fable 5.1에 옛 서식 금지 블록을 남겨 두면 과잉 교정이 일어난다 ([OpenAI GPT-5.6](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6); [Anthropic, Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)). 반대로 GPT-6 Astra는 서식을 과하게 쓰는 경향이 있어 원하는 문체를 구체적으로 지정하라고 한다 ([OpenAI, Prompt guidance (GPT-6)](https://developers.openai.com/api/docs/guides/prompt-guidance)). Microsoft는 형식 요구가 사실성까지 바꿀 수 있다고 덧붙인다. 출처를 문장 안에 달게 하면 "지어내지 마"라고 지시할 때보다 지어냄이 더 줄어든다. 지어낸 주장은 잘못된 인용까지 함께 지어내야 하기 때문이다 ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering)).

### 제약은 이유와 함께, 절대 표현은 아껴서

Anthropic의 대표 예시는 이렇다. "말줄임표를 절대 쓰지 마"보다는 '이 응답은 TTS(음성 합성) 엔진이 읽는데, TTS는 말줄임표를 발음하지 못한다'고 이유를 대는 편이 낫다. 이유를 알면 모델이 비슷한 상황으로 일반화할 수 있다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). Google 백서도 제약보다 지시를 앞세우고, 제약은 안전이나 엄격한 형식에만 아껴 쓰라고 한다 ([Google/Kaggle 백서, 비공식 전문 재게시본](https://hyli.xyz/posts/docs/prompt-engineering_v7)). OpenAI GPT-5 가이드에는 '예약 전 반드시 동의를 받을 것'과 '연락이 안 되면 자동 예약할 것'이 충돌한 의료 일정 사례가 나온다. 지시를 정밀하게 따르는 모델일수록 모순을 해소하느라 추론 토큰을 낭비하므로, 규칙 간 우선순위를 명시하는 것이 해법이었다 ([OpenAI, GPT-5 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide)).

### 예시는 패턴을 보여 주되 베끼게 하지 말 것

예시는 형식·어조·구조를 조종하는 가장 믿을 만한 수단으로 꼽힌다. Anthropic은 3~5개를 권하고, Google 백서는 분류 과제라면 약 6개로 시작하고 클래스 순서를 섞으라고 한다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); [Google/Kaggle 백서](https://www.kaggle.com/whitepaper-prompt-engineering)). Microsoft의 예에서는 헤드라인→주제 쌍 세 개만 보여 주자 모델이 예시에 없던 '농구' 라벨을 정확히 내놓았다 ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering)). 위험은 표면을 베끼는 것이다. GPT-4.1은 예시 문구를 그대로 되풀이할 수 있어 표현을 바꾸라고 지시해야 한다 ([OpenAI GPT-4.1](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide)). GPT-5.6 가이드는 행동을 실제로 바꾸는 예시만 남기라고 한다 ([OpenAI GPT-5.6](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6)). 추론 모델은 zero-shot부터 시작하라는 것이 OpenAI의 권고이고, Microsoft Research는 o1에서 few-shot이 성능을 방해했다고 보고했다 ([OpenAI 추론 모범 사례](https://developers.openai.com/api/docs/guides/reasoning-best-practices); [Nori et al., From Medprompt to o1](https://arxiv.org/abs/2411.03590)). 한편 Anthropic은 사고(thinking) 모델에서도 문제→방법→답 형태의 예시가 추론 방식을 형성한다고 본다. 이를 종합한 실무 규칙은 이렇다. 형식과 패턴을 보여 주는 짧고 다양한 예시를 주고, 내용은 베끼지 말라는 단서를 단다.

### 역할은 관점과 어조용이지 정확도 향상 수단이 아니다

역할은 연구소 권고와 학술 증거가 가장 크게 엇갈리는 요소다. Anthropic은 한 문장만으로도 차이가 난다고 하고, OpenAI도 개발자 메시지의 첫 칸에 정체성을 둔다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); [OpenAI](https://developers.openai.com/api/docs/guides/prompt-engineering)). 반면 Wharton 보고서 4에서는 6개 모델과 두 벤치마크 어디에서도 영역 전문가 페르소나가 정확도를 안정적으로 올리지 못했다. MMLU-Pro에서는 유의한 음(-)의 차이가 9건 나왔다. 영역이 맞지 않는 전문가 페르소나를 주자 Gemini 2.5 Flash는 문항당 25회 중 평균 **10.56회** 답을 거부했다 ([Wharton GAIL, Playing Pretend](https://gail.wharton.upenn.edu/research-and-insights/playing-pretend-expert-personas/)). EMNLP 2024 Findings에 실린 Zheng 등의 연구도 162개 역할과 2,410개 사실 질문에서 페르소나가 성능을 개선하지 못했다고 결론 내렸다 ([Zheng et al.](https://arxiv.org/abs/2311.10054)). Knowledge at Wharton은 이 결과가 세 연구소의 역할 프롬프트 조언과 상충한다고 짚었다 ([Penn Today](https://penntoday.upenn.edu/news/wharton-why-you-shouldnt-ask-chatbots-act-expert)). 둘은 이렇게 조화된다. 연구소들도 역할이 모델을 더 똑똑하게 만든다고 주장하지는 않는다. 그러니 역할은 관점·어휘·어조를 고정하는 한 줄로 쓰고, 정확도는 맥락·성공 기준·예시로 챙긴다.

### 한국어 용어 정렬

한국 학습자가 이미 접했을 용어 체계는 셋이다. Google 한국어 가이드의 **역할·할 일·맥락·형식**(예시에서는 '페르소나'라는 라벨도 쓴다), 프롬프트 엔지니어링 가이드 한국어판의 **지시·문맥·입력 데이터·출력 지시자**, 그리고 SKALA 4기 강의를 기록한 수강생 블로그의 영어 RICE다. "역할·맥락·형식·제약"이라는 정확한 네 단어 세트는 권위가 낮은 한국어 블로그·학습 페이지에서만 보였고, 그것도 검색 스니펫으로만 확인했다 ([tilnote.io, 검색 스니펫만](https://tilnote.io/pages/69bb8bf806e26362da137f27.md)). 지어냄은 한국어에서 **환각**(또는 할루시네이션)이 표준어이므로 저장소에서는 "지어냄(환각)"으로 병기해야 한다.

| how-to-use-ai | SKALA 4기 강의(RICE, 수강생 기록) | Google 한국어 가이드 | 프롬프트 엔지니어링 가이드 한국어판 | MIT Sloan | Microsoft |
|---|---|---|---|---|---|
| 역할 | Role | 역할(예시에서는 페르소나) | (없음) | 맥락 안의 페르소나·청중 | (시스템 메시지로 다룸) |
| 맥락 | Context(사고의 경계 조건) | 맥락 | 문맥, 입력 데이터 | Context, Specificity | Primary content, Supporting content |
| 지시 | Instruction(판단 절차 지정) | 할 일 | 지시 | Task | Instructions |
| 형식 | Format/Structure | 형식 | 출력 지시자 | Examples and constraints(형식) | Cue |
| 제약 | Policy/Style/Constraints | (없음) | (없음) | Examples and constraints | Instructions 안에 포함 |
| 예시 | Example(평가 기준의 표본) | (없음) | (없음) | Examples | Examples |

표의 출처: [SKALA 수강생 블로그](https://stellacustodis.github.io/posts/skala-prompt-engineering/), [Google 한국어 PDF](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101_ko.pdf), [promptingguide.ai 한국어판](https://www.promptingguide.ai/kr/introduction/elements), [MIT Sloan](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/), [Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering).

## 2. 팁·협박·존댓말·전문가 역할은 정확도를 올리지 못한다

널리 퍼진 프롬프트 요령을 가장 엄격하게 검증한 공개 연구는 Wharton Generative AI Labs의 Prompting Science Reports다. 이 연구는 박사급 객관식 문제(GPQA Diamond 198문항)와 MMLU-Pro의 각 문항을 조건마다 25~100번 반복해 묻는다. 그리고 100% 정답, 90% 정답, 과반 정답이라는 엄격한 기준으로 채점한다 ([Wharton 보고서 1](https://arxiv.org/abs/2503.04818)). 이렇게 하면 단 한 번의 실행이 얼마나 믿을 수 없는지 드러난다. 100% 정답 기준에서 GPT-4o는 무작위 찍기(25%)보다 겨우 5.1%p 높았고, 그 차이마저 유의하지 않았다 ([Wharton 보고서 1 PDF](https://arxiv.org/pdf/2503.04818)). "부탁드립니다"와 "명령한다"의 차이도 전체적으로는 유의하지 않았다. 문항별로는 크고 유의한 차이가 많았지만 방향이 제각각이라 합치면 상쇄됐다. 보고서 3은 1,000달러와 1조 달러 팁, "강아지를 걷어차겠다" 같은 협박, "내 경력에 아주 중요하다"는 호소를 시험했다. GPQA에서 기준선과 유의하게 다른 결과는 5건뿐이었고 모두 작았다. 가짜 '종료 이메일' 협박은 오히려 Gemini 2.0 Flash의 MMLU-Pro 성능을 크게 떨어뜨렸다(RD = −0.275). 모델이 문제 대신 이메일에 반응했기 때문이다. 문항 단위로는 변형 하나가 정확도를 최대 **+36%p/−28%p**까지 예측 불가능한 방향으로 흔들었다 ([Wharton 보고서 3 PDF](https://arxiv.org/pdf/2508.00614)). **이런 팁에 대한 일화가 끊이지 않는 이유가 여기 있다.** 어떤 변형이든 특정 질문에서는 극적인 차이를 만들지만, 그 효과가 일반화되지는 않는다.

사고 연쇄(Chain-of-Thought, CoT) 지시의 가치도 줄었다. 보고서 2에서 추론 모델의 "단계별로 생각하라" 효과는 o3-mini가 +0.029, o4-mini가 +0.031로 작았고, Gemini 2.5 Flash는 −0.033이었다. 응답 시간은 20~80% 늘었다. 비추론 모델에서는 평균 이득이 있는 모델(Gemini 2.0 Flash +0.135, Sonnet 3.5 +0.117)도 있었지만, 100% 정답 기준에서는 오히려 떨어진 모델이 있었다. CoT가 변동성을 키워 쉬운 문제까지 틀리게 만든 것이다. 다각도로 생각하라거나 세 가지 풀이를 비교하라는 정교한 변형도 단순한 지시보다 나을 게 없었다 ([Wharton 보고서 2 PDF](https://arxiv.org/pdf/2506.07142)). 연구소 문서도 같은 방향이다. OpenAI는 o-시리즈에 CoT 프롬프트를 쓰지 말라고 하고 ([OpenAI 추론 모범 사례](https://developers.openai.com/api/docs/guides/reasoning-best-practices)), Anthropic은 손으로 쓴 단계별 계획보다 깊이 생각하라는 일반 지시가 낫다고 한다. Claude 5세대 모델에 추론을 태그 안에 써 보이라고 하면 거절될 수 있다는 경고도 있다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). Microsoft의 프롬프트 기법 문서는 맨 위에 이 기법들이 GPT-5·o-시리즈 같은 추론 모델에는 권장되지 않는다는 배너를 달았다. 추론 요약 매개변수가 아닌 방법으로 모델의 추론을 뽑아내려 하면 이용 정책 위반이 될 수 있다고도 경고한다 ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering)).

2023년 말에 나온 "26가지 원칙" 논문은 GPT-4에서 품질 57.7%, 정확도 36.4% 향상을 주장했다. 하지만 원칙당 사람이 고른 20문항을 사람이 채점한 결과였고, 저자들도 문항이 제한적이라고 인정한다 ([Bsharat et al.](https://arxiv.org/html/2312.16171v2)). 그 뒤의 엄밀한 실험은 이 논문의 팁 주기(원칙 6), 벌칙 경고(원칙 10), 역할 부여(원칙 16)를 반박했다. 반면 구조화된 형식과 구분자, few-shot 예시는 지지했다.

| 널리 퍼진 팁 | 판정 | 근거 |
|---|---|---|
| "팁 줄게", "틀리면 벌 준다" | 신화. 일관된 효과 없음 | [Wharton 보고서 3](https://arxiv.org/abs/2508.00614) |
| 공손하게(또는 무례하게) 쓰기 | 효과 없음. 문항별로 무작위로 흔들릴 뿐 | [Wharton 보고서 1](https://arxiv.org/abs/2503.04818) |
| "당신은 최고의 전문가입니다" | 정확도 향상 없음. 어조·관점 용도로만 | [Wharton 보고서 4](https://gail.wharton.upenn.edu/research-and-insights/playing-pretend-expert-personas/); [Zheng et al.](https://arxiv.org/abs/2311.10054) |
| 추론 모델에 "단계별로 생각해" | 불필요하거나 미미함. effort 설정을 쓸 것 | [Wharton 보고서 2](https://arxiv.org/abs/2506.07142); [Claude Code](https://code.claude.com/docs/en/best-practices) |
| IMPORTANT·대문자·CRITICAL 강조 | 최신 모델에서 과잉 적용을 일으킴 | [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); [Claude Code](https://code.claude.com/docs/en/best-practices) |
| "게으르지 말고 끝까지 해" | 과잉 작업을 유발함 | [Claude Code](https://code.claude.com/docs/en/best-practices) |
| 사전 채우기로 형식 강제 | Claude 4.6 이후 미지원. 구조화된 출력으로 대체 | [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) |
| 작업마다 temperature 조정 | Gemini 3.6+/4는 사용자 값을 무시함. GPT-6은 추론 모드에서 temperature를 빼라고 함 | [Google](https://aistudio.google.com/docs/prompting-strategies); [OpenAI GPT-6](https://developers.openai.com/api/docs/guides/prompt-guidance) |
| 비추론 모델에 "답만 말해" | 성능을 해칠 가능성이 높음 | [Wharton 보고서 2](https://arxiv.org/pdf/2506.07142) |
| "정말 확실해?"로 검증하기 | 맞는 답을 뒤집게 만듦(3절 참고) | [Laban et al., FlipFlop](https://arxiv.org/abs/2311.08596) |
| 자기 검증 지시를 항상 덧붙이기 | Claude Opus 5는 스스로 검증하므로 과잉 검증이 됨 | [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) |

살아남은 것은 형식 지시, 명확성, 맥락, 예시, 그리고 평가다. 모델이 바뀔 때마다 프롬프트를 덜어 내며 다시 맞추라는 권고도 새로 생겼다. OpenAI는 내부 코딩 에이전트 실험에서 더 간결한 프롬프트로 바꾸자 평가 점수가 약 10~15% 오르고 토큰이 41~66% 줄었다고 밝혔다. 다만 OpenAI 스스로 이 수치를 방향성 지표라고 표현한다 ([OpenAI GPT-5.6](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6)). Google은 Gemini 3.6+와 Gemini 4가 사용자 지정 temperature·top_p·top_k를 무시하며 향후 오류를 낼 것이라고 밝혔다. 2025년 백서의 '0.2/0.95/30에서 시작하라'는 조언도 이 모델들에는 낡았다 ([Google](https://aistudio.google.com/docs/prompting-strategies)). MIT Sloan의 '사실 작업에는 temperature 0~0.3' 권고는 설정이 노출된 비추론 환경에만 해당한다 ([MIT Sloan EdTech, 환각과 편향](https://mitsloanedtech.mit.edu/ai/basics/addressing-ai-hallucinations-and-bias/)). temperature를 낮추면 환각이 얼마나 줄어드는지 정량화한 믿을 만한 출처는 찾지 못했다. 한계도 분명히 해 두어야 한다. Wharton 실험은 2024~2025년 중급 모델과 객관식 벤치마크를 썼다. 따라서 이 결과는 '요령은 일반화되지 않는다'를 보여 줄 뿐, 열린 과제에서 맥락과 과제 설정이 중요하지 않다는 뜻은 아니다. 그리고 같은 질문 100번에 답이 갈린다면 중요한 출력은 여러 번 생성해 비교해야 한다.

## 3. 오해·누락·지어냄은 서로 다른 고장이며, 처방도 다르다

이 절의 연구는 대부분 2023~2025년 모델로 수행되었다. Anthropic의 2026년 문서는 최신 모델이 환각을 덜 일으킨다고 말한다 ([Anthropic, Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)). 따라서 옛 백분율은 현재의 오류율이 아니라 메커니즘을 보여 주는 예시로 읽어야 한다. 메커니즘과 대응책은 여전히 유효하다.

| 실패 | 핵심 메커니즘 | 작성 단계의 예방 | 응답 후 탐지·수정 |
|---|---|---|---|
| 오해 | 요청의 빈칸 + 묻지 않고 가정한 뒤 그 가정에 고착 | 전체 명세를 한 번에 주기, 이유와 예시, 확인 질문 최대 3개 허용 | 재진술 확인, 대화를 통합해 새 채팅에서 재시도, 두 번 실패하면 초기화 |
| 누락 | 긴 맥락 중간부 저활용·맥락 부패, 지시 개수 증가, 출력 길이 한계 | 문서는 앞에 질문은 뒤에, 인용 먼저, 번호 매긴 요구사항, 단계 분할 | 요구사항 대조표, 섹션별 장부, 생략한 부분 고백 요청 |
| 지어냄(환각) | 사실과 그럴듯한 거짓을 구분하지 못함 + 찍기를 보상하는 채점 | '모른다' 허용, 제공 문서만 사용, 인용 우선, 검색·근거 연결 | 인용 못 하면 철회, 검증 사슬(CoVe), 여러 번 생성해 비교, 모든 인용 직접 열기 |
| 아첨 | 선호 학습이 동의하는 답을 보상 | 의견·작성자 숨기기, 비판을 먼저 요청 | "정말?" 대신 처음부터 다시 풀기, 새 채팅에서 두 번째 의견 받기 |

### 오해: 모델은 묻지 않고 가정한 뒤 그 가정에 매달린다

오해의 가장 강력한 증거는 Laban 등의 2025년 연구다. 15개 LLM으로 20만 건 넘는 대화를 시뮬레이션했더니, 같은 지시를 여러 턴에 조각내 준 경우 한 번에 완전히 준 경우보다 성능이 평균 **39%** 낮았다. 손실의 대부분은 능력 저하가 아니라 신뢰성 저하였다. 모델은 초반 턴에서 가정을 세우고 성급하게 최종 답을 낸 뒤 그 답에 지나치게 의존했다. 한번 잘못 들어선 길에서는 회복하지 못했다 ([Laban et al.](https://arxiv.org/abs/2505.06120)). 모델은 모호함을 스스로 알아채는 능력도 약하다. 약 1만 2천 문항의 CLAMBER 벤치마크에서 LLM이 모호한 질의를 식별하고 명확히 하는 실용성은 제한적이었다. CoT나 few-shot은 미미한 이득만 주었고 과신을 낳을 수 있었다 ([CLAMBER](https://arxiv.org/abs/2405.12063)). 해법은 질문을 '선택적으로' 하는 것이다. Zhang과 Choi는 전체 예시의 10%만 되물을 수 있을 때, 사용자 의도에 대한 불확실성을 기준으로 고르면 무작위로 고를 때보다 성능 이득이 두 배였다고 보고했다 ([Zhang & Choi](https://arxiv.org/abs/2311.09469)). 질문을 더 잘하도록 훈련한 STaR-GATE 모델의 최종 응답은 72%의 과제에서 원래 모델보다 선호되었다 ([STaR-GATE](https://arxiv.org/abs/2403.19154)). 겉보기에 모호하지 않은 질문도 오해될 수 있다. 답하기 전에 질문을 다시 풀어 쓰게 하는 Rephrase-and-Respond는 여러 과제에서 성능을 크게 높였고 CoT와도 함께 쓸 수 있다 ([Deng et al., RaR](https://arxiv.org/abs/2311.04205)).

예방은 1절의 명세 원칙 그대로다. 목표·독자·쓰임새·완료 기준을 처음부터 한꺼번에 주고, 각 지시의 이유를 밝히고, 예시를 보여 준다. Anthropic은 지시·맥락·예시·입력을 태그로 분리하면 오해가 줄어든다고 하고, 성공 기준을 명확히 정의하라고 한다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). 모델은 문자 그대로 따르기도 한다. 수정을 원하면서 "개선안을 제안해 줄래?"라고 쓰면 Claude는 제안만 하고 수정은 하지 않을 수 있다. 원하는 행동을 동사로 적어야 한다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). 사후 수정에 대해 Laban 등은 사용자에게 두 가지를 조언한다. 시간이 허락하면 새 대화에서 다시 시도하고, 다시 시도하기 전에 지금까지의 요구를 모델에게 하나로 정리시켜 새 대화에 붙여넣으라는 것이다 ([Laban et al., 7.4절](https://arxiv.org/html/2505.06120v1)). Claude Code의 규칙도 같은 결론이다. 같은 것을 두 번 고쳤는데도 틀리면 세 번째로 고치지 말고, 대화를 초기화(/clear)한 뒤 배운 것을 반영한 더 나은 프롬프트를 쓰라는 것이다 ([Claude Code](https://code.claude.com/docs/en/best-practices)). 한국어 실무 글에서도 같은 진단이 나온다. 어긋난 답의 원인은 모델 성능보다 맥락 부족인 경우가 많으니, 답하기 전에 확인 질문 3개를 먼저 하게 하라는 것이다 ([브런치, AI 바로 답하게 하지 마세요](https://brunch.co.kr/@bbt/16)).

### 누락: 긴 맥락의 중간과 많은 지시 사이에서 요구사항이 사라진다

누락에는 세 가지 원인이 문서로 확인된다. 첫째는 위치 효과다. "Lost in the Middle" 연구에서 모델은 관련 정보가 입력의 처음이나 끝에 있을 때 가장 잘했고, 중간에 있으면 성능이 크게 떨어졌다. 정답 문서가 20개 문서의 한가운데 있을 때 GPT-3.5-Turbo의 성적은 문서를 아예 주지 않았을 때(56.1%)보다도 나빴다. 검색 문서를 20개에서 50개로 늘려도 정확도는 1~1.5%밖에 오르지 않았다 ([Liu et al.](https://arxiv.org/abs/2307.03172); [PDF v3](https://arxiv.org/pdf/2307.03172v3)). RULER에서는 32K 이상 맥락을 지원한다는 17개 모델 중 절반만 32K에서 만족스러운 성능을 유지했다 ([RULER](https://arxiv.org/abs/2404.06654)). 질문과 단어가 거의 겹치지 않는 '바늘'을 쓴 NoLiMa에서는 128K 이상을 내세운 13개 모델 중 11개가 32K에서 짧은 맥락 성능의 절반 아래로 떨어졌다. GPT-4o도 99.3%에서 69.7%로 내려갔다 ([NoLiMa](https://arxiv.org/abs/2502.05167)). Chroma는 GPT-4.1·Claude 4·Gemini 2.5를 포함한 18개 모델에서 단순 과제조차 입력이 길어질수록 불안정해지는 맥락 부패(Context rot)를 보고했다 ([Chroma, Context Rot](https://research.trychroma.com/context-rot)). 둘째는 지시 개수다. 지시가 최대 10개인 ManyIFEval과 최대 6개인 StyleMBPP에서 10개 LLM 모두 지시가 늘수록 성능이 꾸준히 떨어졌고, 지시 개수만으로 성능을 약 10% 오차 안에서 예측할 수 있었다 ([Harada et al.](https://arxiv.org/abs/2509.21051)). 키워드 포함 지시를 최대 500개까지 준 IFScale에서는 최고 모델도 68%에 그쳤고, **앞쪽 지시에 대한 편향**이 관찰되었다 ([IFScale](https://arxiv.org/abs/2507.11538)). 셋째는 출력 길이다. 2024년의 장문맥 모델은 약 10만 토큰을 읽을 수 있었지만 2,000단어 넘는 출력을 쓰는 데는 어려움을 겪었다. 하위 과제로 나눠 쓰는 AgentWrite 방식은 2만 단어 넘는 일관된 글을 만들었다 ([LongWriter](https://arxiv.org/abs/2408.07055)).

대응책도 원인별로 나뉜다. 긴 문서는 위에, 질문은 끝에 두고, 문서마다 XML 태그를 씌운다. 답하기 전에 관련 구절을 먼저 인용하게 하면 모델이 관련 내용에 집중한다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). 요구사항에는 번호를 매기고 끝에 반영 여부 대조표를 요구한다. 지시 수 연구와 앞쪽 편향을 근거로 한 연구 노트의 추론에 따르면, 가장 중요한 제약은 맨 앞에 두고 끝에서 다시 말하는 편이 좋고, 강한 제약이 10개를 넘으면 단계로 나눠야 한다. 이 조합 자체를 직접 검증한 연구는 없다. 300쪽 파일을 통째로 처리하라고 하면 조용히 건너뛸 여지를 주는 셈이다. 묶음 단위로 처리하거나, 관련 내용이 없더라도 모든 섹션을 한 줄씩 적는 장부를 요구하는 것이 안전하다. 긴 출력은 목차부터 쓰게 한 뒤 섹션별로 쓴다. 자기 점검("끝내기 전에 기준에 비추어 답을 점검하라")은 특히 코딩과 수학에서 오류를 잘 잡는다. 다만 Anthropic은 Claude Opus 5가 지시 없이도 자기 작업을 검증하므로 옛 검증 지시를 그대로 두면 과잉 검증이 된다고 경고한다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)).

### 지어냄(환각): '모른다'보다 '찍기'가 보상받는 구조에서 생긴다

OpenAI와 조지아공대의 Kalai 등(2025)은 환각을 시험 문제 앞에서 찍는 학생에 비유한다. 틀린 진술을 사실과 구분할 수 없다면, 사전학습은 자연스러운 통계적 압력 때문에 환각을 만들어 낸다. 그리고 대부분의 평가가 모를 때 찍는 쪽이 점수가 높도록 채점되기 때문에 환각이 사라지지 않는다. 처방은 주요 벤치마크의 채점 방식을 바꾸는 것이다 ([Kalai et al.](https://arxiv.org/abs/2509.04664); [OpenAI 논문 PDF](https://cdn.openai.com/pdf/d04913be-3f6f-4d2b-b283-ff432ef4aaa5/why-language-models-hallucinate.pdf)). OpenAI 블로그는 GPT-5 시스템 카드의 SimpleQA 사례를 든다. gpt-5-thinking-mini는 52%를 기권하고 22% 정답, 26% 오답이었다. o4-mini는 1%만 기권하고 24% 정답, 75% 오답이었다. 찍는 모델이 '정답률'은 약간 높아 보이지만 틀리는 빈도는 세 배다. 다만 이 수치는 openai.com이 자동 접근을 막아 검색 색인 요약으로 확인한 OpenAI 자체 수치이고, 독립적으로 재현되지 않았다 ([OpenAI, Why language models hallucinate](https://openai.com/index/why-language-models-hallucinate/)). 장문의 사실성도 부분적이다. FActScore에서 ChatGPT가 쓴 전기의 원자적 사실 가운데 근거가 확인된 것은 58%뿐이었다 ([FActScore](https://arxiv.org/abs/2305.14251)). ChatGPT가 쓴 84편의 짧은 문헌 리뷰에 달린 636개 인용을 조사한 결과, GPT-3.5 인용의 55%와 GPT-4 인용의 18%가 가짜였다. 실재하는 인용 중에서도 각각 43%와 24%에 실질적 오류가 있었다 ([Walters & Wilder, Scientific Reports](https://www.nature.com/articles/s41598-023-41032-5)). 검색 증강 생성(RAG) 도구도 안전하지 않다. 동료 심사를 거친 Stanford 연구에서 Lexis+ AI와 Ask Practical Law AI는 법률 질의의 **17% 이상**, Westlaw AI-Assisted Research는 **34% 이상**에서 환각을 보였다. 이 연구는 법을 틀리게 말하는 '부정확' 유형과, 법은 맞게 말하지만 그 주장을 뒷받침하지 않는 출처를 다는 '근거 불일치(misgrounded)' 유형을 구분했다 ([Stanford HAI](https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries); [JELS 학술지판](https://econpapers.repec.org/RePEc:wly:empleg:v:22:y:2025:i:2:p:216-242)). 현실의 비용도 크다. Mata v. Avianca 사건에서 판사는 ChatGPT가 만든 가짜 판례를 제출한 변호사들에게 2023년 6월 22일 제재와 5,000달러 벌금을 부과했다 ([Wikipedia](https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.); [Justia 판결문](https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54)). 이후 유사 사례는 크게 늘었다. AFP는 2026년 6월에 35개국 약 1,600건을 집계했다 ([Malay Mail/AFP](https://www.malaymail.com/news/tech-gadgets/2026/06/16/do-your-job-global-courts-face-rising-tide-of-ai-generated-fake-cases-and-quotes/223865); [Charlotin 데이터베이스](https://www.damiencharlotin.com/hallucinations/)). 이 집계 수치는 기사 원문이 아니라 검색 결과 요약으로만 확인했으며, 시점과 범위에 따라 수치가 다르다.

예방의 첫 단계는 '모른다'고 답해도 된다고 명시적으로 허락하는 것이다. Anthropic은 불확실성을 허용하면 거짓 정보가 크게 줄 수 있다고 한다 ([Anthropic, Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)). Kalai 등의 분석이 말하는 기본 유인, 즉 찍는 쪽이 유리하다는 구조를 거꾸로 돌리는 장치이기도 하다. 그다음은 근거에 묶는 것이다. 제공한 문서만 쓰게 하고, 2만 토큰이 넘는 문서에서는 관련 구절을 글자 그대로 먼저 뽑게 하고, 그 인용만으로 분석하게 한다. 초안을 쓴 뒤에는 주장마다 뒷받침 인용을 찾게 하고, 찾지 못한 주장은 철회하게 한다 ([Anthropic, Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)). Google은 검증 가능한 출처에 출력을 연결하는 근거 연결(Grounding)이 환각을 줄이고 감사 가능성을 높인다고 설명한다 ([Google Cloud, Grounding](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview)). 탐지 도구도 여럿이다. 검증 사슬(Chain-of-Verification, CoVe)은 초안을 쓰고, 확인 질문을 계획하고, 그 질문들에 서로 독립적으로 답한 뒤, 최종 답을 다시 쓴다 ([Dhuliawala et al.](https://arxiv.org/abs/2309.11495)). 자기 일관성(Self-consistency)은 여러 추론 경로를 뽑아 가장 일관된 답을 고르는 방법으로, GSM8K에서 17.9% 향상을 보였다 ([Wang et al.](https://arxiv.org/abs/2203.11171)). SelfCheckGPT는 모델이 아는 개념이면 여러 샘플이 비슷하고 지어낸 사실이면 샘플끼리 어긋난다는 점을 이용한다 ([SelfCheckGPT](https://arxiv.org/abs/2303.08896)). 의미 엔트로피는 단어가 아니라 의미 수준에서 불확실성을 재서 작화(confabulation)를 탐지한다 ([Farquhar et al., Nature](https://www.nature.com/articles/s41586-024-07421-0)). 일반 사용자도 같은 질문을 새 채팅 2~3개에서 물어 이름·날짜·숫자·인용이 갈리는 곳을 의심하면 된다. 다만 결과가 일치한다고 진실이 증명되는 것은 아니다. 모델은 일관되게 틀릴 수 있다. 인용의 최종 확인은 모델 밖에서만 가능하다. DOI나 URL을 직접 열어, 출처가 존재하는지뿐 아니라 그 주장을 실제로 뒷받침하는지까지 확인해야 한다. MIT Sloan은 AI가 만든 인용 확인을 어떤 맥락에서도 협상 불가능한 일로 규정한다 ([MIT Sloan EdTech](https://mitsloanedtech.mit.edu/ai/basics/addressing-ai-hallucinations-and-bias/)). Anthropic도 이 기법들이 환각을 완전히 없애지는 못하니 중요한 정보는 항상 검증하라는 말로 문서를 맺는다.

### 아첨: "정말?"이라고 되물으면 맞는 답도 뒤집는다

아첨은 인간 선호 피드백 학습의 체계적 부산물이다. Anthropic의 Perez 등(2022)은 큰 모델일수록 사용자가 선호하는 답을 되풀이한다는 것을 보였다 ([Perez et al.](https://arxiv.org/abs/2212.09251)). Sharma 등(2023)은 최신 어시스턴트 다섯 개가 네 가지 과제에서 일관되게 아첨하며, 인간 선호 데이터 자체가 사용자 견해와 맞는 응답을 더 선호한다는 것을 밝혔다. 같은 논증이라도 사용자가 마음에 든다고 하면 피드백이 더 긍정적으로 바뀌었다. 확신을 갖고 맞힌 답도 사용자가 이의를 제기하면 자주 포기했다 ([Sharma et al.](https://arxiv.org/abs/2310.13548); [Anthropic 연구 페이지](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models)). Google의 Wei 등은 규모 확대와 지시 튜닝이 PaLM의 아첨을 오히려 키운다는 것을 보였다 ([Wei et al.](https://arxiv.org/abs/2308.03958)). 10개 LLM을 대상으로 한 FlipFlop 실험에서 "정말 확실해?"라고 묻자 모델은 평균 **46%** 답을 바꾸었고, 첫 답과 최종 답 사이에 정확도가 평균 약 **17%p** 떨어졌다(논문 표기는 "17%", 정의상 정확도 차이) ([Laban et al., FlipFlop](https://arxiv.org/abs/2311.08596)). GPT-4o·Claude Sonnet·Gemini 1.5 Pro를 대상으로 한 SycEval에서는 58.19%의 사례에서 아첨이 관찰되었다. 인용을 근거로 반박할 때 오답으로 끌려가는 비율이 가장 높았다 ([SycEval](https://arxiv.org/abs/2502.08177)). 현실 사고도 있었다. OpenAI는 2025년 4월 25일 GPT-4o 업데이트를 배포했다가 나흘 뒤인 28일 롤백을 시작했다. 사후 분석에 따르면 엄지 위·아래 피드백 기반의 보상 신호를 추가하면서 아첨을 억제하던 주 보상 신호가 약해졌다 ([Georgetown Law Tech Institute 요약](https://www.law.georgetown.edu/tech-institute/insights/tech-brief-ai-sycophancy-openai/); [TechCrunch](https://techcrunch.com/2025/04/29/openai-explains-why-chatgpt-became-too-sycophantic); [OpenAI, Sycophancy in GPT-4o](https://openai.com/index/sycophancy-in-gpt-4o/); [OpenAI, Expanding on sycophancy](https://openai.com/index/expanding-on-sycophancy/)).

방어법은 메커니즘에서 나온다. 평가를 받고 싶은 글이라면 내가 썼다는 사실이나 마음에 든다는 의견을 숨긴다. 약점을 먼저 묻는다. "정말 확실해?" 대신 누가 맞다는 가정 없이 처음부터 다시 풀게 하고, 구체적 오류를 찾았을 때만 답을 바꾸게 한다. 그리고 내 의견과 첫 답변을 보지 않은 새 채팅에서 두 번째 의견을 받는다. SKALA 4기 강의 기록에 나오는 반대 논증자(Devil's Advocate)와 다중 페르소나(CFO 대 COO) 기법도 과도한 동의 대신 적절한 불일치를 끌어내려는 같은 목적을 갖는다 ([SKALA 수강생 블로그](https://stellacustodis.github.io/posts/skala-prompt-engineering/)). 다만 "솔직하게 말해" 같은 사용자 지시가 2025~2026년 최신 모델의 아첨을 줄인다는 통제 연구는 찾지 못했다. 위 방어법은 메커니즘 연구에서 끌어낸 것이다. 모델이 이의 제기 뒤에 "맞습니다"라고 하면 확인이 아니라 독립 검증이 필요하다는 신호로 받아들여야 한다.

### 붙여넣기용 처방과 위험도별 검증 사다리

아래 문구는 저장소에서 바로 쓸 수 있도록 한국어로 옮긴 것이다. '벤더'는 연구소 문서의 기법을 옮긴 것이고, '파생'은 연구 노트 작성자가 연구 결과를 바탕으로 만든 것이다. 파생 문구는 사용자 프롬프트로서 직접 효과가 검증된 적은 없다.

| 대상 | 붙여넣기용 문구 | 근거 |
|---|---|---|
| 오해 | 목표: ___ / 독자: ___ / 쓰일 곳: ___ / 완료 기준: ___ / 형식·분량: ___ / 피할 것: ___ | 파생, [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) |
| 오해 | 답하기 전에 내 요청을 2~3문장으로 다시 말하고, 가정한 점을 나열한 뒤 내 확인을 기다려줘. | 파생, [RaR](https://arxiv.org/abs/2311.04205), [Laban](https://arxiv.org/abs/2505.06120) |
| 오해 | 중요한데 불분명한 점이 있으면 최대 3개까지 먼저 질문하고, 명확하면 바로 진행해. | 파생, [Zhang & Choi](https://arxiv.org/abs/2311.09469), [CLAMBER](https://arxiv.org/abs/2405.12063) |
| 오해 | (대화가 꼬였을 때) 지금까지 내가 말한 내용을 하나로 정리해줘. → 결과를 새 채팅에 붙여넣기 | [Laban 7.4절](https://arxiv.org/html/2505.06120v1) |
| 누락 | 필수 요구사항: 1) … 2) … 3) … 끝에 '요구사항 번호 / 반영 여부 / 답변 내 위치' 표를 붙여줘. | 파생, [ManyIFEval](https://arxiv.org/abs/2509.21051), [IFScale](https://arxiv.org/abs/2507.11538) |
| 누락 | (문서를 앞에, 질문을 뒤에 두고) 먼저 질문과 관련된 구절을 그대로 인용하고, 그 인용만으로 답해줘. | 벤더, [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) |
| 누락 | 문서의 모든 섹션을 순서대로 한 줄씩 정리해줘. 관련 내용이 없으면 '없음'이라고 쓰고 건너뛰지 마. | 파생, [Lost in the Middle](https://arxiv.org/abs/2307.03172) |
| 누락 | 생략하거나 줄이거나 확신이 없었던 부분을 모두 적어줘. | 파생 |
| 누락 | 먼저 목차를 쓰고, 한 섹션씩 작성하자. | [LongWriter](https://arxiv.org/abs/2408.07055) |
| 지어냄(환각) | 모르거나 자료에 없으면 '모른다'고 답해. 추측보다 그게 낫다. | 벤더, [Anthropic](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations), [Kalai](https://arxiv.org/abs/2509.04664) |
| 지어냄(환각) | 질문과 관련된 정확한 인용을 번호 붙여 먼저 뽑고, 답할 때 인용 번호를 달아줘. 관련 인용이 없으면 '관련 인용 없음'이라고 써. | 벤더, [Anthropic](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) |
| 지어냄(환각) | 초안을 쓴 뒤 주장마다 뒷받침 인용을 찾고, 인용이 없는 주장은 지운 뒤 그 자리에 [ ] 표시를 남겨. | 벤더, [Anthropic](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) |
| 지어냄(환각) | 답변의 사실 주장을 나열하고, 주장마다 확인 질문을 하나씩 만들어 따로 답한 뒤 수정된 최종 답을 줘. | [CoVe](https://arxiv.org/abs/2309.11495) |
| 지어냄(환각) | 핵심 주장마다 [출처 확인] / [기억에 의존] / [불확실] 꼬리표를 달아줘. | 파생, [Kalai](https://arxiv.org/abs/2509.04664) |
| 지어냄(환각) | URL이나 DOI로 확인할 수 있는 참고문헌만 제시하고, 기억으로 만든 참고문헌은 쓰지 마. → 모든 링크를 직접 열어 확인 | 파생, [Walters & Wilder](https://www.nature.com/articles/s41598-023-41032-5) |
| 아첨 | (작성자와 내 의견을 밝히지 않고) 이 초안을 평가해줘. 가장 큰 약점 3가지를 먼저, 강점은 그다음에. | 파생, [Sharma](https://arxiv.org/abs/2310.13548) |
| 아첨 | 누가 맞다고 가정하지 말고 처음부터 다시 풀어줘. 구체적인 오류를 찾은 경우에만 답을 바꾸고, 그 오류를 보여줘. | 파생, [FlipFlop](https://arxiv.org/abs/2311.08596) |
| 검증 | 회의적인 검토자로서 이 답변에서 가장 가능성 높은 오류 5개와 각각을 확인하는 방법을 적어줘. | 파생, [CoVe](https://arxiv.org/abs/2309.11495) |

검증에 드는 노력은 위험도에 비례해야 한다. 아래 사다리는 위 출처들을 종합한 연구 노트의 제안이다. 브레인스토밍이나 초안처럼 위험이 낮으면 훑어 읽고 생략하거나 불확실한 부분을 물으면 된다. 업무 문서처럼 중간이면 요구사항 대조표, 내 자료에 근거한 인용-또는-철회, 새 채팅에서 받는 두 번째 의견 한 번을 더한다. 법률·의료·재무·공개 발표처럼 위험이 높으면 모든 인용을 직접 열고, 핵심 주장마다 다른 독립 출처를 찾아보는 교차 읽기(Lateral reading)를 한다 ([Civic Online Reasoning](https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/)). 숫자는 스프레드시트나 코드로 다시 계산하고, 코드는 실행하고 테스트하며, 텍스트는 원자적 사실로 쪼개 하나씩 확인한다 ([FActScore](https://arxiv.org/abs/2305.14251)). 같은 모델이 동의했다는 것은 증거로 쓰지 않는다. 사람의 경계심도 변수다. 고품질 AI를 받은 채용 담당자는 오히려 몰입이 떨어져 더 나쁜 결정을 내렸다. 운전대에서 조는 현상이다 ([One Useful Thing](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)). 319명의 지식 노동자 조사에서는 AI에 대한 신뢰가 높을수록 비판적 사고를 덜 했다 ([Lee et al., CHI 2025](https://www.microsoft.com/en-us/research/?p=1135061)). CS50 학생의 69%는 비판적으로 생각하라는 안내를 받고도 AI의 정확성에 자신감을 보였다 ([CS50 SIGCSE 2024 논문](https://cs.harvard.edu/malan/publications/V1fp0567-liu.pdf)). 모델이 좋아질수록 검증 습관은 느슨해지기 쉬운데, 증거는 오히려 더 엄격해져야 한다고 말한다.

## 4. 프롬프트 한 줄보다 맥락 설계와 검증 루프가 결과를 좌우한다

### 맥락 엔지니어링: 가장 작은 고신호 토큰 집합을 고르는 일

2025년 6월 말 Shopify CEO 토비 뤼트케(Tobi Lütke)가 '프롬프트 엔지니어링'보다 '맥락 엔지니어링'이라는 말이 좋다고 했고, 카파시가 동의했다. 카파시는 이를 다음 단계에 딱 맞는 정보로 맥락 창을 채우는 기술로 설명했다 ([Simon Willison, 2025-06-27](https://simonwillison.net/2025/Jun/27/context-engineering/); [Karpathy X 게시물](https://x.com/karpathy/status/1937902205765607626); [Tobi Lütke X 게시물](https://twitter.com/tobi/status/1935533422589399127)). 윌리슨은 많은 사람이 '프롬프트 엔지니어링'을 챗봇에 타이핑하는 일 정도로 받아들이기 때문에 새 용어가 이길 것이라고 봤다. Anthropic의 2025년 9월 글은 맥락 엔지니어링을 이렇게 정의한다. 시스템 프롬프트·도구·MCP·외부 데이터·대화 이력처럼 추론 시점에 모델이 보는 토큰 집합을 매 호출마다 최적으로 큐레이션하는 반복 작업이다. 프롬프트 엔지니어링은 그 앞 단계, 즉 일회성 지시문 작성에 초점을 둔 활동으로 자리매김된다. 같은 글은 맥락 부패도 설명한다. 토큰이 늘수록 회상력은 절벽이 아니라 경사처럼 떨어지므로 맥락은 유한한 주의 예산이다. 그래서 지도 원리는 원하는 결과를 낼 가능성을 가장 높이는 **가장 작은 고신호 토큰 집합**이다 ([Anthropic, Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). 시스템 프롬프트는 깨지기 쉬운 if-else 하드코딩과, 맥락을 공유한다고 가정하는 모호한 지침 사이의 '적정 고도'로 쓴다. 최소한으로 시작해, 실패가 관찰될 때만 지시와 예시를 더한다. 긴 작업에는 세 가지 기법을 쓴다. 대화를 요약해 다시 시작하는 압축(Compaction), NOTES.md나 할 일 목록 같은 구조화된 노트, 그리고 깨끗한 맥락에서 일하고 1,000~2,000토큰짜리 요약만 돌려주는 하위 에이전트다.

메모리 파일에 대한 권고는 벤더를 가리지 않고 수렴한다. CLAUDE.md는 매 세션 로드되므로 모든 줄이 모든 작업에서 주의를 조금씩 소모한다. 그래서 정확한 테스트·린트 명령, 코드가 오해를 부르는 지점, 저장소에 기록되지 않은 팀 결정, 두 번 이상 고친 것만 넣고 200줄 이하로 유지하라고 한다 ([Claude Code](https://code.claude.com/docs/en/best-practices)). AGENTS.md는 리눅스 재단 산하 Agentic AI Foundation이 관리하는 개방형 표준이다. 사이트는 6만 개 이상의 오픈소스 프로젝트가 쓴다고 밝힌다. 편집 중인 파일에서 가장 가까운 AGENTS.md가 우선하고, 사용자의 명시적 채팅 지시는 그 모두를 덮어쓴다 ([agents.md](https://agents.md/)). Codex는 같은 실수가 두 번 반복될 때만 규칙을 추가하라고 한다 ([OpenAI Codex best practices](https://learn.chatgpt.com/guides/best-practices)). 짧게 유지하고, 반복된 실수 뒤에만 추가하고, 가까운 파일이 우선하고, 긴 절차는 스킬로 옮기라는 것이다. 세 출처가 독립적으로 같은 결론에 이르므로 벤더 중립적 권고로 삼아도 된다(Claude Code가 AGENTS.md를 기본으로 읽는지는 확인하지 못했다). 주제가 바뀌면 새 채팅을 열라는 조언은 MIT Sloan, 카파시, Claude Code, Codex에서 모두 나온다 ([MIT Sloan](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/); [카파시 How I use LLMs 요약](https://tuananhbui89.github.io/blog/2025/karpathy-lec09); [Codex](https://learn.chatgpt.com/guides/best-practices)). 2026년에는 1M 토큰 창과 자동 압축 덕분에 맥락이 모자랄 일이 드물다. 그래도 Claude Code 문서는 더 나은 답과 비용 절감을 위해 집중된 맥락을 권한다. 2025년에서 2026년 사이 강조점은 '창이 넘치지 않게 관리하라'에서 '관련성과 비용을 관리하라'로 옮겨갔다. 카파시의 LLM Wiki 패턴은 개인 차원의 맥락 엔지니어링이다. LLM이 원자료를 바탕으로 서로 연결된 마크다운 지식 베이스를 조금씩 유지하는 방식으로, 질의 사이에 아무것도 쌓이지 않는 단순 RAG의 대안으로 제시된다 ([Karpathy llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)).

### 체이닝과 다섯 가지 패턴: 가장 단순한 것부터

Anthropic의 '효과적인 에이전트 구축'(2024-12-19)은 두 가지를 구분한다. 미리 정한 코드 경로로 LLM을 엮는 워크플로(Workflow)와, LLM이 스스로 과정과 도구 사용을 결정하는 에이전트(Agent)다. 그리고 가능한 한 가장 단순한 해법을 찾고, 필요할 때만 복잡도를 높이라고 한다 ([Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)). 다섯 패턴은 다음과 같다. 순차 호출 사이에 점검 관문을 두는 프롬프트 체이닝(Prompt chaining), 입력을 분류해 전문 프롬프트나 모델로 보내는 라우팅(Routing), 독립된 하위 작업을 동시에 돌리거나(섹셔닝) 같은 작업을 여러 번 돌리는(투표) 병렬화(Parallelization), 중앙 LLM이 일을 분해·위임·종합하는 오케스트레이터-워커(Orchestrator-workers), 생성과 평가를 번갈아 반복하는 평가자-최적화자(Evaluator-optimizer)다. 비개발자도 채팅 화면에서 그대로 쓸 수 있다. 목차→내가 확인→초안→체크리스트 비판→수정을 별도 턴으로 나누면 체이닝이다. 같은 질문을 2~3번, 혹은 다른 모델에 돌려 답이 갈리는 곳을 찾으면 투표다. 기준을 좁힌 두 번째 채팅이 초안을 비판하게 하면 평가자-최적화자다. 이 대응은 연구 노트의 종합이며 벤더가 권고한 것은 아니다. 카파시의 llm-council은 투표와 평가를 실제로 구현한 예다. 여러 모델이 각자 답하고, 익명화된 서로의 답에 순위를 매긴 뒤, 의장 모델이 최종 답을 쓴다 ([karpathy/llm-council](https://github.com/karpathy/llm-council)).

2026년 Anthropic 문서는 적응형 사고와 하위 에이전트 덕분에 Claude가 다단계 추론 대부분을 내부에서 처리한다고 본다. 그래도 중간 산출물을 검사하거나 파이프라인을 강제해야 할 때는 명시적 체이닝이 여전히 유용하다. 가장 흔한 사슬은 초안→기준 대비 검토→수정으로 이어지는 자기 교정이다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). 다중 에이전트는 비싸다. Anthropic 리서치 시스템에서 Opus 4 리드와 Sonnet 4 하위 에이전트 조합은 내부 평가에서 단일 Opus 4보다 **90.2%** 앞섰지만, 채팅보다 약 **15배**의 토큰을 썼다. Anthropic은 공유 맥락이 필요하거나 의존성이 많은 작업, 그리고 병렬화할 부분이 적은 대부분의 코딩에는 다중 에이전트가 맞지 않는다고 밝혔다 ([Anthropic, multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)). Claude Code 문서도 정리한다. 같은 일을 하위 에이전트에 넘긴다고 더 똑똑한 답이 나오지는 않는다. 도움이 되는 것은 작성 과정을 보지 않은 새 리뷰어다 ([Claude Code](https://code.claude.com/docs/en/best-practices)).

### 명세→계획→실행→검증→반영: 에이전트 코딩의 합의된 루프

Claude Code 문서에 따르면 실망스러운 세션의 원인은 거의 항상 넷 중 하나다. 저장소에서 얻을 수 없는 정보가 없었거나, 자기 작업을 확인할 수단이 없었거나, 예외 없이 지켜야 할 규칙이 하네스로 강제되지 않았거나, 기본 설정이 작업 가치보다 많은 시간·토큰·확인을 요구한 경우다. 이 문서는 지시를 두 종류로 나눈다. 프롬프트·CLAUDE.md·스킬은 모델이 따를지 말지 판단하는 비결정적 지시다. 훅·거부 규칙·관리형 설정·테스트·CI는 하네스가 매번 강제하는 결정론적 지시다. 결정론적 장치는 프로젝트 고유의 '항상'과 '절대' 규칙에만 쓴다 ([Claude Code](https://code.claude.com/docs/en/best-practices)). 하버드 CS50의 경험이 이 구분을 뒷받침한다. 정교한 시스템 프롬프트로 정답 코드를 주지 말라고 지시해도, CS50 덕(Duck)은 코드를 검사·거부하는 별도 코드를 둔 지금도 응답의 최대 4분의 1에서 코드 블록을 보인다. 데이비드 말란은 프롬프트만으로는 대개 충분하지 않다고 말한다 ([Harvard Gazette, 2026-09-25](https://news.harvard.edu/gazette/story/2026/09/taming-the-duck-for-starters/)).

| 단계 | 할 일 | 근거 |
|---|---|---|
| 0. 준비 | 짧은 CLAUDE.md·AGENTS.md(명령어·함정·결정·반복 수정), 비밀 파일 거부 규칙, 샌드박스, 기본 승인 모드, 병렬 작업용 git worktree | [Claude Code](https://code.claude.com/docs/en/best-practices); [Codex](https://learn.chatgpt.com/guides/best-practices); [agents.md](https://agents.md/) |
| 1. 명세(Specify) | 목표·맥락·제약·완료 기준. 요구가 흐릿하면 AI가 나를 인터뷰해 SPEC.md로 정리 | [Codex](https://learn.chatgpt.com/guides/best-practices); [Claude Code](https://code.claude.com/docs/en/best-practices) |
| 2. 계획(Plan) | 다단계 작업은 계획 모드(plan mode)로 계획부터 검토. 절차의 무게는 작업 크기에 맞춤 | [Codex](https://learn.chatgpt.com/guides/best-practices); [Böckeler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) |
| 3. 실행(Execute) | 새 세션에서, 돌려볼 수 있는 확인 수단(테스트·타입체크·스크린샷)을 기준으로 구현. 레드/그린 TDD | [Claude Code](https://code.claude.com/docs/en/best-practices); [Willison, Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/) |
| 4. 검증(Verify) | 증거(실행한 명령과 출력, 스크린샷) 요구. 대화를 보지 않은 새 리뷰어가 명세 대비 정확성만 검토. 사람이 직접 테스트 | [Claude Code](https://code.claude.com/docs/en/best-practices); [Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) |
| 5. 반영(Learn) | 직접 읽은 코드만 담은 작은 PR. 반복 실수는 메모리 파일로, 반복 프롬프트는 스킬로, 예외 없는 규칙은 훅·거부 규칙으로 | [Willison, Anti-patterns](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/); [Codex](https://learn.chatgpt.com/guides/best-practices) |

검증 단계의 세부 지침은 이렇다. 테스트 파일, 빌드 종료 코드, 린터, 출력을 기준 파일과 비교하는 스크립트, 목업과 비교하는 스크린샷처럼 통과·실패를 돌려주는 것이면 무엇이든 확인 수단이 된다. 그리고 '테스트 다 통과했어요'라는 말이 아니라 실행한 명령과 그 출력이라는 증거를 요구한다. 리뷰어에게는 정확성에 영향을 주는 빈틈만 보고하고 스타일은 건너뛰라고 시킨다. 문제를 찾으라고 지시받은 리뷰어는 언제나 뭔가를 찾아내고, 그 지적을 모두 고치다 보면 과잉 설계로 이어지기 때문이다 ([Claude Code](https://code.claude.com/docs/en/best-practices)). 무인 실행 전에는 다섯 가지를 확인한다. 완료가 어떤 모습인지 아는가, 스스로 확인할 수 있는가, 무엇을 건드려도 되는가, 무엇이 멈추게 하는가(턴 수·비용 상한), 결과는 어디로 가고 누가 승인하는가. Codex도 목표·맥락·제약·완료 기준 템플릿을 제시하고, 지속되는 규칙을 프롬프트에 두는 것, 빌드·테스트 방법을 알려주지 않는 것, 다단계 작업에서 계획을 건너뛰는 것, 워크플로를 이해하기 전에 전체 권한을 주는 것을 흔한 실수로 꼽는다 ([Codex](https://learn.chatgpt.com/guides/best-practices)). 여러 세션에 걸친 장기 작업에 대해 Anthropic은 첫 세션의 초기화 에이전트가 init 스크립트, 진행 로그, 모든 기능을 '실패'로 시작하는 JSON 기능 목록을 만들게 하라고 한다. 이후 세션은 기능을 하나씩 완성하며 메모를 남긴다. JSON을 쓴 이유는 모델이 마크다운보다 덜 덮어쓰기 때문이다 ([Anthropic, Effective harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)). 테스트 통과에 매달려 값을 하드코딩하는 경향도 경고 대상이다. 테스트는 정확성을 확인하는 수단이지 해법을 정의하는 것이 아니라고 알려주고, 테스트가 틀렸다고 판단되면 우회하지 말고 보고하게 해야 한다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)).

명세 주도 개발(Spec-driven development, SDD)은 이 루프를 정형화한 도구다. GitHub Spec Kit은 constitution→specify→plan→tasks→implement→converge 명령을 제공하지만, README는 이 과정들이 필수 단계가 아니라 독립된 진입점이며 필요를 충족하는 가장 작은 변경부터 시작하라고 한다 ([github/spec-kit](https://github.com/github/spec-kit)). Thoughtworks의 Birgitta Böckeler는 경고한다. Kiro는 작은 버그 하나를 사용자 스토리 4개와 인수 기준 16개로 부풀렸고, 에이전트는 명세 메모를 무시하거나 원칙을 과잉 적용했으며, 이는 통제하고 있다는 착각을 줄 수 있다 ([Böckeler, martinfowler.com](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)). 바이브 코딩(Vibe coding)과의 경계도 분명해졌다. 카파시는 2025년 2월 분위기에 완전히 몸을 맡기고 코드가 존재한다는 사실조차 잊는 방식을 바이브 코딩이라 불렀다 ([Karpathy X 게시물](https://x.com/karpathy/status/1886192184808149383)). 윌리슨은 바이브 코딩을 'AI가 쓴 코드를 검토하지 않는 것'으로 좁게 정의한다. 검토하고 테스트하고 이해한 LLM 보조 작업은 그냥 소프트웨어 개발이며, 자신은 남에게 설명하지 못할 코드는 커밋하지 않는다고 말한다 ([Willison, 2025-03-19](https://simonwillison.net/2025/Mar/19/vibe-coding/)). 카파시는 2026년 4월 바이브 코딩이 바닥을 높인다면 에이전틱 엔지니어링(Agentic engineering)은 천장을 높인다고 정리했다. 에이전틱 엔지니어는 명세를 쓰고, 계획을 감독하고, diff를 검사하고, 테스트와 평가 루프를 만들고, 권한을 관리하고, worktree를 격리하고, 끝까지 책임지는 사람이다 ([Karpathy, Sequoia Ascent 2026 summary](https://karpathy.bearblog.dev/sequoia-ascent-2026/)). 판단 기준은 도구가 아니라 검토와 검증이다. 다른 사람이 실행하거나, 실제 데이터나 돈을 건드린다면 바이브가 아니라 엔지니어링으로 다뤄야 한다.

### 지식 노동에도 같은 루프가 통한다

같은 패턴이 지식 노동으로 옮겨진다. 리서치에서는 심층 리서치 도구가 오케스트레이터-워커 방식으로 자료를 모으고, 사람이 검증한다. OpenAI는 심층 리서치 출시 당시 이 도구가 사실을 지어내거나 잘못 추론할 수 있고, 권위 있는 정보와 소문을 잘 구분하지 못하며, 확신도 보정이 약하다고 밝혔다. 이 내용은 원문이 403으로 막혀 2차 보도로 확인했다 ([Computing](https://www.computing.co.uk/news/2025/ai/openai-announces-deep-research); [OpenAI 출시 글](https://openai.com/index/introducing-deep-research/)). Anthropic의 리서치 시스템에서는 사람 테스터가 자동 평가가 놓친 문제를 잡아냈다. 시스템이 권위 있는 출처보다 SEO 콘텐츠 농장을 선호했던 것이다 ([Anthropic, multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)). 글쓰기는 목차→초안→기준 대비 비판→수정을 분리된 단계로 진행하고, 비판자의 범위는 정확성과 독자로 좁힌다. 데이터 분석은 모델이 코드를 실행하게 해서 답이 실행 결과에 근거하게 한다. 카파시도 정확한 계산에는 파이썬 인터프리터를 쓰라고 권한다 ([Willison, 2025-03-11](https://simonwillison.net/2025/Mar/11/using-llms-for-code/); [카파시 How I use LLMs 요약](https://mvark.blogspot.com/2025/03/how-i-use-llms-andrej-karpathy.html)). 요약은 인용 추출→인용 기반 요약→주장별 인용→근거 없는 주장 철회의 순서를 따른다. 메타 프롬프팅(Meta-prompting)은 AI가 나를 인터뷰하게 하거나 프롬프트 초안을 쓰게 한 뒤, 실제 입력 5~10개로 시험해 실패를 고치는 것이다. Anthropic Console의 프롬프트 개선기는 2024년 다중 라벨 분류 테스트에서 정확도 30% 향상을 보고했다 ([Anthropic, Prompt improver](https://claude.com/blog/prompt-improver)). 다만 이 도구의 '사전 채우기 추가' 단계는 최신 모델에서는 낡았다. OpenAI의 데이터셋 기반 프롬프트 최적화기는 Evals 플랫폼과 함께 퇴역 중이다. Evals는 2026년 10월 31일 읽기 전용으로 바뀌었고 11월 30일 종료될 예정이다 ([OpenAI, Prompt optimizer](https://developers.openai.com/api/docs/guides/prompt-optimizer)). 안정된 프롬프트는 재사용 단위로 포장한다. Anthropic의 에이전트 스킬(Agent Skills)은 이름과 설명만 시스템 프롬프트에 두고, 필요할 때 SKILL.md 본문과 연결 파일을 읽는 점진적 공개 방식이다. 2025년 12월 개방형 표준으로 공개되었다 ([Anthropic, Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)). 언제 스킬로 만들지는 Codex의 기준이 가장 명료하다. 같은 프롬프트를 계속 재사용하거나 같은 워크플로를 계속 교정하고 있다면 스킬로 만든다 ([Codex](https://learn.chatgpt.com/guides/best-practices)).

### 평가(Evals): 실제 출력을 읽는 데서 시작한다

평가 실무의 합의는 일반 지표가 아니라 오류 분석에서 출발한다는 것이다. Hamel Husain과 Shreya Shankar는 실제 추적 기록(trace)을 읽고, 자유 형식으로 메모하고, 실패 유형으로 묶어 개수를 세는 오류 분석을 평가의 가장 중요한 활동으로 꼽는다. 이들의 권고는 이렇다. 리커트 척도 대신 통과/실패 이진 판정을 쓴다. 약 100개의 추적 기록을 검토하고, 그중 최소 30개는 직접 라벨링한다. LLM 판정자는 사람 라벨과 대조해 참양성률(TPR)과 참음성률(TNR)로 보정한다. BERTScore나 ROUGE 같은 일반 지표는 피한다. 이들은 개발 시간의 60~80%를 오류 분석과 평가에 쓴다고 한다 ([Hamel Husain & Shreya Shankar, Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)). Anthropic의 2026년 1월 글도 같은 방향이다. 실제 실패에서 뽑은 20~50개 과제로 일찍 시작하고, 가능하면 결정론적 채점기를 쓰고, 에이전트가 거친 경로가 아니라 만든 결과를 채점하라고 한다. 예약했다는 말이 아니라 예약이 실제로 데이터베이스에 있는지를 보라는 것이다. 그리고 점수만 믿지 말고 기록을 읽으라고 한다. 이 글은 일관성 지표도 구분한다. k번 중 한 번 이상 성공할 확률(pass@k)과 k번 모두 성공할 확률(pass^k)이다. 시도당 성공률이 75%라면 세 번 연속 성공할 확률은 약 42%다. 최신 모델의 통과율이 0%라면 대개 과제 자체가 잘못된 것이다 ([Anthropic, Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)). 반복 작업이라면 손으로 다듬은 프롬프트를 지표 기반 최적화로 넘길 수 있다. Stanford의 DSPy는 자체 부트스트랩 파이프라인으로 표준 few-shot보다 GPT-3.5에서 25% 이상, llama2-13b-chat에서 65% 이상 좋은 성능을 냈다 ([DSPy](https://arxiv.org/abs/2310.03714)). Prompt Report의 사례 연구에서는 전문가가 약 20시간 수작업으로 F1 0.53에 도달했고, DSPy는 0.548을 기록했다. 저자들은 자동화와 사람의 수정을 결합한 방식이 가장 성공적이었다고 결론지었다 ([Prompt Report](https://arxiv.org/html/2406.06608v6)). 개인 단위로 줄이면 이렇다. 이진 성공 기준 3~5개를 쓰고, 실제 입력 10~20개를 모으고, 출력을 모두 읽고, 변형들을 같은 세트로 비교하고, 통과한 사례를 회귀 세트로 남겨 모델이나 프롬프트를 바꿀 때마다 다시 돌린다. 채점 척도에 대해서는 의견이 갈린다. Anthropic의 옛 Console은 5점 척도를 썼고, Hamel과 Shankar는 이진 판정을 권하며, Anthropic의 2026년 글은 이진·가중·부분 점수를 모두 허용한다.

## 5. 인젝션은 구조로 막고, 자율성은 검증 가능성에 맞춰라

### 프롬프트 인젝션은 미해결이므로 설계로 막는다

프롬프트 인젝션(Prompt injection)은 여전히 풀리지 않았다. LLM은 사용자의 지시와, 자신이 읽는 콘텐츠 속에 숨은 지시를 확실히 구분하지 못한다. 윌리슨의 '치명적 삼중주(lethal trifecta)'는 세 가지가 한 세션에 모이는 상황을 가리킨다. 비공개 데이터 접근, 신뢰할 수 없는 콘텐츠 노출, 외부와 통신할 수 있는 능력이다. 그는 인젝션을 확실히 막는 방법은 알려져 있지 않으며, 공격의 95%를 막는다는 가드레일 제품도 웹 보안 기준으로는 낙제점이라고 지적한다. 사용자가 할 수 있는 유일한 안전책은 세 가지 조합을 피하는 것이다 ([Willison, The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)). Meta의 '에이전트 2의 규칙(Agents Rule of Two)'도 같은 생각이다. 한 세션의 에이전트는 신뢰할 수 없는 입력 처리, 민감한 시스템·비공개 데이터 접근, 상태 변경·외부 통신 가운데 둘까지만 가져야 하고, 셋이 다 필요하면 사람의 승인 없이 자율로 돌려서는 안 된다 ([Meta, Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/)). OWASP LLM01:2025는 직접 인젝션과, 웹 페이지나 파일에 숨은 간접 인젝션을 구분한다. 완화책으로는 모델 행동 제한, 결정론적 코드로 출력 형식 검증, 입출력 필터링, 최소 권한, 고위험 행동에 대한 사람 승인, 외부 콘텐츠의 분리와 표시, 적대적 테스트를 든다 ([OWASP LLM01:2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)). 도구 차원에서는 Claude Code의 거부 규칙(예: `.env` 읽기 금지)이 모든 권한 모드에서 유지된다. 한계도 있다. 읽기 거부는 `cat .env`는 막지만 그 파일을 여는 스크립트는 막지 못하고, 웹 접근 거부는 샌드박스를 켜지 않으면 `curl`을 막지 못한다. 자동 모드는 분류기라서 틀릴 수 있다. 그래서 '절대' 규칙은 거부 규칙이나 훅에 두고, 비밀 스캔 훅은 실패하면 차단하도록 설정하라고 한다 ([Claude Code](https://code.claude.com/docs/en/best-practices)). 에이전트 프롬프트에 넣을 가역성 기준은 이렇다. 되돌릴 수 있는 로컬 작업은 진행해도 된다. 파일 삭제처럼 파괴적이거나, force-push처럼 되돌리기 어렵거나, 푸시·댓글·메시지처럼 남에게 보이는 행동은 먼저 묻는다 ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). 공급망도 위험하다. 스킬은 신뢰할 수 있는 출처에서만 설치하고 덜 믿을 만한 것은 감사해야 하며 ([Anthropic, Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)), Spec Kit 커뮤니티 카탈로그 등재는 감사나 보증이 아니다 ([github/spec-kit](https://github.com/github/spec-kit)). 비밀과 개인정보에 대해서는 윌리슨이 바이브 코딩의 주의 사항으로 비밀 노출과 개인 데이터 취급을 든다 ([Willison, 2025-03-19](https://simonwillison.net/2025/Mar/19/vibe-coding/)). 행정안전부의 ChatGPT 활용 가이드도 저작권·개인정보·중요정보 유출·답변 신뢰성을 주의 사항으로 다룬다는 보도가 있다 ([korea.kr, 검색 스니펫만](https://m.korea.kr/briefing/pressReleaseView.do?newsId=156566491)). 개인정보·회사 정책에 관한 1차 출처(OWASP LLM02, NIST AI RMF 등)는 이번 조사에서 확인하지 않았다.

### 자율성은 검증 가능성과 가역성에 비례시킨다

카파시는 2025년 6월 YC 강연에서 '부분 자율성' 앱과 자율성 슬라이더를 주장했다. 완전 자율 로봇이 아니라 사람을 증강하는 '아이언맨 슈트'를 만들라는 것이다. 이 내용은 2차 요약으로 확인했다 ([ikyle.me 강연 요약](https://ikyle.me/blog/2025/andrej-karpathy-software-is-changing-again); [YouTube, Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ)). 그는 AI를 짧은 목줄에 묶어 작은 단위로 일하라고 했다 (Business Insider 보도, AOL 재게시본. 2026-11-09 재확인 시 링크 만료). 2026년에는 2025년 12월 무렵 에이전트 출력이 눈에 띄게 신뢰할 만해졌다며 기능·리팩터링 같은 '거시 행동'을 위임하는 쪽으로 무게를 옮겼다 ([Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/)). 그러나 명세, 검증, 사람의 이해라는 상수는 그대로다. Claude Code의 권한 사다리는 수동 승인, 자동 모드, 사전 승인 도구만 쓰는 모드, 일회용 컨테이너에서만 쓸 우회 모드로 이어진다. 수동 승인은 열 번째 확인쯤부터 읽지 않고 승인하는 승인 피로가 생긴다. 자동 모드는 연속 3회 또는 누적 20회 차단되면 멈춘다 ([Claude Code](https://code.claude.com/docs/en/best-practices)). 연구 노트가 종합한 결정 규칙은 다음과 같다. 성공을 자동으로 확인할 수 있고, 행동을 되돌릴 수 있고(샌드박스·worktree·브랜치), 위험이 낮고, 치명적 삼중주가 없을 때 자율성을 높인다. 하나라도 충족하지 못하면 단계별 검토로 돌아간다.

AI를 덜 쓰거나 쓰지 말아야 할 때도 있다. BCG 컨설턴트 758명이 참여한 '들쭉날쭉한 프런티어(Jagged frontier)' 실험에서, AI 능력 범위 안의 과제에서는 GPT-4 사용자가 과제를 **12.2%** 더 완료하고 **25.1%** 더 빨랐으며 품질이 **40%** 높았다. 하지만 범위 밖의 과제에서는 AI 없이 84%가 정답을 냈는데 AI 사용자는 60~70%만 맞혔다. 이 수치는 HBS·INFORMS 원문 페이지가 막혀 공저자 몰릭의 글과 2차 보도로 확인했다 ([One Useful Thing](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged); [Organization Science DOI](https://doi.org/10.1287/orsc.2025.21838)). METR의 무작위 연구에서는 숙련된 오픈소스 개발자 16명이 자기가 잘 아는 저장소의 실제 이슈 246개를 다뤘다. AI를 허용하자 이들은 **19% 느려졌다.** 시작 전에는 24% 빨라질 것으로 예상했고, 끝난 뒤에도 20% 빨라졌다고 믿었다. METR 페이지는 이 결과가 이제 낡았다고 밝히며 2026년 2월 업데이트로 연결하는데, 업데이트의 수치는 확인하지 않았다 ([METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)). Stanford AI Index 2026은 같은 들쭉날쭉함을 대규모로 보여 준다. 에이전트의 Terminal-Bench 성공률은 20%에서 77.3%로 뛰었지만, AI는 여전히 시계 읽기와 다단계 계획에서 뒤처진다 ([Stanford HAI, AI Index 2026](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report)). 정리하면 이런 경우에는 AI를 덜 써야 한다. 출력을 검증할 수 없는데 위험이 높을 때, 과제가 프런티어 밖일 가능성이 클 때, 전문가가 익숙한 코드에서 작은 작업을 할 때, 데이터가 기밀이거나 정책상 제한될 때, 목적이 자기 실력을 기르는 것일 때, 그리고 프롬프트를 쓰고 출력을 검토하는 것보다 직접 하는 편이 빠를 때다.

### 생각을 외주 주면 배움이 무너진다

학습에서 가장 분명한 인과 증거는 Wharton 주도의 PNAS 연구다. 튀르키예 고등학생 약 1,000명을 대상으로 한 현장 실험에서 ChatGPT 같은 GPT Base는 연습 성적을 48% 올렸지만, 이후 AI 없이 치른 시험 성적을 **17%** 떨어뜨렸다. 정답 대신 힌트를 주도록 설계한 GPT Tutor는 연습 성적을 127% 올리면서도 시험 성적을 해치지 않았다 ([Knowledge at Wharton](https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/); [PNAS 서지](https://econpapers.repec.org/RePEc:nas:journl:v:122:y:2025:p:e2422633122)). 48%와 127%는 2024년 워킹페이퍼 보도에서 나온 수치이고, PNAS 초록으로 확인된 것은 17% 감소다. 하버드 CS50은 이 교훈을 정책으로 만들었다. 자체 AI인 CS50 덕은 해답을 바로 주지 않고 해답 쪽으로 안내하도록 설계되었고, 답을 대신 써 주는 상용 AI는 과제에 쓸 수 없다 ([CS50x 학업 정직성 정책](https://cs50.harvard.edu/x/honesty/); [CS50 SIGCSE 2024 논문](https://cs.harvard.edu/malan/publications/V1fp0567-liu.pdf)). MIT 미디어랩의 프리프린트 'Your Brain on ChatGPT'는 참가자 54명 가운데 LLM으로 에세이를 쓴 집단이 뇌 연결성이 가장 약하고, 글에 대한 주인의식이 가장 낮고, 자기 글을 인용하는 데 어려움을 겪었다고 보고했다. 먼저 혼자 쓰고 나중에 LLM을 쓴 집단은 회상과 활성화가 더 높았다 ([arXiv 2506.08872](https://arxiv.org/abs/2506.08872)). 다만 표본 크기와 EEG 방법론을 지적하는 공식 논평이 나와 있으므로 논쟁 중인 초기 신호로 다뤄야 한다 ([Comment, arXiv 2601.00856](https://arxiv.org/abs/2601.00856)). 실무 원칙은 이렇다. 먼저 생각하거나 초안을 쓰고 나서 AI를 쓴다. 배우는 중이라면 답이 아니라 힌트·설명·퀴즈를 요청한다. 카파시의 말이 이 원칙을 요약한다. "You can outsource your thinking, but you can't outsource your understanding." ([Karpathy, Sequoia Ascent 2026 summary](https://karpathy.bearblog.dev/sequoia-ascent-2026/))

## 6. 연구소·대학·카파시는 다른 길로 같은 결론에 도착했다

네 부류의 출처는 서로 다른 방법으로 같은 결론에 이른다. 연구소는 자사 모델에서 효과가 있었던 지시를 살아 있는 문서로 갱신한다. 대학은 통제 실험과 현장 실험으로 일반화 가능성을 검증한다. 카파시와 실무자들은 매일의 사용 경험에서 원칙을 뽑는다. 이 셋이 겹치는 지점, 즉 명확한 명세·관련 맥락·돌려볼 수 있는 확인·사람의 최종 책임이 저장소가 가장 자신 있게 가르칠 수 있는 내용이다. 엇갈리는 지점은 역할 프롬프트(연구소는 권장, Wharton은 정확도 효과 없음)와 CoT(MIT Sloan은 추론 노출용으로 권장, 연구소는 추론 모델에 불필요) 정도다. 두 경우 모두 '어떤 목적에 쓰는가'를 구분하면 해소된다.

| 출처 | 대표 자료 | 핵심 메시지 | 증거의 성격 |
|---|---|---|---|
| Anthropic | [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), [맥락 엔지니어링](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [Claude Code](https://code.claude.com/docs/en/best-practices), [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) | 명확·직접, 이유 설명, 예시 3~5개, 문서는 앞에 질문은 뒤에, 인용 먼저, 과잉 강조 제거, 결정론적 강제 | 살아 있는 문서, 대부분 날짜 없음. 30% 같은 자사 수치는 독립 재현되지 않음 |
| OpenAI | [Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering), [GPT-5.6](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6), [추론 모범 사례](https://developers.openai.com/api/docs/guides/reasoning-best-practices), [Codex](https://learn.chatgpt.com/guides/best-practices) | 추론 모델은 목표를 주면 알아서 하는 선배 동료처럼, 목표와 성공 기준, 간결한 프롬프트, 절대 표현은 불변 조건에만, 평가 먼저 | 모델 세대별 문서. GPT-4.1·GPT-5 가이드는 아카이브됨 |
| Google | [Prompt design strategies](https://aistudio.google.com/docs/prompting-strategies), [Kaggle 백서](https://www.kaggle.com/whitepaper-prompt-engineering) | 일관된 구조, 맥락은 먼저 질문은 나중에, 예시를 항상, 샘플링 매개변수는 기본값 | 백서는 2025년 기준이라 매개변수 조언이 일부 낡음 |
| Microsoft | [Foundry 프롬프트 기법](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering) | 다섯 요소, 끝에서 지시 반복, 출처 인용 요구 | GPT-4 기반 테스트. 추론 모델에는 비권장이라는 배너 |
| MIT | [Sloan 가이드](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/), [NANDA 보고서](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf) | 네 요소, 새 주제엔 새 채팅, 인용 확인은 필수, 기업 실패의 원인은 맥락·학습 부재 | 기관 가이드. NANDA는 동료 심사를 거치지 않은 예비 보고서 |
| Harvard | [Jagged frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged), [Cybernetic Teammate](https://www.nber.org/papers/w33641), [CS50](https://cs.harvard.edu/malan/publications/V1fp0567-liu.pdf) | 프런티어 안에서는 큰 이득이지만 밖에서는 정확도 하락, 프롬프트만으로는 행동 강제가 부족 | 현장 실험(일부 2차 확인), SIGCSE 동료 심사 |
| Wharton | [Prompting Science Reports](https://arxiv.org/abs/2503.04818), [PNAS 학습 연구](https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/), [Mollick](https://www.oneusefulthing.org/p/getting-started-with-ai-good-enough) | 요령은 일반화되지 않음, 형식·맥락·예시·평가에 투자, 가드레일 없는 AI는 학습을 해침 | 벤치마크 프리프린트, PNAS 동료 심사 |
| Stanford | [법률 환각](https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries), [AI Index 2026](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report), [DSPy](https://arxiv.org/abs/2310.03714) | RAG 도구도 17~34% 환각, 능력은 들쭉날쭉, 반복 작업은 프로그램적으로 최적화 | 동료 심사(JELS), 기관 보고서 |
| 카파시 | [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw), [2025 Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/), [Sequoia 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/) | 모델 확인, 새 채팅, 자료 붙여넣기, 도구 사용, 작은 단위 검증, 명세 먼저, 이해는 외주 불가 | 영상·블로그. 일부는 2차 요약 |
| 실무자 | [Willison](https://simonwillison.net/guides/agentic-engineering-patterns/), [Hamel Husain](https://hamel.dev/blog/posts/evals-faq/), [Böckeler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html), [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | 설명할 수 없는 코드는 커밋하지 않음, 오류 분석 우선, SDD 과잉 경계, 전문가가 오히려 느려지는 사례 | 실무 경험, 무작위 대조 연구 |

학술 연구에는 생산성의 분포에 관한 일관된 결과도 있다. BCG 실험에서 평균 이하 성과자는 43%, 평균 이상 성과자는 17% 향상되었다 ([One Useful Thing](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)). 고객 상담원 5,172명을 다룬 QJE 연구에서 AI 보조는 시간당 해결 건수를 약 15% 늘렸는데, 경험이 적은 사람은 속도와 품질이 모두 올랐고 가장 숙련된 사람은 품질이 약간 떨어졌다 ([EurekAlert, QJE](https://www.eurekalert.org/news-releases/1071936)). P&G 전문가 776명을 대상으로 한 사전 등록 실험에서는 AI를 쓴 개인(+0.37 SD)이 AI 없는 팀(+0.24 SD)과 같거나 더 높은 수준에 도달했다 ([One Useful Thing, Cybernetic Teammate](https://www.oneusefulthing.org/p/the-cybernetic-teammate)). Noy와 Zhang의 Science 연구에서는 중간 수준의 전문 글쓰기 과제에서 ChatGPT가 시간을 40% 줄이고 품질을 18% 올렸다. 이 수치는 논문 원문을 열지 않고 검색 요약으로 확인했다 ([Science DOI](https://doi.org/10.1126/science.adh2586)). 정리하면 초보자에게는 바닥을 올려 주는 도구이고, 전문가에게는 품질 기준을 지켜야 하는 선택적 도구다. MIT Sloan이 인용하는 '프롬프트보다 문제 정의'라는 관점, 즉 문제와 범위와 경계를 정의하는 능력이 장기적으로 문구 기술보다 중요하다는 주장도 같은 맥락이다 ([MIT Sloan](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/)). Prompt Report도 가장 중요한 교훈으로 프롬프트 작성자와 도메인 전문가의 협업을 꼽는다 ([Prompt Report](https://arxiv.org/html/2406.06608v6)).

카파시의 실용 조언은 2025년 2월 영상 'How I use LLMs'에 가장 잘 정리되어 있다. 다만 이 보고서는 영상을 직접 보지 않았고, 서로 일치하는 제3자 요약에 의존한다 ([Tuan-Anh Bui 요약](https://tuananhbui89.github.io/blog/2025/karpathy-lec09); [mvark 요약](https://mvark.blogspot.com/2025/03/how-i-use-llms-andrej-karpathy.html)). 요약에 따르면 그는 다음을 권한다. 마케팅 대신 리더보드로 모델을 비교하고 지금 UI에서 어떤 모델이 켜져 있는지 확인한다. 주제를 바꿀 때는 새 채팅을 연다. 어려운 수학·논리·코딩에는 사고 모델을, 최신 정보에는 검색을, 정확한 계산에는 파이썬을 쓰고, 심층 리서치 결과는 1차 출처로 검증할 초안으로 다룬다. 2025년 4월 MenuGen 글에서는 모델이 폐기된 API를 제안해서 최신 문서를 대화에 직접 붙여 넣었다고 썼다. 실제로 어려웠던 부분은 배포·비밀 관리·인증·결제였다고 한다 ([Karpathy, Vibe coding MenuGen](https://karpathy.bearblog.dev/vibe-coding-menugen/)). 2025년 연말 회고에서는 검증 가능한 보상 기반 강화학습(RLVR)이 추론 능력을 낳았지만, 모델은 천재 박식가와 쉽게 헷갈리는 초등학생이 한 몸에 있는 들쭉날쭉한 지능이라고 정리했다 ([Karpathy, 2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/)). 2026년 4월에는 '검증 가능성'을 핵심어로 내세웠다. 전통 소프트웨어는 명세할 수 있는 것을 자동화하지만 LLM은 검증할 수 있는 것을 자동화한다. 모델이 많이 훈련된 영역 밖이라면 맥락·도구·평가를 더해야 한다는 것이다 ([Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/)). 그의 원칙이 '목줄'(2025년 6월)과 '에이전트의 10년'(2025년 10월, [Dwarkesh Podcast](https://www.youtube.com/watch?v=lXUZvyajciY))에서 '에이전트 오케스트레이터'(2026년)로 옮겨간 것은 모순이 아니다. 모델이 발전한 결과이고, 명세·검증·이해라는 상수는 바뀌지 않았다.

GitHub 저장소는 별 수가 인기를 보여 줄 뿐 품질을 보장하지는 않는다. 아래 표는 2026년 11월 9일 GitHub API로 확인한 대표 저장소를 저장소 독자층에 맞춰 묶은 것이다. 시스템 프롬프트 유출 모음(x1xhlol, asgeirtj)은 구조를 배우기에는 유익하지만 출처가 불분명한 독점 텍스트이므로 '학습 전용, 출처·저작권 주의'로 표시해야 한다. obra/superpowers의 31만 개 넘는 별은 claude-code 본체보다도 많아서, 플러그인 마켓 설치나 유행이 반영되었을 수 있다.

| 대상 | 저장소 | 별(2026-11-09) | 상태와 용도 |
|---|---|---|---|
| 입문 | [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 79,910 | 활성. 기법 레퍼런스이며 맥락 엔지니어링·에이전트까지 다룸. [한국어판 사이트](https://www.promptingguide.ai/kr/introduction/elements) 있음 |
| 입문 | [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | 39,148 | 활성. 장별 실습(명확성·역할·XML·예시·환각 회피) |
| 입문 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 123,134 | 활성. 21강 입문 커리큘럼 |
| 입문 | [f/prompts.chat](https://github.com/f/prompts.chat) | 176,491 | 활성. 영감 수집용이며 기법 학습용은 아님 |
| 실무 | [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | 25,395 | 에이전트용 README 표준 |
| 실무 | [anthropics/skills](https://github.com/anthropics/skills) | 189,325 | 공식 에이전트 스킬 예시 |
| 실무 | [obra/superpowers](https://github.com/obra/superpowers) | 314,454 | 브레인스토밍→계획→TDD→리뷰를 강제하는 스킬 프레임워크 |
| 실무 | [github/spec-kit](https://github.com/github/spec-kit) | 148,629 | 명세 주도 개발 도구 |
| 실무 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 57,529 | Claude Code 커뮤니티 색인 |
| 실무 | [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) | 13,901 | 맥락 엔지니어링 템플릿 |
| 실무 | [karpathy/llm-council](https://github.com/karpathy/llm-council) | 26,338 | 여러 모델 교차 검증 |
| 빌더 | [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | 27,044 | 2025-09 이후 푸시 없음. 원칙은 유효 |
| 빌더 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) / [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 54,429 / 77,003 | 벤더 레시피 |
| 빌더 | [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) / [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 38,971 / 26,958 | 프로그램적 최적화와 평가 |
| 내부 이해 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | 60,370 | 활성. 폐기된 nanoGPT를 대체 |
| 주의 | [karpathy/LLM101n](https://github.com/karpathy/LLM101n) / [anthropics/courses](https://github.com/anthropics/courses) / [brexhq/prompt-engineering](https://github.com/brexhq/prompt-engineering) | 37,479 / 22,993 / 9,590 | 각각 아카이브(강의 없음) / 아카이브 / 2023년 이후 정체 |

## 7. Pre-SKALA는 '지시 → 결과 검증'을 내걸었지만 강의 내용은 비공개다

SKALA는 SK그룹의 채용 연계형 전일제 대면 AI 교육과정이다. SK AX 보도자료는 'SK AI Leader Academy(스칼라)'라고 부르고, 공식 사이트는 SK가 만든 AI Leader Academy라고 소개한다. 'SK Academy for Leading AI'라는 영문 풀이는 어떤 출처에서도 확인되지 않았다 ([SK AX 뉴스룸, 2026-05-07](https://www.skax.co.kr/company/news-room/sk-ax-skala-%EA%B4%91%EC%A3%BC%C2%B7%EC%9A%B8%EC%82%B0%EC%9C%BC%EB%A1%9C-%ED%99%95%EB%8C%80%ED%95%B4-ai%EC%9D%B8%EC%9E%AC-%EC%9C%A1%EC%84%B1%ED%95%9C%EB%8B%A4); [SKALA 공식 사이트](http://2026skala.co.kr/)). 1기는 2024년 12월 SK C&C가 고용노동부 K-디지털 트레이닝의 일환으로 공고했고, 약 5개월간 약 90명이 프로그래밍·생성형 AI·데이터 분석·머신러닝·클라우드·AI 서비스 개발 프로젝트를 배웠다 ([Byline Network](https://byline.network/2024/12/12-351/)). SK C&C와 SK AX가 사명 변경으로 같은 조직이라는 점은 추론이며, 이번에 가져온 출처가 직접 확인해 주지는 않는다. 4기는 19~34세를 대상으로 2026년 7~12월 판교·광주·울산에서 운영되며, 핵심 영역은 데이터 분석과 AIOps, Cloud Native AI, 생성형 AI 서비스 개발이다. 반도체·에너지·통신의 실제 문제로 팀 프로젝트를 한다. SK AX는 1~2기 수료생 194명 중 80% 이상이 취업했다고 밝혔지만 독립 검증은 없다 ([SK AX 뉴스룸](https://www.skax.co.kr/company/news-room/sk-ax-skala-%EA%B4%91%EC%A3%BC%C2%B7%EC%9A%B8%EC%82%B0%EC%9C%BC%EB%A1%9C-%ED%99%95%EB%8C%80%ED%95%B4-ai%EC%9D%B8%EC%9E%AC-%EC%9C%A1%EC%84%B1%ED%95%9C%EB%8B%A4); [서울대 컴퓨터공학부 공지](https://cse.snu.ac.kr/en/community/notice/25050)).

Pre-SKALA는 SK AX가 주최하고 SK하이닉스가 후원하는 짧은 사전 과정이다. 3주간의 자기주도 온라인 AI 부트캠프와 1박 2일 해커톤으로 구성된다. 500명을 선발했고 온라인 과정 상위 100명만 해커톤(2026년 11월 28~29일, SK AX 판교 캠퍼스)에 초대되며, 혜택은 3년간 유효한 SKALA 입과 우대다 ([Pre-SKALA 공식 페이지](https://2026pre-skala.co.kr/); [서울대 공지](https://cse.snu.ac.kr/en/community/notice/25679)). 공개된 온라인 커리큘럼은 모듈 제목뿐이다. 'Agent 이해와 업무 분석', '바이브코딩 입문'(그 안에 "AI 지시 및 결과 검증"과 'Agent 디버깅 및 설계'), '에이전트 구성 및 실행'(도구 연결·업무지식 설계·자동화·테스트 및 개선), 최종과제 '나만의 Agent 만들기'다. 이 페이지에는 프롬프트·역할·맥락·형식·제약·예시·환각이라는 단어가 한 번도 나오지 않는다. 바이브코딩과 Agent는 나온다 ([Pre-SKALA 공식 페이지](https://2026pre-skala.co.kr/)). **Pre-SKALA의 강의 내용은 공개되지 않았다.** 슬라이드도, 영상도, 모듈 제목 이상의 강의계획서도, 수강생 블로그나 저장소도 찾지 못했다. 2026년 과정은 조사 시점에 아직 진행 중이었다. 따라서 "AI 지시 및 결과 검증" 모듈이 구체적으로 무엇을 가르치는지는 알 수 없다. 이 모듈이 역할·맥락·형식·제약이나 오해·누락·지어냄을 가르친다고 주장해서는 안 된다.

SKALA 본과정의 프롬프트 수업에 대한 유일하게 상세한 공개 기록은 판교 캠퍼스 4기 수강생의 블로그 글이다. 그는 2026년 7월 15일 하루 동안 진행된 생성형 AI 과정의 첫 모듈 'Prompt 설계와 Context'를 이후 LLM·RAG·AI 에이전트 과정의 출발점으로 기록했다 ([SKALA 수강생 블로그](https://stellacustodis.github.io/posts/skala-prompt-engineering/); [원본 마크다운](https://github.com/stellacustodis/stellacustodis.github.io/blob/main/_posts/2026-07-15-skala-prompt-engineering.md)). 기록에 따르면 수업은 생성형 AI 트렌드, 다음 토큰 예측과 환각이라는 한계, 토큰·샘플링 매개변수, RICE 구조, few-shot·CoT·Step-back·Self-Consistency 기법, 맥락 엔지니어링·하네스 엔지니어링 순으로 진행되었다. 중심 틀은 RICE다. Role은 누구처럼 생각할지, Instruction은 어떤 절차로 판단할지, Context는 사고가 허용되는 경계 조건, Example은 출력 견본이 아니라 평가 기준의 표본으로 설명되었다. 여기에 정책·문체·제약과 형식·구조가 추가 요소로 붙었다. 좋은 프롬프트의 핵심은 자세함보다 구조라는 것이 수업의 표어였다. 예시는 최소 3~5개를 권했고, 환각은 내부 정보 부재·적시성과 함께 기업 도입의 세 장애물로 제시되어 RAG와 맥락 엔지니어링의 동기가 되었다. 오해를 막는 장치로는 모델이 먼저 질문하게 하는 소크라테스식 프롬프팅이, 아첨을 막는 장치로는 반대 논증자와 다중 페르소나가 소개되었다. 그 수강생은 슬라이드의 사실 오류(CoT 90.2% 수치의 출처 오기, temperature와 top-p 적용 순서 반전)를 직접 지적하기도 했다. 슬라이드 자체가 권위 있는 자료는 아니라는 뜻이다. 같은 수강생은 입과 전에 AI 에이전트와 바이브 코딩을 연습하지 않은 것을 아쉬워했다 ([SKALA 1개월 회고](https://github.com/stellacustodis/stellacustodis.github.io/blob/main/_posts/2026-08-18-skala-1month-review.md)). 다른 수강생들의 공개 저장소는 AI 에이전트 캡스톤, Spring AI, RAG, 클라우드 모듈의 존재를 확인해 준다 ([skalamok/capstone-v1](https://github.com/skalamok/capstone-v1); [sjjeon0925/skala-springAI-practicecode](https://github.com/sjjeon0925/skala-springAI-practicecode)). 수업 노트를 질문 기반으로 복습하는 학생 제작 스킬도 있다. 학습자들이 이미 에이전트 스킬을 쓰고 있다는 증거다 ([yongchane/skala-review-skill](https://github.com/yongchane/skala-review-skill)).

| 항목 | 공개적으로 확인된 내용 | 확인 수준 |
|---|---|---|
| SKALA의 정체 | SK AX의 채용 연계형 AI 교육(SK AI Leader Academy), 약 5개월, 19~34세 | 공식(보도자료·사이트) |
| SKALA 4기 커리큘럼 | 데이터 분석·AIOps, Cloud Native AI, 생성형 AI 서비스 개발. 상세 커리큘럼은 텍스트 없는 이미지 | 공식(상위 영역만) |
| SKALA 프롬프트 수업 | RICE + 정책·문체·제약 + 형식·구조, few-shot 3~5, CoT, 맥락·하네스 엔지니어링 | 비공식(수강생 1인 기록) |
| Pre-SKALA 구조·일정 | 3주 온라인 + 1박 2일 해커톤, 500명 선발, 상위 100명 | 공식 |
| Pre-SKALA 커리큘럼 | 모듈 제목. "AI 지시 및 결과 검증"이 바이브코딩 입문 안에 있음 | 공식(제목만) |
| Pre-SKALA 강의 내용 | 없음 | **비공개. 추정 금지** |
| 오해·누락·지어냄 3분류 | 어떤 한국어 출처에서도 세트로 발견되지 않음 | 미확인(저장소 고유 틀일 가능성) |
| 역할·맥락·형식·제약 4분류 | 권위 낮은 블로그 검색 스니펫에서만 보임 | 미확인 |

저장소에 주는 함의는 세 가지다. 첫째, 학습자는 영어 RICE나 Google의 '역할·할 일·맥락·형식'을 먼저 접했을 가능성이 높다. 그러니 여섯 요소를 소개할 때 1절의 정렬표로 연결해 주어야 한다. 둘째, Pre-SKALA의 "AI 지시 및 결과 검증"은 공식 한국어 표현 가운데 이 저장소의 '프롬프트 작성 후 검증' 루프에 가장 가깝다. 따라서 저장소의 핵심 루프를 '지시 → 결과 검증'으로 부르면 어휘가 맞아떨어진다. 이것은 어휘의 정렬일 뿐 내용이 일치한다는 주장이 아니다. 셋째, Pre-SKALA와 SKALA는 모두 프롬프트를 에이전트 작업으로 가는 한 단계로 다루고, 대상은 비전공자를 포함한 19~34세다. 그러므로 단독 프롬프트 팁보다 에이전트 워크플로 안의 지시·검증으로 틀을 잡은 자료가 학습자가 곧 마주할 내용과 맞는다. 4절의 바이브 코딩과 에이전틱 엔지니어링의 구분도 이 독자에게 특히 중요하다. 학습자 대부분이 곧 바이브코딩 도구를 쓰게 되기 때문이다.

## 8. 검증된 것과 검증되지 않은 것

이 보고서를 저장소의 근거로 쓰려면 주장마다 확인 수준이 다르다는 점을 알아야 한다. 연구소 문서는 모두 2026년 11월 9일에 직접 가져왔지만 대부분 날짜가 없는 살아 있는 문서다. 모델 이름(Claude Fable 5.1, Opus 5.5, GPT-6 Astra, GPT-5.6 Sol, Gemini 4 등)은 그 공식 페이지에 적힌 그대로 옮겼다. arXiv 논문은 arXiv API로 제목·저자·날짜·초록을 확인했다.

| 주장 또는 자료 | 상태 | 비고 |
|---|---|---|
| 연구소 가이드의 권고 | 1차 출처 확인(2026-11-09) | 자사 수치(질문을 끝에 두면 30%, 간결한 프롬프트로 10~15% 등)는 독립 재현되지 않음 |
| arXiv·학술지 논문 | 초록·서지 확인 | 결과는 대부분 2023~2025년 모델 기준. 메커니즘의 예시로 읽을 것 |
| OpenAI 블로그 수치(SimpleQA 기권율, GPT-4o 아첨 사후 분석) | 2차 확인 | openai.com이 자동 접근을 막아(403) 검색 색인·Georgetown 요약으로 확인 |
| 법원 가짜 판례 건수(약 1,600건 등) | 검색 요약만 | AFP·MSBA·Bloomberg Law 기사 원문을 열지 않음. 시점과 범위마다 수치가 다름 |
| Jagged frontier 수치 | 2차 확인 | HBS·INFORMS 페이지 403. 공저자 몰릭의 글로 확인 |
| Noy & Zhang 40%/18% | 검색 요약 | Science 원문을 열지 않음 |
| Bastani 48%/127% | 워킹페이퍼 보도 | PNAS 초록으로 확인된 것은 −17%뿐 |
| 카파시 'How I use LLMs' 조언 | 제3자 요약 | 영상을 직접 시청하지 않음 |
| 카파시 '에이전틱 엔지니어링' 명명(2026년 2월) | 2차 보도 | 원 게시물 미확인. 날짜(2월 4일 대 8일) 불일치 |
| 카파시 '자율성 슬라이더'·'목줄' | 2차 요약 | 강연 원 녹취를 확보하지 못함 |
| GPT-5.5 가이드 원문 | 확인 불가 | 같은 URL이 지금은 GPT-6 지침을 보여 줌 |
| Google/Kaggle 백서 | 비공식 재게시본으로 확인 | 공식 PDF 텍스트를 추출하지 못함 |
| 'Curse of Instructions'(GPT-4o 15%, Claude 3.5 44%) | 미확인 | OpenReview 접근 차단. 본문에서 제외 |
| MIT 'Your Brain on ChatGPT' | 프리프린트, 논쟁 중 | 공식 논평(arXiv 2601.00856) 있음 |
| MIT NANDA '95% 수익 없음' | 예비·비동료심사 | PDF가 mit.edu가 아니라 mlq.ai에 호스팅됨 |
| METR 19% 감속 | 1차 확인 | 페이지 스스로 결과가 낡았다고 밝힘. 2026년 2월 업데이트 미확인 |
| SKALA 4기 프롬프트 수업 | 비공식 | 수강생 1인 블로그. 다른 캠퍼스·강사는 다를 수 있음 |
| Pre-SKALA 강의 내용 | 비공개 | 모듈 제목만 공식 공개 |
| 오해·누락·지어냄 3분류 | 출처 없음 | 저장소 고유의 교육 틀로 명시할 것 |
| 행정안전부·NIA·부산시 가이드 | 검색 스니펫만 | 1차 PDF 미확보 |
| GitHub 별 수 | API 확인(2026-11-09) | 인기 지표일 뿐이며 별 부풀리기 여부는 평가하지 않음 |
| temperature를 낮추면 환각이 줄어드는가 | 근거 없음 | 정량 출처를 찾지 못함 |
| "솔직하게 말해" 지시가 아첨을 줄이는가 | 근거 없음 | 최신 모델 대상 통제 연구를 찾지 못함 |

## 결론

이 조사가 바꾸는 이해의 핵심은 이렇다. 'AI 활용법'의 단위는 더 이상 좋은 문장이 아니라 **좋은 명세와 좋은 확인 수단의 쌍**이다. 여섯 요소는 신입 직원에게 일을 맡길 때의 체크리스트로 가르치고, 세 가지 실패는 각자의 메커니즘에 맞는 처방으로 가르치는 것이 증거와 맞는다. 오해는 빈칸 메우기와 재시작, 누락은 배치와 대조표, 지어냄은 근거 연결과 외부 검증이다. 여기서 덜 알려진 함의가 하나 나온다. 모델이 좋아질수록 위험의 성격이 바뀐다. 명백한 오류는 줄지만, 그럴듯한 오류와 사람의 방심은 늘어난다. 고품질 AI 앞에서 운전대에서 조는 현상, AI 신뢰가 높을수록 비판적 사고가 줄어드는 상관, 경고를 받고도 꺼지지 않는 학생들의 자신감이 모두 같은 방향을 가리킨다. 그러니 검증 습관은 모델 발전에 맞춰 느슨해지는 것이 아니라 오히려 제도화되어야 한다. 카파시가 말하는 '검증 가능한 것만 자동화된다'는 원리와 Claude Code의 결정론적 강제 원칙은, 개인 사용자에게는 '확인할 방법이 없는 일은 맡기지 말라'는 규칙으로 번역된다.

how-to-use-ai 저장소에 대한 실천적 결론은 세 가지다. 첫째, 연구소 지침은 모델 세대마다 바뀐다(사전 채우기 폐지, temperature 무시, 간결성 기본값 변화). 그러니 모든 팁에 확인 날짜와 '낡은 조언' 라벨을 붙이고, 모델이 바뀌면 프롬프트를 덜어 내고 다시 맞추라고 가르쳐야 한다. 둘째, 저장소의 고유 틀인 오해·누락·지어냄(환각)은 공개 출처가 없다는 점을 밝히는 대신, 각 실패를 이 보고서의 메커니즘 연구에 연결하면 오히려 신뢰를 얻는다. 셋째, SKALA 계열 학습자에게 가장 가치 있는 것은 그들이 곧 쓸 에이전트·바이브코딩 도구 안에서 '지시 → 결과 검증' 루프를 돌리는 구체적 습관이다. Pre-SKALA의 실제 강의 내용은 공개될 때 다시 대조해야 한다.

## 참고문헌

모든 URL은 연구 노트에 기록된 그대로이며, 확인일은 별도 표시가 없으면 2026-11-09다. "검색 스니펫만"은 원문을 열지 않고 검색 결과로만 본 출처다.

### A. 공식 연구소 가이드

**Anthropic**
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) — 살아 있는 문서, 날짜 표시 없음
- [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)
- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- [Effective context engineering for AI agents (2025-09-29)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Building effective agents (2024-12-19)](https://www.anthropic.com/engineering/building-effective-agents)
- [Claude Code: Best practices](https://code.claude.com/docs/en/best-practices) — 옛 주소 https://www.anthropic.com/engineering/claude-code-best-practices 에서 308 리다이렉트
- [How we built our multi-agent research system (2025-06-13)](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Effective harnesses for long-running agents (2025-11-26)](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Demystifying evals for AI agents (2026-01-09)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Equipping agents for the real world with Agent Skills (2025-10-16)](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Introducing Agent Skills](https://www.anthropic.com/news/skills)
- [Prompt improver 블로그 (2024-10-14)](https://claude.com/blog/prompt-improver)
- [Towards understanding sycophancy in language models (2023-10-23)](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models)
- [Prompt engineering overview (옛 docs 주소)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

**OpenAI**
- [Prompt engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering) — 옛 주소 [platform.openai.com](https://platform.openai.com/docs/guides/prompt-engineering)
- [Prompt guidance (GPT-6 family)](https://developers.openai.com/api/docs/guides/prompt-guidance)
- [Prompting guidance for GPT-5.6 Sol](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6)
- [GPT-5 prompting guide (아카이브)](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide)
- [GPT-4.1 Prompting Guide (아카이브)](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide)
- [Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
- [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Prompt optimizer](https://developers.openai.com/api/docs/guides/prompt-optimizer) — Evals 플랫폼 종료 예정 2026-11-30
- [Codex best practices](https://learn.chatgpt.com/guides/best-practices)
- [Why language models hallucinate (블로그, 403 — 검색 색인으로 확인)](https://openai.com/index/why-language-models-hallucinate/)
- [Sycophancy in GPT-4o (2025-04)](https://openai.com/index/sycophancy-in-gpt-4o/)
- [Expanding on what we missed with sycophancy (403)](https://openai.com/index/expanding-on-sycophancy/)
- [Introducing deep research (403)](https://openai.com/index/introducing-deep-research/)

**Google**
- [Prompt design strategies (AI Studio)](https://aistudio.google.com/docs/prompting-strategies) — 옛 주소 ai.google.dev/gemini-api/docs/prompting-strategies 에서 301
- [Prompt Engineering 백서 (Lee Boonstra, Kaggle)](https://www.kaggle.com/whitepaper-prompt-engineering) — 텍스트 추출 불가
- [백서 비공식 전문 재게시본](https://hyli.xyz/posts/docs/prompt-engineering_v7)
- [Grounding overview (Vertex AI)](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview)

**Microsoft**
- [Prompt engineering techniques (Foundry/Azure OpenAI, ms.date 2026-05-13)](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering)

**Meta**
- [Agents Rule of Two (2025-10-31)](https://ai.meta.com/blog/practical-ai-agent-security/)

### B. 연구 논문

**오해**
- [Laban et al., LLMs Get Lost in Multi-Turn Conversation (arXiv 2505.06120)](https://arxiv.org/abs/2505.06120); [HTML 전문](https://arxiv.org/html/2505.06120v1)
- [Zhang et al., CLAMBER (arXiv 2405.12063)](https://arxiv.org/abs/2405.12063)
- [Andukuri et al., STaR-GATE (arXiv 2403.19154)](https://arxiv.org/abs/2403.19154)
- [Zhang & Choi, Clarify When Necessary (arXiv 2311.09469)](https://arxiv.org/abs/2311.09469)
- [Deng et al., Rephrase and Respond (arXiv 2311.04205)](https://arxiv.org/abs/2311.04205)

**누락**
- [Liu et al., Lost in the Middle (arXiv 2307.03172)](https://arxiv.org/abs/2307.03172); [PDF v3](https://arxiv.org/pdf/2307.03172v3)
- [Hsieh et al., RULER (arXiv 2404.06654)](https://arxiv.org/abs/2404.06654)
- [Modarressi et al., NoLiMa (arXiv 2502.05167)](https://arxiv.org/abs/2502.05167)
- [Hong, Troynikov, Huber, Context Rot (Chroma 기술 보고서, 2025)](https://research.trychroma.com/context-rot)
- [Zhou et al., IFEval (arXiv 2311.07911)](https://arxiv.org/abs/2311.07911)
- [Harada et al., When Instructions Multiply (arXiv 2509.21051)](https://arxiv.org/abs/2509.21051)
- [Jaroslawicz et al., IFScale (arXiv 2507.11538)](https://arxiv.org/abs/2507.11538)
- [Bai et al., LongWriter (arXiv 2408.07055)](https://arxiv.org/abs/2408.07055)

**지어냄(환각)**
- [Kalai et al., Why Language Models Hallucinate (arXiv 2509.04664)](https://arxiv.org/abs/2509.04664); [OpenAI PDF](https://cdn.openai.com/pdf/d04913be-3f6f-4d2b-b283-ff432ef4aaa5/why-language-models-hallucinate.pdf)
- [Huang et al., 환각 서베이 (arXiv 2311.05232)](https://arxiv.org/abs/2311.05232)
- [Min et al., FActScore (arXiv 2305.14251)](https://arxiv.org/abs/2305.14251)
- [Walters & Wilder, Scientific Reports 2023](https://www.nature.com/articles/s41598-023-41032-5)
- [Dhuliawala et al., Chain-of-Verification (arXiv 2309.11495)](https://arxiv.org/abs/2309.11495)
- [Wang et al., Self-Consistency (arXiv 2203.11171)](https://arxiv.org/abs/2203.11171)
- [Manakul et al., SelfCheckGPT (arXiv 2303.08896)](https://arxiv.org/abs/2303.08896)
- [Farquhar et al., Semantic entropy (Nature 2024)](https://www.nature.com/articles/s41586-024-07421-0)
- [Magesh et al., Hallucination-Free? (JELS 22(2), 2025)](https://econpapers.repec.org/RePEc:wly:empleg:v:22:y:2025:i:2:p:216-242); [Stanford Law 목록](https://law.stanford.edu/publications/hallucination-free-assessing-the-reliability-of-leading-ai-legal-research-tools)

**아첨**
- [Perez et al. (arXiv 2212.09251)](https://arxiv.org/abs/2212.09251)
- [Sharma et al. (arXiv 2310.13548)](https://arxiv.org/abs/2310.13548); [HTML v4](https://arxiv.org/html/2310.13548v4)
- [Wei et al. (arXiv 2308.03958)](https://arxiv.org/abs/2308.03958)
- [Laban et al., FlipFlop (arXiv 2311.08596)](https://arxiv.org/abs/2311.08596)
- [Fanous et al., SycEval (arXiv 2502.08177)](https://arxiv.org/abs/2502.08177)

**프롬프트 기법·신화 검증**
- [Meincke et al., Prompting Science Report 1 (arXiv 2503.04818)](https://arxiv.org/abs/2503.04818); [PDF](https://arxiv.org/pdf/2503.04818)
- [Meincke et al., Report 2: The Decreasing Value of Chain of Thought (arXiv 2506.07142)](https://arxiv.org/abs/2506.07142); [PDF](https://arxiv.org/pdf/2506.07142)
- [Meincke et al., Report 3: I'll pay you or I'll kill you (arXiv 2508.00614)](https://arxiv.org/abs/2508.00614); [PDF](https://arxiv.org/pdf/2508.00614)
- [Basil et al., Report 4: Playing Pretend (SSRN 5879722)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5879722)
- [Schulhoff et al., The Prompt Report (arXiv 2406.06608)](https://arxiv.org/abs/2406.06608); [HTML v6](https://arxiv.org/html/2406.06608v6)
- [Bsharat et al., Principled Instructions (26 Principles, arXiv 2312.16171v2)](https://arxiv.org/html/2312.16171v2)
- [Zheng et al., Personas in System Prompts (EMNLP 2024 Findings, arXiv 2311.10054)](https://arxiv.org/abs/2311.10054)
- [Nori et al., From Medprompt to o1 (arXiv 2411.03590)](https://arxiv.org/abs/2411.03590)
- [Khattab et al., DSPy (arXiv 2310.03714)](https://arxiv.org/abs/2310.03714)

**사람의 판단·학습·생산성**
- [Kosmyna et al., Your Brain on ChatGPT (arXiv 2506.08872, 프리프린트)](https://arxiv.org/abs/2506.08872)
- [Stankovic et al., Comment on Your Brain on ChatGPT (arXiv 2601.00856)](https://arxiv.org/abs/2601.00856)
- [Bastani et al., PNAS 122(26) 2025 서지](https://econpapers.repec.org/RePEc:nas:journl:v:122:y:2025:p:e2422633122); [SSRN 워킹페이퍼](https://papers.ssrn.com/abstract=4895486)
- [Lee et al., The Impact of Generative AI on Critical Thinking (CHI 2025)](https://www.microsoft.com/en-us/research/?p=1135061); [저자 PDF](https://advait.org/files/lee_2025_ai_critical_thinking_survey.pdf)
- [Noy & Zhang, Science 2023 (DOI)](https://doi.org/10.1126/science.adh2586); [MIT 워킹페이퍼 PDF](https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1_0.pdf)
- [Brynjolfsson, Li, Raymond, Generative AI at Work (QJE 2025) 보도자료](https://www.eurekalert.org/news-releases/1071936); [RePEc](https://econpapers.repec.org/RePEc:oup:qjecon:v:140:y:2025:i:2:p:889-942.)
- [Dell'Acqua et al., Jagged Frontier (Organization Science DOI, 내용 미확인)](https://doi.org/10.1287/orsc.2025.21838)
- [Dell'Acqua et al., The Cybernetic Teammate (NBER w33641)](https://www.nber.org/papers/w33641)
- [Liu et al., Teaching CS50 with AI (SIGCSE 2024)](https://cs.harvard.edu/malan/publications/V1fp0567-liu.pdf)
- [METR, Early-2025 AI experienced OS developer study (2025-07-10)](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

### C. 대학·연구기관 보고서와 가이드

- [MIT Sloan EdTech, Effective Prompts for AI: The Essentials](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/)
- [MIT Sloan EdTech, When AI Gets It Wrong](https://mitsloanedtech.mit.edu/ai/basics/addressing-ai-hallucinations-and-bias/)
- [MIT NANDA, The GenAI Divide 2025 (PDF, mlq.ai 호스팅, 예비 보고서)](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf); [Fortune 보도](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo)
- [MIT 6.S191 Introduction to Deep Learning](https://introtodeeplearning.com/)
- [MIT OCW RES.9-010](https://ocw.mit.edu/courses/res-9-010-bcs-tutorials-optimizing-the-full-stack-for-generative-image-and-video-models-fall-2025/pages/)
- [Harvard CS50x 학업 정직성 정책](https://cs50.harvard.edu/x/honesty/)
- [Harvard Gazette, Taming the duck (2026-09-25)](https://news.harvard.edu/gazette/story/2026/09/taming-the-duck-for-starters/)
- [Harvard HUIT, AI prompts (403, 미확인)](https://www.huit.harvard.edu/news/ai-prompts)
- [Ethan Mollick, Centaurs and Cyborgs on the Jagged Frontier (2023-09-16)](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)
- [Ethan Mollick, The Cybernetic Teammate](https://www.oneusefulthing.org/p/the-cybernetic-teammate)
- [Ethan Mollick, Getting started with AI: Good enough prompting (2024-11-24)](https://www.oneusefulthing.org/p/getting-started-with-ai-good-enough)
- [Wharton GAIL, Playing Pretend: Expert Personas](https://gail.wharton.upenn.edu/research-and-insights/playing-pretend-expert-personas/)
- [Knowledge at Wharton, Without guardrails generative AI can harm education](https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/)
- [Knowledge at Wharton, Why you shouldn't ask chatbots to act like an expert](https://knowledge.wharton.upenn.edu/article/why-you-shouldnt-ask-chatbots-to-act-like-an-expert/); [Penn Today](https://penntoday.upenn.edu/news/wharton-why-you-shouldnt-ask-chatbots-act-expert)
- [Stanford HAI, AI on Trial: Legal models hallucinate (2024)](https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries)
- [Stanford HAI, AI Index 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report)
- [Stanford HAI, AI Index 2026의 12가지 요점](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report)
- [Stanford CS336](https://cs336.stanford.edu/)
- [Civic Online Reasoning, Teaching Lateral Reading](https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/)

### D. 안드레이 카파시(Andrej Karpathy)

**영상**(조회 수는 2026-11-09 기준)
- [Intro to Large Language Models (2023-11-22)](https://www.youtube.com/watch?v=zjkBMFhNj_g)
- [Deep Dive into LLMs like ChatGPT (2025-02-05)](https://www.youtube.com/watch?v=7xTGNNLPyMI)
- [How I use LLMs (2025-02-27)](https://www.youtube.com/watch?v=EWvNQjAaOHw)
- [Software Is Changing (Again), YC AI Startup School (2025-06-18)](https://www.youtube.com/watch?v=LCEmiRjPEtQ)
- [Dwarkesh Podcast (2025-10-17)](https://www.youtube.com/watch?v=lXUZvyajciY); [대담 페이지](https://dwarkesh.com/p/andrej-karpathy)
- [State of GPT (2023-05-25)](https://www.youtube.com/watch?v=bZQun8Y4L2A)
- [Let's build GPT (2023-01-17)](https://www.youtube.com/watch?v=kCc8FmEb1nY)
- [Zero to Hero 재생목록](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)

**블로그·게시물**
- [블로그 목록](https://karpathy.bearblog.dev/blog/)
- [Sequoia Ascent 2026 summary (2026-04-30)](https://karpathy.bearblog.dev/sequoia-ascent-2026/)
- [2025 LLM Year in Review (2025-12-19)](https://karpathy.bearblog.dev/year-in-review-2025/)
- [Vibe coding MenuGen (2025-04-27)](https://karpathy.bearblog.dev/vibe-coding-menugen/)
- [Power to the people (2025-04-07)](https://karpathy.bearblog.dev/power-to-the-people/)
- [HackerTube (2026-10-31)](https://karpathy.bearblog.dev/hacker-tube/)
- [X: 바이브 코딩 (2025-02-02)](https://x.com/karpathy/status/1886192184808149383)
- [X: 맥락 엔지니어링 (2025-06-25)](https://x.com/karpathy/status/1937902205765607626)
- [Gist: llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Gist: microgpt](https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95)
- [karpathy.ai](https://karpathy.ai/)

**2차 요약·보도**
- [Tuan-Anh Bui, How I use LLMs 요약](https://tuananhbui89.github.io/blog/2025/karpathy-lec09)
- [mvark, How I use LLMs 요약](https://mvark.blogspot.com/2025/03/how-i-use-llms-andrej-karpathy.html)
- [ikyle.me, Software Is Changing (Again) 요약](https://ikyle.me/blog/2025/andrej-karpathy-software-is-changing-again)
- Business Insider via AOL, Keep AI on the leash (2026-11-09 재확인 시 링크 만료)
- [Business Insider via AOL, 에이전틱 엔지니어링 명명](https://www.aol.com/articles/guy-coined-vibe-coding-says-181826669.html)
- [tianpan.co 포럼](https://tianpan.co/forum/t/karpathy-says-vibe-coding-is-passe-at-its-one-year-anniversary-agentic-engineering-is-the-new-paradigm/628)
- [The New Stack, Vibe coding is passé (제목만 확인)](https://thenewstack.io/vibe-coding-is-passe/)
- [The New Stack, AI agents are still 10 years away](https://thenewstack.io/openai-co-founder-ai-agents-are-still-10-years-away/)
- [Wikipedia: Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding)
- [Analytics Vidhya, Software 3.0](https://www.analyticsvidhya.com/blog/2025/06/andrej-karpathy-on-the-rise-of-software-3-0/)
- [travis.media, Software 3.0](https://travis.media/blog/software-3-0-ai-changing-programming-karpathy)
- [Latent Space, Software 3.0 (유료, 제목만 확인)](https://www.latent.space/p/s3)

### E. 실무자·보안·표준

- [Simon Willison, Context engineering (2025-06-27)](https://simonwillison.net/2025/Jun/27/context-engineering/)
- [Tobi Lütke X 게시물 (미확인)](https://twitter.com/tobi/status/1935533422589399127)
- [Simon Willison, Here's how I use LLMs to help me write code (2025-03-11)](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)
- [Simon Willison, Not all AI-assisted programming is vibe coding (2025-03-19)](https://simonwillison.net/2025/Mar/19/vibe-coding/)
- [Simon Willison, Agentic Engineering Patterns (가이드 목차)](https://simonwillison.net/guides/agentic-engineering-patterns/)
- [What is agentic engineering?](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/)
- [Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)
- [Anti-patterns](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)
- [Agentic Engineering Patterns 발표 글 (검색 스니펫만)](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/)
- [Simon Willison, The lethal trifecta (2025-06-16)](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- [Simon Willison, prompt-engineering 태그](https://simonwillison.net/tags/prompt-engineering/)
- [Hamel Husain & Shreya Shankar, Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
- [Birgitta Böckeler, Understanding Spec-Driven-Development (2025-10-15)](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- [OWASP LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [AGENTS.md](https://agents.md/)
- [Learn Prompting](https://learnprompting.org/)
- [promptingguide.ai](https://www.promptingguide.ai/)
- [One Useful Thing](https://www.oneusefulthing.org/)

### F. 사례·언론 보도

- [Wikipedia: Mata v. Avianca, Inc.](https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.)
- [Justia, Mata v. Avianca Document 54](https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54)
- [Damien Charlotin, AI Hallucination Cases 데이터베이스](https://www.damiencharlotin.com/hallucinations/)
- [Malay Mail/AFP (2026-06-16, 검색 요약만)](https://www.malaymail.com/news/tech-gadgets/2026/06/16/do-your-job-global-courts-face-rising-tide-of-ai-generated-fake-cases-and-quotes/223865)
- [Maryland State Bar Association (2026-07, 검색 요약만)](https://www.msba.org/site/content/News-and-Publications/News/General-News/Confronting_the_Hard%20Numbers_Behind_Lawyers_AI_and_Phantom_Precedents.aspx)
- [Bloomberg Law (검색 요약만)](https://news.bloomberglaw.com/us-law-week/ai-faked-cases-become-core-issue-irritating-overworked-judges)
- [Georgetown Law Tech Institute, AI 아첨 브리프](https://www.law.georgetown.edu/tech-institute/insights/tech-brief-ai-sycophancy-openai/)
- [TechCrunch (2025-04-29)](https://techcrunch.com/2025/04/29/openai-explains-why-chatgpt-became-too-sycophantic)
- [Computing, OpenAI deep research (검색 스니펫만)](https://www.computing.co.uk/news/2025/ai/openai-announces-deep-research)
- [The Decoder, GPT-5.5 프롬프트](https://the-decoder.com/openai-says-old-prompts-are-holding-gpt-5-5-back-and-developers-need-a-fresh-baseline/)
- [LLRX, 법률 AI 환각 논평 (2026-04)](https://www.llrx.com/2026/04/hallucinations-by-west-lexis-ai/)
- [Consultancy.uk, BCG 파일럿](https://www.consultancy.uk/news/35431/chatgpt-most-benefits-below-average-consultants-finds-bcg-pilot)
- [Computing.co.uk, Jagged frontier 보도](https://www.computing.co.uk/news/4131152/study-hard-ai-productivity-boost)
- [beginnersinai.org, GPTs·Projects·Gems 비교 (검색 스니펫만)](https://beginnersinai.org/custom-gpts-vs-claude-projects-vs-gemini-gems/)

### G. GitHub 저장소 (별 수와 마지막 푸시, 확인일 2026-11-09, GitHub REST API)

본문에 인용하지 않은 저장소도 저장소 재사용을 위해 함께 싣는다.

**카파시**

| 저장소 | 별 | 마지막 푸시 | 상태 |
|---|---|---|---|
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 99,567 | 2026-03-26 | 활성 |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | 64,550 | 2025-11-12 | 폐기(nanochat으로 대체) |
| [karpathy/nanochat](https://github.com/karpathy/nanochat) | 60,370 | 2026-09-07 | 활성 |
| [karpathy/LLM101n](https://github.com/karpathy/LLM101n) | 37,479 | 2024-08-01 | 아카이브(강의 없음) |
| [karpathy/llm.c](https://github.com/karpathy/llm.c) | 31,408 | 2025-06-26 | 2025년 중반 이후 정체 |
| [karpathy/llm-council](https://github.com/karpathy/llm-council) | 26,338 | 2025-11-22 | 소형 도구 |
| [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) | 25,383 | 2024-08-18 | 완결 |
| [karpathy/minGPT](https://github.com/karpathy/minGPT) | 25,010 | 2024-08-15 | 비활성 |
| [karpathy/llama2.c](https://github.com/karpathy/llama2.c) | 20,254 | 2024-08-06 | 비활성 |
| [karpathy/micrograd](https://github.com/karpathy/micrograd) | 18,764 | 2026-08-03 | 간헐 활동 |
| [karpathy/minbpe](https://github.com/karpathy/minbpe) | 11,021 | 2024-07-01 | 완결 |
| [karpathy/build-nanogpt](https://github.com/karpathy/build-nanogpt) | 5,624 | 2024-08-13 | 비활성 |
| [karpathy/makemore](https://github.com/karpathy/makemore) | 4,540 | 2024-06-04 | 비활성 |
| [karpathy/reader3](https://github.com/karpathy/reader3) | 3,899 | 2025-11-18 | 소형 도구 |
| [karpathy/rendergit](https://github.com/karpathy/rendergit) | 2,497 | 2025-08-21 | 소형 도구 |
| [karpathy/jobs](https://github.com/karpathy/jobs) | 2,042 | 2026-03-16 | 소형 도구 |
| [karpathy/hn-time-capsule](https://github.com/karpathy/hn-time-capsule) | 690 | 2025-12-10 | 소형 도구 |
| [karpathy/rustbpe](https://github.com/karpathy/rustbpe) | 527 | 2026-01-03 | 활성 |

**프롬프트 엔지니어링**

| 저장소 | 별 | 마지막 푸시 | 상태 |
|---|---|---|---|
| [f/prompts.chat](https://github.com/f/prompts.chat) (구 awesome-chatgpt-prompts) | 176,491 | 2026-11-08 | 활성 |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 144,559 | 2026-10-12 | 유출 자료(출처·저작권 주의) |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 123,134 | 2026-11-05 | 활성 |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 79,910 | 2026-03-11 | 활성 |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 77,003 | 2026-11-06 | 활성 |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 71,029 | 2026-11-08 | 유출 자료(출처·저작권 주의) |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) (구 anthropic-cookbook) | 54,429 | 2026-11-04 | 활성 |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | 39,148 | 2026-08-28 | 활성 |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | 38,971 | 2026-11-08 | 활성 |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 26,958 | 2026-11-08 | 활성 |
| [anthropics/courses](https://github.com/anthropics/courses) | 22,993 | 2026-08-28 | 아카이브 |
| [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | 17,915 | 2026-11-05 | 활성 |
| [jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) | 15,008 | 2026-09-23 | 유출 자료(출처·저작권 주의) |
| [langgptai/LangGPT](https://github.com/langgptai/LangGPT) | 12,679 | 2026-09-11 | 활성 |
| [brexhq/prompt-engineering](https://github.com/brexhq/prompt-engineering) | 9,590 | 2023-10-23 | 정체(GPT-4 시대) |
| [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) | 7,927 | 2026-10-31 | 활성 |
| [promptslab/Awesome-Prompt-Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering) | 6,436 | 2026-11-08 | 활성 |
| [microsoft/promptbase](https://github.com/microsoft/promptbase) | 5,773 | 2024-06-04 | 정체 |
| [trigaten/Learn_Prompting](https://github.com/trigaten/Learn_Prompting) | 4,743 | 2025-01-14 | 저장소 정체(웹사이트 사용) |

**맥락 엔지니어링**

| 저장소 | 별 | 마지막 푸시 | 상태 |
|---|---|---|---|
| [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) | 13,901 | 2026-03-16 | 활성 |
| [jasontang-ai/Context-Engineering](https://github.com/jasontang-ai/Context-Engineering) (구 davidkimai, 301) | 9,279 | 2026-02-27 | 활성 |
| [Meirtz/Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) | 3,339 | 2026-05-28 | 활성 |
| [humanlayer/advanced-context-engineering-for-coding-agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents) | 2,823 | 2026-10-16 | 활성 |
| [langchain-ai/how_to_fix_your_context](https://github.com/langchain-ai/how_to_fix_your_context) | 545 | 2025-07-25 | 아카이브 |

**에이전트 원칙·스킬**

| 저장소 | 별 | 마지막 푸시 | 상태 |
|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 314,454 | 2026-11-03 | 활성 |
| [anthropics/skills](https://github.com/anthropics/skills) | 189,325 | 2026-11-06 | 공식 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 79,046 | 2026-09-18 | 업체 운영 목록 |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 46,435 | 2026-11-08 | 공식 |
| [openai/skills](https://github.com/openai/skills) | 28,597 | 2026-10-28 | 공식 |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | 27,044 | 2025-09-21 | 푸시 없음, 원칙은 유효 |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | 25,395 | 2026-09-10 | 활성 |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 15,743 | 2026-04-28 | 독립 목록 |

**코딩 에이전트·큐레이션**

| 저장소 | 별 | 마지막 푸시 |
|---|---|---|
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 154,976 | 2026-11-06 |
| [openai/codex](https://github.com/openai/codex) | 133,757 | 2026-11-08 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 108,781 | 2026-11-08 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 57,529 | 2026-11-08 |
| [wshobson/agents](https://github.com/wshobson/agents) | 42,305 | 2026-11-08 |
| [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | 41,134 | 2026-05-30 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | 40,925 | 2026-11-06 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | 33,210 | 2026-11-08 |

**명세 주도 개발(SDD)**

| 저장소 | 별 | 마지막 푸시 |
|---|---|---|
| [github/spec-kit](https://github.com/github/spec-kit) | 148,629 | 2026-11-07 |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 74,272 | 2026-11-07 |
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 55,124 | 2026-11-08 |
| [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | 28,326 | 2026-04-28 |

**빌더 강좌·튜토리얼**

| 저장소 | 별 | 마지막 푸시 |
|---|---|---|
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 144,175 | 2026-11-06 |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 108,015 | 2026-11-06 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 97,476 | 2026-11-06 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 91,871 | 2026-11-05 |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 84,950 | 2026-02-05 |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 79,192 | 2026-11-07 |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | 34,599 | 2026-11-03 |
| [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | 30,855 | 2026-08-21 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 30,556 | 2026-11-08 |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 30,272 | 2026-11-02 |
| [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) | 27,489 | 2025-07-31 |
| [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) | 24,875 | 2026-11-02 |
| [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) | 21,851 | 2026-11-02 |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | 19,272 | 2026-11-06 |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | 17,625 | 2026-11-02 |
| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | 8,486 | 2026-11-06 |

**한국어**

| 저장소 | 별 | 마지막 푸시 | 비고 |
|---|---|---|---|
| [teddylee777/langchain-kr](https://github.com/teddylee777/langchain-kr) | 2,058 | 2025-08-18 | 한국어 LangChain 튜토리얼(최신 LangChain보다 뒤처질 수 있음) |

### H. 한국어 출처

**SKALA·Pre-SKALA 공식·준공식**
- [SK AX 뉴스룸, SKALA 광주·울산 확대 (2026-05-07)](https://www.skax.co.kr/company/news-room/sk-ax-skala-%EA%B4%91%EC%A3%BC%C2%B7%EC%9A%B8%EC%82%B0%EC%9C%BC%EB%A1%9C-%ED%99%95%EB%8C%80%ED%95%B4-ai%EC%9D%B8%EC%9E%AC-%EC%9C%A1%EC%84%B1%ED%95%9C%EB%8B%A4)
- [SKALA 공식 사이트](http://2026skala.co.kr/)
- [Pre-SKALA 공식 페이지](https://2026pre-skala.co.kr/)
- [Byline Network, SKALA 1기 공고 (2024-12-12)](https://byline.network/2024/12/12-351/)
- [서울대 컴퓨터공학부 공지 25050 (SKALA 4기)](https://cse.snu.ac.kr/en/community/notice/25050)
- [서울대 컴퓨터공학부 공지 25679 (Pre-SKALA)](https://cse.snu.ac.kr/en/community/notice/25679)

**SKALA 수강생 자료(비공식)**
- [stellacustodis, [SKALA] Prompt 설계와 Context Engineering (2026-07-15)](https://stellacustodis.github.io/posts/skala-prompt-engineering/); [원본 마크다운](https://github.com/stellacustodis/stellacustodis.github.io/blob/main/_posts/2026-07-15-skala-prompt-engineering.md)
- [stellacustodis, SKALA 1개월 회고 (2026-08-18)](https://github.com/stellacustodis/stellacustodis.github.io/blob/main/_posts/2026-08-18-skala-1month-review.md)
- [stellacustodis 블로그 _posts 폴더](https://github.com/stellacustodis/stellacustodis.github.io/tree/main/_posts)
- [skalamok/capstone-v1](https://github.com/skalamok/capstone-v1)
- [yunsly/ai-mini-project-v0.5](https://github.com/yunsly/ai-mini-project-v0.5)
- [ssunju-02/skala-toxicity-prediction](https://github.com/ssunju-02/skala-toxicity-prediction)
- [Gwangdev/skala-vue](https://github.com/Gwangdev/skala-vue)
- [Ready-Bridge/skala-cloud](https://github.com/Ready-Bridge/skala-cloud)
- [sjjeon0925/skala-springAI-practicecode](https://github.com/sjjeon0925/skala-springAI-practicecode)
- [yongchane/skala-review-skill](https://github.com/yongchane/skala-review-skill)

**한국어 프롬프트 가이드**
- [Google, Google Workspace를 위한 Gemini 프롬프트 작성 가이드 101 (한국어, 2024년 4월판)](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101_ko.pdf)
- [프롬프트 엔지니어링 가이드 한국어판, 프롬프트의 구성 요소](https://www.promptingguide.ai/kr/introduction/elements)
- [Anthropic Claude 문서 한국어판, 프롬프트 엔지니어링 개요](https://platform.claude.com/docs/ko/build-with-claude/prompt-engineering/overview)
- [브런치, AI 바로 답하게 하지 마세요 (2026-04-21)](https://brunch.co.kr/@bbt/16)
- [tilnote.io, 프롬프트 기본기: 명확성·맥락·형식·제약 (검색 스니펫만, 권위 불명)](https://tilnote.io/pages/69bb8bf806e26362da137f27.md)
- [tilnote.io, 환각 방지 지시 관련 페이지 (검색 스니펫만, 귀속 미확인)](https://tilnote.io/pages/69f1c6c883b513f85f27aeeb)
- [promptquorum, CO-STAR 한국어 (검색 스니펫만)](https://www.promptquorum.com/ko/frameworks/co-star)
- [promptquorum, RISEN 한국어 (검색 스니펫만)](https://www.promptquorum.com/ko/frameworks/risen)
- [위키독스, 나 그리고 프롬프트 (검색 스니펫만)](https://wikidocs.net/book/17643)

**한국 공공부문(모두 검색 스니펫만, 1차 문서 미확보)**
- [korea.kr, 행정안전부 ChatGPT 활용 가이드 보도자료](https://m.korea.kr/briefing/pressReleaseView.do?newsId=156566491)
- [Daum 뉴스, 공공부문 AI 도입·활용 가이드 (2026-07-22)](https://v.daum.net/v/20260722053449437)
- smartcity.go.kr, 부산시 공무원 생성형 AI 활용 지침 (2025-03-12, 검색 스니펫만. 2026-11-09 재확인 시 원 링크가 404로 열리지 않아 링크를 제거함)
- [PyTorch KR, 방송통신위원회·NIA 생성형 AI 윤리 가이드북 논의](https://discuss.pytorch.kr/t/nia-ai-pdf-72p/3136)
