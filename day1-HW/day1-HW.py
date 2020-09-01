#open file as read only
f = open('/Users/cmdb/data/results/SRR072893.sam', 'r')
l = f.readline()
print(l)

#Count number of alignments
f = open('/Users/cmdb/data/results/SRR072893.sam', 'r')
counter = 0
for l in f:
    counter+=1
print('Number of alignments ', counter)

#Count number of alignments that match perfectly using flag NM:i:0
f = open('/Users/cmdb/data/results/SRR072893.sam', 'r')
perfalign = 0
substring = 'NM:i:0'
for l in f:
    if substring in l:
        perfalign+=1
print('Number of perfect alignments ', perfalign)

#
#f = open('/Users/cmdb/data/results/SRR072893.sam', 'r')
f.seek(0)
#First 10 chr
print('First 10 alignments ')
for i in range(10):
    l= f.readline()
    read_list = l.split('\t')
    print(read_list[2])

f.seek(0)
total_mapq = 0
for line in f:
    read_list = line.split('\t')
    total_mapq+= int(read_list[4])
print('Average MapQ score across all reads ',total_mapq/counter)

f.seek(0)
chr2L= '2L'
counter2= 0
for line in f:
    if chr2L in line:
        read_list = line.split('\t')
        if int(read_list[3]) > 10000 and int(read_list[3])<= 20000:
            counter2+=1
print('Number of reads of Chromosome 2L between 10000 and 20000 ', counter2)

f.close()
