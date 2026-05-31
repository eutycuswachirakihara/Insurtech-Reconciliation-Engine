# Insurtech Ledger Automation & Multi-Tier Reconciliation Engine

## Project Overview
This project serves as an operational financial prototype modeled after venture-backed fintech/insurtech architectures. It is designed to bridge corporate double-entry accounting with high-velocity data programming to maintain ledger integrity, handle month-end closures, and automate localized statutory tax compliance.

## Core Architecture & Components

### 1. General Ledger & Accounts Payable (AP) Registry
* **Tooling:** Google Sheets / Advanced Spreadsheet Frameworks
* **Execution:** Designed a standardized **Chart of Accounts (CoA)** mapping core assets, liabilities, and revenue items specific to automated API platforms.
* **Internal Controls:** Developed an **AP Invoice Registry** running multi-tiered nested conditional logic arguments `=IF(H2<0, "Overpaid", IF(H2=0, "Fully Paid", ...))` to eliminate manual administrative status errors and dynamically track supplier credit exceptions.
* **Risk Management:** Engineered a live, automated **Creditor Ageing Dashboard** separating liabilities into operational tranches (0-30 days, 31-60 days, 61+ days) to manage rolling working capital requirements.

### 2. High-Volume Premium Reconciliation Engine
* **Tooling:** Python (Pandas) / Google Colab
* **Execution:** Developed a high-speed data-matching matrix simulating an outer merge join between internal transactional API database records and external institutional underwriter statement collections.
* **Exception Management:** Programmed algorithmic filters to instantly isolate premium amount variances and missing transaction rows, shifting data reconciliation processing times from hours to **under 3 seconds**.

### 3. Statutory Tax Compliance Matrix
* **Tooling:** Advanced Spreadsheet Formula Arrays
* **Execution:** Built a live compliance mapping engine automating calculations for Kenyan corporate financial obligations, ensuring perfect structural alignment for **VAT (16%)**, **Withholding Tax (5% on management fees)**, and progressive employment tier **PAYE** schedules for direct KRA iTax uploads.

---
*Developed by Eutycus Wachira Kihara.*
