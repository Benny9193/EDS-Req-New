# Workflow: Budget & Approval

[Home](../../index.md) > [Business](../index.md) > [Workflows](index.md) > Budget & Approval

---

## Overview

The budget and approval workflow ensures that all purchases are properly funded and authorized. This workflow runs in parallel with requisition processing to validate financial controls.

---

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       BUDGET & APPROVAL WORKFLOW                            │
│                                                                             │
│    ┌──────────────────────────────────────────────────────────────────┐    │
│    │                    BUDGET VALIDATION                             │    │
│    │                                                                  │    │
│    │   ┌──────────┐    ┌──────────┐    ┌──────────┐                  │    │
│    │   │  Select  │───▶│ Validate │───▶│ Available│                  │    │
│    │   │ Account  │    │  Code    │    │ Balance? │                  │    │
│    │   └──────────┘    └──────────┘    └────┬─────┘                  │    │
│    │                                        │                        │    │
│    │                    ┌───────────────────┼───────────────────┐    │    │
│    │                    │                   │                   │    │    │
│    │                    ▼                   ▼                   ▼    │    │
│    │              ┌──────────┐        ┌──────────┐        ┌────────┐│    │
│    │              │ Continue │        │  Warning │        │ Blocked││    │
│    │              │          │        │ Proceed? │        │        ││    │
│    │              └──────────┘        └──────────┘        └────────┘│    │
│    └────────────────────┬─────────────────────────────────────┬─────┘    │
│                         │                                     │          │
│    ┌────────────────────▼─────────────────────────────────────▼─────┐    │
│    │                    APPROVAL ROUTING                            │    │
│    │                                                                │    │
│    │   ┌──────────┐    ┌──────────┐    ┌──────────┐                │    │
│    │   │Determine │───▶│  Route   │───▶│  Multi-  │                │    │
│    │   │  Level   │    │ Approver │    │  Level?  │                │    │
│    │   └──────────┘    └──────────┘    └────┬─────┘                │    │
│    │                                        │                       │    │
│    │                              ┌─────────┴─────────┐             │    │
│    │                              ▼                   ▼             │    │
│    │                        ┌──────────┐        ┌──────────┐       │    │
│    │                        │  Single  │        │ Parallel │       │    │
│    │                        │ Sequence │        │  or Seq  │       │    │
│    │                        └──────────┘        └──────────┘       │    │
│    └────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│    ┌────────────────────────────────────────────────────────────────┐    │
│    │                    APPROVAL DECISION                           │    │
│    │                                                                │    │
│    │   ┌──────────┐    ┌──────────┐    ┌──────────┐                │    │
│    │   │  Review  │───▶│ Decision │───▶│ Document │                │    │
│    │   │ Request  │    │          │    │  Action  │                │    │
│    │   └──────────┘    └────┬─────┘    └──────────┘                │    │
│    │                        │                                       │    │
│    │              ┌─────────┼─────────┬─────────────┐               │    │
│    │              ▼         ▼         ▼             ▼               │    │
│    │         ┌────────┐┌────────┐┌────────┐   ┌──────────┐         │    │
│    │         │Approve ││ Reject ││ Return │   │ Escalate │         │    │
│    │         └────────┘└────────┘└────────┘   └──────────┘         │    │
│    └────────────────────────────────────────────────────────────────┘    │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Budget Validation

### Account Code Structure
Typical school district account code:

```
FFF-SSSS-PPP-OOOO-FFFFF-XXXX

FFF    = Fund (100 = General, 200 = Special Revenue)
SSSS   = School/Location
PPP    = Program (Instruction, Admin, etc.)
OOOO   = Object (Supplies, Services, etc.)
FFFFF  = Function
XXXX   = Project/Grant
```

### Validation Steps

1. **Code Exists** - Is this a valid account code?
2. **Code Active** - Is account accepting charges?
3. **Fiscal Year** - Is it current fiscal year?
4. **Available Balance** - Are funds available?

### Balance Check
```sql
SELECT b.AccountCode,
       b.OriginalBudget,
       b.Adjustments,
       b.OriginalBudget + b.Adjustments as RevisedBudget,
       b.Encumbered,
       b.Expended,
       (b.OriginalBudget + b.Adjustments - b.Encumbered - b.Expended)
           as AvailableBalance
FROM Budgets b
WHERE b.AccountCode = @AccountCode
  AND b.FiscalYear = @FiscalYear
```

### Validation Results

| Result | Action |
|--------|--------|
| **Sufficient Funds** | Continue normally |
| **Warning (< 20%)** | Alert user, allow proceed |
| **Insufficient** | Block or require override |
| **Invalid Code** | Reject, require correction |

---

## Budget States

```
Original Budget: $10,000
       │
       ├── Adjustment: +$2,000
       │
       ▼
Revised Budget: $12,000
       │
       ├── Encumbered (POs): $3,500
       │
       ├── Expended (Paid): $6,000
       │
       ▼
Available: $2,500
```

### State Definitions

| State | Description |
|-------|-------------|
| **Original** | Initial allocation |
| **Adjusted** | After transfers/amendments |
| **Encumbered** | Reserved for approved POs |
| **Expended** | Actually spent (invoiced) |
| **Available** | Can be spent |

---

## Approval Routing

### Routing Factors

The system determines approvers based on:

| Factor | Examples |
|--------|----------|
| Dollar Amount | $0-500, $501-2500, $2501+ |
| School | Elementary, Middle, High |
| Department | Curriculum, Athletics, Admin |
| Account Type | Operating, Capital, Grant |
| Item Category | Technology, Furniture, Services |

### Approval Thresholds

