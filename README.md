# graphLDVELH

##Goal:

 Providing visual representation of a LDVELH (livre dont vous êtes le héros) as a directed graph and highlighting cycles in it.

## Installation:

- If you don't have python3 and pip installed on your computer, install it through your package manager.
- Install python-graph (should be available in your package manager, or see https://github.com/pmatiello/python-graph)
- Install graphviz (should be available in your package manager)
- Clone this repo on your computer.  
```bash
git clone https://github.com/axelhenry/graphLDVELH.git
```
- Go into the newly created directory.
- __Optional step, but strongly advised__ : Open a terminal and create a new virtual environment in this directory.
```bash
virtualenv venv --system-site-packages
source venv/bin/activate
```
- Open a terminal and install required dependencies:
```bash
pip install -r stable-req.txt
```

## Usage:

This script takes 3 arguments:
- __--xml_file__ or __-xml__
- __--json_component_file__ or __-json__
- __--svg_graph_file__ or __-svg__


```bash
./launcher4XmlFile.py -f /path/to/xml_file -svg /path/to/svg/graph/file -json /path/to/json/component/file
```


## Sidenotes:

- doesn't support filepath with special characters, so keep it simple :)
- legends are implemented in our graph, but a little reminder never hurt so :
  - Red node : certainty of death
  - Orange node : possibility of death, watch your steps
  - Yellow node : you might encounter ennemies on this paragraph, depending on your actions
  - Green node : the start of your adventure
  - Purple edge : nodes linked are part of a cycle in your graph

## Thanks to:
- python-graph's developers
- bwesterb for his implementation of Tarjan's algorithm
- Mathias Laurin for find_all_cycles.py
