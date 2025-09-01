# EPSS-Score-Extractor
A series of scripts to download all EPSS historical data, and extract all EPSS scores for a given CVE or a set of CVEs

The script downloader.py downloads all historical EPSS data, from a hardcoded date until today. The hardcoded date in the file (as it is) is the earliest for which historical EPSS data is available (2021, 4, 14) but you can change it if you want later data only. The data is saved in a subfolder called  epss_data.

The script unzipper.py unzips every file in the folder epss_data and saves the resulting cvs files in a new folder called epss_unzipped.

The script singleCVEExtractor.py takes as input a single CVE number (hardcoded in the script, change it to any CVE numbr you want) and produces a text file with every EPSS score for that CVE, one per line, along with the date where that CVE had that score. Sample output:

2021-06-11, 0.0023

2021-06-12, 0.0024

2021-06-13, 0.0025

The script multiCVEExtractor.py does the same thing, but taakes as input multiple CVE numbers  (again, hardcoded in the script so you have to change it). Sample output:

CVE-2021-34527

2021-06-11, 0.0023


2021-06-12, 0.0024


CVE-2021-44228

2021-12-10, 0.9456

2021-12-11, 0.9567
