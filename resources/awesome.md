# 참고 자료 모음 (Awesome List)

> 공식 연구소 가이드, Andrej Karpathy, 대학·연구기관, 유명 GitHub 저장소를 **직접 확인한 것만** 모았습니다.
> GitHub 별 수와 상태는 **2026-11-09**에 GitHub API로 확인한 값입니다. 별 수는 인기를 보여 줄 뿐 품질을 보장하지 않습니다.

**범례:** 🟢 활발히 관리 중 · 🟡 완결됐거나 업데이트가 뜸함 · 🔴 보관(archived) 또는 폐기 · ⚠️ 주의해서 볼 것

---

## 1. 공식 연구소 가이드 (가장 먼저 읽을 것)

| 기관 | 자료 | 한 줄 요약 |
|---|---|---|
| Anthropic | [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | 명확하게, 이유와 함께, 예시 3~5개, 긴 자료는 위에. 최신 모델용 "버릴 습관"까지 정리 |
| Anthropic | [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) · [한국어판](https://platform.claude.com/docs/ko/build-with-claude/prompt-engineering/overview) | 프롬프트를 다듬기 전에 성공 기준과 테스트부터 |
| Anthropic | [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) | 모른다고 말할 권리, 인용 먼저, 인용 못 하면 철회 |
| Anthropic | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (2025-09) | 맥락은 한정된 주의력 예산. 가장 작은 고신호 정보 |
| Anthropic | [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) (2024-12) | 5가지 워크플로 패턴. 가장 단순한 것부터 |
| Anthropic | [Claude Code best practices](https://code.claude.com/docs/en/best-practices) | 실패의 4가지 원인, 부탁 vs 강제, "더 이상 할 필요 없는 것" |
| Anthropic | [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (2026-01) | 실제 실패에서 20~50개 과제로 시작, 결과를 채점 |
| OpenAI | [Prompt engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering) | 추론 모델 = 선배 동료, 일반 모델 = 신입 동료 |
| OpenAI | [Prompt guidance (최신 모델)](https://developers.openai.com/api/docs/guides/prompt-guidance) · [GPT-5.6 가이드](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6) | 목표와 성공 기준, 덜어낸 프롬프트, 강조 표현은 불변 조건에만 |
| OpenAI | [Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices) | 추론 모델엔 CoT 지시 불필요, 예시 없이 먼저 (o-시리즈 기준) |
| OpenAI | [Codex best practices](https://learn.chatgpt.com/guides/best-practices) | 목표·맥락·제약·완료 기준 템플릿, 흔한 실수 목록 |
| Google | [Prompt design strategies](https://aistudio.google.com/docs/prompting-strategies) | 형식이 같은 예시, 자료를 직접 넣기, thinking 모델 다루기 |
| Google | [Gemini 프롬프트 가이드 101 (한국어 PDF)](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101_ko.pdf) | 역할 · 할 일 · 맥락 · 형식 (2024년판) |
| Google | [Prompt Engineering 백서 (Lee Boonstra, Kaggle)](https://www.kaggle.com/whitepaper-prompt-engineering) | 기법 총정리. 샘플링 매개변수 조언은 최신 모델에선 일부 낡음 |
| Microsoft | [Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering) | 일반 모델용 기법 정리. 추론 모델에는 비권장 배너 |

> ⚠️ OpenAI의 [GPT-4.1](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide), [GPT-5](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide) 프롬프트 가이드는 보관(archived) 문서입니다. 원리는 유효하지만 세부 내용은 이전 세대 기준입니다.

---

## 2. Andrej Karpathy

OpenAI 공동 창업자이자 전 Tesla AI 디렉터. "바이브 코딩", "컨텍스트 엔지니어링"을 대중화했고, LLM을 **처음부터 만들어 보며 이해하는** 교육 자료로 유명합니다.

### 영상 (일반 사용자에게 가장 추천하는 순서)

| 영상 | 날짜 | 무엇을 배우나 |
|---|---|---|
| [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) | 2025-02-27 | **일반 사용자 필수.** 모델 고르기, 새 채팅, 검색·코드 도구, 사고 모델 |
| [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) | 2025-02-05 | LLM이 어떻게 만들어지고 왜 환각하는지 (3시간 30분) |
| [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) | 2023-11-22 | 1시간 입문 |
| [Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ) (YC) | 2025-06-18 | Software 3.0, 부분 자율성, 아이언맨 슈트 |
| [Dwarkesh Podcast 대담](https://www.youtube.com/watch?v=lXUZvyajciY) | 2025-10-17 | 에이전트의 한계와 "에이전트의 10년" |
| [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | — | 신경망부터 GPT까지 직접 구현 (개발자용) |

### 글

| 글 | 날짜 | 핵심 |
|---|---|---|
| [Sequoia Ascent 2026 요약](https://karpathy.bearblog.dev/sequoia-ascent-2026/) | 2026-04-30 | **가장 최신 실무 조언.** 에이전트에게 큰 단위로 위임하되 명세·검증·이해는 사람이. "LLM은 검증 가능한 것을 자동화한다" |
| [2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/) | 2025-12-19 | 들쭉날쭉한 지능, 한 해 정리 |
| [Vibe coding MenuGen](https://karpathy.bearblog.dev/vibe-coding-menugen/) | 2025-04-27 | 바이브 코딩 실전기. 어려운 건 배포·인증·결제였다 |
| [바이브 코딩 게시물](https://x.com/karpathy/status/1886192184808149383) | 2025-02-02 | 용어의 기원 |
| [컨텍스트 엔지니어링 게시물](https://x.com/karpathy/status/1937902205765607626) | 2025-06-25 | 용어 대중화 |
| [llm-wiki (gist)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | 2026-04 | AI가 마크다운 지식 베이스를 계속 관리하게 하는 패턴 |

### 저장소

| 저장소 | ⭐ | 상태 | 메모 |
|---|---|---|---|
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 99,567 | 🟢 | 사람은 `program.md`(지시문)만 고치고 에이전트가 실험을 돌림. 컨텍스트 엔지니어링의 실례 |
| [karpathy/nanochat](https://github.com/karpathy/nanochat) | 60,370 | 🟢 | "100달러로 만드는 최고의 ChatGPT". nanoGPT의 후속 |
| [karpathy/llm-council](https://github.com/karpathy/llm-council) | 26,338 | 🟡 | 여러 모델이 답하고 서로 평가 → 의장 모델이 종합 |
| [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) | 25,383 | 🟡 | 강의 코드 (완결) |
| [karpathy/micrograd](https://github.com/karpathy/micrograd) | 18,764 | 🟡 | 역전파를 100줄로 |
| [karpathy/minbpe](https://github.com/karpathy/minbpe) | 11,021 | 🟡 | 토큰화 이해 (LLM이 글자 세기에 약한 이유) |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | 64,550 | 🔴 | README에 "오래되고 폐기됨" 명시 → nanochat 사용 |
| [karpathy/llm.c](https://github.com/karpathy/llm.c) | 31,408 | 🟡 | 2025년 중반 이후 업데이트 없음 |
| [karpathy/LLM101n](https://github.com/karpathy/LLM101n) | 37,479 | 🔴 | 보관됨. **강의는 아직 존재하지 않음** (README 명시) |

---

## 3. 대학·연구기관

| 기관 | 자료 | 핵심 |
|---|---|---|
| **MIT** Sloan | [Effective Prompts for AI: The Essentials](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/) | 과업·맥락·구체성·예시와 제약, 새 주제엔 새 채팅, "프롬프트보다 문제 정의" |
| **MIT** Sloan | [Addressing AI Hallucinations and Bias](https://mitsloanedtech.mit.edu/ai/basics/addressing-ai-hallucinations-and-bias/) | 인용 확인은 타협 불가 |
| **MIT** | [6.S191 Introduction to Deep Learning](https://introtodeeplearning.com/) | 딥러닝 입문 공개 강의 (슬라이드·실습·영상) |
| **MIT** Media Lab | [Your Brain on ChatGPT](https://arxiv.org/abs/2506.08872) (프리프린트) · [반론](https://arxiv.org/abs/2601.00856) | LLM으로 쓴 글은 기억·주인의식이 낮음. 논쟁 중인 초기 신호 |
| **MIT** NANDA | [The GenAI Divide 2025](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf) (예비 보고서) | 기업 AI 실패의 원인은 맥락·학습 부재. 그림자 AI |
| **Wharton** GAIL | Prompting Science Reports [1](https://arxiv.org/abs/2503.04818) · [2](https://arxiv.org/abs/2506.07142) · [3](https://arxiv.org/abs/2508.00614) · [4](https://gail.wharton.upenn.edu/research-and-insights/playing-pretend-expert-personas/) | **프롬프트 요령의 진실.** 팁·협박·정중함·전문가 역할 효과 없음, CoT 효과 감소, 형식 지시는 효과 있음 |
| **Wharton** | [Bastani et al., PNAS 2025](https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/) | 답을 주는 AI는 학습을 해치고, 힌트를 주는 튜터형은 해치지 않음 |
| **Wharton** | [Ethan Mollick, One Useful Thing](https://www.oneusefulthing.org/) | 실무자를 위한 가장 꾸준한 AI 활용 블로그 |
| **Harvard** / BCG | [Navigating the Jagged Technological Frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged) | 들쭉날쭉한 경계, 켄타우로스 vs 사이보그, 운전대에서 졸기 |
| **Harvard** / P&G | [The Cybernetic Teammate](https://www.nber.org/papers/w33641) | AI를 쓴 개인 ≈ AI 없는 팀 |
| **Harvard** CS50 | [CS50 AI 정책](https://cs50.harvard.edu/x/honesty/) · [Taming the Duck (2026)](https://news.harvard.edu/gazette/story/2026/09/taming-the-duck-for-starters/) | 답 대신 안내하는 AI 튜터. "프롬프트만으로는 행동 강제가 부족하다" |
| **Stanford** | [법률 AI 환각 연구](https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries) | 법률 전문 도구도 17~34% 환각 |
| **Stanford** HAI | [AI Index 2026 핵심 12가지](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report) | 능력은 여전히 들쭉날쭉 |
| **Stanford** NLP | [DSPy](https://arxiv.org/abs/2310.03714) · [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) ⭐38,971 | "프롬프팅이 아니라 프로그래밍". 프롬프트 자동 최적화 |
| **Stanford** | [CS336 Language Modeling from Scratch](https://cs336.stanford.edu/) | LLM을 처음부터 (개발자용) |
| UMD 외 | [The Prompt Report](https://arxiv.org/abs/2406.06608) | 58개 텍스트 프롬프트 기법 분류 체계. 가장 포괄적인 서베이 |
| CMU · Microsoft Research | [Lee et al., CHI 2025](https://advait.org/files/lee_2025_ai_critical_thinking_survey.pdf) | AI 신뢰가 높을수록 비판적 사고 감소 (319명) |

---

## 4. GitHub 저장소

### 🔰 입문: 프롬프트를 배우고 싶다

| 저장소 | ⭐ | 상태 | 메모 |
|---|---|---|---|
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 79,910 | 🟢 | 가장 유명한 프롬프트 기법 레퍼런스. [한국어 사이트](https://www.promptingguide.ai/kr) 있음 |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | 39,148 | 🟢 | Anthropic 공식 실습 튜토리얼 (명확성·역할·XML·예시·환각 회피) |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 123,134 | 🟢 | 21강 생성형 AI 입문 커리큘럼 |
| [f/prompts.chat](https://github.com/f/prompts.chat) (구 awesome-chatgpt-prompts) | 176,491 | 🟢 | 프롬프트 아이디어 모음. 기법 학습용은 아님 |
| [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) | 7,927 | 🟢 | 기법별 노트북 튜토리얼 |
| [Learn Prompting](https://learnprompting.org/) | — | 🟢 | 웹 강의 (GitHub 저장소는 2025년 이후 정체) |

### 🛠 실무: AI로 일하고 코딩한다

| 저장소 | ⭐ | 상태 | 메모 |
|---|---|---|---|
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 154,976 | 🟢 | Claude Code |
| [openai/codex](https://github.com/openai/codex) | 133,757 | 🟢 | OpenAI Codex CLI |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 108,781 | 🟢 | Gemini CLI |
| [anthropics/skills](https://github.com/anthropics/skills) | 189,325 | 🟢 | 공식 에이전트 스킬 예시 |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | 25,395 | 🟢 | AGENTS.md 표준 ([agents.md](https://agents.md/)) |
| [github/spec-kit](https://github.com/github/spec-kit) | 148,629 | 🟢 | 명세 주도 개발 도구 |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 74,272 | 🟢 | 경량 명세 주도 개발 |
| [obra/superpowers](https://github.com/obra/superpowers) | 314,454 | 🟢 | 브레인스토밍→계획→TDD→리뷰 흐름을 강제하는 스킬 모음 (⚠️ 별 수가 이례적으로 많음) |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 57,529 | 🟢 | Claude Code 커뮤니티 자료 색인 |
| [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) | 13,901 | 🟢 | 컨텍스트 엔지니어링 템플릿 |
| [jasontang-ai/Context-Engineering](https://github.com/jasontang-ai/Context-Engineering) (구 davidkimai) | 9,279 | 🟢 | 컨텍스트 엔지니어링 핸드북 |

### 🏗 빌더: AI 앱·에이전트를 만든다

| 저장소 | ⭐ | 상태 | 메모 |
|---|---|---|---|
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 77,003 | 🟢 | OpenAI 공식 레시피 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) (구 anthropic-cookbook) | 54,429 | 🟢 | Anthropic 공식 레시피 |
| [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | 17,915 | 🟢 | Google 공식 레시피 |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 79,192 | 🟢 | 에이전트 입문 강의 |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | 34,599 | 🟢 | Hugging Face 에이전트 강의 |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | 27,044 | 🟡 | 실서비스 에이전트 설계 원칙 (2025-09 이후 업데이트 없음, 원칙은 유효) |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 30,272 | 🟢 | RAG 기법 모음 |
| [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) | 24,875 | 🟢 | 에이전트 구현 튜토리얼 |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 26,958 | 🟢 | 프롬프트 평가·레드팀 도구 |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | 17,625 | 🟢 | MCP 입문 |

### 🧠 원리: LLM이 어떻게 동작하는지 알고 싶다

| 저장소 | ⭐ | 상태 | 메모 |
|---|---|---|---|
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 108,015 | 🟢 | LLM을 처음부터 구현하는 책의 코드 |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 84,950 | 🟡 | LLM 학습 로드맵 |
| [karpathy/nanochat](https://github.com/karpathy/nanochat) | 60,370 | 🟢 | 작은 ChatGPT 전체 파이프라인 |

### ⚠️ 주의해서 볼 것

| 저장소 | 이유 |
|---|---|
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) ⭐144,559 | 여러 AI 도구의 **유출된** 시스템 프롬프트 모음. 구조를 배우기엔 유익하지만 출처가 불분명하고 저작권 문제가 있을 수 있음 |
| [anthropics/courses](https://github.com/anthropics/courses) | 🔴 보관됨 |
| [brexhq/prompt-engineering](https://github.com/brexhq/prompt-engineering) | 🟡 2023년 이후 업데이트 없음 (GPT-4 시절 내용) |
| [microsoft/promptbase](https://github.com/microsoft/promptbase) | 🟡 2024년 이후 업데이트 없음 |

---

## 5. 실무자 (꾸준히 읽을 만한 사람들)

| 사람 | 자료 | 왜 |
|---|---|---|
| Simon Willison | [블로그](https://simonwillison.net/tags/prompt-engineering/) · [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/) · [치명적 삼박자](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) | LLM 실사용과 보안에 대해 가장 정확하고 꾸준한 기록 |
| Hamel Husain & Shreya Shankar | [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) | 평가(evals)의 실무 표준 |
| Ethan Mollick | [One Useful Thing](https://www.oneusefulthing.org/) | 와튼 교수. 일반 직장인 관점의 AI 활용 |
| Birgitta Böckeler | [Understanding Spec-Driven Development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | 명세 주도 개발의 냉정한 평가 |

---

## 6. 한국어 자료

| 자료 | 메모 |
|---|---|
| [프롬프트 엔지니어링 가이드 한국어판](https://www.promptingguide.ai/kr/introduction/elements) | dair-ai 가이드의 한국어판. 지시·문맥·입력 데이터·출력 지시자 |
| [Google Gemini 프롬프트 가이드 101 한국어판 (PDF)](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101_ko.pdf) | 역할·할 일·맥락·형식. 업무별 예시가 많음 |
| [Anthropic 프롬프트 엔지니어링 문서 (한국어)](https://platform.claude.com/docs/ko/build-with-claude/prompt-engineering/overview) | 공식 문서 한국어판 |
| [teddylee777/langchain-kr](https://github.com/teddylee777/langchain-kr) ⭐2,058 | 한국어 LangChain 튜토리얼 (🟡 최신 LangChain보다 뒤처질 수 있음) |
| [위키독스: 나 그리고 프롬프트](https://wikidocs.net/book/17643) | 한국어 프롬프트 활용서 |

→ SKALA / Pre-SKALA 관련 자료는 [pre-skala.md](pre-skala.md)에 따로 정리했습니다.

---

> 전체 출처 288개와 각 자료의 확인 수준은 [research/evidence-report.md](../research/evidence-report.md)의 참고문헌에 있습니다.
