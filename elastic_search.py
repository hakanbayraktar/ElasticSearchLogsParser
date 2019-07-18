from elasticsearch import Elasticsearch

host = input("Enter the URL address or press enter for localhost\n>\t")
port = input("Enter Port Number or press enter for default port 9200 for Elasticsearch\n>\t")
if host == '':
	host = 'localhost'
if port == '':
	port = 9200

es = Elasticsearch([{'host': host, 'port': port}])

filename = input("Enter filename along with full path\n>\t")
if filename == '':
	filename = 'auth.log'

col_labels = input("Enter column names separated by space\n>\t")
if col_labels == '':
	col_labels = 'Month Day Time User Identifier Other Session_Info'
col_labels = str(col_labels).split(' ')

no_cols = len(col_labels)
print(no_cols)
if no_cols == 0:
	exit(1)

logs = [line.strip() for line in open(filename)]

#cols = ['month', 'day', 'time', 'host', 'protocol']
index1 = input("Enter name for new index\n>\t")
doc_type1 = input("Enter type of document\n>\t")

if index1 == '':
	index1 = 'test_index'

if doc_type1 == '':
	doc_type1 = 'test_doc'


j = 1
for i in logs:
	fields = str(i).split(' ')

	content = '{"'
	for j in range(len(fields)):
		#print(len(fields))
		if j < no_cols:
			content += col_labels[j] + '":"' + fields[j]
		else:
			content += 'col' + str(j) + '":"' + fields[j]
		if j < len(fields) - 1:
			content += '","'
	content += '"}'
	#print(content)
	es.index(index=index1, doc_type=doc_type1, id=j, body=content)
	j += 1
print("Logs indexed.\n")