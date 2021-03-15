# Outfall.py
#
# Project: SWMM2PEST
# Version: 3.0
# Date:   03/11/2021 (version 3.0; author: F.Dumont)
#
# Class type for Outfalls and all its parameters as variables


"""
 · invert elevation
· type of boundary condition and its associated stage data
· presence of a flap gate to prevent backflow through the outfall.

"""
from Core.Subcatchments import DataField
class Outfall():

    def __init__(self, outfall_index, name):
        self.outfall_index = outfall_index
        self.name = name

        self.invert_elevation = DataField('invert_elevation', "Invert_Elevation",self.name, index = 0)

        self.detailed_report_file = ''



    def get_outfall_index(self):
        return self.outfall_index

    def get_outfall_data_as_list(self):
        return [self.invert_elevation]

    def get_all_selected_pars(self):

        list_of_selected_pars = []

        for parameter in self.get_outfall_data_as_list():

            if parameter.check_if_selected_for_estimation():
                print(parameter.name)
                print('get_all_selected_pars')
                list_of_selected_pars.append(parameter)

        print("List of selected pars: ")
        print(list_of_selected_pars)

        return list_of_selected_pars