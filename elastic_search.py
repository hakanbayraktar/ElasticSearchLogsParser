from elasticsearch import Elasticsearch

host = input("Enter the URL address or press enter for localhost\n>\t")
port = input("Enter Port Number or press enter for default port 9200 for Elasticsearch\n>\t")
if host == '':
	host = 'localhost'
if port == '':
	port = 9200

es = Elasticsearch([{'host': host, 'port': port}])

filename = input("Enter filename along with full path\n>\t")
#filename = '/home/ebryx/Downloads/sample-syslog.txt' #str(input("Enter filename and extension with full path"))

#file = open(filename, 'r')
file = set(line.strip() for line in open(filename))

cols = input("Enter column names separated by space\n>\t")
cols = [str(cols).strip(' ')]
#cols = ['month', 'day', 'time', 'host', 'protocol']
index1 = input("Enter name for new index\n>\t")
doc_type1 = input("Enter type of document\n>\t")

no_cols = len(cols)
if no_cols == 0:
	exit(1)

for i in file:
	fields = str(file).strip(' ')

	content = '{"'
	for j in range(no_cols):
		content += cols[j] + '":"' + fields[j]
		if j < no_cols - 1:
			content += '","'
	content += '"}'
	
	es.index(index=index1, doc_type=doc_type1, id=i, body=content)

	print("Logs indexed.\n")