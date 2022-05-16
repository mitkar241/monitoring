#!/usr/bin/python3

from kibanatool.covid19.generaldetails import *
from kibanatool.covid19.countrydetails import *
from kibanatool.common.utils import *

def getPanelRefList(reference_uuid):
  panel_array = []
  references_list = []

  ##########
  # ROW 1
  ##########

  # Unique Count Confirmed
  gridData = {"x": 0, "y": 0, "w": 16, "h": 10}
  panel_array, references_list = createPanel(panel_array, references_list, reference_uuid, gridData, UniqueCountConfirmed)

  # Unique Count Deaths
  gridData = {"x": 16, "y": 0, "w": 16, "h": 10}
  panel_array, references_list = createPanel(panel_array, references_list, reference_uuid, gridData, UniqueCountDeaths)

  # Unique Count Recovered
  gridData = {"x": 32, "y": 0, "w": 16, "h": 10}
  panel_array, references_list = createPanel(panel_array, references_list, reference_uuid, gridData, UniqueCountRecovered)

  ##########
  # ROW 2
  ##########

  # Total Count Confirmed
  gridData = {"x": 0, "y": 10, "w": 16, "h": 5}
  panel_array, references_list = createPanel(panel_array, references_list, reference_uuid, gridData, TotalCountConfirmed)

  # Total Count Deaths
  gridData = {"x": 16, "y": 10, "w": 16, "h": 5}
  panel_array, references_list = createPanel(panel_array, references_list, reference_uuid, gridData, TotalCountDeaths)

  # Total Count Recovered
  gridData = {"x": 32, "y": 10, "w": 16, "h": 5}
  panel_array, references_list = createPanel(panel_array, references_list, reference_uuid, gridData, TotalCountRecovered)

  ##########
  # ROW 3
  ##########

  # Bar Percentage Panel
  gridData = {"x": 0, "y": 15, "w": 48, "h": 15}
  panel_array, references_list = createPanel(panel_array, references_list, reference_uuid, gridData, BarPercentagePanel)

  ##########
  # ROW 4
  ##########

  # Average Confirmed By Country
  gridData = {"x": 0, "y": 30, "w": 16, "h": 10}
  panel_array, references_list = createPanel(panel_array, references_list, reference_uuid, gridData, AverageConfirmedByCountry)

  # Average Confirmed By Country
  gridData = {"x": 16, "y": 30, "w": 16, "h": 10}
  panel_array, references_list = createPanel(panel_array, references_list, reference_uuid, gridData, AverageDeathsByCountry)

  # Average Confirmed By Country
  gridData = {"x": 32, "y": 30, "w": 16, "h": 10}
  panel_array, references_list = createPanel(panel_array, references_list, reference_uuid, gridData, AverageRecoveredByCountry)

  return panel_array, references_list
