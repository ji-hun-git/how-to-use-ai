# 07. AI 코딩: 바이브 코딩에서 에이전틱 엔지니어링으로

> Claude Code, Codex, Gemini CLI, Cursor 같은 **코딩 에이전트**는 파일을 읽고, 명령을 실행하고, 코드를 고칩니다.
> 2025년 말부터 에이전트가 큰 단위의 일을 맡길 만큼 믿을 만해졌다는 평가가 나오면서(Karpathy), 핵심 기술은 "코드 작성"에서 **"명세하고, 확인하고, 책임지는 것"**으로 옮겨 갔습니다.

---

## 1. 바이브 코딩 vs 에이전틱 엔지니어링

| | 바이브 코딩 (Vibe coding) | 에이전틱 엔지니어링 (Agentic engineering) |
|---|---|---|
| 만든 사람 | Karpathy (2025-02) | Karpathy가 후속 개념으로 제안 (2026-02, 언론 보도 기준), Simon Willison이 실천 가이드로 정리 |
| 정의 | AI가 쓴 코드를 **읽지 않고** 결과만 보고 진행 | 에이전트에게 맡기되, 명세·계획 검토·diff 확인·테스트·권한 관리를 **사람이 책임짐** |
| 어울리는 곳 | 주말 프로젝트, 프로토타입, 학습용 실험 | 실제 서비스, 팀 프로젝트, 배포 코드 |
| Karpathy의 표현 | 바닥을 올린다 (누구나 만들 수 있게) | 천장을 올린다 (전문가가 훨씬 더 많이 하게) |

> Simon Willison의 원칙: **다른 사람에게 설명할 수 없는 코드는 커밋하지 않는다.**

---

## 2. 세션이 실망스러운 4가지 이유

Claude Code 공식 문서(2026)는 실망스러운 세션의 원인이 거의 항상 아래 넷 중 하나라고 정리합니다.

| 원인 | 해결 |
|---|---|
| ① 저장소만 봐서는 알 수 없는 **정보가 없었다** | 증상, 재현 방법, 의도, 제약을 프롬프트나 `AGENTS.md`로 제공 |
| ② 에이전트가 **스스로 확인할 방법이 없었다** | 테스트, 빌드, 린터, 스크린샷 비교처럼 통과/실패가 나오는 기준 제공 |
| ③ 절대 어기면 안 되는 규칙을 **도구가 강제하지 않았다** | 프롬프트가 아니라 훅·권한 거부 규칙·CI로 강제 |
| ④ 기본 설정이 **일의 가치보다 비쌌다** | 작업 규모에 맞게 추론 강도와 절차 조절 |

### 두 종류의 지시

| 종류 | 예 | 성격 |
|---|---|---|
| **부탁** (비결정적) | 프롬프트, `CLAUDE.md`/`AGENTS.md`, 스킬 | 모델이 대부분 따르지만 **100%는 아님** |
| **강제** (결정적) | 훅(hook), 권한 거부(deny) 규칙, 테스트, CI | 매번 **반드시** 적용됨 |

> "`.env` 파일 읽지 마"를 `CLAUDE.md`에 쓰는 것은 부탁입니다. 꼭 지켜야 한다면 **권한 설정**으로 막으세요.

---

## 3. 기본 루프

```
0. 준비     짧은 AGENTS.md, 비밀 파일 접근 차단, 샌드박스, 기본 승인 모드
1. 탐색·명세  코드를 읽게 하고(계획 모드), 요구사항이 흐리면 인터뷰 받아 SPEC.md 작성
2. 계획     여러 단계 작업은 코드 작성 전에 계획을 검토
3. 구현     실패하는 테스트 먼저 (Red → Green), 스스로 확인할 기준과 함께
4. 검증     증거(실행한 명령과 출력, 스크린샷) 요구 + 새 세션이나 하위 에이전트가 독립 검토
5. 머지     작고 사람이 읽은 PR만
6. 반영     반복되는 실수는 AGENTS.md, 스킬, 훅에 추가
```

### 작업 지시 템플릿 (OpenAI Codex 권장 4칸)

```markdown
## 목표 (Goal)
## 맥락 (Context)       관련 파일, 문서, 에러 메시지 원문
## 제약 (Constraints)   표준, 규칙, 건드리지 말 것
## 완료 기준 (Done when) 통과해야 할 테스트, 확인 방법
```

→ 전체 템플릿: [templates/coding-task.md](../templates/coding-task.md) · 전체 예제: [examples/05-coding-agent.md](../examples/05-coding-agent.md)

### 구체적으로 지시하기

