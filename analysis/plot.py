import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_plots():
    csv_file = "results.csv"
    
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found. Run the parser first.")
        return
        
    df = pd.read_csv(csv_file)
    
    # 1. Performance Scaling Plot (GFLOPS)
    plt.figure(figsize=(8, 5))
    plt.plot(df['Nodes'], df['GFLOPS'], marker='o', linewidth=2, color='blue', label='Measured Performance')
    plt.title('HPC Benchmark Scaling Analysis (1 to 4 Nodes)')
    plt.xlabel('Node Count')
    plt.ylabel('Performance (GFLOPS)')
    plt.xticks(df['Nodes'])
    plt.grid(True, linestyle='--')
    plt.legend()
    
    perf_plot = "analysis/performance_scaling.png"
    plt.savefig(perf_plot, bbox_inches='tight')
    plt.close()
    print(f"Generated scaling visualization: {perf_plot}")

    # 2. Energy Efficiency Plot (GFLOPS/W)
    plt.figure(figsize=(8, 5))
    plt.bar(df['Nodes'].astype(str), df['GFLOPS_Per_Watt'], color='green', alpha=0.7, width=0.4)
    plt.title('Energy Efficiency Evaluation')
    plt.xlabel('Node Count')
    plt.ylabel('Efficiency (GFLOPS/W)')
    plt.grid(axis='y', linestyle='--')
    
    energy_plot = "analysis/energy_efficiency.png"
    plt.savefig(energy_plot, bbox_inches='tight')
    plt.close()
    print(f"Generated energy efficiency visualization: {energy_plot}")

if __name__ == "__main__":
    generate_plots()
