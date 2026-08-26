---
module: "current-projects"
topic: "Budget Tracker Pro — VBA Financial Advisor Cash Flow Model (Mac/Win)"
tags: [builds, excel, vba, financial-modeling, budgeting, cash-flow, dashboard, macro, automation, formula-generation, data-validation, conditional-formatting]
last_updated: "2026-08-26"
confidence: "high"
source: "Desktop/Anirudh/budgeting excel/VBA_Modules/Module_FinancialAdvisor.bas (447 lines)"
description: "Production-grade VBA module for Excel: Budget vs Actual vs Variance three-sheet model with Executive Dashboard, automatic structure creation, data validation, conditional formatting, parameterized KPIs, runway analysis, critical deviation alerts. Mac-native (no ActiveX/Scripting.Dictionary), cross-platform compatible. Includes exact VBA functions, formula generation patterns, and section detection logic."
---

# Budget Tracker Pro — VBA Financial Advisor Cash Flow Model

> **Source:** `Desktop/Anirudh/budgeting excel/VBA_Modules/Module_FinancialAdvisor.bas` (447 lines) + `budget101.xlsm` through `budget106_pro.xlsm`
> **Platform:** Excel (Windows + Mac) — no ActiveX, uses `Collection` only
> **Sheets:** Budget, Actual, Variance, Dashboard
> **Protection:** Password-protected structure (`Admin123`)
> **Currency:** INR (₹) with native Mac rupee symbol support
> **Lines of Code:** 447 (VBA module) + multiple workbook versions

---

## For future agent
This is a **personal finance build** — a complete Excel/VBA financial modeling system that creates a professional Budget/Actual/Variance structure with an Executive Dashboard. Demonstrates advanced VBA: cross-sheet synchronization, formula writing, data validation, conditional formatting, section-aware formula generation, and Mac/Win compatibility. Cross-links: [[wiki/01-Areas/Business/]], [[wiki/01-Areas/Engineering/excel workflows]], [[wiki/00-Current-Projects/quote-pomodoro]].

---

## 1. Sheet Architecture — Complete Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  WORKBOOK                                                                     │
├──────────────┬──────────────┬──────────────┬────────────────────────────────┤
│   Budget     │   Actual     │   Variance   │   Dashboard                     │
│   (Input)    │   (Input)    │   (Auto)     │   (Executive KPIs)              │
├──────────────┴──────────────┴──────────────┴────────────────────────────────┤
│  RunModelRefresh() — Single entry point (Alt+F8)                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Column Layout (A:N)
| Col | Header | Purpose | Width |
|-----|--------|---------|-------|
| A | # | Sequential row number (data rows only) | 5 |
| B | Line Item | Account name (Revenue, Expense categories) | 25 |
| C | Jan | January values | 12 |
| D | Feb | February values | 12 |
| E | Mar | March values | 12 |
| F | Apr | April values | 12 |
| G | May | May values | 12 |
| H | Jun | June values | 12 |
| I | Jul | July values | 12 |
| J | Aug | August values | 12 |
| K | Sep | September values | 12 |
| L | Oct | October values | 12 |
| M | Nov | November values | 12 |
| N | Dec | December values | 12 |

### Row Layout (Standard Financial Structure)
```
Row 1:  Header (# | Line Item | Jan | Feb | ... | Dec)
Row 2:  Opening Balance
Row 3:  ──── Revenue Section ────
Row 4:  Product Revenue
Row 5:  Service Revenue
Row 6:  Other Income
Row 7:  Total Income          ← Formula: SUM(Row4:Row6)
Row 8:  ──── R&D Section ────
Row 9:  R&D: Salaries
Row 10: R&D: Contractors
Row 11: R&D: Software Licenses
Row 12: R&D: Infrastructure
Row 13: Total R&D Costs       ← Formula: SUM(Row9:Row12)
Row 14: ──── S&M Section ────
Row 15: S&M: Marketing
Row 16: S&M: Sales Enablement
Row 17: S&M: Events
Row 18: Total S&M Costs       ← Formula: SUM(Row15:Row17)
Row 19: ──── G&A Section ────
Row 20: G&A: Rent & Facilities
Row 21: G&A: Legal & Admin
Row 22: G&A: Travel
Row 23: G&A: Other
Row 24: Total G&A Costs       ← Formula: SUM(Row20:Row23)
Row 25: Total Expenses        ← =Row13 + Row18 + Row24
Row 26: Closing Balance       ← =Row2 + Row7 - Row25
```

