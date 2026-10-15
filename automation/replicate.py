import os

def allocate_safe_run_directory(base_path, config_id):
    """
    Dynamically searches the file system to assign an auto-incrementing 
    replicate suffix, resolving the directory overwrite blockages noted on page 15.
    """
    # Define the initial run target directory
    target_dir = os.path.join(base_path, f"run_{config_id}")
    
    # If the folder path doesn't exist yet, it's completely safe to use as-is
    if not os.path.exists(target_dir):
        return target_dir, 0

    # If it does exist, loop until we find a free auto-incremented suffix path
    replicate_index = 1
    while True:
        suffix_dir = os.path.join(base_path, f"run_{config_id}_rep{replicate_index}")
        if not os.path.exists(suffix_dir):
            return suffix_dir, replicate_index
        replicate_index += 1

def simulate_replicate_allocator():
    print("Initializing Multi-Trial Replicate Path Engine...")
    
    # Simulated run space directory inside your workspace folder
    test_base_path = "tests"
    os.makedirs(test_base_path, exist_ok=True)
    
    # We will simulate allocating the same exact configuration 3 times sequentially
    simulated_config = "hpcg_144x2_p6q24"
    
    for trial in range(3):
        allocated_path, rep_id = allocate_safe_run_directory(test_base_path, simulated_config)
        
        # Simulate creating the run directory folder
        os.makedirs(allocated_path, exist_ok=True)
        print(f"Trial {trial + 1} -> Successfully allocated separate path: {allocated_path} (Replicate ID: {rep_id})")

if __name__ == "__main__":
    simulate_replicate_allocator()
