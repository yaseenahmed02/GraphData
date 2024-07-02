'''
This file contains the predefined prompts that are used to generate new prompts for explaining graphs described by a Graph Description Language (GDL). 
These prompts guide the model to create diverse and contextually relevant prompts for various types of graph descriptions, ensuring comprehensive and easy-to-understand explanations.

Each variable in this file represents a different context or approach for generating these prompts, such as explaining a graph in simple terms, from an expert perspective, or within specific contexts like social media networks, political networks, and more.
'''

prompt_easy = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph in an easy-to-understand manner. 
Here are some examples:
You are given a graph description language <GDL>. Explain it like you would explain to a child.
You are given the description of a graph <GDL>. Now give me some high-level descriptions of the graph.
Don't focus on the details and don't sound like an expert. Describe it as if you were a normal person without much background in graph theory. Ensure it aligns with the graph I gave you in the GDL.
Imagine you are explaining the graph described by the language <GDL> to someone who is not familiar with graphs. Highlight the main points and keep the explanation simple.
Given the graph description language <GDL>, describe the graph's overall pattern and connectivity as if you were explaining it to a child.
Using the graph description language <GDL>, create a high-level summary of the graph that avoids technical details and focuses on the big picture.
You have a graph description language <GDL>. Explain the connections and relationships in the graph in a straightforward manner, suitable for someone without a technical background.
With the graph description language <GDL>, describe the graph's nodes and their connections using everyday language and simple examples.
Using the graph description language <GDL>, provide a step-by-step explanation of how the nodes in the graph are connected, making it easy for a novice to understand.
Imagine you are writing a blog post for a general audience using the graph description language <GDL>. Describe the graph in an engaging and easy-to-understand way, avoiding technical terminology.
Generate a new prompt following this style, be very creative:
"""

prompt_expert = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph from an expert’s perspective, using appropriate technical terminology and providing a thorough analysis. 
Here are some examples:
You are given a graph description language <GDL>. Explain the technical intricacies and nuances of the graph, including terms like 'adjacency matrix', 'degree distribution', and 'clustering coefficient'.
You are given the description of a graph <GDL>. Provide a detailed analysis of the graph’s structure, such as identifying strongly connected components, cycles, and paths.
You are given a graph description language <GDL>. Describe the graph's properties, including density, diameter, and average path length.
Generate a new prompt following this style, focusing on an expert-level explanation with detailed technical insights:
"""

prompt_political = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph in the context of a political network, highlighting the relationships and connections between various political figures. 
Here are some examples:
You are given a graph description language <GDL>. Describe the connections and relationships in a political network, such as alliances, rivalries, and power dynamics.
You are given the description of a graph <GDL>. Explain the influence and importance of each connection in a political context, identifying key influencers and followers.
You are given a graph description language <GDL>. Describe how different political factions are connected and their impact on policy decisions.
Generate a new prompt following this style, focusing on political relationships and their significance:
"""

prompt_social = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph in the context of a social media network, describing how individuals are connected and interact with each other. 
Here are some examples:
You are given a graph description language <GDL>. Explain the social dynamics and interactions within a social media network, including clusters, influencers, and common interests.
You are given the description of a graph <GDL>. Describe the most significant connections and clusters within the network, highlighting popular nodes and communities.
You are given a graph description language <GDL>. Describe the patterns of communication and engagement within the network, such as frequent interactions and retweet patterns.
Generate a new prompt following this style, focusing on social media interactions and dynamics:
"""

prompt_incident = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to describe the graph as an incident report, explaining how different nodes (representing incidents) are connected. 
Here are some examples:
You are given a graph description language <GDL>. Describe the sequence and relationships between incidents in the graph, identifying causes and effects.
You are given the description of a graph <GDL>. Provide a detailed incident report based on the graph’s structure, including timelines and incident impact.
You are given a graph description language <GDL>. Explain the connections between different incidents and how they influence each other.
Generate a new prompt following this style, focusing on incident connections and their implications:
"""

prompt_friendship = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph as a friendship network, focusing on the relationships and connections between different people. 
Here are some examples:
You are given a graph description language <GDL>. Describe the friendships and social bonds represented in the graph, highlighting close-knit groups and key individuals.
You are given the description of a graph <GDL>. Explain how friendships form and the dynamics of the social network, including mutual friends and central figures.
You are given a graph description language <GDL>. Describe the evolution of the friendship network over time, including new friendships and dissolved connections.
Generate a new prompt following this style, focusing on friendships and their dynamics:
"""


