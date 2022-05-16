#!/usr/bin/python3

import uuid

from kibanatool.covid19.kibanamain import *
from kibanatool.covid19.generaldetails import *
from kibanatool.covid19.countrydetails import *
from kibanatool.common.dashboardndjsondetails import *
from kibanatool.common.utils import *
from kibanatool.common.model import *

##########
# GLOBAL VARIABLES
##########
elk_version = "7.17.0"
index_pattern_version = "7.11.0"
dashboard_file_location = "./covid_19_dashboard.ndjson"

if __name__ == "__main__":
  dashboard_uuid = str(uuid.uuid4())
  reference_uuid = str(uuid.uuid4())

  searchSourceJSON_str = getSearchSourceJSON()
  optionsJSON_str = getOptionsJSON()
  panel_array, references_list = getPanelRefList(reference_uuid)
  panelsJSON_str = modJsonSchema(panel_array)

  dashboard1_str = getDashboardNdjson1(reference_uuid, "logstash-*")
  dashboard2_str = getDashboardNdjson2(searchSourceJSON_str, optionsJSON_str, panelsJSON_str, dashboard_uuid, references_list, "covid_19_dashboard", "Dashboard for displaying details regarding covid-19", )
  dashboard3_str = getDashboardNdjson3()

  dashboard_str_list = [dashboard1_str, dashboard2_str, dashboard3_str]
  dashboard_str = "\n".join(dashboard_str_list)

  createNdjsonFile(dashboard_file_location, dashboard_str)
