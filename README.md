# graphLDVELH

usage:

./launcher4XmlFile.py -f /path/to/xml_file -of /path/to/output/graph/file -cf /path/to/output/cycle/txt/file

to use this script, you'll need : 

python3, 

graph-tools (see : http://graph-tool.skewed.de/),

beautifulSoup4 (pip install beautifulsoup4),

tarjan (pip install tarjan)

doesn't support filepath with special characters, so keep it simple :)

legends aren't implemented yet on our graph, so there is our used color code :

RED DOT = certainty of death

ORANGE DOT = possibility of death

YELLOW DOT = you might encounter ennemies on this paragraph, depending on your actions

GREEN DOT = the start of our adventure

BLUE DOT = nothing specific to say about it, standard paragraph, nothing dangerous will happen to you here

PURPLE CIRCLED = part of a cycle