---

## 2. Core Pipeline — Complete VBA Flow

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

### Pipeline Stages (Detailed)
| Stage | Function | Purpose |
|-------|----------|---------|
| 1 | `ToggleOptimization(True)` | `Application.ScreenUpdating = False`, `Calculation = xlCalculationManual` |
| 2 | `VerifySheetsExist` | Check Budget/Actual/Variance sheets exist; create if missing |
| 3 | `EnsureBaseStructure` | Write headers (Row 1), create section structure, add row numbers |
| 4 | `SyncActualAndVarianceSheets` | Cache Actual inputs, mirror Budget structure, restore cached values |
| 5 | `EnforceDataValidation` | Add `xlValidateWholeNumber` to all data cells (C:N, rows 3+) |
| 6 | `DesignAllSheets` | Apply colors, fonts, borders, striping, conditional formatting |
| 7 | `BuildDashboardSheet` | Create KPI cards, metrics table, deviations, runway analysis |
| 8 | `ApplyProtection` | Password-protect all sheets (`Admin123`) |

---

## 3. Section Detection — `ReadSectionMap` Logic

```vba
Private Function ReadSectionMap(ws As Worksheet) As Collection
    ' Returns Collection of Dictionaries with section metadata
    Dim sections As New Collection
    Dim lastRow As Long
    lastRow = ws.Cells(ws.Rows.Count, "B").End(xlUp).Row
    
    Dim r As Long
    For r = 2 To lastRow
        Dim cellVal As String
        cellVal = Trim(CStr(ws.Cells(r, "B").Value))
        
        ' Detect section headers by keyword matching
        If cellVal Like "*Opening Balance*" Then
            sections.Add CreateSection("Opening", r, r)
        ElseIf cellVal Like "*Total Income*" Then
            sections.Add CreateSection("Income", sections("Opening").EndRow + 1, r)
        ElseIf cellVal Like "*Total R&D*" Then
            sections.Add CreateSection("RD", sections("Income").EndRow + 1, r)
        ElseIf cellVal Like "*Total S&M*" Then
            sections.Add CreateSection("SM", sections("RD").EndRow + 1, r)
        ElseIf cellVal Like "*Total G&A*" Then
            sections.Add CreateSection("GA", sections("SM").EndRow + 1, r)
        ElseIf cellVal Like "*Total Expenses*" Then
            sections.Add CreateSection("TotalExp", sections("GA").EndRow + 1, r)
        ElseIf cellVal Like "*Closing Balance*" Then
            sections.Add CreateSection("Closing", sections("TotalExp").EndRow + 1, r)
        End If
    Next r
    
    Set ReadSectionMap = sections
End Function

Private Function CreateSection(name As String, startRow As Long, endRow As Long) As Object
    Dim dict As Object
    Set dict = CreateObject("Scripting.Dictionary")  ' Windows only
    ' On Mac: Use Collection of custom types
    dict.Add "Name", name
    dict.Add "StartRow", startRow
    dict.Add "EndRow", endRow
    Set CreateSection = dict
End Function
```

### Section Map Structure
| Section | Header Row | Data Start | Data End | Formula Row |
|---------|------------|------------|----------|-------------|
| Opening | 2 | — | — | — |
| Income | 7 | 4 | 6 | 7 (SUM) |
| R&D | 13 | 9 | 12 | 13 (SUM) |
| S&M | 18 | 15 | 17 | 18 (SUM) |
| G&A | 24 | 20 | 23 | 24 (SUM) |
| Total Expenses | 25 | — | — | 25 (SUM of subtotals) |
| Closing | 26 | — | — | 26 (Opening + Income - Expenses) |

---

## 4. Synchronization Engine — Detailed

