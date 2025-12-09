def analyze_logs(status_codes):
    counts = {}

    print(f"Analyzing {len(status_codes)} Server Requests")

    for code in status_codes:
        if code in counts:
            counts[code] += 1
        else:
            counts[code] = 1
    print("\nStatus Report:")

    for code, frequency in counts.items():
        print(f"Code {code}: {frequency} times")

    total_requests = len(status_codes)

    success_count = counts.get(200,0)

    error_rate = (total_requests-success_count) / total_requests * 100

    print(f"\nError Rate: {error_rate: .2f}%")

    if error_rate > 10:
        print("ALERT: High Error Rate Detected! Paging SRE Team ...")
    else:
        print("System Normal")


raw_log_data = [
        200, 200, 200, 404, 200, 500, 200, 200, 
        404, 404, 200, 503, 200, 200, 500
 ]

analyze_logs(raw_log_data)
        
    
