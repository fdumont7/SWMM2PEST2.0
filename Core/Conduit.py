# Conduit.py
#
# Project: SWMM2PEST
# Version: 3.0
# Date:   03/11/2021 (version 3.0; author: F.Dumont)
#
# Class type for Conduits and all its parameters as variables


"""
· identities of the inlet and outlet nodes
· offset height or elevation above the inlet and outlet node inverts
· conduit length
· Manning's roughness coefficient
· cross-section shape and dimensions.
"""
from Core.Subcatchments import DataField
class Conduit():

    def __init__(self, con_index, name):
        self.con_index = con_index
        self.name = name

        self.mannings_roughness = DataField('mannings_roughness', "Mannings_Roughness", self.name, index=0)
        self.inlet_height = DataField('inlet_height', "Inlet_Height",self.name, index = 0)
        self.outlet_height = DataField('outlet_height', "Outlet_Height", self.name, index=0)
        self.init_flow = DataField('init_flow', "Init_Flow", self.name, index = 0)
        self.max_flow = DataField('max_flow', "Max_Flow", self.name, index=0)


        self.detailed_report_file = ''



    def get_con_index(self):
        return self.con_index

    def get_conduit_data_as_list(self):
        return [self.mannings_roughness,self.inlet_height,self.outlet_height,self.init_flow,self.max_flow]

    def get_all_selected_pars(self):

        list_of_selected_pars = []

        for parameter in self.get_conduit_data_as_list():

            if parameter.check_if_selected_for_estimation():
                print(parameter.name)
                print('get_all_selected_pars')
                list_of_selected_pars.append(parameter)

        print("List of selected pars: ")
        print(list_of_selected_pars)

        return list_of_selected_pars