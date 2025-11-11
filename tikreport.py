#!/usr/bin/env python3
# tiktok_report_simulator.py
# HACKING WORLD™ — TikTok Report Simulator (FAKE / PRANK / SAFE)
# NOTE: 100% LOCAL DEMO. No network calls. Do not use for harassment.

import os, sys, time, random

# Colors
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'
C = '\033[1;36m'; M = '\033[1;35m'; W = '\033[1;37m'; RESET = '\033[0m'

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def typewrite(text, delay=0.006):
    for ch in text:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

def spinner(msg, secs=1.8):
    frames = ['|','/','-','\\']
    sys.stdout.write(Y + msg + " ")
    t0 = time.time(); i = 0
    while time.time() - t0 < secs:
        sys.stdout.write(frames[i % 4]); sys.stdout.flush()
        time.sleep(0.10); sys.stdout.write('\b'); i += 1
    print(G + " ✓" + RESET)

def progress_bar(title, width=36, duration=2.0):
    sys.stdout.write(C + title + "\n")
    steps = max(1, int(duration / 0.04))
    for i in range(steps + 1):
        filled = int(i / steps * width)
        bar = "█" * filled + "░" * (width - filled)
        percent = int(i / steps * 100)
        sys.stdout.write(M + f"[{bar}] {percent:3d}%\r" + RESET)
        sys.stdout.flush(); time.sleep(0.04)
    print()

def banner():
    clear()
    art = [
        f"{M}████████╗██╗██╗  ██╗████████╗",
        f"{C}╚══██╔══╝██║██║  ██║╚══██╔══╝",
        f"{G}   ██║   ███████║   ██║   ",
        f"{Y}   ██║   ██╔══██║   ██║   ",
        f"{R}   ██║   ██║  ██║   ██║   {RESET}"
    ]
    for ln in art: print(ln); time.sleep(0.01)
    print(W + "\n    H A C K I N G   W O R L D™ — TikTok Report Simulator\n" + RESET)
    print(R + "!!! DEMO / PRANK — This program does NOT send real reports. Do not harass others. !!!\n" + RESET)

def choose_reason():
    reasons = [
        "Harassment / Bullying",
        "Spam / Fake engagement",
        "Nudity / Sexual content",
        "Hate speech",
        "Impersonation",
        "Dangerous acts",
        "Other"
    ]
    print(C + "Select report reason:" + RESET)
    for i,r in enumerate(reasons,1):
        print(f" [{i}] {r}")
    choice = input(Y + "Choose (1-7, default 1): " + W).strip()
    try:
        idx = max(1, min(7, int(choice)))
    except:
        idx = 1
    return reasons[idx-1]

def fake_prepare(username, reason, count):
    typewrite(C + f"Preparing {count} simulated report(s) for @{username} — Reason: {reason}" + RESET, 0.008)
    spinner("[*] Packaging report payload (visual)", 1.6)
    progress_bar("[#] Encrypting & signing (simulation)", 36, 1.6)
    spinner("[*] Dispatching to moderation mesh (visual)", 1.6)

def fake_evaluate():
    # weighted outcomes: mostly No Violation or Review Pending
    r = random.random()
    if r < 0.65:
        return ("NO VIOLATION FOUND", "No policy violation detected. Report dismissed.", False)
    elif r < 0.9:
        return ("REVIEW PENDING", "Report is queued for manual review by moderators.", None)
    else:
        return ("ACTION TAKEN", "Policy violation detected — account action suggested (SIMULATION).", True)

def save_log(username, reason, count, outcome_label):
    try:
        os.makedirs("sim_logs", exist_ok=True)
        path = f"sim_logs/tiktok_report_sim_{int(time.time())}.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write("TIKTOK REPORT SIMULATION — HACKING WORLD™\n")
            f.write(f"time: {time.ctime()}\n")
            f.write(f"username: @{username}\n")
            f.write(f"reason: {reason}\n")
            f.write(f"simulated_reports: {count}\n")
            f.write(f"outcome: {outcome_label}\n")
        return path
    except Exception:
        return None

