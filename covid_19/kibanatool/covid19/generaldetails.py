#!/usr/bin/python3

import uuid
from kibanatool.common.model import *

def UniqueCountConfirmed(elk_version, reference_uuid, gridData, layer_uuid):
  panel_uuid = gridData["i"]
  col_xAccessor_uuid = str(uuid.uuid4())
  col_accessors_uuid_list = [
    str(uuid.uuid4())
  ]

  panel = get_lnsXY_panel()

  panel["version"] = elk_version
  panel["gridData"] = gridData
  panel["panelIndex"] = panel_uuid

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
      "accessors": col_accessors_uuid_list,
      "position": "top",
      "seriesType": "area",
      "showGridlines": False,
      "layerType": "data",
      "xAccessor": col_xAccessor_uuid
    }
  ]
  panel["embeddableConfig"]["attributes"]["state"]["visualization"]["layers"] = layers_list

  indexpattern = {
    "layers": {
      layer_uuid: {
        "columns": {
          col_xAccessor_uuid: {
            "label": "ObservationData",
            "dataType": "date",
            "operationType": "date_histogram",
            "sourceField": "ObservationData",
            "isBucketed": True,
            "scale": "interval",
            "params": {
              "interval": "auto"
            }
          },
          col_accessors_uuid_list[0]: {
            "label": "Unique count of Confirmed",
            "dataType": "number",
            "operationType": "unique_count",
            "scale": "ratio",
            "sourceField": "Confirmed",
            "isBucketed": False
          }
        },
        "columnOrder": [
          col_xAccessor_uuid,
          col_accessors_uuid_list[0]
        ],
        "incompleteColumns": {}
      }
    }
  }
  panel["embeddableConfig"]["attributes"]["state"]["datasourceStates"]["indexpattern"] = indexpattern
  return panel

def UniqueCountDeaths(elk_version, reference_uuid, gridData, layer_uuid):
  panel_uuid = gridData["i"]
  col_xAccessor_uuid = str(uuid.uuid4())
  col_accessors_uuid_list = [
    str(uuid.uuid4())
  ]

  panel = get_lnsXY_panel()

  panel["version"] = elk_version
  panel["gridData"] = gridData
  panel["panelIndex"] = panel_uuid

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
      "accessors": col_accessors_uuid_list,
      "position": "top",
      "seriesType": "area",
      "showGridlines": False,
      "layerType": "data",
      "xAccessor": col_xAccessor_uuid
    }
  ]
  panel["embeddableConfig"]["attributes"]["state"]["visualization"]["layers"] = layers_list

  indexpattern = {
    "layers": {
      layer_uuid: {
        "columns": {
          col_xAccessor_uuid: {
            "label": "ObservationData",
            "dataType": "date",
            "operationType": "date_histogram",
            "sourceField": "ObservationData",
            "isBucketed": True,
            "scale": "interval",
            "params": {
              "interval": "auto"
            }
          },
          col_accessors_uuid_list[0]: {
            "label": "Unique count of Deaths",
            "dataType": "number",
            "operationType": "unique_count",
            "scale": "ratio",
            "sourceField": "Deaths",
            "isBucketed": False
          }
        },
        "columnOrder": [
          col_xAccessor_uuid,
          col_accessors_uuid_list[0]
        ],
        "incompleteColumns": {}
      }
    }
  }
  panel["embeddableConfig"]["attributes"]["state"]["datasourceStates"]["indexpattern"] = indexpattern
  return panel

def UniqueCountRecovered(elk_version, reference_uuid, gridData, layer_uuid):
  panel_uuid = gridData["i"]
  col_xAccessor_uuid = str(uuid.uuid4())
  col_accessors_uuid_list = [
    str(uuid.uuid4())
  ]

  panel = get_lnsXY_panel()

  panel["version"] = elk_version
  panel["gridData"] = gridData
  panel["panelIndex"] = panel_uuid

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
      "accessors": col_accessors_uuid_list,
      "position": "top",
      "seriesType": "area",
      "showGridlines": False,
      "layerType": "data",
      "xAccessor": col_xAccessor_uuid
    }
  ]
  panel["embeddableConfig"]["attributes"]["state"]["visualization"]["layers"] = layers_list

  indexpattern = {
    "layers": {
      layer_uuid: {
        "columns": {
          col_xAccessor_uuid: {
            "label": "ObservationData",
            "dataType": "date",
            "operationType": "date_histogram",
            "sourceField": "ObservationData",
            "isBucketed": True,
            "scale": "interval",
            "params": {
              "interval": "auto"
            }
          },
          col_accessors_uuid_list[0]: {
            "label": "Unique count of Recovered",
            "dataType": "number",
            "operationType": "unique_count",
            "scale": "ratio",
            "sourceField": "Recovered",
            "isBucketed": False
          }
        },
        "columnOrder": [
          col_xAccessor_uuid,
          col_accessors_uuid_list[0]
        ],
        "incompleteColumns": {}
      }
    }
  }
  panel["embeddableConfig"]["attributes"]["state"]["datasourceStates"]["indexpattern"] = indexpattern
  return panel

