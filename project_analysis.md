# Project Analysis Document: Delivery Route Optimization 
- Application Name: Delivery Route Optimization System
- Domain: Transportation

## Description
This application seeks to optimize delivery routes between a warehouse and customers. It calculates the most efficient path to minimize time and delivery costs. The application uses Dijkstra's algorithm by determining the shortest route in a weighted graph. The graph represents the delivery network of where nodes are locations, and edges are paths with weights as distance or travel costs.

## Key Capabilities and Requirements

### Key Capabilities: 
1. Graph of Delivery Network
- Nodes represent warehouses and customers.
- Edges present the connection between locations using weights as indication of travel costs or distance.

2. Shortest Path Calculation
- Uses Dijkstra's algorithm to determine the shortest route between the starting point and target location. 
- Starting point would be the warehouse and the target location would be the customer.
- Returns the most optimal route and total cost.

### Key Requirements:
1. **Functional Requirements**
- Locations and connections represented by the graph. 
- Allow the addition of nodes and edges. 
- Determine the shortest paths for destinations. 

## Chosen Data Structure
- Data Structure Used: Graph / Adjacency List 

### Why was this data structure selected?:
1. **Relevance to the Domain**
- The adjacency list is well-suited for showing a sparse graph, which is commonly used in logistic networks where locations are not completely interconnected with each other. 
- It effectively represents the relationships and weights (costs and distances) between locations.

2. **Efficiency and Reliability** 
- The process of adding nodes and edges is both simple and quick. 
- Operations such as querying neighbors and iterating through edges are efficiently supported. 

## Big O Performance Characteristics 
1. **Space Complexity:**
- O(V + E), V represents the number of nodes and E denotes the number of edges.  
- This complexity is particularly memory efficient for sparse graphs.  

2. **Adding a node:** 
- O(1), This operation consists of inserting a key into the adjacency list. 

3. **Adding an edge:**  
- O(1) for each direction in an undirected graph, which involves a single append to the list.

## Alternative Data Structure:
- Alternative Data Structure: Incidence List

### Why was this data structure not selected:
1. **Inefficient in neighbor lookups:**
- Dijkstra’s algorithms require efficient access to a node’s neighbors.
- Incidence lists require you to check every edge, making searching for neighbors inefficient and expensive.
  
2. **Inefficient in node-based operations:** 
- Finding all neighbors of a node requires searching through the full list of edges, making it O(E). 
- In an adjacency list, retrieving neighbors is O(1). 

Overall, incidence lists are simple and efficient for edge-based operations. However, it was not selected for its inefficiency in neighbor lookups and node-based operations. The inefficiency would have slowed down crucial parts of the delivery system application. 

## Reflection on the use of Generative AI: 
Generative AI such as ChatGPT and Microsoft Copilot are both useful in offering insight and feedback to coding and documentation. AI was able to simplify concepts such as “Big O Performance Characteristics” and made it easier to understand. AI also provided helpful recommendations for the Delivery Optimization System, such as adding error handling to create a more robust application.  
