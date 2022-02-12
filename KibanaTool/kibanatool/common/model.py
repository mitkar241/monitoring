#!/usr/bin/python3

def get_lnsXY_panel():
  lnsXY_panel = {
    "version": "7.17.0",
    "type": "lens",
    "gridData": {
      "x": 16,
      "y": 0,
      "w": 16,
      "h": 11,
      "i": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    "panelIndex": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "embeddableConfig": {
      "attributes": {
        "title": "",
        "visualizationType": "lnsXY",
        "type": "lens",
        "references": [
          {
            "type": "index-pattern",
            "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "name": "indexpattern-datasource-current-indexpattern"
          },
          {
            "type": "index-pattern",
            "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "name": "indexpattern-datasource-layer-" + "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
          }
        ],
        "state": {
          "visualization": {
            "legend": {
              "isVisible": True,
              "position": "right"
            },
            "valueLabels": "hide",
            "fittingFunction": "None",
            "yLeftExtent": {
              "mode": "full"
            },
            "yRightExtent": {
              "mode": "full"
            },
            "axisTitlesVisibilitySettings": {
              "x": True,
              "yLeft": True,
              "yRight": True
            },
            "tickLabelsVisibilitySettings": {
              "x": True,
              "yLeft": True,
              "yRight": True
            },
            "labelsOrientation": {
              "x": 0,
              "yLeft": 0,
              "yRight": 0
            },
            "gridlinesVisibilitySettings": {
              "x": True,
              "yLeft": True,
              "yRight": True
            },
            "preferredSeriesType": "bar_stacked",
            "layers": [
              {
                "layerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "accessors": [
                  "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                ],
                "position": "top",
                "seriesType": "area",
                "showGridlines": False,
                "layerType": "data",
                "xAccessor": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
              }
            ]
          },
          "query": {
            "query": "",
            "language": "kuery"
          },
          "filters": [],
          "datasourceStates": {
            "indexpattern": {
              "layers": {
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx": {
                  "columns": {
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx": {
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
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx": {
                      "label": "Unique count of Confirmed",
                      "dataType": "number",
                      "operationType": "unique_count",
                      "scale": "ratio",
                      "sourceField": "Confirmed",
                      "isBucketed": False
                    }
                  },
                  "columnOrder": [
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                  ],
                  "incompleteColumns": {}
                }
              }
            }
          }
        }
      },
      "hidePanelTitles": False,
      "enhancements": {}
    },
    "title": ""
  }
  return lnsXY_panel

def get_lnsMetric_panel():
  lnsMetric_panel = {
    "version": "7.17.0",
    "type": "lens",
    "gridData": {
      "x": 0,
      "y": 11,
      "w": 16,
      "h": 4,
      "i": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    "panelIndex": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "embeddableConfig": {
      "attributes": {
        "title": "",
        "visualizationType": "lnsMetric",
        "type": "lens",
        "references": [
          {
            "type": "index-pattern",
            "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "name": "indexpattern-datasource-current-indexpattern"
          },
          {
            "type": "index-pattern",
            "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "name": "indexpattern-datasource-layer-" + "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
          }
        ],
        "state": {
          "visualization": {
            "layerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "accessor": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "layerType": "data"
          },
          "query": {
            "query": "",
            "language": "kuery"
          },
          "filters": [],
          "datasourceStates": {
            "indexpattern": {
              "layers": {
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx": {
                  "columns": {
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx": {
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
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                  ],
                  "incompleteColumns": {}
                }
              }
            }
          }
        }
      },
      "enhancements": {}
    },
    "title": ""
  }
  return lnsMetric_panel

def get_lnsPie_panel():
  lnsPie_panel = {
    "version": "7.17.0",
    "type": "lens",
    "gridData": {
      "x": 0,
      "y": 29,
      "w": 17,
      "h": 11,
      "i": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    "panelIndex": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "embeddableConfig": {
      "attributes": {
        "title": "",
        "visualizationType": "lnsPie",
        "type": "lens",
        "references": [
          {
            "type": "index-pattern",
            "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "name": "indexpattern-datasource-current-indexpattern"
          },
          {
            "type": "index-pattern",
            "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "name": "indexpattern-datasource-layer-" + "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
          }
        ],
        "state": {
          "visualization": {
            "shape": "donut",
            "layers": [
              {
                "layerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "groups": [
                  "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                ],
                "metric": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "numberDisplay": "percent",
                "categoryDisplay": "default",
                "legendDisplay": "default",
                "nestedLegend": False,
                "layerType": "data"
              }
            ]
          },
          "query": {
            "query": "",
            "language": "kuery"
          },
          "filters": [],
          "datasourceStates": {
            "indexpattern": {
              "layers": {
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx": {
                  "columns": {
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx": {
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
                          "columnId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                        },
                        "orderDirection": "desc",
                        "otherBucket": True,
                        "missingBucket": False
                      }
                    },
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx": {
                      "label": "Average of Confirmed",
                      "dataType": "number",
                      "operationType": "average",
                      "sourceField": "Confirmed",
                      "isBucketed": False,
                      "scale": "ratio"
                    }
                  },
                  "columnOrder": [
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                  ],
                  "incompleteColumns": {}
                }
              }
            }
          }
        }
      },
      "enhancements": {},
      "hidePanelTitles": False
    },
    "title": ""
  }
  return lnsPie_panel
