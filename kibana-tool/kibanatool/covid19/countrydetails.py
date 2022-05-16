#!/usr/bin/python3

import uuid
from kibanatool.common.model import *

def AverageConfirmedByCountry(elk_version, reference_uuid, gridData, layer_uuid):
  panel_uuid = gridData["i"]
  col_metric_uuid = str(uuid.uuid4())
  col_groups_uuid_list = [
    str(uuid.uuid4())
  ]

  panel = get_lnsPie_panel()

  panel["version"] = elk_version
  panel["gridData"] = gridData
  panel["panelIndex"] = panel_uuid
  panel["title"] = "Average Confirmed cases"

  references_list = [
    {
      "type": "index-pattern",
      "id": reference_uuid,
      "name": "indexpattern-datasource-current-indexpattern"
    },
    {
      "type": "index-pattern",
      "id": reference_uuid,
      "name": "indexpattern-datasource-layer-" + layer_uuid
    }
  ]
  panel["embeddableConfig"]["attributes"]["title"] = ""
  panel["embeddableConfig"]["attributes"]["references"] = references_list
  
  layers_list = [
    {
      "layerId": layer_uuid,
      "groups": col_groups_uuid_list,
      "metric": col_metric_uuid,
      "numberDisplay": "percent",
      "categoryDisplay": "default",
      "legendDisplay": "default",
      "nestedLegend": False,
      "layerType": "data"
    }
  ]
  panel["embeddableConfig"]["attributes"]["state"]["visualization"]["layers"] = layers_list

  indexpattern = {
    "layers": {
      layer_uuid: {
        "columns": {
          col_groups_uuid_list[0]: {
            "label": "Top values of Country/Region.keyword",
            "dataType": "string",
            "operationType": "terms",
            "scale": "ordinal",
            "sourceField": "Country/Region.keyword",
            "isBucketed": True,
            "params": {
              "size": 50,
              "orderBy": {
                "type": "column",
                "columnId": col_metric_uuid
              },
              "orderDirection": "desc",
              "otherBucket": True,
              "missingBucket": False
            }
          },
          col_metric_uuid: {
            "label": "Average of Confirmed",
            "dataType": "number",
            "operationType": "average",
            "sourceField": "Confirmed",
            "isBucketed": False,
            "scale": "ratio"
          }
        },
        "columnOrder": [
          col_groups_uuid_list[0],
          col_metric_uuid
        ],
        "incompleteColumns": {}
      }
    }
  }
  
  panel["embeddableConfig"]["attributes"]["state"]["datasourceStates"]["indexpattern"] = indexpattern
  return panel

def AverageDeathsByCountry(elk_version, reference_uuid, gridData, layer_uuid):
  panel_uuid = gridData["i"]
  col_metric_uuid = str(uuid.uuid4())
  col_groups_uuid_list = [
    str(uuid.uuid4())
  ]

  panel = get_lnsPie_panel()

  panel["version"] = elk_version
  panel["gridData"] = gridData
  panel["panelIndex"] = panel_uuid
  panel["title"] = "Average Deaths cases"

  references_list = [
    {
      "type": "index-pattern",
      "id": reference_uuid,
      "name": "indexpattern-datasource-current-indexpattern"
    },
    {
      "type": "index-pattern",
      "id": reference_uuid,
      "name": "indexpattern-datasource-layer-" + layer_uuid
    }
  ]
  panel["embeddableConfig"]["attributes"]["title"] = ""
  panel["embeddableConfig"]["attributes"]["references"] = references_list
  
  layers_list = [
    {
      "layerId": layer_uuid,
      "groups": col_groups_uuid_list,
      "metric": col_metric_uuid,
      "numberDisplay": "percent",
      "categoryDisplay": "default",
      "legendDisplay": "default",
      "nestedLegend": False,
      "layerType": "data"
    }
  ]
  panel["embeddableConfig"]["attributes"]["state"]["visualization"]["layers"] = layers_list

  indexpattern = {
    "layers": {
      layer_uuid: {
        "columns": {
          col_groups_uuid_list[0]: {
            "label": "Top values of Country/Region.keyword",
            "dataType": "string",
            "operationType": "terms",
            "scale": "ordinal",
            "sourceField": "Country/Region.keyword",
            "isBucketed": True,
            "params": {
              "size": 50,
              "orderBy": {
                "type": "column",
                "columnId": col_metric_uuid
              },
              "orderDirection": "desc",
              "otherBucket": True,
              "missingBucket": False
            }
          },
          col_metric_uuid: {
            "label": "Average of Deaths",
            "dataType": "number",
            "operationType": "average",
            "sourceField": "Deaths",
            "isBucketed": False,
            "scale": "ratio"
          }
        },
        "columnOrder": [
          col_groups_uuid_list[0],
          col_metric_uuid
        ],
        "incompleteColumns": {}
      }
    }
  }
  
  panel["embeddableConfig"]["attributes"]["state"]["datasourceStates"]["indexpattern"] = indexpattern
  return panel

def AverageRecoveredByCountry(elk_version, reference_uuid, gridData, layer_uuid):
  panel_uuid = gridData["i"]
  col_metric_uuid = str(uuid.uuid4())
  col_groups_uuid_list = [
    str(uuid.uuid4())
  ]

  panel = get_lnsPie_panel()

  panel["version"] = elk_version
  panel["gridData"] = gridData
  panel["panelIndex"] = panel_uuid
  panel["title"] = "Average Recovered cases"

  references_list = [
    {
      "type": "index-pattern",
      "id": reference_uuid,
      "name": "indexpattern-datasource-current-indexpattern"
    },
    {
      "type": "index-pattern",
      "id": reference_uuid,
      "name": "indexpattern-datasource-layer-" + layer_uuid
    }
  ]
  panel["embeddableConfig"]["attributes"]["title"] = ""
  panel["embeddableConfig"]["attributes"]["references"] = references_list
  
  layers_list = [
    {
      "layerId": layer_uuid,
      "groups": col_groups_uuid_list,
      "metric": col_metric_uuid,
      "numberDisplay": "percent",
      "categoryDisplay": "default",
      "legendDisplay": "default",
      "nestedLegend": False,
      "layerType": "data"
    }
  ]
  panel["embeddableConfig"]["attributes"]["state"]["visualization"]["layers"] = layers_list

  indexpattern = {
    "layers": {
      layer_uuid: {
        "columns": {
          col_groups_uuid_list[0]: {
            "label": "Top values of Country/Region.keyword",
            "dataType": "string",
            "operationType": "terms",
            "scale": "ordinal",
            "sourceField": "Country/Region.keyword",
            "isBucketed": True,
            "params": {
              "size": 50,
              "orderBy": {
                "type": "column",
                "columnId": col_metric_uuid
              },
              "orderDirection": "desc",
              "otherBucket": True,
              "missingBucket": False
            }
          },
          col_metric_uuid: {
            "label": "Average of Recovered",
            "dataType": "number",
            "operationType": "average",
            "sourceField": "Recovered",
            "isBucketed": False,
            "scale": "ratio"
          }
        },
        "columnOrder": [
          col_groups_uuid_list[0],
          col_metric_uuid
        ],
        "incompleteColumns": {}
      }
    }
  }
  
  panel["embeddableConfig"]["attributes"]["state"]["datasourceStates"]["indexpattern"] = indexpattern
  return panel
