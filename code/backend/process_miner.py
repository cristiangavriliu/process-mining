import os

import graphviz
import pm4py

from a_miner import *


def process_miner(file, algorithm):
    """ Process miner function:
        Input:  File name and name of Discovery algorithm
        Logic:  1. Reads the file and filters the data into a simple activity log [list]
                2. Calls the correct function depending on the inputted algorithm
        Output: Gives back the printer log which is provided by the algorithm function """

    # this code part converts the xes file info a double list that shows all activities
    event_log = pm4py.read_xes(os.path.join(os.path.dirname(__file__), os.pardir, 'frontend', 'uploads', file))
    activity_log = []

    # filters the activities into a list
    for case in event_log:
        case_log = []

        for trace in case:
            if "lifecycle" not in trace or trace["lifecycle:transition"] == "complete":
                case_log.append(trace["concept:name"])
        activity_log.append(case_log)

    # console output for debugging purposes
    print("The activity log for " + file + " is : " + str(activity_log))

    if algorithm == "α-algorithm":
        pl, transitions, fl, printer = a_miner(activity_log)
        create_petri_net(pl, transitions, fl)
        return printer
    else:
        print("b-miner")


def create_petri_net(places, transitions, flow):
    """Creates a Petri net graph from the given places, transitions and flow.
        Input:  places (set): Set of places
                transitions (set): Set of transitions
                flow (set): Set of flow.
        Logic: Creates 2 petri_net graphs with the given input( one with place labels one without)
                Saves the 2 graphs to the frontend"""
    # Initialize the Petri net graph
    petri_net = graphviz.Digraph(name='Petri_Net', format='png')
    petri_net.graph_attr["rankdir"] = "LR"
    petri_net.graph_attr["sep"] = "5"
    petri_net.edge_attr.update(arrowhead='vee')

    # copy petri net in order to create the same graph just without lables
    petri_net_simple = petri_net.copy()

    # Add places to the Petri net
    for place in places:
        if place == 'start':
            petri_net.node(str(place), "", xlabel="iL", shape='point', color='darkgreen', width='0.2', height='0.2')
            petri_net_simple.node(str(place), "", shape='point', color='darkgreen', width='0.2', height='0.2')

        elif place == 'end':
            petri_net.node(str(place), "", xlabel="oL", shape='doublecircle', color='darkred', width='0.1',
                           height='0.1')
            petri_net_simple.node(str(place), "", shape='doublecircle', color='darkred', width='0.1',
                                  height='0.1')

        else:
            petri_net.node(str(place), "", xlabel="p" + str(place).replace("'", ""), shape='circle',
                           width='0.2', height='0.2')
            petri_net_simple.node(str(place), "", shape='circle',
                                  width='0.2', height='0.2')

    # Add transitions to the Petri net
    for transition in transitions:
        petri_net.node(str(transition), shape='box')
        petri_net_simple.node(str(transition), shape='box')

    # Add arcs to the Petri net
    for arc in flow:
        petri_net.edge(str(arc[0]), str(arc[1]))
        petri_net_simple.edge(str(arc[0]), str(arc[1]))
    petri_net.render(os.path.join(os.path.dirname(__file__), os.pardir, 'frontend', 'web', 'static', 'img', 'petrinet'),
                     view=False)
    petri_net_simple.render(
        os.path.join(os.path.dirname(__file__), os.pardir, 'frontend', 'web', 'static', 'img', 'petrinet_simp'),
        view=False)
