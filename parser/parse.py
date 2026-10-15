import re
import os
import csv
import subprocess

def parse_hpl_log(file_path):
    # Searches for performance data in HPL output logs
    gflops = None
    runtime = None
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            # Match the typical HPL summary table row structure
            # e.g., WR11C2R4 ... time ... GFLOPS
            match = re.search(r'WR\d+\w+\s+\d+\s+\d+\s+\d+\s+\d+\s+([\d\.]+)\s+([\d\.e\+]+)', content)
            if match:
                runtime = float(match.group(1))
                gflops = float(match.group(2))
    return runtime, gflops

def get_energy_consumed(job_id):
    # Connects to SLURM to grab actual Joules consumed
    try:
        result = subprocess.run(
            ["sacct", "-j", str(job_id), "--format=ConsumedEnergy", "-p", "-n"],
            capture_output=True, text=True, check=True
        )
        energy_str = result.stdout.strip().replace('M', '') # strip formatting
        if energy_str and energy_str != "None":
            return float(energy_str)
    except Exception:
        pass
    return 0.0

def main():
    print("Telemetry Extraction System Initialized.")
    # Example placeholder creating a base results spreadsheet
    headers = ["Job_ID", "Nodes", "Runtime_Sec", "GFLOPS", "Joules", "GFLOPS_Per_Watt"]
    
    with open("results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        # Template row showing how it accumulates data
        writer.writerow(["123456", 1, 60.5, 450.2, 30000, 450.2 / (30000/60.5)])
        
    print("Created data summary placeholder: results.csv")

if __name__ == "__main__":
    main()
