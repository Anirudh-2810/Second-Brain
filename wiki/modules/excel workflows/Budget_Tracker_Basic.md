Option Exclusive
'==================================================================================
' BUDGET TRACKER BASIC - MAC NATIVE
' Standalone budget tracking workbook (simplified from Financial Advisor model)
' No ActiveX, no Scripting.Dictionary, runtime OS detection
'==================================================================================

Option Explicit

'=== CONSTANTS ===
Private Const SHEET_PASSWORD As String = "Budget2026"
Private Const CURRENCY_SYMBOL As String = "₹" ' U+20B9 Indian Rupee

'=== WORKSHEET NAMES ===
Private const WS_BUDGET As String = "Budget"
Private const WS_ACTUAL As String = "Actual"
Private const WS_SUMMARY As String = "Summary"

'=== TRACER CELL FOR DEBUG ===
'Writes execution step to Dashboard!G4 (for troubleshooting)

'=== PUBLIC API ===
Public Sub RunBudgetTracker()
    On Error GoTo ErrorHandler
    ToggleOptimization True
    
    If Not BudgetWorkbookExists Then
        MsgBox "Budget workbook structure incomplete.", vbExclamation
        GoTo CleanExit
    End If
    
    BuildBudgetStructure
    SyncActualToBudget
    ApplyDataValidation
    BuildSummarySheet
    ApplyProtection
    
CleanExit:
    ToggleOptimization False
    Exit Sub
    
ErrorHandler:
    ToggleOptimization False
    MsgBox "Budget Tracker Error: " & Err.Number & " - " & Err.Description, vbCritical
    Resume CleanExit
End Sub

'=== WORKBOOK EXISTENCE CHECK ===
Private Function BudgetWorkbookExists() As Boolean
    On Error Resume Next
    BudgetWorkbookExists = (ThisWorkbook.Name = "BudgetTracker.xlsm")
    On Error GoTo 0
End Function

