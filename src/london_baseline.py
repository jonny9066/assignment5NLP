# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

from tqdm import tqdm

city_names = [line.split('\t')[1][:-1] for line in tqdm(open("birth_dev.tsv", encoding='utf-8'))] # cut last char = \n

london_times = sum([1 for x in city_names if x == "London"])

percent_baseline = london_times/len(city_names)

print(london_times, "out of ", len(city_names),":",percent_baseline*100, "%")