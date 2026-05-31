import pandas as pd

# Step 1: Simulating Lami's High-Volume Internal Transaction Records
lami_ledger_data = {
    'Policy_ID': ['POL-9901', 'POL-9902', 'POL-9903', 'POL-9904', 'POL-9905'],
    'Customer_Name': ['John Omwamba', 'Aminah Kabura', 'David Kiprono', 'Mary Atieno', 'Ezra Mwangi'],
    'Internal_Amount_KES': [4500, 1200, 3500, 8500, 2200]
}
df_lami = pd.DataFrame(lami_ledger_data)

# Step 2: Simulating the Underwriting Insurance Company's Received Statement
underwriter_statement_data = {
    'Policy_ID': ['POL-9901', 'POL-9902', 'POL-9903', 'POL-9905'],
    'Underwriter_Amount_KES': [4500, 1200, 3100, 2200]
}
df_underwriter = pd.DataFrame(underwriter_statement_data)

# Step 3: Executing a structural Data Merge (Reconciliation Match)
reconciliation_sheet = pd.merge(df_lami, df_underwriter, on='Policy_ID', how='left')

# Step 4: Isolate Missing Transactions (Where Underwriter Amount is NaN)
missing_policies = reconciliation_sheet[reconciliation_sheet['Underwriter_Amount_KES'].isna()]

# Step 5: Isolate Amount Variances (Where amounts exist but do not match)
amount_mismatches = reconciliation_sheet[
    (reconciliation_sheet['Underwriter_Amount_KES'].notna()) & 
    (reconciliation_sheet['Internal_Amount_KES'] != reconciliation_sheet['Underwriter_Amount_KES'])
].copy()

# Calculate the exact variance amount for the mismatches
amount_mismatches['Variance_KES'] = amount_mismatches['Internal_Amount_KES'] - amount_mismatches['Underwriter_Amount_KES']

# Step 6: Print the Final Audit Reports to Console
print("⚠️ EXCEPTION REPORT 1: MISSING FROM UNDERWRITER")
print(missing_policies[['Policy_ID', 'Customer_Name', 'Internal_Amount_KES']])
print("\n🔍 EXCEPTION REPORT 2: PREMIUM AMOUNT MISMATCHES")
print(amount_mismatches[['Policy_ID', 'Customer_Name', 'Internal_Amount_KES', 'Underwriter_Amount_KES', 'Variance_KES']])
