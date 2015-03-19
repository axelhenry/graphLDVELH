# graphLDVELH

##Goal:

 Providing visual representation of a LDVELH (livre dont vous êtes le héros) as a directed graph and highlighting cycles in it.

##Usage:

./launcher4XmlFile.py -f /path/to/xml_file -ogf /path/to/output/graph/svg_file -ocf /path/to/output/cycle/txt/file

##Dependencies:

To use this script, you'll need : 
- python3 
- beautifulSoup4 (pip install beautifulsoup4, see http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- tarjan (pip install tarjan, see https://github.com/bwesterb/py-tarjan)
- python-graph (should be available in your package manager, see https://github.com/pmatiello/python-graph)
  - you may need pydot as a dependency of python-graph instead of python-dot
- graphviz (should be available in your package manager)
- treelib (pip install treelib, see https://github.com/caesar0301/treelib)


##Sidenotes:

- doesn't support filepath with special characters, so keep it simple :)
- legends are implemented in our graph, but a little reminder never hurt so :
  - Red node : certainty of death
  - Orange node : possibility of death, watch your steps
  - Yellow node : you might encounter ennemies on this paragraph, depending on your actions
  - Green node : the start of your adventure
  - Purple edge : nodes linked are part of a cycle in your graph

##Thanks to:
- python-graph's developers
- bwesterb for his implementation of Tarjan's algorithm
- Mathias Laurin for find_all_cycles.py