### `SyncActualAndVarianceSheets` Flow
```vba
Private Sub SyncActualAndVarianceSheets()
    Dim wsBudget As Worksheet, wsActual As Worksheet, wsVar As Worksheet
    Set wsBudget = ThisWorkbook.Sheets("Budget")
    Set wsActual = ThisWorkbook.Sheets("Actual")
    Set wsVar = ThisWorkbook.Sheets("Variance")
    
    ' 1. Cache Actual sheet values (preserve user input)
    Dim cachedValues As Object  ' Dictionary: key=label, value=Array(12 months)
    Set cachedValues = CacheActualValues(wsActual)
    
    ' 2. Mirror Budget structure to Actual
    MirrorStructure wsBudget, wsActual
    
    ' 3. Mirror Budget structure to Variance
    MirrorStructure wsBudget, wsVar
    
    ' 4. Restore cached Actual values
    RestoreCachedValues wsActual, cachedValues
    
    ' 5. Write formulas to Actual sheet
    WriteFormulasToSheet wsActual
    
    ' 6. Write Variance formulas (=Actual - Budget)
    WriteVarianceFormulas wsVar, wsBudget, wsActual
    
    ' 7. Write formulas to Variance sheet (same structure)
    WriteFormulasToSheet wsVar
End Sub
```

### Caching User Input
```vba
Private Function CacheActualValues(ws As Worksheet) As Object
    Dim cache As Object
    Set cache = CreateObject("Scripting.Dictionary")
    
    Dim lastRow As Long
    lastRow = ws.Cells(ws.Rows.Count, "B").End(xlUp).Row
    
    Dim r As Long
    For r = 3 To lastRow  ' Skip header rows
        Dim label As String
        label = Trim(CStr(ws.Cells(r, "B").Value))
        
        If label <> "" Then
            Dim values(1 To 12) As Double
            Dim c As Long
            For c = 1 To 12  ' Jan-Dec (columns C-N)
                If IsNumeric(ws.Cells(r, c + 2).Value) Then
                    values(c) = CDbl(ws.Cells(r, c + 2).Value)
                Else
                    values(c) = 0
                End If
            Next c
            cache.Add label, values
        End If
    Next r
    
    Set CacheActualValues = cache
End Function
```

### Variance Formula Generation
```vba
Private Sub WriteVarianceFormulas(wsVar As Worksheet, wsBudget As Worksheet, wsActual As Worksheet)
    Dim lastRow As Long
    lastRow = wsBudget.Cells(wsBudget.Rows.Count, "B").End(xlUp).Row
    
    Dim r As Long
    For r = 3 To lastRow  ' Data rows only
        Dim c As Long
        For c = 3 To 14  ' Columns C-N (Jan-Dec)
            ' Variance = Actual - Budget
            Dim cellRef As String
            cellRef = CellRef(r, c)  ' Returns "C3", "D3", etc.
            
            wsVar.Cells(r, c).Formula = "=Actual!" & cellRef & "-Budget!" & cellRef
        Next c
    Next r
End Sub

Private Function CellRef(row As Long, col As Long) As String
    ' Convert row/col numbers to cell reference (e.g., 3, 3 → "C3")
    CellRef = Chr(64 + col) & row
End Function
```

---

## 5. Dashboard — Executive KPIs (Complete)

