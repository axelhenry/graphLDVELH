# graphLDVELH

usage:

./launcher4XmlFile.py -f /path/to/xml_file -of /path/to/output/graph/file -cf /path/to/output/cycle/txt/file

to use this script, you'll need : 
- python3 
- beautifulSoup4 (pip install beautifulsoup4, see http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- tarjan (pip install tarjan, see https://github.com/bwesterb/py-tarjan)
- python-graph (should be available in your package manager, see https://github.com/pmatiello/python-graph)

graph-tool (see : http://graph-tool.skewed.de/),





doesn't support filepath with special characters, so keep it simple :)

legends aren't implemented yet on our graph, so there is our used color code :

RED DOT = certainty of death

ORANGE DOT = possibility of death

YELLOW DOT = you might encounter ennemies on this paragraph, depending on your actions

GREEN DOT = the start of our adventure

BLUE DOT = nothing specific to say about it, standard paragraph, nothing dangerous will happen to you here

PURPLE CIRCLED = part of a cycle
