
import dns.resolver
import time

domain = input("Enter domain name: ")

record_types = ["A", "AAAA", "MX", "NS", "CNAME"]

for record_type in record_types:

    print("\n==============================")
    print(record_type, "RECORD")
    print("==============================")

    try:
        start_time = time.time()

        # use a small lifetime to avoid hanging too long
        answers = dns.resolver.resolve(domain, record_type, lifetime=5.0)

        end_time = time.time()

        for answer in answers:
            # MX answers have preference and exchange; print raw answer for simplicity
            print(answer)

        response_time = (end_time - start_time) * 1000

        print(f"Response Time: {response_time:.2f} ms")

    except dns.resolver.NoAnswer:
        print("No record found: NoAnswer (server returned no answer)")
        
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist (NXDOMAIN)")
    except dns.resolver.Timeout:
        print("Query timed out")
    except dns.resolver.NoNameservers as e:
        print("No nameservers responded:", e)
    except Exception as e:
        print("Error while querying:", e)