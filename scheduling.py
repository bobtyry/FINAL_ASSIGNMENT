# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:44:32 2026

@author: steev
"""

from math import lcm

# ==========================================================
# FINAL ASSIGNMENT - EXACT OPTIMAL SCHEDULER
# Branch and Bound (Non-preemptive)
# C1 = 3
# Objective:
#   1) No missed deadlines
#   2) Minimize total waiting time
# ==========================================================

tasks = [
    {"name": "T1", "C": 3, "T": 10},
    {"name": "T2", "C": 3, "T": 10},
    {"name": "T3", "C": 2, "T": 20},
    {"name": "T4", "C": 2, "T": 20},
    {"name": "T5", "C": 2, "T": 40},
    {"name": "T6", "C": 2, "T": 40},
    {"name": "T7", "C": 3, "T": 80},
]

# ==========================================================
# Hyperperiod
# ==========================================================
hyper = 1
for t in tasks:
    hyper = lcm(hyper, t["T"])

print("Hyperperiod =", hyper)

# ==========================================================
# Generate jobs over hyperperiod
# ==========================================================
jobs = []

for task in tasks:
    nb = hyper // task["T"]

    for i in range(nb):
        r = i * task["T"]
        d = r + task["T"]

        jobs.append({
            "id": f"{task['name']}_{i+1}",
            "task": task["name"],
            "C": task["C"],
            "release": r,
            "deadline": d
        })

# ==========================================================
# Branch and Bound
# ==========================================================
best_wait = float("inf")
best_sched = None

def lower_bound_wait(time, remaining):
    """
    optimistic lower bound:
    each remaining job starts immediately when possible
    """
    lb = 0
    t = time

    future = sorted(remaining, key=lambda x: x["release"])

    for j in future:
        start = max(t, j["release"])
        lb += start - j["release"]
        t = start + j["C"]

    return lb

def branch(time, remaining, schedule, total_wait):

    global best_wait, best_sched

    # all jobs done
    if not remaining:
        if total_wait < best_wait:
            best_wait = total_wait
            best_sched = schedule[:]
        return

    # pruning with lower bound
    if total_wait + lower_bound_wait(time, remaining) >= best_wait:
        return

    # ready jobs
    ready = [j for j in remaining if j["release"] <= time]

    # if none ready -> jump to next release
    if not ready:
        next_release = min(j["release"] for j in remaining)
        branch(next_release, remaining, schedule, total_wait)
        return

    # heuristic order: earliest deadline first
    ready.sort(key=lambda x: x["deadline"])

    for job in ready:

        start = time
        finish = start + job["C"]

        # hard deadline
        if finish > job["deadline"]:
            continue

        wait = start - job["release"]

        new_sched = schedule + [{
            "Job": job["id"],
            "Start": start,
            "Finish": finish,
            "Deadline": job["deadline"],
            "Waiting": wait,
            "Response": finish - job["release"]
        }]

        new_remaining = remaining.copy()
        new_remaining.remove(job)

        branch(
            finish,
            new_remaining,
            new_sched,
            total_wait + wait
        )

# ==========================================================
# Run optimization
# ==========================================================
branch(0, jobs, [], 0)

# ==========================================================
# Results
# ==========================================================
print("\n===== OPTIMAL RESULT =====")

if best_sched is None:
    print("Task set NOT schedulable")
else:
    print("Schedulable = YES")
    print("Minimum Total Waiting Time =", best_wait)
    print()

    for row in best_sched:
        print(row)