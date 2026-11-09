#!/usr/bin/env python3
"""Generate ticket-export.txt, a long synthetic ticket-tracker export for the long-input eval case.

The question asked about it: which tickets are open and assigned to Priya on March 31?
The answer is computed by replaying the activity log, not written by hand, and the script
prints the ID sets that the case's code checks use (see cases-hard.yaml, case coverage-ticket-export).

Traps: tickets reassigned to and away from Priya, closed and reopened tickets, a ticket that
went away and came back, tickets that Priya only commented on, and a second person named Priyanka.

Run:  python evals/skills/data/make_ticket_export.py   (deterministic: fixed seed)
"""
from __future__ import annotations

import datetime as dt
import random
from pathlib import Path

SEED = 20260309
N_TICKETS = 180
OUT = Path(__file__).resolve().parent / "ticket-export.txt"

PEOPLE = ["Marcus", "Lena", "Tom", "Aisha", "Jonas", "Sofia", "Wei", "Priyanka"]
AREAS = ["Export", "Login", "Billing", "Sync", "Search", "Notifications", "Sharing", "Reports",
         "Calendar", "Attachments", "Settings", "Onboarding", "API", "Mobile app", "Web app"]
PROBLEMS = [
    "CSV file is missing the header row", "page loads slowly for large accounts",
    "error message is unclear", "duplicate items after reconnecting", "button does nothing on first tap",
    "dates shown in the wrong timezone", "email arrives twice", "filter resets after refresh",
    "totals do not match the invoice", "upload fails for files over 20 MB", "dark text on dark background",
    "wrong language after switching accounts", "rate limit hit during bulk import", "share link expires too early",
    "search ignores accented characters", "sort order changes randomly", "reminder fires an hour late",
    "crash when the list is empty", "password reset link not received", "permissions not applied to new members",
]
DESCRIPTIONS = [
    "Customer reports the issue happens every time on their account.",
    "Reproduced internally on staging; steps attached to the ticket.",
    "Only some users are affected; we have not found the pattern yet.",
    "Started after the last release according to the customer.",
    "Workaround exists but customers find it confusing.",
    "Reported by three different customers this week.",
    "Low impact, but it shows up in support chats regularly.",
    "Customer sent a screen recording; see attachment.",
]
OPEN_STATUSES = ["Open", "In progress", "Waiting on customer"]
COMMENTS = [
    "Looked at the logs; this may share a root cause with {other}.",
    "Customer confirmed the workaround helps for now.",
    "Could not reproduce on the latest build. Asking for more details.",
    "Adding this to the next sprint's candidate list.",
    "Same report came in through chat today.",
    "Linked to {other} for tracking.",
    "Customer asked for an update; replied with the current status.",
    "Needs a decision from product before we continue.",
]


