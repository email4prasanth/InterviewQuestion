import requests
import logging
from datetime import time

def check_system_health():
    # example
    latency_ms = 450 #threshol 200ms
    error_rate = 0.12 #threshold is 5%
    if latency_ms > 200 or error_rate <0.05:
        return {
            "status": "issue",
            
        }
def raise_ticket():

def main():
    health =  check_system_health()
    if health["status"] == "issue":
        logging.warning("Prodution issue detected")
        raise_ticket()
    else:
        logging.info("system healthy")
if __name__ == "__main__":
    main()
