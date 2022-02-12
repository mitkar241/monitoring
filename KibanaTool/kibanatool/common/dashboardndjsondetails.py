#!/usr/bin/python3

from kibanatool.common.utils import *

def getDashboardNdjson1(reference_uuid, title):
  elk_version = "7.17.0"
  index_pattern_version = "7.11.0"
  json1 = {
    "attributes": {
      "fieldAttrs": "{}",
      "fields": "[]",
      "runtimeFieldMap": "{}",
      "timeFieldName": "ObservationData",
      "title": title,
      "typeMeta": "{}"
    },
    "coreMigrationVersion": elk_version,
    "id": reference_uuid,
    "migrationVersion": {
      "index-pattern": index_pattern_version
    },
    "references": [],
    "type": "index-pattern",
    "updated_at": "2022-02-09T19:43:25.291Z",
    "version": "WzE4OTEsNl0="
  }
  return modJsonSchema(json1)

def getDashboardNdjson2(searchSourceJSON_str, optionsJSON_str, panelsJSON_str, dashboard_uuid, references_list, title, description):
  elk_version = "7.17.0"
  json2 = {
    "attributes": {
      "description": description,
      "hits": 0,
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": searchSourceJSON_str
      },
      "optionsJSON": optionsJSON_str,
      "panelsJSON": panelsJSON_str,
      "timeRestore": False,
      "title": title,
      "version": 1
    },
    "coreMigrationVersion": elk_version,
    "id": dashboard_uuid,
    "migrationVersion": {
      "dashboard": elk_version
    },
    "references": references_list,
    "type": "dashboard",
    "updated_at": "2022-02-11T17:55:40.842Z",
    "version": "WzIxMjQsNl0="
  }
  return modJsonSchema(json2)

def getDashboardNdjson3():
  json3 = {
    "excludedObjects": [],
    "excludedObjectsCount": 0,
    "exportedCount": 2,
    "missingRefCount": 0,
    "missingReferences": []
  }
  return modJsonSchema(json3)

def getSearchSourceJSON():
  searchSourceJSON = {
    "query": {
      "query": "",
      "language": "kuery"
    },
    "filter": []
  }
  return modJsonSchema(searchSourceJSON)

def getOptionsJSON():
  optionsJSON = {
    "useMargins": True,
    "syncColors": True,
    "hidePanelTitles": False
  }
  return modJsonSchema(optionsJSON)
