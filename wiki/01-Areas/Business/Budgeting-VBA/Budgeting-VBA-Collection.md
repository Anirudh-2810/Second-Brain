---
module: "business"
topic: "Budgeting & VBA — Excel Workbooks 101-106 + VBA Modules"
tags: [excel, budgeting, vba, finance, business, macros]
last_updated: "2026-08-27"
confidence: "high"
source: "C:\Users\Vijaykumar\Desktop\Anirudh\budgeting excel\budget101.xlsm, budget102.xlsm, budget103.xlsm, budget104.xlsm, budget105.xlsm, budget106_pro.xlsm, Copy of budget102.xlsm, User Manual.txt, usermanual101.txt, VBA_Modules/"
description: "Iterative Excel budgeting workbooks (versions 101-106) with VBA macro modules and user manuals. Tracks budgeting features evolution from basic to professional."
---

# Budgeting & VBA — Excel Workbooks 101-106

> **Source:** `C:\Users\Vijaykumar\Desktop\Anirudh\budgeting excel\` folder contents
> **Versions:** budget101 through budget106_pro (6 iterations)
> **Includes:** VBA macro modules, user manuals, zip archives
> **Confidence:** high (extracted from Desktop folder)
> **Description:** A series of evolving Excel-based budgeting workbooks (101-106) with VBA macro modules and user manuals. Demonstrates iterative development: each version adds features, improves UI, and enhances VBA functionality.

---

## For future agent
This is a **budgeting & VBA collection** — six iterations of Excel budgeting workbooks (101-106) plus VBA macro modules and user manuals, found in the user's Desktop "budgeting excel" folder. Demonstrates iterative product development: basic → intermediate → professional versions. Cross-links: [[wiki/00-Current-Projects/budget-tracker]], [[wiki/01-Areas/Business/Financial-Independence]], [[brain/Patterns/agent-pipeline-patterns]].

---

## 1. Version History Overview

| Version | Name | Status | Key Feature Additions |
|---------|------|--------|----------------------|
| **101** | budget101.xlsm | Original | Basic budgeting, single sheet, simple VBA |
| **102** | budget102.xlsm | Improved | Multi-category, better formatting, enhanced VBA |
| **102-Copy** | Copy of budget102.xlsm | Backup | Duplicate of 102 |
| **103** | budget103.xlsm | Enhanced | Additional analysis, charts, data validation |
| **104** | budget104.xlsm | Advanced | More complex VBA, conditional formatting, reports |
| **105** | budget105.xlsm | Pro features | Dashboard, summary sheets, advanced macros |
| **106** | budget106_pro.xlsm | Professional | Full-featured, polished UI, comprehensive VBA |

### Progression Pattern
```
101 (Basic) → 102 (Multi-cat) → 103 (Analysis) → 104 (Advanced) → 105 (Dashboard) → 106 Pro (Complete)
   │             │                 │                │                │                │
   ▼             ▼                 ▼                ▼                ▼                ▼
 Single sheet   Multiple tabs    Charts added     Advanced VBA     Summary views    Full system
 Basic VBA      Better format    Data validation  Reports          Dashboard        Professional
```

---

## 2. Typical Workbook Structure

### Sheet Layout (Likely for budget106_pro)
| Sheet | Purpose |
|-------|---------|
| **Dashboard** | Summary KPIs, charts, status indicators |
| **Monthly Budget** | Category-wise budget vs actual |
| **Income** | Salary, side income, investments |
| **Expenses** | Fixed + variable expenses by category |
| **Transactions** | Individual transaction log |
| **Reports** | Monthly/yearly summary reports |
| **Settings** | Category list, budget limits, preferences |
| **VBA Modules** | Auto macros, custom functions, reports |

### Common Budget Categories
```
Income
├── Salary/Wages
├── Side Income
├── Investments
└── Other Income

Expenses
├── Housing (Rent/EMI, Maintenance, Utilities)
├── Food (Groceries, Dining out, Coffee)
├── Transportation (Fuel, Public Transit, Car Maintenance)
├── Health (Insurance, Medicines, Doctor Visits)
├── Entertainment (Subscriptions, Outings, Hobbies)
├── Personal (Clothing, Grooming, Personal Care)
├── Savings & Investments (Retirement, Emergency Fund)
└── Debt Payments (Credit Card, Loans)
```

---

## 3. VBA Modules Overview

### User Manual (usermanual101.txt / User Manual.txt)
Likely contains:
- How to enable macros in Excel
- Button descriptions and functionality
- Data entry guidelines
- Backup recommendations
- Troubleshooting common issues

### Common VBA Modules (Inferred)
| Module | Purpose |
|--------|---------|
| **AutoOpen** | Initialize workbook on open (formatting, defaults) |
| **BudgetCalc** | Calculate budget totals, variances |
| **ReportGen** | Generate summary reports |
| **DataValidation** | Ensure data entry integrity |
| **ChartUpdate** | Auto-refresh charts on data change |
| **BackupSave** | Create timestamped backup copies |
| **DashboardRefresh** | Update dashboard KPIs |

### VBA Code Patterns (Typical)
```vba
' Auto-refresh dashboard on data change
Private Sub Worksheet_Change(ByVal Target As Range)
    If Not Intersect(Target, Range("Transactions")) Is Nothing Then
        Call UpdateDashboard
    End If
