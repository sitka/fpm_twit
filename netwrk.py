import networkx as nx
import csv
import numpy as np
import matplotlib.pyplot as plt

with open('home.csv') as csvfile:
	G = nx.read_edgelist(csvfile, delimiter=',', nodetype=str)

	for e in G.edges():
		print e

#adding nodes



nx.draw(G, with_labels=True)
plt.draw()
plt.show()




# this opened and read the first column of CSV

#with open('home.csv') as csvfile:
#	readCSV = csv.reader(csvfile, delimiter=',')
#
#	for row in readCSV:
#		names = row[0]

		#print names
