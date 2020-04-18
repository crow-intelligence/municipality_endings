import icu

with open("data/raw/telepulesek.txt", "r") as infile:
    everything = infile.read().split("\n")

everything = set([e for e in everything if e.islower() and len(e) > 1])
collator = icu.Collator.createInstance(icu.Locale("hu_HU.UTF-8"))
everything = sorted(everything, key=collator.getSortKey)

with open("data/processed/endings.txt", "w") as outfile:
    for e in everything:
        if len(e) > 1:
            outfile.write(e + "\n")