def run_simulation():
    banner()
    print(W + "⚠️  Reminder: This tool is a LOCAL SIMULATION. It does NOT contact TikTok or send reports.\n" + RESET)
    username = input(Y + "Enter TikTok username (without @): " + W).strip().lstrip('@')
    if not username:
        print(R + "Username required. Exiting." + RESET); time.sleep(0.8); return

    reason = choose_reason()
    try:
        count = int(input(Y + "How many reports to simulate? (e.g. 1-50, default 1): " + W).strip())
        count = max(1, min(500, count))
    except:
        count = 1

    print()
    fake_prepare(username, reason, count)
    # simulate sending each report visually
    for i in range(1, count+1):
        spinner(f"Sending simulated report {i}/{count}", 0.9)
        # small randomized pause
        time.sleep(random.uniform(0.2, 0.8))
    # await moderation simulation
    spinner("[*] Awaiting moderation result (visual)", 2.4)
    outcome_label, outcome_text, action_flag = fake_evaluate()

    # display result
    print()
    print(M + "──────────────────────────────────────────────" + RESET)
    print(G + f"Result: {outcome_label}" + RESET)
    print(W + outcome_text + RESET)
    if action_flag is True:
        print(Y + "Simulation note: (action would be suspension/strike) — THIS IS A DEMO." + RESET)
    elif action_flag is False:
        print(Y + "Simulation note: (no action taken) — THIS IS A DEMO." + RESET)
    else:
        print(Y + "Simulation note: (under manual review) — THIS IS A DEMO." + RESET)
    print(M + "──────────────────────────────────────────────\n" + RESET)

    if input(Y + "[?] Save simulation log locally? (y/N): " + W).strip().lower() == 'y':
        p = save_log(username, reason, count, outcome_label)
        if p:
            print(G + "[✓] Saved simulation log → " + p + RESET)
        else:
            print(R + "[!] Save failed." + RESET)

    input(W + "\nPress Enter to return to menu..." + RESET)

def main_menu():
    while True:
        banner()
        print(C + "Menu:" + RESET)
        print(" [1] Run a new report simulation")
        print(" [2] Batch simulate (multiple usernames from file)")
        print(" [3] View saved simulation logs")
        print(" [0] Exit\n")
        choice = input(Y + "Choose (0-3): " + W).strip()
        if choice == '1':
            run_simulation()
        elif choice == '2':
            filename = input(Y + "Enter path to file (one username per line): " + W).strip()
            if not os.path.isfile(filename):
                print(R + "File not found. Returning to menu." + RESET); time.sleep(0.8); continue
            reason = choose_reason()
            try:
                count = int(input(Y + "Reports per user (e.g. 1): " + W).strip())
            except:
                count = 1
            with open(filename, 'r', encoding='utf-8') as f:
                users = [line.strip().lstrip('@') for line in f if line.strip()]
            for u in users:
                print()
                fake_prepare(u, reason, count)
                for i in range(1, count+1):
                    spinner(f"Sending simulated report {i}/{count} for @{u}", 0.7)
                    time.sleep(random.uniform(0.15,0.6))
                spinner("[*] Awaiting moderation result (visual)", 1.4)
                lab, txt, _ = fake_evaluate()
                print(G + f"Result for @{u}: {lab}" + RESET)
                time.sleep(0.6)
            input(W + "\nBatch complete. Press Enter to return to menu..." + RESET)
        elif choice == '3':
            d = "sim_logs"
            if not os.path.isdir(d):
                print(R + "No logs found." + RESET); time.sleep(0.8); continue
            files = sorted(os.listdir(d))
            for i,fname in enumerate(files,1):
                print(f" [{i}] {fname}")
            pick = input(Y + "Enter number to view or press Enter to go back: " + W).strip()
            if pick.isdigit():
                idx = int(pick)-1
                if 0 <= idx < len(files):
                    path = os.path.join(d, files[idx])
                    clear()
                    print(G + f"--- Viewing: {files[idx]} ---\n" + RESET)
                    print(open(path, 'r', encoding='utf-8').read())
                    input(W + "\nPress Enter to return..." + RESET)
        else:
            print(R + "Exiting. Stay responsible." + RESET)
            time.sleep(0.6)
            break

if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n" + R + "Interrupted. Exiting." + RESET)