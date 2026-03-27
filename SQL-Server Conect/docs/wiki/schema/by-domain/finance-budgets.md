# Schema: Finance & Budgets Domain

[Home](../../index.md) > [Schema](../index.md) > [By Domain](index.md) > Finance & Budgets

---

## Overview

The finance domain contains 18 tables managing budget allocations, encumbrances, expenditures, and financial reporting.

---

## Table Count: 18

### Core Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| Budgets | Budget allocations | BudgetId, AccountCode, FiscalYear, Amount |
| AccountCodes | GL account definitions | AccountCodeId, Code, Description, Type |
| FiscalYears | Year definitions | FiscalYearId, StartDate, EndDate, IsCurrent |
| Encumbrances | Committed funds (POs) | EncumbranceId, POId, AccountCode, Amount |
| Expenditures | Actual spending | ExpenditureId, InvoiceId, AccountCode, Amount |

### Transfer Tables

| Table | Purpose |
|-------|---------|
| BudgetTransfers | Movement between accounts |
| BudgetAdjustments | Non-transfer changes |
| TransferApprovals | Transfer workflow |

### Reporting Tables

| Table | Purpose |
|-------|---------|
| BudgetSnapshots | Point-in-time balances |
| MonthlyTotals | Monthly aggregates |
| YearEndBalances | Rollover tracking |

---

## Key Relationships

```
AccountCodes (1) ──────► (N) Budgets ──────► (1) FiscalYears
                              │
                              ├──► (N) Encumbrances ──► PurchaseOrders
                              │
                              └──► (N) Expenditures ──► Invoices

BudgetTransfers ──────► (2) AccountCodes (Source, Dest)
```

---

## Account Code Structure

### Typical Format
```
FFF-SSSS-PPP-OOOO-FFFFF-XXXX

FFF    = Fund (100=General, 200=Special Revenue, etc.)
SSSS   = School/Location Code
PPP    = Program (Instruction, Administration, etc.)
OOOO   = Object (Supplies, Services, Equipment, etc.)
FFFFF  = Function
XXXX   = Project/Grant Code
```

### Fund Examples
| Code | Description |
|------|-------------|
| 100 | General Fund |
| 200 | Special Revenue |
| 300 | Capital Projects |
| 400 | Debt Service |
| 500 | Food Service |
| 600 | Internal Service |

### Object Examples
| Code | Description |
|------|-------------|
| 6100 | Salaries |
| 6200 | Benefits |
| 6300 | Purchased Services |
| 6400 | Supplies & Materials |
| 6500 | Capital Outlay |
| 6600 | Other Objects |

---

## Critical Table: Budgets

### Schema
| Column | Type | Description |
|--------|------|-------------|
| BudgetId | INT | Primary key |
| AccountCode | VARCHAR(50) | Full account code |
| FiscalYearId | INT | Fiscal year FK |
| SchoolId | INT | School FK (optional) |
| OriginalBudget | DECIMAL | Initial allocation |
| Adjustments | DECIMAL | Net adjustments |
| Encumbered | DECIMAL | Committed (POs) |
| Expended | DECIMAL | Actually spent |
| Created | DATETIME | Create date |
| Modified | DATETIME | Last modified |

### Calculated Fields
```sql
RevisedBudget = OriginalBudget + Adjustments
Available = RevisedBudget - Encumbered - Expended
PercentUsed = (Encumbered + Expended) / RevisedBudget * 100
```

---

## Budget Lifecycle

```
Budget Created (Original)
       │
       ├── Adjustment (+/-)
       │       │
       │       ▼
       │   Revised Budget
       │
       ├── PO Created ──► Encumbrance (+)
       │
       ├── Invoice Paid ──► Encumbrance (-) ──► Expenditure (+)
       │
       └── Year End ──► Rollover or Close
```

---

## Common Queries

### Budget Status by Account
```sql
SELECT b.AccountCode, ac.Description,
       b.OriginalBudget,
       b.Adjustments,
       b.OriginalBudget + b.Adjustments as RevisedBudget,
       b.Encumbered,
       b.Expended,
       (b.OriginalBudget + b.Adjustments - b.Encumbered - b.Expended) as Available
FROM Budgets b
JOIN AccountCodes ac ON b.AccountCode = ac.Code
JOIN FiscalYears fy ON b.FiscalYearId = fy.FiscalYearId
WHERE fy.IsCurrent = 1
  AND b.SchoolId = @SchoolId
ORDER BY b.AccountCode
```

