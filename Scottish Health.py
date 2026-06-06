import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



#Load the dataset
data = pd.read_csv('Scottish Health 1000(Sheet1).csv')




#Group by age and smoking status
age_groupby = data.groupby(['age', 'smoke'])


#Count smoking status by age
smoke_by_age = age_groupby['smoke'].count()


count_smoke = data['smoke'].value_counts()


#Create lists for bar chart
groups = ['Group 1, 18-32', 'Group 2, 33-46', 'Group 3, 47-60', 'Group 4, 61+']
never = []
lite = []
moderate = []
heavy = []
ex = []





#Group into age ranges and smoking status

#Group 1
age_group1 = data[data['age'] < 33] #262
group1_smokestatus = age_group1['smoke'].value_counts() #ex, hvy, mod, lite, nevr



#Group 1 data for each smoking status

#Count and append ex smokers to list for group 1
group1_ex = age_group1[age_group1['smoke'] == 'ex']
group1_ex_count = group1_ex['smoke'].count()
ex.append(group1_ex_count)

#Count and append heavy smokers to list for group 1
group1_hvy = age_group1[age_group1['smoke'] == 'hvy']
group1_hvy_count = group1_hvy['smoke'].count()
heavy.append(group1_hvy_count)

#Count and append moderate smokers to list for group 1
group1_mod = age_group1[age_group1['smoke'] == 'mod']
group1_mod_count = group1_mod['smoke'].count()
moderate.append(group1_mod_count)

#Count and append lite smokers to list for group 1
group1_lite = age_group1[age_group1['smoke'] == 'lite']
group1_lite_count = group1_lite['smoke'].count()
lite.append(group1_lite_count)

#Count and append never smokers to list for group 1
group1_nevr = age_group1[age_group1['smoke'] == 'nevr']
group1_nevr_count = group1_nevr['smoke'].count()
never.append(group1_nevr_count)


#Group 2
age_group2 = data[(data['age'] >= 33) & (data['age'] < 47)] #271
group2_smokestatus = age_group2['smoke'].value_counts()



#Group 2 data for each smoking status

#Count and append ex smokers to list for group 2
group2_ex = age_group2[age_group2['smoke'] == 'ex']
group2_ex_count = group2_ex['smoke'].count()
ex.append(group2_ex_count)

#Count and append heavy smokers to list for group 2
group2_hvy = age_group2[age_group2['smoke'] == 'hvy']
group2_hvy_count = group2_hvy['smoke'].count()
heavy.append(group2_hvy_count)

#Count and append moderate smokers to list for group 2
group2_mod = age_group2[age_group2['smoke'] == 'mod']
group2_mod_count = group2_mod['smoke'].count()
moderate.append(group2_mod_count)

#Count and append lite smokers to list for group 2
group2_lite = age_group2[age_group2['smoke'] == 'lite']
group2_lite_count = group2_lite['smoke'].count()
lite.append(group2_lite_count)

#Count and append never smokers to list for group 2
group2_nevr = age_group2[age_group2['smoke'] == 'nevr']
group2_nevr_count = group2_nevr['smoke'].count()
never.append(group2_nevr_count)

#Group 3
age_group3 = data[(data['age'] >= 47) & (data['age'] < 61)] #250
group3_smokestatus = age_group3['smoke'].value_counts()


#Group 3 data for each smoking status

#Count and append ex smokers to list for group 3
group3_ex = age_group3[age_group3['smoke'] == 'ex']
group3_ex_count = group3_ex['smoke'].count()
ex.append(group3_ex_count)

#Count and append heavy smokers to list for group 3
group3_hvy = age_group3[age_group3['smoke'] == 'hvy']
group3_hvy_count = group3_hvy['smoke'].count()
heavy.append(group3_hvy_count)

#Count and append moderate smokers to list for group 3
group3_mod = age_group3[age_group3['smoke'] == 'mod']
group3_mod_count = group3_mod['smoke'].count()
moderate.append(group3_mod_count)

#Count and append lite smokers to list for group 3
group3_lite = age_group3[age_group3['smoke'] == 'lite']
group3_lite_count = group3_lite['smoke'].count()
lite.append(group3_lite_count)

#Count and append never smokers to list for group 3
group3_nevr = age_group3[age_group3['smoke'] == 'nevr']
group3_nevr_count = group3_nevr['smoke'].count()
never.append(group3_nevr_count)

#Group 4
age_group4 = data[data['age'] >= 61] #217
group4_smokestatus = age_group4['smoke'].value_counts()


#Group 4 data for each smoking status

#Count and append ex smokers to list for group 4
group4_ex = age_group4[age_group4['smoke'] == 'ex']
group4_ex__count = group4_ex['smoke'].count()
ex.append(group4_ex__count)

#Count and append heavy smokers to list for group 4
group4_hvy = age_group4[age_group4['smoke'] == 'hvy']
group4_hvy_count = group4_hvy['smoke'].count()
heavy.append(group4_hvy_count)

#Count and append moderate smokers to list for group 4
group4_mod = age_group4[age_group4['smoke'] == 'mod']
group4_mod_count = group4_mod['smoke'].count()
moderate.append(group4_mod_count)

#Count and append lite smokers to list for group 4
group4_lite = age_group4[age_group4['smoke'] == 'lite']
group4_lite_count = group4_lite['smoke'].count()
lite.append(group4_lite_count)

#Count and append never smokers to list for group 4
group4_nevr = age_group4[age_group4['smoke'] == 'nevr']
group4_nevr_count = group4_nevr['smoke'].count()
never.append(group4_nevr_count)


#Change data type from np.int64 to int for each list
never = [i.item() for i in never]
lite = [i.item() for i in lite]
moderate = [i.item() for i in moderate]
heavy = [i.item() for i in heavy]
ex = [i.item() for i in ex]


#Create Bar Chart


#Set width for bars in bar chart
w = 0.12

#Create x value for each smoking status
never_x = np.arange(len(groups))
lite_x = [x + w for x in never_x]
moderate_x = [x + w for x in lite_x]
heavy_x = [x + w for x in moderate_x]
ex_x = [x + w for x in heavy_x]


#Change plot size
plt.figure(figsize=(10, 8), facecolor='gainsboro')


#Plot bars for each smoking status with appropriate x values and labels
plt.bar(never_x, never, width=w, label='Never', color='goldenrod')
plt.bar(lite_x, lite, width=w, label='Lite', color='salmon')
plt.bar(moderate_x, moderate, width=w, label='Moderate', color='wheat')
plt.bar(heavy_x, heavy, width=w, label='Heavy', color='firebrick')
plt.bar(ex_x, ex, width=w, label='Ex', color='violet')

#Set x and y labels
plt.xlabel('Age Groups', fontweight='bold', fontsize=12, labelpad=20)
plt.ylabel('Count of Smoking Status', fontweight='bold', fontsize=12, labelpad=35)


#Create title
plt.title('Smoking Status by Age Groups', fontweight='bold', fontsize=20, pad=20)


#Add legend to plot
plt.legend()



#Set x ticks and center them for each group
plt.xticks(never_x + 0.24, groups, fontweight='bold')


#Save image of graph
plt.savefig('Smoking Status by Age Group.png', dpi=300)


#Show plot
plt.show()