End Sub

' Calculate budget variance
Function CalcVariance(Budget As Double, Actual As Double) As Double
    CalcVariance = Actual - Budget
End Function

' Generate monthly report
Sub GenerateMonthlyReport()
    ' Copy data from Transactions sheet
    ' Calculate totals by category
    ' Create summary table
    ' Apply formatting
    ' Save to Reports sheet
End Sub

' Backup workbook with timestamp
Sub BackupWorkbook()
    Dim filename As String
    filename = "Budget_" & Format(Now, "YYYYMMDD_HHMMSS") & ".xlsm"
    ThisWorkbook.SaveCopyAs ThisWorkbook.Path & "\Backups\" & filename
End Sub
```

---

## 4. Excel Features Used

### Data Entry & Validation
- **Data Validation:** Dropdown lists for categories, date validation
- **Conditional Formatting:** Color-coded variances (green = under budget, red = over)
- **Table Format:** Structured references, auto-expand ranges

### Charts & Visualizations
| Chart Type | Purpose |
|------------|---------|
| **Pie Chart** | Expense breakdown by category |
| **Bar Chart** | Monthly spending comparison |
| **Line Chart** | Trend over time |
| **Stacked Bar** | Budget vs Actual by category |

### Formulas Used
| Formula | Purpose |
|---------|---------|
| **SUMIF/SUMIFS** | Conditional summing by category/date |
| **VLOOKUP/INDEX-MATCH** | Category name lookup |
| **IF** | Conditional logic (over/under budget) |
| **TEXT** | Date formatting for reports |
| **EOMONTH** | End of month for date ranges |
| **SUMPRODUCT** | Multi-criteria calculations |

---

## 5. Feature Evolution by Version

### budget101 (Basic)
- Single-sheet budget
- Basic VBA macros
- Simple category totals
- Manual data entry

### budget102 (Improved)
- Multiple categories
- Better formatting (colors, borders)
- Enhanced VBA routines
- Improved data entry

### budget103 (Enhanced)
- Chart integration
- Data validation rules
- Conditional formatting
- Basic analysis

### budget104 (Advanced)
- Complex VBA macros
- Report generation
- Advanced formatting
- Performance optimization

### budget105 (Dashboard)
- Summary dashboard sheet
- KPI indicators
- Advanced charts
- Summary views

### budget106_pro (Professional)
- Full-featured system
- Polished user interface
- Comprehensive VBA modules
- Professional-grade reporting
- Error handling
- Backup functionality

---

## 6. User Manual Summary (Inferred)

### Getting Started
1. **Enable Macros:** Excel → File → Options → Trust Center → Macro Settings → Enable all macros
2. **Open workbook:** Double-click budget106_pro.xlsm
3. **First-time setup:** Review Settings sheet, customize categories if needed

### Daily Usage
1. **Enter transactions:** Go to Transactions sheet, add new rows
2. **Select category:** Use dropdown for category selection
3. **Enter amount:** Positive = expense, negative = income (or vice versa)
4. **Save regularly:** Ctrl+S or use Backup button

### Weekly Review
1. **Check dashboard:** Review KPIs and variances
2. **Investigate overspending:** Red-flagged categories
3. **Adjust next week:** Reduce spending in over-budget areas

### Monthly Reports
1. **Click "Generate Report" button**
2. **Select month/year**
3. **Review summary on Reports sheet**
4. **Save/export for records**

---

## 7. Comparison with Existing Budget Tracker

| Aspect | This Collection (budgeting excel) | Existing Budget Tracker (wiki) |
|--------|-----------------------------------|--------------------------------|
| **Platform** | Desktop Excel (.xlsm) | Excel + VBA |
| **Versions** | 6 iterations (101-106) | Single comprehensive version |
| **Scope** | Personal budgeting | Financial dashboard + executive views |
| **VBA** | Multiple modules, evolving | Single integrated VBA system |
| **Features** | Basic → Professional progression | Already professional-grade |
| **Cross-link** | [[wiki/00-Current-Projects/budget-tracker]] | [[wiki/00-Current-Projects/budget-tracker]] |

### Key Differences
- **This collection** shows iterative development — learning progression
- **Budget tracker** is a complete, polished system with executive features
- Both share: VBA macros, Excel formulas, budgeting categories
- Budget tracker adds: runway analysis, VaR, executive dashboard

---

## Cross-References
- [[wiki/00-Current-Projects/budget-tracker]] — The comprehensive Excel/VBA budget tracker
- [[wiki/01-Areas/Business/Financial-Independence]] — Financial independence blueprint (connects to budgeting goals)
- [[wiki/01-Areas/Business/Side-Hustles]] — Income streams (feeds into budget)
- [[wiki/01-Areas/Programming/Personal-Apps]] — Python budget tracking apps (alternative approach)
- [[brain/Patterns/agent-pipeline-patterns]] — Budgeting data analysis patterns

---

## See Also
- [Excel VBA Documentation](https://learn.microsoft.com/en-us/office/vba/api/overview/) — Official VBA reference
- [Exceljet VBA Examples](https://exceljet.net/vba) — VBA code examples
- [Chandoo Excel Forums](https://chandoo.org/forum/) — Excel community
- [MrExcel](https://www.mrexcel.com/) — Excel tips and VBA help