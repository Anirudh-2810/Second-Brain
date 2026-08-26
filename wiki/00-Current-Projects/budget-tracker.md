---
module: "current-projects"
topic: "Budget Tracker Pro — VBA Financial Advisor Cash Flow Model (Mac/Win)"
tags: [builds, excel, vba, financial-modeling, budgeting, cash-flow, dashboard, macro, automation]
last_updated: "2026-08-26"
confidence: "high"
source: "Desktop/Anirudh/budgeting excel/VBA_Modules/Module_FinancialAdvisor.bas"
description: "Production-grade VBA module for Excel: Budget vs Actual vs Variance three-sheet model with Executive Dashboard, automatic structure creation, data validation, conditional formatting, parameterized KPIs, runway analysis, critical deviation alerts. Mac-native (no ActiveX/Scripting.Dictionary), cross-platform compatible."
---

# Budget Tracker Pro — VBA Financial Advisor Cash Flow Model

> **Source:** `Desktop/Anirudh/budgeting excel/VBA_Modules/Module_FinancialAdvisor.bas` + `budget101.xlsm` through `budget106_pro.xlsm`
> **Platform:** Excel (Windows + Mac) — no ActiveX, uses `Collection` only
> **Sheets:** Budget, Actual, Variance, Dashboard
> **Protection:** Password-protected structure (`Admin123`)
> **Currency:** INR (₹) with native Mac rupee symbol support

---

## For future agent
This is a **personal finance build** — a complete Excel/VBA financial modeling system that creates a professional Budget/Actual/Variance structure with an Executive Dashboard. Demonstrates advanced VBA: cross-sheet synchronization, formula writing, data validation, conditional formatting, section-aware formula generation, and Mac/Win compatibility. Cross-links: [[wiki/01-Areas/Business/]], [[wiki/01-Areas/Engineering/excel workflows]], [[wiki/00-Current-Projects/quote-pomodoro]].

---

## 1. Sheet Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  WORKBOOK                                                     │
├──────────┬──────────┬──────────┬────────────────────────────┤
│ Budget   │ Actual   │ Variance │ Dashboard                  │
│ (Input)  │ (Input)  │ (Auto)   │ (Executive KPIs)           │
├──────────┴──────────┴──────────┴────────────────────────────┤
│  RunModelRefresh() — Single entry point                       │
└─────────────────────────────────────────────────────────────┘
```

**Column Layout (A:N):**
| Col | Header | Purpose |
|-----|--------|---------|
| A | # | Sequential row number (data rows only) |
| B | Line Item | Account name (Revenue, Expense categories) |
| C:N | Jan–Dec | Monthly values (12 months) |

---

## 2. Core Pipeline (`RunModelRefresh`)

```vba
Public Sub RunModelRefresh()
    On Error GoTo ErrorHandler
    ToggleOptimization True        ' ScreenUpdating=False, Calculation=Manual
    
    If Not VerifySheetsExist Then GoTo CleanExit
    EnsureBaseStructure            ' Create standard layout if missing
    SyncActualAndVarianceSheets    ' Mirror Budget → Actual/Variance, restore cached inputs
    EnforceDataValidation          ' Whole numbers ≥ 0 on data cells
    DesignAllSheets                ' Professional formatting, striping, headers
    BuildDashboardSheet            ' Executive KPIs, metrics, deviations, runway
    ApplyProtection                ' Password-protect all sheets
    
CleanExit:
    ToggleOptimization False
    Exit Sub
ErrorHandler:
    ToggleOptimization False
    MsgBox "Sync Error: " & Err.Description, vbCritical
