def process_transactions(transactions):
    approved = []
    rejected = []
    audit = []

    print(f"Processing Batch of {len(transactions)} Transactions ")

    for amount in transactions:
        if amount < 0:
            print(f"ERROR Invalid Transaction Detected: {amount}")
            rejected.append(amount)
        elif amount > 10000:
            print(f"ALERT: Large Transaction Flagged: {amount}")
            audit.append(amount)
        else:
            print(f"Transaction approved for {amount}")
            approved.append(amount)

    print("\n Batch Summary")
    print(f"Approved: {approved}")
    print(f"Rejected: {rejected}")
    print(f"Audit: {audit}")

incoming_batch = [500, 20, -50, 1000, 50000, -5, 200, 15000, 10]

process_transactions(incoming_batch)        
