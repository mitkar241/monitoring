# Logstash
---

[GITHUB](https://github.com/elastic/logstash)

![logstash logo](https://static-www.elastic.co/v3/assets/bltefdd0b53724fa2ce/bltfb3eae3c1d365f00/5ea8c90f6b62d4563b6ecec8/brand-logstash-220x130.svg)

## What are Logstash?
---
[Logstash](https://www.elastic.co/logstash/) is an open source data collection engine with real-time pipelining capabilities. Logstash can dynamically unify data from disparate sources and normalize the data into destinations of your choice. Cleanse and democratize all your data for diverse advanced downstream analytics and visualization use cases.

While Logstash originally drove innovation in log collection, its capabilities extend well beyond that use case. Any type of event can be enriched and transformed with a broad array of input, filter, and output plugins, with many native codecs further simplifying the ingestion process. Logstash accelerates your insights by harnessing a greater volume and variety of data.

## ingest
---
*Inputs, filters & outputs*

Logstash dynamically ingests, transforms, and ships your data regardless of format or complexity. Derive structure from unstructured data with grok, decipher geo coordinates from IP addresses, anonymize or exclude sensitive fields, and ease overall processing.

## inputs
---
*Ingest data of all shapes, sizes, and sources*

Data is often scattered or siloed across many systems in many formats. Logstash supports a variety of inputs that pull in events from a multitude of common sources, all at the same time. Easily ingest from your logs, metrics, web applications, data stores, and various AWS services, all in continuous, streaming fashion.

## filters
---
*Parse & transform your data on the fly*

As data travels from source to store, Logstash filters parse each event, identify named fields to build structure, and transform them to converge on a common format for more powerful analysis and business value.

Logstash dynamically transforms and prepares your data regardless of format or complexity:

Derive structure from unstructured data with grok
Decipher geo coordinates from IP addresses
Anonymize PII data, exclude sensitive fields completely
Ease overall processing, independent of the data source, format, or schema.
The possibilities are endless with our rich library of filters and versatile Elastic Common Schema.

## outputs
---
*Choose your stash, transport your data*

While Elasticsearch is our go-to output that opens up a world of search and analytics possibilities, it's not the only one available.

Logstash has a variety of outputs that let you route data where you want, giving you the flexibility to unlock a slew of downstream use cases.

## extensibility
---
*Create and configure your pipeline, your way*

Logstash has a pluggable framework featuring over 200 plugins. Mix, match, and orchestrate different inputs, filters, and outputs to work in pipeline harmony.

Ingesting from a custom application? Don't see a plugin you need? Logstash plugins are easy to build. We've got a fantastic API for plugin development and a plugin generator to help you start and share your creations.

## plug & play
---
*Accelerated time to insight with the Elastic Stack*

Logstash modules orchestrate a turnkey ingest-to-visualize experience with popular data sources like ArcSight and NetFlow. With the power to instantly deploy ingestion pipelines and sophisticated dashboards, your data exploration starts in minutes.

## durability & security
---
*Trust in a pipeline built to deliver*

If Logstash nodes happen to fail, Logstash guarantees at-least-once delivery for your in-flight events with its persistent queue. Events that are not successfully processed can be shunted to a dead letter queue for introspection and replay. With the ability to absorb throughput, Logstash scales through ingestion spikes without having to use an external queueing layer. Plus, we've made it possible for you to fully secure your ingest pipelines.

## monitoring
---
*Have full visibility into your deployments*

Logstash pipelines are often multipurpose and can become sophisticated, making a strong understanding of pipeline performance, availability, and bottlenecks invaluable. With monitoring and pipeline viewer features, you can easily observe and study an active Logstash node or full deployment.
