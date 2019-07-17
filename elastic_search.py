from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

filename = '/home/ebryx/Downloads/sample-syslog.txt' #str(input("Enter filename and extension with full path"))

#file = open(filename, 'r')
file = set(line.strip() for line in open(filename))

cols = ['month', 'day', 'time', 'host', 'protocol']

no_cols = len(cols)
for i in file:
	fields = str(file).strip(' ')

	content = '{"'
	for j in range(no_cols):
		content += cols[j] + '":"' + fields[j]
		if j < no_cols - 1:
			content += '","'
	content += '"}'
	
	es.index(index='test', doc_type='log', id=i, body=content)