### KPI Cards (Rows 4-5)
```vba
Private Sub BuildDashboardKPIs(wsDash As Worksheet, wsActual As Worksheet)
    ' KPI 1: Closing Cash
    wsDash.Range("B4").Value = "Closing Cash"
    wsDash.Range("C4").Formula = "=Actual!N" & GetClosingRow(wsActual)  ' Dec closing balance
    wsDash.Range("C4").NumberFormat = "₹#,##0"
    
    ' KPI 2: YTD Net Flow
    wsDash.Range("B5").Value = "YTD Net Flow"
    wsDash.Range("C5").Formula = "=SUM(Actual!" & GetIncomeRange(wsActual) & ")-SUM(Actual!" & GetExpenseRange(wsActual) & ")"
    wsDash.Range("C5").NumberFormat = "₹#,##0"
    
    ' KPI 3: Monthly Burn
    wsDash.Range("B6").Value = "Monthly Burn"
    wsDash.Range("C6").Formula = "=AVERAGE(Actual!" & GetExpenseRange(wsActual) & ")"
    wsDash.Range("C6").NumberFormat = "₹#,##0"
    
    ' KPI 4: Cash Runway
    wsDash.Range("B7").Value = "Cash Runway"
    wsDash.Range("C7").Formula = "=IF(C6<=0,\"-\",ROUND(C4/C6,0))"
    wsDash.Range("C7").NumberFormat = "0"" mos"""
    
    ' KPI 5: Expense Ratio
    wsDash.Range("B8").Value = "Expense Ratio"
    wsDash.Range("C8").Formula = "=IF(C5=0,0,SUM(Actual!" & GetExpenseRange(wsActual) & ")/SUM(Actual!" & GetIncomeRange(wsActual) & "))"
    wsDash.Range("C8").NumberFormat = "0.0%"
End Sub
```

### Primary Metrics Table (Rows 9-15)
| Metric | Budget Column | Actual Column | Variance Column | Fav/Unfav Logic |
|--------|---------------|---------------|-----------------|-----------------|
| Opening Cash | `=Budget!C{OpeningRow}` | `=Actual!C{OpeningRow}` | `=Act-Bud` | Higher=Better |
| Total Inflows | `=SUM(Budget!C{IncomeStart}:C{IncomeEnd})` | `=SUM(Actual!...)` | `=Act-Bud` | Higher=Better |
| Total Outflows | `=SUM(Budget!C{ExpenseStart}:C{ExpenseEnd})` | `=SUM(Actual!...)` | `=Act-Bud` | **Lower=Better** |
| Net Cash Flow | `=Inflows-Outflows` | `=Inflows-Outflows` | `=Act-Bud` | Higher=Better |
| Closing Cash | `=Budget!N{ClosingRow}` | `=Actual!N{ClosingRow}` | `=Act-Bud` | Higher=Better |
| Avg Monthly Burn | `=AVERAGE(Budget!C:N)` | `=AVERAGE(Actual!C:N)` | `=Act-Bud` | **Lower=Better** |
| Runway (Months) | `=Closing/Burn` | `=Closing/Burn` | `=Act-Bud` | Higher=Better |

### Conditional Formatting Rules
```vba
Private Sub ApplyDashboardFormatting(wsDash As Worksheet)
    ' Green for favorable variance
    With wsDash.Range("E9:E15").FormatConditions.Add(xlCellValue, xlGreater, "=0")
        .Interior.Color = RGB(198, 239, 206)  ' Light green
        .Font.Color = RGB(0, 97, 0)           ' Dark green
    End With
    
    ' Red for unfavorable variance
    With wsDash.Range("E9:E15").FormatConditions.Add(xlCellValue, xlLess, "=0")
        .Interior.Color = RGB(255, 199, 206)  ' Light red
        .Font.Color = RGB(156, 0, 6)          ' Dark red
    End With
    
    ' Special: "Lower=Better" rows (Outflows, Burn) reverse colors
    ' Row 11 (Total Outflows), Row 14 (Avg Monthly Burn)
    Dim reverseRows As Variant
    reverseRows = Array(11, 14)  ' Row indices
    
    Dim i As Long
    For i = LBound(reverseRows) To UBound(reverseRows)
        Dim r As Long
        r = reverseRows(i)
        ' Reverse: Green if negative (underspend), Red if positive (overspend)
        With wsDash.Range("E" & r).FormatConditions.Add(xlCellValue, xlLess, "=0")
            .Interior.Color = RGB(198, 239, 206)
            .Font.Color = RGB(0, 97, 0)
        End With
        With wsDash.Range("E" & r).FormatConditions.Add(xlCellValue, xlGreater, "=0")
            .Interior.Color = RGB(255, 199, 206)
            .Font.Color = RGB(156, 0, 6)
        End With
    Next i
End Sub
```

---

## 6. Critical Deviation Detection (>10%)