End Sub
```

---

## 3. Standard Financial Structure

```
Row 1:  Header (# | Line Item | Jan | Feb | ... | Dec)
Row 2:  Opening Balance
Row 3+: Revenue Items
        Product Revenue
        Service Revenue
        Other Income
        Total Income          ← Formula: SUM above
Row n:  R&D Costs
        Salaries
        Contractors
        Software Licenses
        Infrastructure
        Total R&D Costs       ← Formula: SUM above
Row n:  S&M Costs
        Marketing
        Sales Enablement
        Events
        Total S&M Costs       ← Formula: SUM above
Row n:  G&A Costs
        Rent & Facilities
        Legal & Admin
        Travel
        Other
        Total G&A Costs       ← Formula: SUM above
Row n:  Total Expenses        ← R&D + S&M + G&A
Row n:  Closing Balance       ← Opening + Income - Expenses
```

**Section Map** (auto-detected by `ReadSectionMap`):
| Section | Header Row | Start Row | End Row |
|---------|------------|-----------|---------|
| Opening Balance | "Opening Balance" | — | — |
| Income | "Total Income" | After Opening | Before Total Income |
| R&D | "Total R&D Costs" | After Total Income | Before Total R&D |
| S&M | "Total S&M Costs" | After Total R&D | Before Total S&M |
| G&A | "Total G&A Costs" | After Total S&M | Before Total G&A |
| Total Expenses | "Total Expenses" | — | — |
| Closing Balance | "Closing Balance" | — | — |

---

## 4. Synchronization Engine (`SyncActualAndVarianceSheets`)

**Key Features:**
1. **Preserves user input** — Caches Actual sheet values by line-item label before restructuring
2. **Mirrors Budget structure** — Actual/Variance sheets always match Budget row-for-row
3. **Restores cached inputs** — User-entered Actual values survive refresh
4. **Writes formulas** — Opening chain, section sums, total expenses, closing balance
5. **Variance matrix** — `=Actual!C{r}-Budget!C{r}` for every data cell

```vba
' Variance formula (every data cell)
wsV.Cells(r, col).Formula = "=Actual!" & CellRef(r, col) & "-Budget!" & CellRef(r, col)
```

---

## 5. Dashboard — Executive KPIs

### KPI Cards (Row 4-5)
| KPI | Formula | Format |
|-----|---------|--------|
| **Closing Cash** | `=Actual!{ClosingBalance, Dec}` | ₹ |
| **YTD Net Flow** | `SUM(Actual Income) - SUM(Actual Expenses)` | ₹ |
| **Monthly Burn** | `AVERAGE(Actual Expenses Jan:Dec)` | ₹ |
| **Cash Runway** | `IF(Burn<=0, "-", ClosingCash/Burn)` | "X mos" |
| **Expense Ratio** | `Expenses / Income` | % |

### Primary Metrics Table (Rows 9-15)
| Metric | Budget | Actual | Variance | Fav/Unfav |
|--------|--------|--------|----------|-----------|
| Opening Cash | `=Budget!Opening,Jan` | `=Actual!Opening,Jan` | Act-Bud | Higher=Better |
| Total Inflows | `SUM(Budget Income)` | `SUM(Actual Income)` | Act-Bud | Higher=Better |
| Total Outflows | `SUM(Budget Exp)` | `SUM(Actual Exp)` | Act-Bud | **Lower=Better** |
| Net Cash Flow | Inflows - Outflows | Inflows - Outflows | Act-Bud | Higher=Better |
| Closing Cash | `=Budget!Closing,Dec` | `=Actual!Closing,Dec` | Act-Bud | Higher=Better |
| Avg Monthly Burn | `AVG(Budget Exp)` | `AVG(Actual Exp)` | Act-Bud | **Lower=Better** |
| Runway (Months) | `Closing/Burn` | `Closing/Burn` | Act-Bud | Higher=Better |

**Conditional Formatting:**
- Green (favorable): Variance > 0 for "Higher=Better", Variance < 0 for "Lower=Better"
- Red (unfavorable): Opposite

### Critical Deviations (>10%)
Auto-populated list of line items where `|Actual - Budget| / Budget > 10%`:
| Line Item | Budget Total | Actual Total | Deviation % | Impact |
|-----------|--------------|--------------|-------------|--------|
| Salaries | ₹1,200,000 | ₹1,450,000 | 20.8% | Overspend |
| Marketing | ₹300,000 | ₹220,000 | -26.7% | Underspend |

### Runway Analysis
| Metric | Formula |
|--------|---------|
| Current Runway | `ROUND(ClosingCash / MonthlyBurn, 0) & " months"` |
| Zero-Cash Date | `EOMONTH(TODAY(), Runway - 1)` |
| Monthly Burn (Avg) | `AVERAGE(Actual Expenses)` |
| Recommended Buffer | `MAX(0, (Burn × 6) - ClosingCash)` |

---

## 6. Data Validation & Protection

**Validation Rule:** Whole numbers ≥ 0 on all Budget/Actual data cells (C:N)
```vba
With tgt.Validation
    .Add Type:=xlValidateWholeNumber, AlertStyle:=xlValidAlertStop, _
         Operator:=xlGreaterEqual, Formula1:="0"
    .InputMessage = "Enter positive whole numbers only (INR)."
    .ErrorMessage = "Decimals, negatives and text are not allowed."
End With
```

**Protection:** All sheets password-protected (`Admin123`)
- Budget/Actual/Variance: Structure + contents locked, data cells unlocked for entry
- Dashboard: Fully locked
- Variance Notes section (rows 34-38): Unlocked for commentary

---

## 7. Cross-Platform Compatibility

| Feature | Windows | Mac |
|---------|---------|-----|
| **Font** | Segoe UI | Helvetica Neue |
| **Currency** | ₹ via `ChrW(&H20B9)` | Native ₹ |
| **Dictionary** | `Scripting.Dictionary` ❌ | `Collection` ✅ |
| **FileSystemObject** | ❌ | ❌ (avoided) |
| **API Calls** | ❌ | ❌ (avoided) |

**Platform Detection:**
```vba
Private Function PlatformFont() As String
    If LCase(Application.OperatingSystem) Like "*mac*" Then
        PlatformFont = "Helvetica Neue"
    Else
        PlatformFont = "Segoe UI"
    End If
End Function
```

---

## 8. Version History (v101 → v106_pro)

| Version | Key Changes |
|---------|-------------|
| v101 | Initial structure, basic sync |
| v102 | Dashboard KPIs added |
| v103 | Variance conditional formatting |
| v104 | Critical deviation alerts |
| v105 | Runway analysis, zero-cash date |
| v106_pro | Mac-native fonts, rupee symbol, Collection-only, platform detection |

---

## 9. Usage

1. Open `budget106_pro.xlsm` (or any version)
2. Enable macros
3. Run `RunModelRefresh` (Alt+F8 → RunModelRefresh)
4. Enter Budget figures in **Budget** sheet (Jan–Dec columns)
5. Enter Actuals monthly in **Actual** sheet
6. **Variance** auto-calculates
7. **Dashboard** updates live with KPIs, deviations, runway

---

## 10. Cross-References

- [[wiki/01-Areas/Business/]] — Business domain hub
- [[wiki/01-Areas/Engineering/excel workflows]] — Related Excel automation
- [[wiki/00-Current-Projects/quote-pomodoro]] — Personal productivity companion
- [[wiki/01-Areas/Engineering/engineering-math]] — Financial math formulas

---

## 11. Known Limitations / TODOs

- **No multi-year support** — single 12-month cycle
- **No scenario modeling** — single Budget/Actual pair
- **No pivot/charting** — Dashboard is formula-based only
- **No audit trail** — no change log (could add `ChangeLog` sheet)
- **Password hardcoded** — `Admin123` (should be configurable)
- **No ribbon UI** — run via Alt+F8 or add-in

---

## See Also
- [[wiki/01-Areas/Engineering/excel workflows/FinancialAdvisor_RebuildNotes]] — Rebuild notes
- [[wiki/01-Areas/Engineering/excel workflows/Budget_Tracker_Basic]] — Simplified version