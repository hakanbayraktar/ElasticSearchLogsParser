# ElasticSearchLogsParser
Python3 script to feed any logs from a file to elastic search.
## Details
To index logs from a log file to the elastic search, given the file, column names, filename, file path, index name for new entry, url address and the port at which elastic search is running. It then takes the file, breaks it down into lines and feed each log entity along with its column name as python dictionary to elastic search for indexing.
## Requirements
- ElasticSearch Python Library.
## To Run
Through command line, from the directory where .py extensions file is:
```
python3 elastic_search.py
```
## 