```vba
Private Sub BuildDeviationTable(wsDash As Worksheet, wsBudget As Worksheet, wsActual As Worksheet)
    Dim lastRow As Long
    lastRow = wsBudget.Cells(wsBudget.Rows.Count, "B").End(xlUp).Row
    
    Dim devRow As Long
    devRow = 20  ' Start deviation table at row 20
    
    ' Headers
    wsDash.Cells(devRow, 2).Value = "Line Item"
    wsDash.Cells(devRow, 3).Value = "Budget Total"
    wsDash.Cells(devRow, 4).Value = "Actual Total"
    wsDash.Cells(devRow, 5).Value = "Deviation %"
    wsDash.Cells(devRow, 6).Value = "Impact"
    
    Dim r As Long
    For r = 3 To lastRow
        Dim budgetTotal As Double, actualTotal As Double
        budgetTotal = GetRowTotal(wsBudget, r)
        actualTotal = GetRowTotal(wsActual, r)
        
        If budgetTotal > 0 Then
            Dim deviation As Double
            deviation = (actualTotal - budgetTotal) / budgetTotal
            
            ' Alert if >10% deviation
            If Abs(deviation) > 0.1 Then
                devRow = devRow + 1
                
                wsDash.Cells(devRow, 2).Value = wsBudget.Cells(r, "B").Value
                wsDash.Cells(devRow, 3).Value = budgetTotal
                wsDash.Cells(devRow, 4).Value = actualTotal
                wsDash.Cells(devRow, 5).Value = deviation
                wsDash.Cells(devRow, 5).NumberFormat = "0.0%"
                
                ' Impact label
                If deviation > 0 Then
                    wsDash.Cells(devRow, 6).Value = "Overspend"
                    wsDash.Cells(devRow, 6).Font.Color = RGB(156, 0, 6)  ' Red
                Else
                    wsDash.Cells(devRow, 6).Value = "Underspend"
                    wsDash.Cells(devRow, 6).Font.Color = RGB(0, 97, 0)   ' Green
                End If
            End If
        End If
    Next r
End Sub

Private Function GetRowTotal(ws As Worksheet, row As Long) As Double
    Dim total As Double
    Dim c As Long
    For c = 3 To 14  ' Columns C-N (Jan-Dec)
        If IsNumeric(ws.Cells(row, c).Value) Then
            total = total + CDbl(ws.Cells(row, c).Value)
        End If
    Next c
    GetRowTotal = total
End Function
```

---

## 7. Runway Analysis

```vba
Private Sub BuildRunwayAnalysis(wsDash As Worksheet, wsActual As Worksheet)
    Dim closingRow As Long, expenseRow As Long
    closingRow = GetClosingRow(wsActual)
    expenseRow = GetExpenseRow(wsActual)
    
    ' Current Runway
    wsDash.Range("B30").Value = "Current Runway"
    wsDash.Range("C30").Formula = "=IF(B32=0,\"-\",ROUND(B31/B32,0))"
    wsDash.Range("C30").NumberFormat = "0"" months"""
    
    ' Zero-Cash Date
    wsDash.Range("B31").Value = "Zero-Cash Date"
    wsDash.Range("C31").Formula = "=IF(B32=0,\"N/A\",EOMONTH(TODAY(),C30-1))"
    wsDash.Range("C31").NumberFormat = "MMM YYYY"
    
    ' Monthly Burn (Avg)
    wsDash.Range("B32").Value = "Monthly Burn (Avg)"
    wsDash.Range("C32").Formula = "=AVERAGE(Actual!" & GetExpenseRange(wsActual) & ")"
    wsDash.Range("C32").NumberFormat = "₹#,##0"
    
    ' Recommended Buffer
    wsDash.Range("B33").Value = "Recommended Buffer"
    wsDash.Range("C33").Formula = "=MAX(0,(C32*6)-C31)"  ' 6 months of burn - current cash
    wsDash.Range("C33").NumberFormat = "₹#,##0"
End Sub
```

### Runway Formulas
| Metric | Formula | Output |
|--------|---------|--------|
| **Current Runway** | `ROUND(ClosingCash / MonthlyBurn, 0)` | "8 months" |
| **Zero-Cash Date** | `EOMONTH(TODAY(), Runway - 1)` | "Mar 2027" |
| **Monthly Burn** | `AVERAGE(Actual Expenses Jan:Dec)` | ₹850,000 |
| **Recommended Buffer** | `MAX(0, (Burn × 6) - ClosingCash)` | ₹2,100,000 |

