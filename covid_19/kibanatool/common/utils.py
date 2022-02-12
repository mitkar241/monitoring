#!/usr/bin/python3

import json
import uuid

def getReferencesList(reference_uuid, panel_uuid, layer_uuid):
  references_list = [
    {
      "id": reference_uuid,
      "name": panel_uuid + ":indexpattern-datasource-current-indexpattern",
      "type": "index-pattern"
    },
    {
      "id": reference_uuid,
      "name": panel_uuid + ":indexpattern-datasource-layer-" + layer_uuid,
      "type": "index-pattern"
    }
  ]
  return references_list

def modJsonSchema(dict_item):
  str_item = json.dumps(dict_item)
  #str_item = str_item.replace("\"", "\\\"", -1)
  str_item = str_item.replace("True", "true", -1)
  str_item = str_item.replace("False", "false", -1)
  #print(str_item)
  return str_item

def createPanel(panel_array, references_list, reference_uuid, gridData, panelFunc):
  elk_version = "7.17.0"
  panel_uuid = str(uuid.uuid4())
  layer_uuid = str(uuid.uuid4())
  gridData["i"] = panel_uuid
  panel_array.append(panelFunc(elk_version, reference_uuid, gridData, layer_uuid))
  references_list.extend(getReferencesList(reference_uuid, panel_uuid, layer_uuid))
  return panel_array, references_list

def createNdjsonFile(dashboard_file_location, dashboard_str):
  with open(dashboard_file_location, "w") as file_pointer:
    #file_pointer.write("testing\n")
    #file_pointer.writelines(dashboard_str_list)
    file_pointer.write(dashboard_str)
