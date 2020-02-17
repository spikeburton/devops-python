# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import yaml

with open('../data/playbook.yml', 'r') as opened:
    playbook = yaml.safe_load((opened))


# %%
import xml.etree.ElementTree as ET

tree = ET.parse('../data/feed.xml')
root = tree.getroot()

for ch in root:
    for child in ch:
        print(child.tag, child.attrib)

# %%
