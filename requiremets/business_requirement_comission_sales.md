# **Business Requirements**

### Commission Structure

* **20% commission** on the first order.
* **10% residual commission** on all lifetime repeat orders.
* **Biweekly payouts** once customer invoices are paid.

---

# **Software Requirement Specification (SRS)**

## **Feature 1: Commission Plan**

### Functionalities

1. **Admin can create Commission Plans** with following fields:

   * **Target Period** → Date Range
   * **Sales Person** → Multi-selection (Many2many field)
   * **Disbursement Frequency** → Selection field \[Biweekly / Monthly / Weekly]
   * **First Order Commission** → Numeric input
   * **Residual Commission** → Numeric input

### Business Rules

1. Only **Admin** can create a commission plan.
2. Each plan follows an **Approval Workflow** → `Draft → Approved/Cancelled`.
3. Salesperson can **only view** their assigned commission plan.

---

## **Feature 2: Commission Tracking**

### Functionalities

1. **Real-time Commission View** based on active commission plans (Raw Query)
2. Menus:

   * **My Commission**

     * Salesperson (logged-in user) can view only their commissions.
   * **Commission**

     * Admin can view all commissions.
     * Salesperson has **no access** to this page.
3. **Commision List View** should support:

   * Group by **Salesperson**
   * Group by **Disbursement Frequency**

---

## **Feature 3: Vendor Bill Generation**

### Functionalities

1. System automatically generates **Vendor Bills** for commissions.
2. Bill creation is triggered based on **Disbursement Frequency**.
3. Bills are linked to commission records.