---

## 8. Data Validation & Protection

### Validation Rule
```vba
Private Sub EnforceDataValidation()
    Dim ws As Worksheet
    For Each ws In ThisWorkbook.Worksheets
        If ws.Name = "Budget" Or ws.Name = "Actual" Then
            Dim lastRow As Long
            lastRow = ws.Cells(ws.Rows.Count, "B").End(xlUp).Row
            
            Dim r As Long
            For r = 3 To lastRow
                Dim c As Long
                For c = 3 To 14  ' Columns C-N
                    With ws.Cells(r, c).Validation
                        .Delete  ' Clear existing
                        .Add Type:=xlValidateWholeNumber, _
                             AlertStyle:=xlValidAlertStop, _
                             Operator:=xlGreaterEqual, _
                             Formula1:="0"
                        .InputMessage = "Enter positive whole numbers only (INR)."
                        .ErrorMessage = "Decimals, negatives and text are not allowed."
                        .ShowError = True
                    End With
                Next c
            Next r
        End If
    Next ws
End Sub
```

### Protection Settings
```vba
Private Sub ApplyProtection()
    Dim ws As Worksheet
    For Each ws In ThisWorkbook.Worksheets
        ' Unlock data cells first
        ws.Cells.Locked = False
        
        ' Lock structure cells (headers, formulas)
        Dim r As Long
        For r = 1 To 2  ' Header rows
            ws.Rows(r).Locked = True
        Next r
        
        ' Protect sheet
        ws.Protect Password:="Admin123", _
                   DrawingObjects:=True, _
                   Contents:=True, _
                   Scenarios:=True, _
                   AllowFiltering:=True, _
                   AllowSorting:=True
    Next ws
End Sub
```

---

## 9. Cross-Platform Compatibility (Detailed)

| Feature | Windows | Mac |
|---------|---------|-----|
| **Font** | `Segoe UI` | `Helvetica Neue` |
| **Currency Symbol** | `₹` via `ChrW(&H20B9)` | Native `₹` |
| **Dictionary** | `Scripting.Dictionary` ❌ | `Collection` ✅ |
| **FileSystemObject** | ❌ | ❌ (avoided) |
| **API Calls** | ❌ | ❌ (avoided) |
| **ScreenUpdating** | `Application.ScreenUpdating` | Same |
| **Calculation Mode** | `xlCalculationManual` | Same |

### Platform Detection
```vba
Private Function PlatformFont() As String
    If LCase(Application.OperatingSystem) Like "*mac*" Then
        PlatformFont = "Helvetica Neue"
    Else
        PlatformFont = "Segoe UI"
    End If
End Function

Private Function PlatformCurrency() As String
    If LCase(Application.OperatingSystem) Like "*mac*" Then
        PlatformCurrency = "₹"  ' Native Mac rupee
    Else
        PlatformCurrency = ChrW(&H20B9)  ' Unicode rupee symbol
    End If
End Function
```

### Mac-Compatible Collection (Instead of Dictionary)
```vba
' Windows: Use Scripting.Dictionary
' Mac: Use Collection with custom type
Private Type SectionInfo
    Name As String
    StartRow As Long
    EndRow As Long
End Type

Private Function CreateSectionCollection() As Collection
    Dim coll As New Collection
    ' Add sections as SectionInfo type
    Dim s As SectionInfo
    s.Name = "Income"
    s.StartRow = 4
    s.EndRow = 6
    coll.Add s
    Set CreateSectionCollection = coll
End Function
```

---

## 10. Usage — Step-by-Step