### Budget Summary by School
```sql
SELECT s.SchoolName,
       SUM(b.OriginalBudget + b.Adjustments) as TotalBudget,
       SUM(b.Encumbered) as TotalEncumbered,
       SUM(b.Expended) as TotalExpended,
       SUM(b.OriginalBudget + b.Adjustments - b.Encumbered - b.Expended) as TotalAvailable,
       CAST(SUM(b.Encumbered + b.Expended) * 100.0 /
            NULLIF(SUM(b.OriginalBudget + b.Adjustments), 0) as DECIMAL(5,2)) as PercentUsed
FROM Budgets b
JOIN Schools s ON b.SchoolId = s.SchoolId
JOIN FiscalYears fy ON b.FiscalYearId = fy.FiscalYearId
WHERE fy.IsCurrent = 1
GROUP BY s.SchoolId, s.SchoolName
ORDER BY s.SchoolName
```

### Check Available Balance
```sql
SELECT b.AccountCode,
       (b.OriginalBudget + b.Adjustments - b.Encumbered - b.Expended) as Available,
       CASE
           WHEN (b.OriginalBudget + b.Adjustments - b.Encumbered - b.Expended) >= @RequestAmount
           THEN 'OK'
           WHEN (b.OriginalBudget + b.Adjustments - b.Encumbered - b.Expended) > 0
           THEN 'WARNING'
           ELSE 'INSUFFICIENT'
       END as FundStatus
FROM Budgets b
JOIN FiscalYears fy ON b.FiscalYearId = fy.FiscalYearId
WHERE b.AccountCode = @AccountCode
  AND fy.IsCurrent = 1
```

### Recent Transfers
```sql
SELECT bt.TransferDate, bt.Amount,
       bt.SourceAccountCode, bt.DestAccountCode,
       bt.Reason,
       u.FirstName + ' ' + u.LastName as RequestedBy
FROM BudgetTransfers bt
JOIN Users u ON bt.RequestedById = u.UserId
WHERE bt.Status = 'Approved'
  AND bt.TransferDate > DATEADD(month, -1, GETDATE())
ORDER BY bt.TransferDate DESC
```

---

## Encumbrance Processing

### When PO Created
```sql
-- Create encumbrance
INSERT INTO Encumbrances (POId, AccountCode, Amount, EncumbranceDate)
SELECT @POId, d.AccountCode, SUM(d.ExtendedPrice), GETDATE()
FROM Detail d
WHERE d.RequisitionId = @RequisitionId
GROUP BY d.AccountCode

-- Update budget
UPDATE Budgets
SET Encumbered = Encumbered + @Amount
WHERE AccountCode = @AccountCode
  AND FiscalYearId = @CurrentFiscalYear
```

### When Invoice Paid
```sql
-- Release encumbrance
UPDATE Encumbrances
SET ReleasedAmount = @PaidAmount,
    ReleaseDate = GETDATE()
WHERE POId = @POId
  AND AccountCode = @AccountCode

-- Create expenditure
INSERT INTO Expenditures (InvoiceId, AccountCode, Amount, ExpenditureDate)
VALUES (@InvoiceId, @AccountCode, @PaidAmount, GETDATE())

-- Update budget
UPDATE Budgets
SET Encumbered = Encumbered - @PaidAmount,
    Expended = Expended + @PaidAmount
WHERE AccountCode = @AccountCode
```

---

## Index Recommendations

### Budgets Table
```sql
-- For account lookups
CREATE UNIQUE INDEX IX_Budgets_AccountCode_FiscalYear
ON Budgets (AccountCode, FiscalYearId)
INCLUDE (OriginalBudget, Adjustments, Encumbered, Expended, SchoolId)

-- For school reports
CREATE INDEX IX_Budgets_SchoolId_FiscalYear
ON Budgets (SchoolId, FiscalYearId)
```

### AccountCodes Table
```sql
-- For code lookups
CREATE UNIQUE INDEX IX_AccountCodes_Code
ON AccountCodes (Code)
INCLUDE (Description, Type, Active)
```

---

## Year-End Processing

### Steps
1. Close purchase orders
2. Roll forward encumbrances (if policy allows)
3. Calculate carryover
4. Create new fiscal year budgets
5. Archive old year

### Rollover Types
| Type | Description |
|------|-------------|
| No Rollover | Budget expires |
| Encumbrance Only | Open POs carry forward |
| Full Rollover | Unused funds carry forward |
| Grant Rollover | Per grant terms |

---

## See Also

- [Business: Budget & Approval](../../business/workflows/budget-approval.md)
- [Orders & Purchasing](orders-purchasing.md) - PO/Encumbrance link