| ❌ | ✅ |
|---|---|
| 로그인 버그 고쳐줘 | 세션 만료 후 로그인하면 500 에러. `src/auth/`의 토큰 갱신 로직을 보고, 재현하는 실패 테스트를 먼저 쓴 다음 고쳐줘 |
| 이 기능 만들어줘 | (최소 구현에 그치기 쉬움) → "기본을 넘어 완성도 있게 만들어줘"처럼 **원하는 수준을 명시**. Claude Code 문서는 에이전트가 요청을 만족하는 **가장 작은 것**을 만드는 경향이 있다고 설명 |
| (말로 설명) | `@파일`, 스크린샷, 에러 로그를 **직접** 넘기기 |

---

## 4. 스스로 확인할 수단을 준다 (가장 중요)

에이전트가 "다 했습니다"라고 해도 실제로는 안 된 경우가 많습니다. **통과/실패가 나오는 기준**을 주면 에이전트가 스스로 고치며 진행합니다.

| 느슨함 → 엄격함 | 예 |
|---|---|
| 타입 체크, 린터 | `pnpm typecheck` |
| 기존 테스트 | `pytest tests/cart` |
| 새로 쓴 실패 테스트 (Red → Green) | 버그 재현 테스트 |
| 기대 출력과 비교하는 스크립트 | 결과 파일을 정답 파일과 diff |
| 브라우저 스크린샷과 시안 비교 | UI 작업 |

어떤 방법이든 **증거를 요구**하세요. "테스트 통과했습니다"가 아니라 **실행한 명령과 출력**을 보여 달라고 하세요.

> ⚠️ 테스트를 통과시키려고 **값을 하드코딩하거나 테스트를 고치는** 경우가 있습니다. Anthropic은 "테스트는 정답을 확인하는 도구일 뿐 해법을 정의하지 않는다. 테스트가 틀렸다고 생각하면 우회하지 말고 보고하라"고 알려 주라고 권합니다.

### Red/Green TDD

Simon Willison의 정리입니다. 테스트를 **먼저** 쓰고 실패하는 것(Red)을 확인한 뒤 구현해서 통과시킵니다(Green). 실패를 먼저 확인하면 **새 코드를 실제로 시험하지 않는 테스트**를 걸러낼 수 있습니다. 좋은 모델은 "red/green TDD로 해줘"라는 한마디를 알아듣습니다.

---

## 5. 계획 모드와 명세 주도 개발

### 계획 모드 (Plan mode)

대부분의 코딩 에이전트에는 **읽기만 하고 고치지 않는** 계획 모드가 있습니다 (Claude Code, Codex 모두 지원). 여러 파일을 건드리는 일, 요구사항이 모호한 일은 계획 모드에서 시작하세요. 에이전트에게 **인터뷰를 받고 내 가정에 반박**해 달라고 할 수도 있습니다.

### 명세 주도 개발 (Spec-Driven Development, SDD)

