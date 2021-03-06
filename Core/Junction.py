# Junction.py
#
# Project: SWMM2PEST
# Version: 3.0
# Date:   01/29/2021 (version 3.0; author: F.Dumont)
#
# Class type for Junctions and all its parameters as variables

from Core.Subcatchments import DataField
class Junction():


    def __init__(self, jun_index, name):
        self.jun_index = jun_index
        self.name = name
        self.invert_elevation = DataField('invert_elevation', "Invert_Elevation",self.name, index = 0)
        self.max_depth = DataField('max_depth', "Max_Depth", self.name, index = 0)
        self.init_depth = DataField('init_depth', "Init_Depth", self.name, index = 0)
        self.surcharge_depth = DataField('surcharge_depth', "Surcharge_Depth", self.name, index = 0)
        self.ponded_depth = DataField('ponded_depth', "Ponded_Depth", self.name, index = 0)
        self.detailed_report_file = ''



    def get_jun_index(self):
        return self.jun_index

    def get_junction_data_as_list(self):
        return [self.jun_index, self.name, self.invert_elevation, self.height, self.additional_pressure, self.ponded_surface]

    def get_all_selected_pars(self):

        list_of_selected_pars = []

        for parameter in self.get_jun_data_as_list():

            if parameter.check_if_selected_for_estimation():
                print(parameter.name)
                print('get_all_selected_pars')
                list_of_selected_pars.append(parameter)

        print("List of selected pars: ")
        print(list_of_selected_pars)

        return list_of_selected_pars