'=== BUDGET STRUCTURE BUILDING ===
Private Sub BuildBudgetStructure()
    Dim ws As Worksheet
    Set ws = GetSheet(WS_BUDGET)
    If ws Is Nothing Then Exit Sub
    
    UnprotectSheet ws
    ws.Cells.Clear
    
    ' Header row
    ws.Range("A1:G1").Value = Array("Month", "Income", "R&D", "S&M", "G&A", "Total Expenses", "Net Cash")
    
    ' Set up 12 months
    ws.Range("A2:A13").Value = Application.Transpose(Array("Jan", "Feb", "Mar", "Apr", "May", "Jun", _
                                                              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
    ws.Range("B2:F13").Formula = "0"
    
    ws.Range("A1:G1").Interior.Color = RGB(15, 23, 42)
    ws.Range("A1:G1").Font.Color = RGB(255, 255, 255)
    ws.Range("A1:G1").Font.Bold = True
    
    ProtectSheet ws
End Sub

'=== SYNCHRONIZATION ===
Private Sub SyncActualToBudget()
    Dim wsBudget As Worksheet, wsActual As Worksheet
    Set wsBudget = GetSheet(WS_BUDGET)
    Set wsActual = GetSheet(WS_ACTUAL)
    
    If wsBudget Is Nothing Or wsActual Is Nothing Then Exit Sub
    
    UnprotectSheet wsBudget
    UnprotectSheet wsActual
    
    ' Copy Actual data rows to Budget (months 2-12, columns B-G)
    wsBudget.Range("B2:G13").Value = wsActual.Range("B2:G13").Value
    
    ' Copy Net Cash (column G) formula: Income - Expenses
    wsBudget.Range("G2:G13").Formula = "=B2-F2" ' Simplified: Income - Total Expenses
    
    ProtectSheet wsBudget
    ProtectSheet wsActual
End Sub

'=== DATA VALIDATION ===
Private Sub ApplyDataValidation()
    Dim ws As Worksheet
    For Each ws In Array(WS_BUDGET, WS_ACTUAL)
        Set ws = GetSheet(ws)
        If Not ws Is Nothing Then
            UnprotectSheet ws
            ws.Range("B2:G13").Validation.Type = xlValidateWholeNumber
            ws.Range("B2:G13").Validation.Formula1 = "0"
            ws.Range("B2:G13").Validation.IgnoreBlank = True
            ProtectSheet ws
        End If
    Next ws
End Sub

'=== SUMMARY SHEET ===
Private Sub BuildSummarySheet()
    Dim ws As Worksheet
    Set ws = GetSheet(WS_SUMMARY)
    If ws Is Nothing Then Exit Sub
    
    UnprotectSheet ws
    ws.Cells.Clear
    ws.Range("A1:D1").Value = Array("METRIC", "VALUE", "PRIOR", "STATUS")
    ws.Range("A1:D1").Font.Bold = True
    ws.Range("A1:D1").Interior.Color = RGB(15, 23, 42)
    ws.Range("A1:D1").Font.Color = RGB(255, 255, 255)
    
    ' Basic metrics
    ws.Range("A2").Value = "Total Income"
    ws.Range("B2").Formula = "=SUM(Budget!B2:B13)"
    ws.Range("C2").Value = "Prior Year"
    ws.Range("D2").Formula = 'Simple variance
    
    ws.Range("A3").Value = "Total Expenses"
    ws.Range("B3").Formula = "=SUM(Budget!F2:F13)"
    
    ws.Range("A4").Value = "Net Cash Flow"
    ws.Range("B4").Formula = "=B2-B3"
    
    ws.Range("A5").Value = "Average Monthly Income"
    ws.Range("B5").Formula = "=AVERAGE(Budget!B2:B13)"
    
    ws.Range("A6").Value = "Average Monthly Expenses"
    ws.Range("B6").Formula = "=AVERAGE(Budget!F2:F13)"
    
    ws.Range("A7").Value = "Cash Flow Status"
    ws.Range("B7").Formula = 'Simple status
    
    ws.Range("A1:D7").Interior.Color = RGB(241, 245, 249)
    ws.Range("A1:D7").BorderAround LineStyle:xlContinuous, Weight:xlThin
    
    ProtectSheet ws
End Sub

'=== PROTECTION ===
Private Sub ApplyProtection()
    Dim wsName As Variant
    For Each wsName In Array(WS_BUDGET, WS_ACTUAL, WS_SUMMARY)
        ProtectSheet GetSheet(wsName)
    Next wsName
End Sub

'=== HELPER FUNCTIONS ===
Private Function GetSheet(ByVal name As String) As Worksheet
    On Error Resume Next
    Set GetSheet = ThisWorkbook.Worksheets(name)
    On Error GoTo 0
End Function

Private Sub ToggleOptimization(ByVal enable As Boolean)
    Application.ScreenUpdating = Not enable
    Application.EnableEvents = Not enable
    Application.Calculation = IIf(enable, xlCalculationManual, xlCalculationAutomatic)
    Application.StatusBar = IIf(enable, "Processing budget data...", False)
End Sub

Private Sub UnprotectSheet(ByRef ws As Worksheet)
    If ws Is Nothing Then Exit Sub
    On Error Resume Next
    ws.Unprotect Password:=SHEET_PASSWORD
    On Error GoTo 0
End Sub

Private Sub ProtectSheet(ByRef ws As Worksheet)
    If ws Is Nothing Then Exit Sub
    On Error Resume Next
    ws.Protect Password:=SHEET_PASSWORD, DrawingObjects:=True, Contents:=True, Scenarios:=True
    On Error GoTo 0
End Sub

Private Function IsNumericSafe(ByVal val As Variant) As Boolean
    IsNumericSafe = IsNumeric(val) And Not IsEmpty(val)
End Function