# Kibana
---

[GITHUB](https://github.com/elastic/kibana)

![kibana logo](https://static-www.elastic.co/v3/assets/bltefdd0b53724fa2ce/blt0423c2ca741d3c05/5ea8c90064f47652ec7993f4/brand-kibana-220x130.svg)

## What is Kibana?
[Kibana](https://www.elastic.co/what-is/kibana) is an free and open frontend application that sits on top of the Elastic Stack, providing search and data visualization capabilities for data indexed in Elasticsearch. Commonly known as the charting tool for the Elastic Stack (previously referred to as the ELK Stack after Elasticsearch, Logstash, and Kibana), Kibana also acts as the user interface for monitoring, managing, and securing an Elastic Stack cluster - as well as the centralized hub for built-in solutions developed on the Elastic Stack. Developed in 2013 from within the Elasticsearch community, Kibana has grown to become the window into the Elastic Stack itself, offering a portal for users and companies.

## What is Kibana used for?
---
Kibana's tight integration with Elasticsearch and the larger Elastic Stack make it ideal for supporting the following:

Searching, viewing, and visualizing data indexed in Elasticsearch and analyzing the data through the creation of bar charts, pie charts, tables, histograms, and maps. A dashboard view combines these visual elements to then be shared via browser to provide real-time analytical views into large data volumes in support of use cases such as:

- Logging and log analytics
- Infrastructure metrics and container monitoring
- Application performance monitoring (APM)
- Geospatial data analysis and visualization
- Security analytics
- Business analytics

Monitoring, managing, and securing an Elastic Stack instance via web interface.
Centralizing access for built-in solutions developed on the Elastic Stack for observability, security, and enterprise search applications.

## How does searching and visualizing data in Kibana work?
---
Kibana enables the visual analysis of data from an Elasticsearch index or multiple indices. Indices are created when Logstash (a largescale ingestor) or Beats (a collection of single-purpose data shippers) ingests unstructured data from log files and other sources and converts it into a structured format for Elasticsearch storage and search functionalities.

Kibana's interface allows users to query data in Elasticsearch indices and then visualize the results through standard chart options or built-in apps like Lens, Canvas, and Maps. Users can choose between different chart types, change the aggregations of numbers, and filter to specific segments of data.

## What is a Kibana dashboard?
---
A Kibana dashboard is a collection of charts, graphs, metrics, searches, and maps that have been collected together onto a single pane. Dashboards provide at-a-glance insights into data from multiple perspectives and enable users to drill down into the details.

## How do I create dashboards in Kibana?
---
To build a dashboard in Kibana, users must have data indexed in Elasticsearch and have already built a search, visualization, or map. From within Kibana, click Dashboard in the side navigation. When opening the Dashboard interface, an overview of existing dashboards is presented. If there are no dashboards, sample data sets can be added, which include pre-built dashboards.

To build a dashboard, users can follow these steps:

- In the side navigation, click Dashboard.
- Click Create new dashboard.
- Click Add.
- Use Add Panels to add visualizations and saved searches to the dashboard. If there are a large number of visualizations, the lists can be filtered.

If there is a read-only icon in the header, this indicates that a user does not have sufficient permissions to create, edit, or save dashboards. Kibana administrators can change these permission settings on an individual or group basis.

## Kibana Lens
---
Kibana Lens is a built-in tool designed to enable faster access to data insights for both the experienced and uninitiated user. Lens has a drag-and-drop interface to simplify the process of exploring Elasticsearch data and building out visuals. Lens aids the creation of charts with smart suggestions that provide alternative ways to visualize data based on data analysis best practice and common usage patterns.

With Kibana Lens, a user can:

- Explore data in an Elasticsearch index with minimal program interaction
- Drag and drop data fields to create multiple data visualizations
- Simultaneously search across multiple Elasticsearch indices for comparison in the same visualization
- Customize data visualizations by switching chart types and changing aggregations in real time
- Create interactive data visualizations without code or previous experience using Kibana

## Kibana Canvas
---
Canvas is a data visualization and presentation application within Kibana. With Canvas, live data can be pulled directly from Elasticsearch and combined with colors, images, text, and other customized options to create dynamic, multi-page displays.

With Canvas, a user can:

- Create and personalize a workspace with backgrounds, borders, colors, fonts, and more
- Customize workpads with custom visualizations, such as images and text
- Customize data by pulling it directly from Elasticsearch
- Display data with charts, graphs, progress monitors, and more
- Focus on the desired data to display with filters

## Why use Kibana?
---
Kibana is the official interface of Elasticsearch. Users of Elasticsearch will find Kibana to be the most effective interface for discovering data insights and performing active management of the health of their Elastic Stack.

Kibana addresses many use cases. Elastic has invested heavily in the innovation of the visualization interface. Users leverage the built-in features of Kibana for use cases such as APM, security analytics, business analytics, uptime monitoring, geospatial analytics, and more.

Kibana has a strong support community. As an free and open interface, Kibana has seen strong adoption and community contribution. Kibana users' levels of experience vary dramatically - documentation, instruction, and community support reflects this broad spectrum of expertise. Elastic also offers training and individual support to help users get up and running.

## Is Kibana free?
---
Yes, Kibana is free to use under either the Elastic license or SSPL. Additional free features are available under the Elastic license. Below are the features available for free with the default distribution of the Elastic Stack:

- APM
- Canvas
- Metrics
- Logs
- Maps
- SIEM
- Stack Monitoring
- Uptime

In addition to these free features, users can add additional tools, cloud hosting integrations, and training through paid deployment subscriptions.