| Level | Title | Threshold | Approval Rights |
|-------|-------|-----------|-----------------|
| 1 | Department Head | Any | Up to $500 |
| 2 | Principal | > $500 | Up to $2,500 |
| 3 | Purchasing | > $2,500 | Up to $10,000 |
| 4 | Finance Director | > $10,000 | Up to $50,000 |
| 5 | Superintendent | > $50,000 | Up to $100,000 |
| 6 | Board | > $100,000 | Unlimited |

### Routing Logic
```sql
-- Determine approval level
SELECT ar.ApproverUserId, ar.ApprovalLevel,
       r.RoleName, u.Email
FROM ApprovalRules ar
JOIN Roles r ON ar.RoleId = r.RoleId
JOIN Users u ON ar.ApproverUserId = u.UserId
WHERE ar.SchoolId IN (@SchoolId, NULL)  -- Specific or all schools
  AND ar.MinAmount <= @RequestAmount
  AND (ar.MaxAmount >= @RequestAmount OR ar.MaxAmount IS NULL)
ORDER BY ar.ApprovalLevel
```

---

## Multi-Level Approval

### Sequential Approval
Each level must approve before next:

```
Request $15,000
    │
    ▼
Level 1: Department Head ──► Approve ──┐
                                       │
Level 2: Principal ◄───────────────────┘
    │
    └──► Approve ──┐
                   │
Level 3: Purchasing ◄──────────────────┘
    │
    └──► Approve ──┐
                   │
Level 4: Finance Director ◄────────────┘
    │
    └──► Final Approval
```

### Parallel Approval
Multiple approvers at same level:

```
Request $5,000
    │
    ├──► Budget Approver ──► Approve ──┐
    │                                   │
    └──► Dept Approver ──► Approve ────┤
                                       │
                       All Approved ◄──┘
                            │
                            ▼
                    Continue to next level
```

---

## Approver Actions

### Approve
- Requisition advances to next level
- If final level, triggers PO generation
- Notification sent to requestor

### Reject
- Requisition marked as rejected
- Requires new submission if needed
- Notification with reason sent

### Return for Revision
- Sent back to requestor
- Specific changes requested
- Can be resubmitted

### Request Information
- Pauses workflow
- Request clarification
- Continues when provided

### Escalate
- Push to higher level
- Used for exceptions
- Documents reason

---

## Delegation

### Temporary Delegation
Approvers can delegate authority:

```sql
-- Check for delegation
SELECT d.DelegateUserId, d.StartDate, d.EndDate
FROM ApprovalDelegation d
WHERE d.ApproverUserId = @OriginalApprover
  AND d.StartDate <= GETDATE()
  AND d.EndDate >= GETDATE()
  AND d.Active = 1
```

### Auto-Escalation
If no action within time limit:

| Level | Escalate After |
|-------|----------------|
| 1-2 | 2 business days |
| 3-4 | 3 business days |
| 5+ | 5 business days |

---

## Budget Exceptions

### Over-Budget Handling

| Option | Description |
|--------|-------------|
| **Block** | Cannot proceed |
| **Warning** | Alert and continue |
| **Override** | Manager approval required |
| **Transfer** | Move funds from another account |

### Budget Transfer
```sql
-- Transfer funds between accounts
BEGIN TRANSACTION

UPDATE Budgets
SET Adjustments = Adjustments - @Amount
WHERE AccountCode = @SourceAccount

UPDATE Budgets
SET Adjustments = Adjustments + @Amount
WHERE AccountCode = @DestAccount

INSERT INTO BudgetTransfers (...)
VALUES (@SourceAccount, @DestAccount, @Amount, @Reason, ...)

COMMIT
```

---

## Audit Trail

### Logged Actions

| Action | Information Captured |
|--------|---------------------|
| Submission | Who, when, amount |
| Routing | Rules applied |
| Review | Approver, duration |
| Decision | Action, reason, timestamp |
| Override | Justification, authorizer |

### Approval History Query
```sql
SELECT ah.ActionDate, u.FirstName + ' ' + u.LastName as Approver,
       ah.Action, ah.Comments, ah.ApprovalLevel
FROM ApprovalHistory ah
JOIN Users u ON ah.UserId = u.UserId
WHERE ah.RequisitionId = @RequisitionId
ORDER BY ah.ActionDate
```

---

## Common Queries

### Pending My Approval
```sql
SELECT r.RequisitionNumber, r.TotalAmount,
       r.DateSubmitted, u.FirstName + ' ' + u.LastName as Requestor,
       s.SchoolName
FROM Requisitions r
JOIN Users u ON r.UserId = u.UserId
JOIN Schools s ON r.SchoolId = s.SchoolId
WHERE r.Status = 'Pending'
  AND r.CurrentApproverId = @MyUserId
ORDER BY r.DateSubmitted
```

### Budget Status by School
```sql
SELECT s.SchoolName,
       SUM(b.OriginalBudget + b.Adjustments) as TotalBudget,
       SUM(b.Encumbered) as Encumbered,
       SUM(b.Expended) as Spent,
       SUM(b.OriginalBudget + b.Adjustments - b.Encumbered - b.Expended)
           as Available
FROM Budgets b
JOIN Schools s ON b.SchoolId = s.SchoolId
WHERE b.FiscalYear = @FiscalYear
GROUP BY s.SchoolId, s.SchoolName
ORDER BY s.SchoolName
```

---

## Integration Points

| System | Integration |
|--------|-------------|
| Requisitions | Budget check at submission |
| PO Generation | Encumbrance creation |
| Receiving | Expenditure recording |
| Finance System | GL posting |
| Reporting | Budget vs actual |

---

## See Also

- [Requisition to PO](requisition-to-po.md) - Full procurement workflow
- [Requisitions](../entities/requisitions.md) - Request entity
- [Schema: Finance & Budgets](../../schema/by-domain/finance-budgets.md)

