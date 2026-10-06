"""
HUB Test Data Generator
Generates HUB_Test_Data.xlsx with 3 sheets:
  1. All TC        – 500 test cases
  2. Defect List   – 200 defects
  3. Defect vs TC  – ~900 mapping rows
"""
import random, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

random.seed(42)

# ── helpers ────────────────────────────────────────────────────────────────────
def rdate(start, days):
    return start + datetime.timedelta(days=random.randint(0, days))

START_EXEC  = datetime.date(2026, 9, 14)
START_DEF   = datetime.date(2026, 9, 12)
MODULES     = ["Login","Dashboard","Payments","Reports","User Mgmt","API","Search","Notifications","Settings","Audit"]
PRIORITIES  = ["P1","P2","P3","P4"]
PWEIGHTS    = [0.10, 0.25, 0.40, 0.25]
STATUSES_TC = ["Pass","Fail","Blocked","Not Run"]
STWEIGHTS   = [0.765, 0.115, 0.07, 0.05]
STATUSES_D  = ["New","Open","In Progress","Ready for Retest","Closed","Reopen","Assigned"]
DWEIGHTS    = [0.08, 0.18, 0.15, 0.12, 0.32, 0.07, 0.08]
ASSIGNEES   = ["Rahul S","Priya M","Arun K","Sneha T","Vikram R","Deepa L","Karan B","Nisha P"]
TEAMS       = ["Team Alpha","Team Beta","Team Gamma","Team Delta"]
RAISERS     = ["QA Lead","Tester 1","Tester 2","Tester 3","Automation"]
ROOT_CAUSES = ["Code Defect","Requirement Gap","Environment Issue","Data Issue","Config Error","Design Flaw"]
DESCRIPTIONS_D = [
    "Login page crashes on invalid input",
    "Payment gateway timeout on large transactions",
    "Dashboard widgets not loading after session refresh",
    "Report export fails for date ranges > 90 days",
    "User role permissions not enforced on API endpoints",
    "Search returns incorrect results for special characters",
    "Notifications not triggered on status change",
    "Audit log missing entries for bulk operations",
    "Settings page throws 500 error on save",
    "Pagination broken on reports listing page",
    "Password reset email not delivered",
    "Two-factor authentication bypass vulnerability",
    "CSV export includes extra blank rows",
    "Dropdown not populated in IE11",
    "Date picker not working in mobile view",
    "Session timeout not redirecting to login",
    "API returns 200 with empty body on error",
    "Batch upload silently drops records",
    "Chart tooltip shows wrong data on hover",
    "Filter reset button clears mandatory fields",
]

wb = Workbook()

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 1 – All TC
# ══════════════════════════════════════════════════════════════════════════════
ws1 = wb.active
ws1.title = "All TC"
hdr1 = ["TC ID","Test Case Name","Module","Priority","Status","Executed By","Execution Date","Defect ID","Comments"]
ws1.append(hdr1)
tc_rows = []
for i in range(1, 501):
    tcid    = f"TC-{i:04d}"
    mod     = random.choice(MODULES)
    prio    = random.choices(PRIORITIES, PWEIGHTS)[0]
    status  = random.choices(STATUSES_TC, STWEIGHTS)[0]
    execby  = random.choice(ASSIGNEES)
    execdt  = rdate(START_EXEC, 6)
    defid   = f"HUB-{random.randint(1,200):03d}" if status == "Fail" else ""
    comment = "Auto-executed" if i % 5 == 0 else ""
    name    = f"{mod} - Test scenario {i}"
    row = [tcid, name, mod, prio, status, execby, execdt, defid, comment]
    ws1.append(row)
    tc_rows.append({"tcid": tcid, "status": status, "prio": prio, "mod": mod})

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 2 – Defect List
# ══════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("Defect List")
hdr2 = ["Defect ID","Description","Priority","Status","Raised By","Assied To","Assigned Team",
        "Raised on","ETA","Closed on","Root Cause","Comments"]
ws2.append(hdr2)
def_rows = []
for i in range(1, 201):
    did     = f"HUB-{i:03d}"
    desc    = DESCRIPTIONS_D[(i-1) % len(DESCRIPTIONS_D)]
    prio    = random.choices(PRIORITIES, PWEIGHTS)[0]
    status  = random.choices(STATUSES_D, DWEIGHTS)[0]
    raiser  = random.choice(RAISERS)
    assied  = random.choice(ASSIGNEES)
    team    = random.choice(TEAMS)
    raised  = rdate(START_DEF, 4)
    eta_dt  = raised + datetime.timedelta(days=random.randint(3,14))
    closed  = (raised + datetime.timedelta(days=random.randint(5,20))) if status == "Closed" else None
    rc      = random.choice(ROOT_CAUSES)
    comment = f"Tracked in sprint {random.randint(1,4)}"
    row = [did, desc, prio, status, raiser, assied, team, raised, eta_dt, closed, rc, comment]
    ws2.append(row)
    def_rows.append({"id": did, "prio": prio})

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 3 – Defect vs TC
# ══════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("Defect vs TC")
hdr3 = ["Defect ID","TC ID","Relationship"]
ws3.append(hdr3)
tc_ids = [r["tcid"] for r in tc_rows]
p_tc_count = {"P1":(8,12),"P2":(5,7),"P3":(2,4),"P4":(0,1)}
for d in def_rows:
    lo,hi = p_tc_count[d["prio"]]
    cnt   = random.randint(lo, hi)
    chosen = random.sample(tc_ids, min(cnt, len(tc_ids)))
    for tc in chosen:
        ws3.append([d["id"], tc, "Blocks"])

# ── style headers ──────────────────────────────────────────────────────────────
HDR_FILL = PatternFill("solid", fgColor="1E293B")
HDR_FONT = Font(bold=True, color="FFFFFF")
for ws in [ws1, ws2, ws3]:
    for cell in ws[1]:
        cell.fill = HDR_FILL
        cell.font = HDR_FONT
        cell.alignment = Alignment(horizontal="center")
    ws.freeze_panes = "A2"

out = r"C:\Users\RishavGupta\Desktop\BOB\test-management\HUB_Test_Data.xlsx"
wb.save(out)
print(f"Saved: {out}")