def main() -> None:
    rng = random.Random(SEED)
    ids = [f"LST-{1001 + i}" for i in range(N_TICKETS)]
    shuffled = ids[:]
    rng.shuffle(shuffled)
    take = iter(shuffled)

    def pick(n):
        return [next(take) for _ in range(n)]

    # Planned groups (initial state on March 1 -> what happens in March).
    untouched = pick(5)        # Priya, open; no assignment or closing events
    closed_in_march = pick(3)  # Priya, open -> closed
    moved_away = pick(2)       # Priya -> someone else
    away_and_back = pick(1)    # Priya -> someone else -> Priya
    moved_in = pick(3)         # someone else -> Priya
    in_then_closed = pick(1)   # someone else -> Priya -> closed
    reopened = pick(2)         # Priya, closed -> reopened
    priyanka_open = pick(3)    # Priyanka, open (name trap)
    priya_commented = pick(2)  # someone else, open; Priya only comments

    tickets = {}
    for tid in ids:
        tickets[tid] = {
            "title": f"{rng.choice(AREAS)}: {rng.choice(PROBLEMS)}",
            "created": dt.date(2026, 1, 5) + dt.timedelta(days=rng.randrange(0, 53)),
            "assignee": rng.choice([p for p in PEOPLE if p != "Priyanka"]),
            "status": rng.choice(OPEN_STATUSES + ["Closed"]),
            "priority": rng.choice(["P1", "P2", "P2", "P3", "P3", "P3", "P4"]),
            "description": rng.choice(DESCRIPTIONS),
        }
    for tid in untouched + closed_in_march + moved_away + away_and_back:
        tickets[tid].update(assignee="Priya", status=rng.choice(OPEN_STATUSES))
    for tid in moved_in + in_then_closed + priya_commented:
        tickets[tid].update(assignee=rng.choice(["Marcus", "Lena", "Jonas", "Sofia"]),
                            status=rng.choice(OPEN_STATUSES))
    for tid in reopened:
        tickets[tid].update(assignee="Priya", status="Closed")
    for tid in priyanka_open:
        tickets[tid].update(assignee="Priyanka", status=rng.choice(OPEN_STATUSES))
    # A few closed Priya tickets that stay closed, and a few Priyanka ones, as background.
    special = set(untouched + closed_in_march + moved_away + away_and_back + moved_in + in_then_closed
                  + reopened + priyanka_open + priya_commented)
    rest = [t for t in ids if t not in special]
    for tid in rng.sample(rest, 4):
        tickets[tid].update(assignee="Priya", status="Closed")
    for tid in rng.sample([t for t in rest if tickets[t]["assignee"] != "Priya"], 3):
        tickets[tid].update(assignee="Priyanka", status="Closed")

    initial = {t: (v["assignee"], v["status"]) for t, v in tickets.items()}
    events = []  # (datetime, ticket, kind, payload)

    def when(day_lo=2, day_hi=31):
        d = rng.randint(day_lo, day_hi)
        return dt.datetime(2026, 3, d, rng.randint(8, 18), rng.randrange(0, 60))

    def other_than(*names):
        return rng.choice([p for p in PEOPLE if p not in names and p != "Priyanka"])

    for tid in closed_in_march:
        events.append((when(), tid, "status", "Closed"))
    for tid in moved_away:
        events.append((when(), tid, "assign", other_than("Priya")))
    for tid in away_and_back:
        t1 = when(3, 14)
        events.append((t1, tid, "assign", other_than("Priya")))
        events.append((t1 + dt.timedelta(days=rng.randint(4, 12)), tid, "assign", "Priya"))
    for tid in moved_in:
        events.append((when(), tid, "assign", "Priya"))
    for tid in in_then_closed:
        t1 = when(3, 12)
        events.append((t1, tid, "assign", "Priya"))
        events.append((t1 + dt.timedelta(days=rng.randint(3, 10)), tid, "status", "Closed"))
    for tid in reopened:
        events.append((when(), tid, "status", "Open"))
    for tid in priya_commented:
        events.append((when(), tid, "comment-priya", None))
        events.append((when(), tid, "comment-priya", None))

    # Background noise: comments, priority and label changes, status moves between open states,
    # closures and reassignments among other people. None of it touches the planned groups'
    # assignee, and closures only hit tickets that are not Priya's.
    planned_assign = set(moved_away + away_and_back + moved_in + in_then_closed)
    for _ in range(330):
        tid = rng.choice(ids)
        kind = rng.choices(["comment", "priority", "label", "status-open", "close", "assign"],
                           weights=[40, 15, 10, 15, 10, 10])[0]
        a, s = initial[tid]
        if kind == "close" and (a == "Priya" or tid in special or s == "Closed"):
            kind = "comment"
        if kind == "assign" and (a in ("Priya", "Priyanka") or tid in special or tid in planned_assign):
            kind = "priority"
        if kind == "status-open" and s == "Closed":
            kind = "label"
        payload = {
            "comment": None, "priority": rng.choice(["P1", "P2", "P3", "P4"]),
            "label": rng.choice(["needs-info", "regression", "customer-impact", "quick-win", "ux"]),
            "status-open": rng.choice(OPEN_STATUSES), "close": "Closed",
            "assign": other_than(a),
        }[kind]
        events.append((when(), tid, kind, payload))
    events.sort(key=lambda e: e[0])

    # Replay to compute the final state, and render the log.
    state = {t: list(v) for t, v in initial.items()}
    prio = {t: v["priority"] for t, v in tickets.items()}
    log = []
    for ts, tid, kind, payload in events:
        stamp = ts.strftime("%Y-%m-%d %H:%M")
        actor = rng.choice(["Marcus", "Lena", "Tom", "Aisha", "Jonas", "Sofia", "Wei"])
        if kind in ("assign",):
            log.append(f"{stamp}  {tid}  Assignee changed: {state[tid][0]} -> {payload}  (by {actor})")
            state[tid][0] = payload
        elif kind in ("status", "status-open", "close"):
            if state[tid][1] == payload:
                continue
            note = ""
            if payload == "Closed":
                note = f"  (resolution: {rng.choice(['fixed', 'duplicate', 'cannot reproduce', 'fixed'])})"
            elif state[tid][1] == "Closed":
                note = "  (reopened: customer reports the problem is back)"
            log.append(f"{stamp}  {tid}  Status changed: {state[tid][1]} -> {payload}{note}  (by {actor})")
            state[tid][1] = payload
        elif kind == "priority":
            if prio[tid] == payload:
                continue
            log.append(f"{stamp}  {tid}  Priority changed: {prio[tid]} -> {payload}  (by {actor})")
            prio[tid] = payload
        elif kind == "label":
            log.append(f"{stamp}  {tid}  Label added: {payload}  (by {actor})")
        elif kind == "comment":
            text = rng.choice(COMMENTS).format(other=rng.choice(ids))
            log.append(f"{stamp}  {tid}  Comment by {rng.choice(PEOPLE)}: \"{text}\"")
        elif kind == "comment-priya":
            text = rng.choice(COMMENTS).format(other=rng.choice(ids))
            log.append(f"{stamp}  {tid}  Comment by Priya: \"{text}\"")

    expected = sorted(t for t, (a, s) in state.items() if a == "Priya" and s != "Closed")
    # Sanity: the planned groups end where they should.
    assert set(expected) == set(untouched + away_and_back + moved_in + reopened), "plan and replay disagree"
    for t in closed_in_march + in_then_closed:
        assert state[t][1] == "Closed"
    for t in moved_away:
        assert state[t][0] != "Priya"
    for t in priyanka_open:
        assert state[t][0] == "Priyanka" and state[t][1] != "Closed"
    for t in priya_commented:
        assert state[t][0] != "Priya"

    lines = [
        "Listly support tracker: ticket export (fictional example)",
        "Exported: 2026-03-31 18:30. Contains the ticket list as of 2026-03-01, followed by the full activity log for March 2026.",
        "Statuses: Open, In progress, Waiting on customer, Closed. Every status except Closed counts as open.",
        "",
        "=== PART 1: TICKETS AS OF 2026-03-01 ===",
        "",
    ]
    for tid in ids:
        t = tickets[tid]
        lines += [
            f"{tid} | {t['title']}",
            f"  Created: {t['created']} | Assignee: {t['assignee']} | Status: {t['status']} | Priority: {t['priority']}",
            f"  {t['description']}",
            "",
        ]
    lines += ["=== PART 2: ACTIVITY LOG, 2026-03-02 TO 2026-03-31 ===", ""] + log + ["", "=== END OF EXPORT ==="]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")  # LF on every OS

    def fmt(xs):
        return "[" + ", ".join(f'"{x}"' for x in sorted(xs)) + "]"

    print(f"wrote {OUT.name}: {N_TICKETS} tickets, {len(log)} log entries, {len(OUT.read_text(encoding='utf-8').split())} words")
    print("expected (open, Priya):", fmt(expected))
    print("  untouched:", fmt(untouched))
    print("  moved in (incl. away and back):", fmt(moved_in + away_and_back))
    print("  reopened:", fmt(reopened))
    print("excluded, closed in March:", fmt(closed_in_march + in_then_closed))
    print("excluded, moved away:", fmt(moved_away))
    print("excluded, Priyanka:", fmt(priyanka_open))
    print("excluded, Priya only commented:", fmt(priya_commented))


if __name__ == "__main__":
    main()