명세(spec)를 먼저 쓰고 그것을 기준으로 구현하는 방식입니다. GitHub의 [Spec Kit](https://github.com/github/spec-kit)이 대표적입니다(`constitution → specify → plan → tasks → implement`).

**주의할 점 (Thoughtworks Birgitta Böckeler, 2025):**
- 작은 버그에도 무거운 절차를 쓰면 과하다 (작은 버그가 사용자 스토리 4개와 인수 조건 16개로 불어난 사례)
- 검토할 마크다운 문서가 너무 많아진다
- 에이전트가 명세를 **무시**하기도 해서 통제한다는 착각을 줄 수 있다

**권장:** 일의 크기에 맞추세요. 큰 기능은 SDD, 작은 버그는 한 문단 프롬프트. Spec Kit 스스로도 각 단계는 필수가 아니며 **필요한 가장 작은 것부터** 시작하라고 안내합니다.

---

## 6. 프로젝트 메모리 파일: AGENTS.md / CLAUDE.md

에이전트가 매 세션 시작 때 자동으로 읽는 파일입니다. `AGENTS.md`는 여러 도구가 함께 쓰는 오픈 표준(Linux Foundation 산하 Agentic AI Foundation이 관리)이고, Claude Code는 `CLAUDE.md`를 읽습니다.

**공통 권고 (Anthropic · OpenAI · agents.md)**
- **짧게.** CLAUDE.md는 200줄 이내 권장
- **코드에서 알 수 있는 건 쓰지 않기.** 아키텍처 설명은 더 이상 필요 없다고 Claude Code 문서가 명시
- **반복되는 실수가 생길 때마다 한 줄 추가**
- 빌드·테스트 **명령어**는 꼭 넣기 (OpenAI가 꼽은 흔한 실수: 빌드·테스트 방법을 알려 주지 않음)
- 긴 절차는 스킬로 분리

→ 템플릿: [templates/AGENTS.template.md](../templates/AGENTS.template.md)

---

## 7. 세션 운영 요령

| 상황 | 할 일 |
|---|---|
| 처음 1분 | 에이전트가 엉뚱한 방향으로 가는지 **지켜보기**. 바로 멈추고(Esc) 방향 수정 |
| 두 번 고쳐도 실패 | `/clear` 후 배운 것을 반영한 **새 프롬프트** |
| 주제가 바뀜 | 새 세션 |
| 병렬 작업 | git worktree로 작업 공간을 분리. 같은 파일을 두 에이전트가 동시에 고치지 않게 |
| 독립 검토 | 코드를 쓴 세션이 아니라 **새 세션/하위 에이전트**가 명세 대비 검토 |
| 검토 결과가 너무 많음 | "정확성에 영향 주는 문제만". 문제를 **반드시** 찾으라고 하면 뭐라도 찾아내고, 전부 고치면 과잉 설계가 됨 |

### 무인 실행 전 5가지 질문 (Claude Code 문서)

1. 무엇이 "완료"인지 알고 있는가?
2. 스스로 결과를 확인할 수 있는가?
3. 무엇을 건드려도 되는가?
4. 무엇이 멈추게 하는가? (최대 턴 수, 예산 한도)
5. 결과는 어디로 가고, 누가 승인하는가?

---

## 8. 흔한 실수 (OpenAI Codex 가이드 + Willison)

- 오래 지킬 규칙을 프롬프트에만 쓰고 `AGENTS.md`나 스킬에 넣지 않음
- 빌드·테스트 방법을 알려 주지 않음
- 여러 단계 작업에서 계획을 건너뜀
- 작업 방식을 이해하기 전에 **전체 권한**부터 줌
- 병렬 작업에 worktree를 쓰지 않음
- 손으로 해서 안정적이지 않은 작업을 자동 스케줄에 올림
- 프로젝트 전체를 한 채팅으로 진행
- **검토하지 않은 에이전트 코드로 PR을 올림** → 진짜 검토 부담을 동료에게 떠넘기는 것 (Willison)

---

## 9. 생산성에 대한 현실적인 기대

- METR의 2025년 초 실험에서 숙련된 오픈소스 개발자들은 AI를 쓸 때 **19% 더 느렸습니다.** 본인들은 20% 빨라졌다고 느꼈습니다. METR은 이 결과가 2025년 초 도구 기준이라 지금은 맞지 않을 수 있다고 밝혔습니다.
- Karpathy는 2025년 12월 무렵부터 에이전트 결과물이 크고 일관되며 믿을 만해져서, 일의 단위가 "코드 몇 줄"에서 "기능, 리팩터링, 테스트 같은 큰 단위의 위임"으로 바뀌었다고 말합니다. 그래도 **에이전트는 실수가 잦은 인턴**이며, 명세·검토·책임은 사람의 몫이라고 강조합니다.

> 결론: 체감 속도를 믿지 말고, **내 작업에서 직접 재 보세요.**

---

### 출처

- Claude Code, Best practices (2026) — https://code.claude.com/docs/en/best-practices
- OpenAI Codex, Best practices — https://learn.chatgpt.com/guides/best-practices
- AGENTS.md 오픈 표준 — https://agents.md/
- Anthropic, Prompting best practices (테스트 하드코딩 주의) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic, Effective harnesses for long-running agents (2025-11-26) — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- GitHub Spec Kit — https://github.com/github/spec-kit
- Birgitta Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl" (2025-10-15) — https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- Karpathy, "vibe coding" 게시물 (2025-02-02) — https://x.com/karpathy/status/1886192184808149383
- Karpathy, Sequoia Ascent 2026 요약 (2026-04-30) — https://karpathy.bearblog.dev/sequoia-ascent-2026/
- The New Stack, "Vibe coding is passé" (2026-02) — https://thenewstack.io/vibe-coding-is-passe/
- Simon Willison, "Not all AI-assisted programming is vibe coding" (2025-03-19) — https://simonwillison.net/2025/Mar/19/vibe-coding/
- Simon Willison, "Here's how I use LLMs to help me write code" (2025-03-11) — https://simonwillison.net/2025/Mar/11/using-llms-for-code/
- Simon Willison, Agentic Engineering Patterns (2026~) — https://simonwillison.net/guides/agentic-engineering-patterns/
- METR, Early-2025 AI 숙련 개발자 연구 (2025-07-10) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