prompt_coauthor = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph as a co-authorship network, highlighting collaborations between different authors. 
Here are some examples:
You are given a graph description language <GDL>. Describe the co-authorship relationships and collaborative efforts in the graph, identifying frequent collaborators and prolific authors.
You are given the description of a graph <GDL>. Explain the strength and significance of co-authored papers and collaborations, including citation counts and impact factors.
You are given a graph description language <GDL>. Describe the network of researchers and their collaborative patterns, including interdisciplinary work and major research hubs.
Generate a new prompt following this style, focusing on co-authorships and collaborative research:
"""

prompt_fiction = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to describe the graph in the context of a fictional world, such as 'Game of Thrones', detailing the alliances, conflicts, and relationships between characters. 
Here are some examples:
You are given a graph description language <GDL>. Explain the alliances and conflicts within the fictional world represented by the graph, including major factions and rivalries.
You are given the description of a graph <GDL>. Describe the key connections and their significance in the narrative, highlighting main characters and pivotal events.
You are given a graph description language <GDL>. Describe the evolution of relationships in the fictional world, including betrayals, alliances, and character arcs.
Generate a new prompt following this style, focusing on fictional relationships and their narrative importance:
"""

prompt_research = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph as a scientific research network, detailing the collaborations and influences between different researchers. 
Here are some examples:
You are given a graph description language <GDL>. Describe the research collaborations and influence of different researchers within the graph, highlighting frequent collaborators and major research groups.
You are given the description of a graph <GDL>. Explain the key research groups and their interconnections, identifying influential researchers and their collaborators.
You are given a graph description language <GDL>. Describe how research ideas and innovations spread through the network of researchers.
Generate a new prompt following this style, focusing on scientific research networks:
"""

prompt_transport = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph as a transportation network, detailing the routes and connections between different locations. 
Here are some examples:
You are given a graph description language <GDL>. Describe the routes and connections within the transportation network, highlighting major hubs and transit routes.
You are given the description of a graph <GDL>. Explain how different locations are connected and the importance of each route, including the efficiency of travel and potential bottlenecks.
You are given a graph description language <GDL>. Describe the flow of traffic and goods through the transportation network, identifying key routes and connections.
Generate a new prompt following this style, focusing on transportation networks:
"""

prompt_ecosystem = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph as an ecosystem, detailing the interactions and relationships between different species. 
Here are some examples:
You are given a graph description language <GDL>. Describe the interactions and dependencies between different species in the ecosystem, highlighting key species and their roles.
You are given the description of a graph <GDL>. Explain the food web and ecological relationships represented in the graph, identifying predator-prey dynamics and mutualistic relationships.
You are given a graph description language <GDL>. Describe the energy flow and nutrient cycling within the ecosystem, highlighting the importance of different species.
Generate a new prompt following this style, focusing on ecosystem interactions:
"""

prompt_corporate = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph as a corporate hierarchy, detailing the reporting relationships and organizational structure. 
Here are some examples:
You are given a graph description language <GDL>. Describe the organizational structure and reporting relationships within the corporate hierarchy, highlighting key positions and departments.
You are given the description of a graph <GDL>. Explain the roles and positions of different individuals in the corporate hierarchy, including their responsibilities and influence.
You are given a graph description language <GDL>. Describe the flow of information and decision-making within the corporate structure, identifying key nodes and pathways.
Generate a new prompt following this style, focusing on corporate hierarchies:
"""

prompt_telecom = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph as a telecommunications network, detailing the connections and data flow between different nodes. 
Here are some examples:
You are given a graph description language <GDL>. Describe the data flow and connections within the telecommunications network, highlighting key nodes and communication links.
You are given the description of a graph <GDL>. Explain how different nodes are connected and the significance of each connection, including bandwidth and latency considerations.
You are given a graph description language <GDL>. Describe the overall structure and topology of the telecommunications network, identifying major hubs and pathways.
Generate a new prompt following this style, focusing on telecommunications networks:
"""

prompt_family = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph as a family tree, detailing the relationships and connections between different family members. 
Here are some examples:
You are given a graph description language <GDL>. Describe the familial relationships and connections within the family tree, highlighting key family members and their lineage.
You are given the description of a graph <GDL>. Explain the lineage and heritage represented in the graph, identifying ancestors and descendants.
You are given a graph description language <GDL>. Describe the structure of the family tree, including branches and generational connections.
Generate a new prompt following this style, focusing on family trees:
"""

prompt_supplychain = """
You are tasked with generating a prompt to help explain graphs described by a Graph Description Language (GDL). 
The generated prompt should include a placeholder <GDL> where the graph description will be inserted. 
Ensure the prompt guides the model to explain the graph as a supply chain network, detailing the flow of goods and relationships between different entities. 
Here are some examples:
You are given a graph description language <GDL>. Describe the flow of goods and connections within the supply chain network, highlighting key suppliers and distributors.
You are given the description of a graph <GDL>. Explain the relationships and dependencies between different entities in the supply chain, including bottlenecks and critical paths.
You are given a graph description language <GDL>. Describe the overall structure and efficiency of the supply chain, identifying key nodes and links.
Generate a new prompt following this style, focusing on supply chain networks:
"""
