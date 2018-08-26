# Ontario Election Analysis 2018

These are the scripts and notebooks used in my analysis of the Ontario 2018
election. You can read the analysis at
[robbiemeyer.com](http://robbiemeyer.com/projects/ontario-election-analysis).

The data used in the analysis is not included in this repository. You can find
the Ontario Election results on the Elections Ontario website and the census
results on the Statistics Canada website. Links to the actual data sources used
can be found at the bottom of the
[analysis](http://robbiemeyer.com/projects/ontario-election-analysis).

## Files

The following files are in this repository:

- Census Results Cleanup.ipynb
  - A notebook used to cleanup the Canadian Census results for use in the
    analysis
- parse_results.py 
  - A script used to parse the Ontario Election results into a single csv
- ridingcensuslookup.csv
  - Contains both the census riding names and the corresponding election results
    riding names. Used to map the two similar, but sometimes slighly different,
    names.
- ElectionAnalysis.ipynb
  - The notebook in which the data was analyzed