def TotalCountConfirmed(elk_version, reference_uuid, gridData, layer_uuid):
  panel_uuid = gridData["i"]
  col_accessor_uuid = str(uuid.uuid4())

  panel = get_lnsMetric_panel()

  panel["version"] = elk_version
  panel["gridData"] = gridData
  panel["panelIndex"] = panel_uuid

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
  
  visualization = {
    "layerId": layer_uuid,
    "accessor": col_accessor_uuid,
    "layerType": "data"
  }
  panel["embeddableConfig"]["attributes"]["state"]["visualization"] = visualization

  indexpattern = {
    "layers": {
      layer_uuid: {
        "columns": {
          col_accessor_uuid: {
            "label": "Total Confirmed cases",
            "dataType": "number",
            "operationType": "sum",
            "sourceField": "Confirmed",
            "isBucketed": False,
            "scale": "ratio",
            "params": {
              "format": {
                "id": "number",
                "params": {
                  "decimals": 0
                }
              }
            },
            "customLabel": True
          }
        },
        "columnOrder": [
          col_accessor_uuid
        ],
        "incompleteColumns": {}
      }
    }
  }
  panel["embeddableConfig"]["attributes"]["state"]["datasourceStates"]["indexpattern"] = indexpattern
  return panel

def TotalCountDeaths(elk_version, reference_uuid, gridData, layer_uuid):
  panel_uuid = gridData["i"]
  col_accessor_uuid = str(uuid.uuid4())

  panel = get_lnsMetric_panel()

  panel["version"] = elk_version
  panel["gridData"] = gridData
  panel["panelIndex"] = panel_uuid

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
  
  visualization = {
    "layerId": layer_uuid,
    "accessor": col_accessor_uuid,
    "layerType": "data"
  }
  panel["embeddableConfig"]["attributes"]["state"]["visualization"] = visualization

  indexpattern = {
    "layers": {
      layer_uuid: {
        "columns": {
          col_accessor_uuid: {
            "label": "Total Death cases",
            "dataType": "number",
            "operationType": "sum",
            "sourceField": "Deaths",
            "isBucketed": False,
            "scale": "ratio",
            "params": {
              "format": {
                "id": "number",
                "params": {
                  "decimals": 0
                }
              }
            },
            "customLabel": True
          }
        },
        "columnOrder": [
          col_accessor_uuid
        ],
        "incompleteColumns": {}
      }
    }
  }
  panel["embeddableConfig"]["attributes"]["state"]["datasourceStates"]["indexpattern"] = indexpattern
  return panel

def TotalCountRecovered(elk_version, reference_uuid, gridData, layer_uuid):
  panel_uuid = gridData["i"]
  col_accessor_uuid = str(uuid.uuid4())

  panel = get_lnsMetric_panel()

  panel["version"] = elk_version
  panel["gridData"] = gridData
  panel["panelIndex"] = panel_uuid

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
  
  visualization = {
    "layerId": layer_uuid,
    "accessor": col_accessor_uuid,
    "layerType": "data"
  }
  panel["embeddableConfig"]["attributes"]["state"]["visualization"] = visualization

  indexpattern = {
    "layers": {
      layer_uuid: {
        "columns": {
          col_accessor_uuid: {
            "label": "Total Recovered cases",
            "dataType": "number",
            "operationType": "sum",
            "sourceField": "Recovered",
            "isBucketed": False,
            "scale": "ratio",
            "params": {
              "format": {
                "id": "number",
                "params": {
                  "decimals": 0
                }
              }
            },
            "customLabel": True
          }
        },
        "columnOrder": [
          col_accessor_uuid
        ],
        "incompleteColumns": {}
      }
    }
  }
  panel["embeddableConfig"]["attributes"]["state"]["datasourceStates"]["indexpattern"] = indexpattern
  return panel

def BarPercentagePanel(elk_version, reference_uuid, gridData, layer_uuid):
  panel_uuid = gridData["i"]
  col_xAccessor_uuid = str(uuid.uuid4())
  col_accessors_uuid_list = [
    str(uuid.uuid4()),
    str(uuid.uuid4()),
    str(uuid.uuid4())
  ]

  panel = get_lnsXY_panel()

  panel["version"] = elk_version
  panel["gridData"] = gridData
  panel["panelIndex"] = panel_uuid

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
      "accessors": col_accessors_uuid_list,
      "position": "top",
      "seriesType": "bar_percentage_stacked",
      "showGridlines": False,
      "layerType": "data",
      "xAccessor": col_xAccessor_uuid
    }
  ]
  panel["embeddableConfig"]["attributes"]["state"]["visualization"]["layers"] = layers_list

  indexpattern = {
    "layers": {
      layer_uuid: {
        "columns": {
          col_xAccessor_uuid: {
            "label": "ObservationData",
            "dataType": "date",
            "operationType": "date_histogram",
            "sourceField": "ObservationData",
            "isBucketed": True,
            "scale": "interval",
            "params": {
              "interval": "auto"
            }
          },
          col_accessors_uuid_list[0]: {
            "label": "Unique count of Confirmed",
            "dataType": "number",
            "operationType": "unique_count",
            "scale": "ratio",
            "sourceField": "Confirmed",
            "isBucketed": False
          },
          col_accessors_uuid_list[1]: {
            "label": "Unique count of Deaths",
            "dataType": "number",
            "operationType": "unique_count",
            "scale": "ratio",
            "sourceField": "Deaths",
            "isBucketed": False
          },
          col_accessors_uuid_list[2]: {
            "label": "Unique count of Recovered",
            "dataType": "number",
            "operationType": "unique_count",
            "scale": "ratio",
            "sourceField": "Recovered",
            "isBucketed": False
          },
        },
        "columnOrder": [
          col_xAccessor_uuid,
          col_accessors_uuid_list[0],
          col_accessors_uuid_list[1],
          col_accessors_uuid_list[2]
        ],
        "incompleteColumns": {}
      }
    }
  }
  panel["embeddableConfig"]["attributes"]["state"]["datasourceStates"]["indexpattern"] = indexpattern
  return panel
