import subprocess
import hashlib
import os
import json

def get_git_commit():
    """Extracts the active Git commit hash of the current repository state."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"], 
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception:
        return "no_git_repo_detected"

def get_loaded_compiler():
    """Scrapes the active compiler module details from the environment."""
    # Look through common environment variables populated by module load
    for env_var in ['LOADEDMODULES', 'PRGENV']:
        if env_var in os.environ:
            return os.environ[env_var]
            
    # Fallback system check via loaded environment configurations
    try:
        result = subprocess.run(["cc", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.split('\n')[0].strip()
    except Exception:
        pass
    return "default_cirrus_toolchain"

def generate_build_metadata(binary_path=None):
    """
    Generates a secure, verifiable build signature combining git context,
    compiler states, and binary hashes to solve the provenance problem.
    """
    metadata = {
        "git_commit": get_git_commit(),
        "compiler_variant": get_loaded_compiler(),
        "binary_hash": "no_binary_provided"
    }

    # If an actual benchmark binary is target-scanned, compute its unique hash
    if binary_path and os.path.exists(binary_path):
        sha256_hash = hashlib.sha256()
        with open(binary_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        metadata["binary_hash"] = sha256_hash.hexdigest()

    # Generate a unique build ID string from combined variables
    unique_string = f"{metadata['git_commit']}_{metadata['compiler_variant']}_{metadata['binary_hash']}"
    metadata["build_id"] = hashlib.md5(unique_string.encode()).hexdigest()[:8]
    
    return metadata

if __name__ == "__main__":
    print("Initializing Automated Provenance Scraper System...")
    meta = generate_build_metadata()
    print("\n--- Verifiable System Environment Metadata ---")
    print(json.dumps(meta, indent=4))
