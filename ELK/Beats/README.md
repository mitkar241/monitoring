# Beats
---
![beats logo](https://static-www.elastic.co/v3/assets/bltefdd0b53724fa2ce/blt7669678e4e6152dc/5ea8c9063a474c52f7244b1c/brand-beats-220x130.svg)

## What are Beats?
---
[Beats](https://www.elastic.co/guide/en/beats/libbeat/current/beats-reference.html) are open source data shippers that you install as agents on your servers to send operational data to Elasticsearch. Elastic provides Beats for capturing:

| Beat | Purpose |
| --- | --- |
| [Auditbeat](https://www.elastic.co/products/beats/auditbeat) | Audit data |
| [Filebeat](https://www.elastic.co/products/beats/filebeat) | Log files and journals |
| [Functionbeat](https://www.elastic.co/products/beats/functionbeat) | Cloud data |
| [Heartbeat](https://www.elastic.co/products/beats/heartbeat) | Availability |
| [Metricbeat](https://www.elastic.co/products/beats/metricbeat) | Metrics |
| [Packetbeat](https://www.elastic.co/products/beats/packetbeat) | Network traffic |
| [Winlogbeat](https://www.elastic.co/products/beats/winlogbeat) | Windows event logs |

Beats can send data directly to Elasticsearch or via Logstash, where you can further process and enhance the data, before visualizing it in Kibana.

## Need to capture other kinds of data?
---
If you have a specific use case to solve, we encourage you to create a [Community Beat](https://www.elastic.co/guide/en/beats/libbeat/current/community-beats.html). We've created an infrastructure to simplify the process. The libbeat library, written entirely in Go, offers the API that all Beats use to ship data to Elasticsearch, configure the input options, implement logging, and more.
