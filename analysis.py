# analysis.py
# CAC Analysis - Quarterly 2024
# Generates a trend plot and benchmark comparison, and prints summary metrics.
import pandas as pd
import matplotlib.pyplot as plt
import os

data = {
    'quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'cac': [229.04, 225.25, 233.99, 233.39]
}

df = pd.DataFrame(data)
avg_cac = df['cac'].mean()
industry_target = 150.0

print(f"Quarterly CACs:\n{df.to_string(index=False)}\n")
print(f"Average CAC: {avg_cac:.5f} (rounded displayed as 230.42 in README)")
print(f"Industry target: {industry_target}")
diff = avg_cac - industry_target
print(f"Average CAC is {diff:.2f} above the industry target.")

# Create visualization
fig, ax = plt.subplots(figsize=(8,5))
ax.plot(df['quarter'], df['cac'], marker='o', linewidth=2, label='Company CAC')
ax.hlines(industry_target, xmin=0, xmax=3, linestyles='--', label='Industry Target (150)')
ax.set_title('Customer Acquisition Cost (CAC) - 2024 Quarterly Trend')
ax.set_xlabel('Quarter')
ax.set_ylabel('CAC ($)')
ax.set_ylim(min(df['cac'].min(), industry_target) - 20, max(df['cac'].max(), industry_target) + 20)
ax.grid(alpha=0.25)
ax.legend()

# Annotate quarters
for i, row in df.iterrows():
    ax.annotate(f"{row['cac']}", (i, row['cac']), textcoords='offset points', xytext=(0,8), ha='center')

out_dir = 'figures'
os.makedirs(out_dir, exist_ok=True)
fig_path = os.path.join(out_dir, 'cac_trend.png')
plt.tight_layout()
plt.savefig(fig_path, dpi=200)
print(f"Saved plot to {fig_path}")
