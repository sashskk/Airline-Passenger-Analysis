import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from preprocessing import (shares_by_satis, share_loys_vs_dis,
                           df_mean_scores, class_service_means,
                           man_vs_women_pct, loyalty_satisfaction_pct,
                           loyalty_services, age_allocation_pct,
                           age_satisfaction
                           )

sns.set_theme(style='whitegrid', palette='magma')
# 1 Barplot: Shares of satisfied and dissatisfied passengers
# ax = sns.barplot(data=shares_by_satis, x='Satisfaction', y='Percentage', palette='magma')
# for container in ax.containers:
#     ax.bar_label(container)
# plt.xlabel('Satisfaction')
# plt.ylabel('Percentage')
# plt.title('Shares of satisfied and dissatisfied passengers')
# plt.show()

# 2 Heatmap: Average ratings depended on class
# ax1 = sns.heatmap(data=df_mean_scores,
#                   annot=True,
#                   cbar=False,
#                   linewidths=0.5
#                   )
# plt.title('Average ratings depended on class (Business, Eco, Eco Plus)')
# plt.xlabel('Class')
# plt.ylabel('Services')
# plt.show()

# 3 Correlation between services rate and satisfaction
# ax2 = sns.heatmap(
#     data=df_mean_scores,
#     annot=True,
#     square=True,
#     cbar=False,
#     linewidths=0.5
# )
# plt.title('Correlation between services rate and satisfaction')
# plt.xlabel('Ratings')
# plt.ylabel('Services')
# plt.show()

# 4 Average service ratings by customer type

# ax3 = loyalty_services.T.plot(kind='bar', figsize=(12, 6))
# plt.title('Average service ratings by customer type')
# plt.xlabel('Service')
# plt.ylabel('Average rating')
# plt.xticks(rotation=45, ha='right')
# plt.legend(title='Customer Type')
# plt.show()

# 5 Satisfaction Distribution by Gender
#
# ax4 = man_vs_women_pct.pivot(index='satisfaction', columns='Gender', values='percentage').plot(
#     kind='bar',
#     stacked=True,
#     figsize=(10, 6),
#     color=['#fa0f61', '#0fb0fa']
# )
# plt.title('Satisfaction Distribution by Gender', fontsize=16, fontweight='bold')
# plt.xlabel('Percentage (%)')
# plt.ylabel('Satisfaction Level')
# plt.legend(title='Gender', loc='upper right')
# plt.xticks(rotation=45)
# plt.tight_layout()
#
# for container in ax4.containers:
#     ax4.bar_label(container, fmt='%.1f%%', label_type='center', fontweight='bold')
#
# plt.show()


