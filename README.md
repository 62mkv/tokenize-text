# Quick tokenizer for Wikisource texts

## tokenize.py
(conceived as a tool to extract tokens from Kalevipoeg: https://et.wikisource.org/wiki/Kalevipoeg)

Usage: 

```shell
tokenize.py kalevipoeg > tokenized
```

This will produce information akin to: 
```csv
kalevipoeg\Kalevipoeg_I.txt	0	22	0	0	Sõua	sõua
kalevipoeg\Kalevipoeg_I.txt	0	22	6	1	laulik	laulik
kalevipoeg\Kalevipoeg_I.txt	0	22	14	2	lausa	lausa
kalevipoeg\Kalevipoeg_I.txt	0	22	20	3	suuga	suuga
kalevipoeg\Kalevipoeg_I.txt	0	24	0	0	Sõua	sõua
kalevipoeg\Kalevipoeg_I.txt	0	24	5	1	laululaevakesta	laululaevakesta
kalevipoeg\Kalevipoeg_I.txt	0	26	0	0	Pajataja	pajataja
kalevipoeg\Kalevipoeg_I.txt	0	26	9	1	paadikesta	paadikesta
kalevipoeg\Kalevipoeg_I.txt	0	28	0	0	Sõua	sõua
kalevipoeg\Kalevipoeg_I.txt	0	28	5	1	neid	neid
kalevipoeg\Kalevipoeg_I.txt	0	28	10	2	senna	senna
kalevipoeg\Kalevipoeg_I.txt	0	28	16	3	kaldale	kaldale
```

where columns are: 
1. filename
1. Sentence number (globally) (for this to make sense, files need to be ordered alphabetically in the folder)
1. Line number (in file)
1. Token starting position in line
1. Token number in line
1. Token "as is"
1. Token in lower-case