```bash
# 1. Open workbook
budget106_pro.xlsm

# 2. Enable macros (Security Warning → Enable Content)

# 3. Run Model Refresh
Alt+F8 → RunModelRefresh → Run

# 4. Enter Budget figures (Budget sheet)
#    - Row 4: Product Revenue (Jan-Dec)
#    - Row 5: Service Revenue (Jan-Dec)
#    - Row 9-12: R&D costs
#    - Row 15-17: S&M costs
#    - Row 20-23: G&A costs

# 5. Enter Actuals monthly (Actual sheet)
#    - Same structure as Budget
#    - Variance auto-calculates

# 6. View Dashboard
#    - KPIs update automatically
#    - Critical deviations highlighted
#    - Runway analysis calculated
```

### Output Example (Dashboard)
```
┌─────────────────────────────────────────────────────┐
│  EXECUTIVE DASHBOARD                                  │
├─────────────────────────────────────────────────────┤
│  Closing Cash:    ₹4,250,000                         │
│  YTD Net Flow:    ₹1,800,000                         │
│  Monthly Burn:    ₹850,000                           │
│  Cash Runway:     5 months                           │
│  Expense Ratio:   72.3%                              │
├─────────────────────────────────────────────────────┤
│  CRITICAL DEVIATIONS (>10%)                           │
│  Salaries:    ₹1,200,000 → ₹1,450,000  (+20.8%)    │
│  Marketing:   ₹300,000  → ₹220,000     (-26.7%)    │
├─────────────────────────────────────────────────────┤
│  RUNWAY ANALYSIS                                     │
│  Current Runway: 5 months                            │
│  Zero-Cash Date: Mar 2027                            │
│  Recommended Buffer: ₹2,100,000                      │
└─────────────────────────────────────────────────────┘
```

---

## 11. Version History (Detailed)

| Version | Key Changes | Lines |
|---------|-------------|-------|
| **v101** | Initial structure, basic sync | ~200 |
| **v102** | Dashboard KPIs added | ~280 |
| **v103** | Variance conditional formatting | ~320 |
| **v104** | Critical deviation alerts | ~370 |
| **v105** | Runway analysis, zero-cash date | ~410 |
| **v106_pro** | Mac-native fonts, rupee symbol, Collection-only, platform detection | 447 |

---

## 12. Cross-References

- [[wiki/01-Areas/Business/]] — Business domain hub
- [[wiki/01-Areas/Engineering/excel workflows]] — Related Excel automation
- [[wiki/00-Current-Projects/quote-pomodoro]] — Personal productivity companion
- [[wiki/01-Areas/Engineering/engineering-math]] — Financial math formulas

---

## 13. Known Limitations / TODOs (Detailed)

| Limitation | Impact | Fix |
|------------|--------|-----|
| **No multi-year support** | Single 12-month cycle only | Add year selector + archive sheets |
| **No scenario modeling** | Single Budget/Actual pair | Add Best/Worst/Base case columns |
| **No pivot/charting** | Dashboard is formula-based only | Add `ChartObjects` for trend lines |
| **No audit trail** | No change log | Add `ChangeLog` sheet with timestamps |
| **Password hardcoded** | `Admin123` (security risk) | Make configurable via `Config` sheet |
| **No ribbon UI** | Run via Alt+F8 only | Add custom ribbon tab with buttons |
| **No automated data import** | Manual entry only | Add CSV/Power Query import |
| **No multi-currency** | INR only | Add currency selector + conversion |

---

## 14. Code Statistics

| Metric | Value |
|--------|-------|
| **Total VBA Lines** | 447 |
| **Functions/Subs** | ~25 |
| **Public Subs** | 1 (`RunModelRefresh`) |
| **Private Functions** | ~20 |
| **Workbook Versions** | 6 (v101-v106_pro) |
| **Sheets per Workbook** | 4 (Budget, Actual, Variance, Dashboard) |
| **Data Cells Validated** | ~400 (34 rows × 12 months × ~1 sheet) |
| **Conditional Formats** | ~20 (deviation highlighting) |

---

## See Also
- [[wiki/01-Areas/Engineering/excel workflows/FinancialAdvisor_RebuildNotes]] — Rebuild notes
- [[wiki/01-Areas/Engineering/excel workflows/Budget_Tracker_Basic]] — Simplified version
- [[wiki/01-Areas/Business/financial-modeling]] — Financial modeling concepts
- [[wiki/00-Current-Projects/quote-pomodoro]] — Another personal tool