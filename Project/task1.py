# ============================================================
# FRAUDULENT TRANSACTION DETECTION SYSTEM
# Python List, Tuple, Dictionary and String Operations
# ============================================================


# ------------------------------------------------------------
# 1. TUPLE
# Store fixed transaction types
# ------------------------------------------------------------

transaction_types = ("Online", "ATM", "POS", "UPI")

print("Available Transaction Types:")
print(transaction_types)
print()


# ------------------------------------------------------------
# 2. LIST
# Store multiple transaction records
# Each transaction is represented as a dictionary
# ------------------------------------------------------------

transactions = [

    {
        "transaction_id": "TXN1001",
        "customer_id": "CUST101",
        "amount": 2500,
        "type": "UPI",
        "location": "Kozhikode",
        "device": "Mobile",
        "status": "Legitimate"
    },

    {
        "transaction_id": "TXN1002",
        "customer_id": "CUST102",
        "amount": 85000,
        "type": "Online",
        "location": "Mumbai",
        "device": "Unknown",
        "status": "Fraud"
    },

    {
        "transaction_id": "TXN1003",
        "customer_id": "CUST103",
        "amount": 1200,
        "type": "POS",
        "location": "Kochi",
        "device": "POS-Machine",
        "status": "Legitimate"
    },

    {
        "transaction_id": "TXN1004",
        "customer_id": "CUST101",
        "amount": 95000,
        "type": "Online",
        "location": "Delhi",
        "device": "Unknown",
        "status": "Fraud"
    },

    {
        "transaction_id": "TXN1005",
        "customer_id": "CUST104",
        "amount": 4500,
        "type": "ATM",
        "location": "Kannur",
        "device": "ATM",
        "status": "Legitimate"
    },

    {
        "transaction_id": "TXN1006",
        "customer_id": "CUST105",
        "amount": 72000,
        "type": "Online",
        "location": "Bangalore",
        "device": "Unknown",
        "status": "Fraud"
    }
]


# ------------------------------------------------------------
# 3. DISPLAY ALL TRANSACTIONS
# Dictionary operations
# ------------------------------------------------------------

print("ALL TRANSACTIONS")
print("----------------")

for transaction in transactions:

    print("Transaction ID :", transaction["transaction_id"])
    print("Customer ID    :", transaction["customer_id"])
    print("Amount         :", transaction["amount"])
    print("Type           :", transaction["type"])
    print("Location       :", transaction["location"])
    print("Device         :", transaction["device"])
    print("Status         :", transaction["status"])
    print()


# ------------------------------------------------------------
# 4. LIST OPERATION
# Extract all transaction IDs
# ------------------------------------------------------------

transaction_ids = []

for transaction in transactions:
    transaction_ids.append(transaction["transaction_id"])

print("Transaction IDs:")
print(transaction_ids)
print()


# ------------------------------------------------------------
# 5. LIST OPERATION
# Extract all transaction amounts
# ------------------------------------------------------------

amounts = []

for transaction in transactions:
    amounts.append(transaction["amount"])

print("Transaction Amounts:")
print(amounts)
print()


# ------------------------------------------------------------
# 6. STRING OPERATIONS
# ------------------------------------------------------------

print("STRING OPERATIONS")
print("-----------------")

transaction_id = transactions[0]["transaction_id"]

print("Original ID :", transaction_id)
print("Upper Case   :", transaction_id.upper())
print("Lower Case   :", transaction_id.lower())
print("Length       :", len(transaction_id))
print("Starts with TXN :", transaction_id.startswith("TXN"))
print()


# ------------------------------------------------------------
# 7. FIND HIGH-VALUE TRANSACTIONS
# ------------------------------------------------------------

print("HIGH VALUE TRANSACTIONS")
print("-----------------------")

for transaction in transactions:

    if transaction["amount"] > 50000:

        print(
            transaction["transaction_id"],
            "Amount =",
            transaction["amount"]
        )

print()


# ------------------------------------------------------------
# 8. FIND FRAUD TRANSACTIONS
# ------------------------------------------------------------

print("FRAUD TRANSACTIONS")
print("------------------")

for transaction in transactions:

    if transaction["status"] == "Fraud":

        print(
            transaction["transaction_id"],
            "->",
            transaction["customer_id"],
            "->",
            transaction["amount"]
        )

print()


# ------------------------------------------------------------
# 9. FIND LEGITIMATE TRANSACTIONS
# ------------------------------------------------------------

print("LEGITIMATE TRANSACTIONS")
print("-----------------------")

for transaction in transactions:

    if transaction["status"] == "Legitimate":

        print(
            transaction["transaction_id"],
            "->",
            transaction["amount"]
        )

print()


# ------------------------------------------------------------
# 10. SIMPLE FRAUD DETECTION RULE
# ------------------------------------------------------------

print("FRAUD DETECTION")
print("---------------")

for transaction in transactions:

    if transaction["amount"] > 50000:

        print(
            transaction["transaction_id"],
            "-> POSSIBLE FRAUD"
        )

    elif transaction["device"] == "Unknown":

        print(
            transaction["transaction_id"],
            "-> SUSPICIOUS DEVICE"
        )

    else:

        print(
            transaction["transaction_id"],
            "-> NORMAL"
        )

print()


# ------------------------------------------------------------
# 11. COUNT FRAUD AND LEGITIMATE TRANSACTIONS
# ------------------------------------------------------------

fraud_count = 0
legitimate_count = 0

for transaction in transactions:

    if transaction["status"] == "Fraud":
        fraud_count += 1

    else:
        legitimate_count += 1


print("TRANSACTION SUMMARY")
print("-------------------")

print("Total Transactions :", len(transactions))
print("Fraud Transactions :", fraud_count)
print("Legitimate         :", legitimate_count)

print()


# ------------------------------------------------------------
# 12. CALCULATE TOTAL TRANSACTION AMOUNT
# ------------------------------------------------------------

total_amount = 0

for transaction in transactions:

    total_amount += transaction["amount"]

print("Total Transaction Amount :", total_amount)
print()


# ------------------------------------------------------------
# 13. FIND HIGHEST TRANSACTION
# ------------------------------------------------------------

highest_transaction = transactions[0]

for transaction in transactions:

    if transaction["amount"] > highest_transaction["amount"]:

        highest_transaction = transaction


print("HIGHEST TRANSACTION")
print("-------------------")

print("Transaction ID :", highest_transaction["transaction_id"])
print("Customer       :", highest_transaction["customer_id"])
print("Amount         :", highest_transaction["amount"])
print("Status         :", highest_transaction["status"])

print()


# ------------------------------------------------------------
# 14. SEARCH TRANSACTION USING STRING
# ------------------------------------------------------------

search_id = "TXN1004"

print("SEARCH TRANSACTION")
print("------------------")

for transaction in transactions:

    if transaction["transaction_id"].lower() == search_id.lower():

        print("Transaction Found!")
        print(transaction)

print()


# ------------------------------------------------------------
# 15. CHECK SUSPICIOUS TRANSACTIONS
# ------------------------------------------------------------

print("SUSPICIOUS TRANSACTIONS")
print("-----------------------")

for transaction in transactions:

    if (
        transaction["amount"] > 50000
        or transaction["device"].lower() == "unknown"
    ):

        print(
            transaction["transaction_id"],
            "is suspicious"
        )

print()


# ------------------------------------------------------------
# END OF PROGRAM
# ------------------------------------------------------------

print("Fraud Detection Program Completed.")
