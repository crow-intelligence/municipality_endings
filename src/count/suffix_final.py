import pandas as pd

with open("data/raw/telepules_nevek.txt", "r") as infile:
    municipalities = infile.read().split("\n")

with open("data/raw/endings_final.txt", "r") as infile:
    endings = infile.read().split("\n")


def suffix_counter(suffix):
    return len([e for e in municipalities if e.endswith(suffix)])


suffix_counts = {}
for suffix in endings:
    suffix_counts[suffix] = suffix_counter(suffix)

suffix_counts = {
    k: v
    for k, v in sorted(suffix_counts.items(), key=lambda item: item[1], reverse=True)
    if len(k) > 0
}

with open("data/processed/suffix_counts_final.tsv", "w") as outfile:
    h = "Ending\tCount\n"
    outfile.write(h)
    for k, v in suffix_counts.items():
        o = k + "\t" + str(v) + "\n"
        outfile.write(o)


def suffix_categorizer(m):
    for k in list(suffix_counts.keys()):
        if m.endswith(k):
            return k
    return "other"


df = pd.read_csv("data/raw/2018-1986.csv", encoding="utf-8", sep=",")
m_population = dict(zip(df["Település"], df["2018"]))
m_category = {}
with open("data/processed/municipality_endings_final.tsv", "w") as outfile:
    h = "NAME\tending\tpopulation\n"
    outfile.write(h)
    for m in municipalities:
        if len(m) > 0:
            o = m + "\t" + suffix_categorizer(m) + "\t" + str(m_population[m]) + "\n"
            outfile.write(o)
            m_category[m] = suffix_categorizer(m)

category_population = {}

for e in list(suffix_counts.keys()):
    ms = [m for m in municipalities if m.endswith(e)]
    population = sum([m_population[m] for m in ms])
    category_population[e] = population

with open("data/processed/catgegory_count_population_final.tsv", "w") as outfile:
    h = "Ending\tCount\tPopulation\n"
    outfile.write(h)
    for k, v in category_population.items():
        o = k + "\t" + str(suffix_counts[k]) + "\t" + str(v) + "\n"
        outfile.write(o)
