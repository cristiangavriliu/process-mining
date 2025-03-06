from unittest import TestCase

import pm4py

from backend.a_miner import *


# parser that goes through teh event log
def filter_log(event_log):
    activity_log = []

    # filters the activities into a list
    for case in event_log:
        case_log = []

        for trace in case:
            if "lifecycle" not in trace or trace["lifecycle:transition"] == "complete":
                case_log.append(trace["concept:name"])
        activity_log.append(case_log)
    return activity_log


# helper function to format a miner output
def format_to_list(log):
    log_list = []
    for relation in log:
        log_list.append((set(relation[0]), set(relation[1])))
    return log_list


# Unit Tests for each step of the Alpha miner implemented in backend/
class Test(TestCase):
    # initialise event logs as constants for all test sets
    L1_event_log = pm4py.read_xes("../frontend/uploads/datasets/L1.xes")
    L2_event_log = pm4py.read_xes("../frontend/uploads/datasets/L2.xes")
    L3_event_log = pm4py.read_xes("../frontend/uploads/datasets/L3.xes")
    L4_event_log = pm4py.read_xes("../frontend/uploads/datasets/L4.xes")
    L5_event_log = pm4py.read_xes("../frontend/uploads/datasets/L5.xes")
    L6_event_log = pm4py.read_xes("../frontend/uploads/datasets/L6.xes")
    L7_event_log = pm4py.read_xes("../frontend/uploads/datasets/L7.xes")
    billinstances_event_log = pm4py.read_xes("../frontend/uploads/datasets/billinstances.xes")
    flyerinstances_event_log = pm4py.read_xes("../frontend/uploads/datasets/flyerinstances.xes")
    posterinstance_event_log = pm4py.read_xes("../frontend/uploads/datasets/posterinstances.xes")
    running_example_event_log = pm4py.read_xes("../frontend/uploads/datasets/running-example.xes")

    # parse through all tests sets and save them as constants
    L1_activity_log = filter_log(L1_event_log)
    L2_activity_log = filter_log(L2_event_log)
    L3_activity_log = filter_log(L3_event_log)
    L4_activity_log = filter_log(L4_event_log)
    L5_activity_log = filter_log(L5_event_log)
    L6_activity_log = filter_log(L6_event_log)
    L7_activity_log = filter_log(L7_event_log)
    billinstances_activity_log = filter_log(billinstances_event_log)
    flyerinstances_activity_log = filter_log(flyerinstances_event_log)
    posterinstance_activity_log = filter_log(posterinstance_event_log)
    running_example_activity_log = filter_log(running_example_event_log)

    # Formatted PM4PY output for L1
    L1_S1 = {'c', 'b', 'e', 'd', 'a'}
    L1_S2 = {'a'}
    L1_S3 = {'d'}
    L1_S4 = [({'a'}, {'e'}), ({'e'}, {'d'}), ({'a'}, {'c'}), ({'b'}, {'d'}), ({'a'}, {'b'}), ({'c'}, {'d'}),
             ({'a'}, {'e', 'c'}), ({'a'}, {'b', 'e'}), ({'b', 'e'}, {'d'}), ({'e', 'c'}, {'d'})]
    L1_S5 = [({'a'}, {'e', 'c'}), ({'a'}, {'b', 'e'}), ({'b', 'e'}, {'d'}), ({'e', 'c'}, {'d'})]
    L1_S6 = [({'a'}, {'b', 'e'}), ({'a'}, {'c', 'e'}), ({'b', 'e'}, {'d'}), ({'c', 'e'}, {'d'}), 'start', 'end']
    L1_S7 = [('start', 'a'), ('d', 'end'), ('a', ({"a"}, {"b", "e"})), (({'a'}, {'b', 'e'}), 'b'),
             (({'a'}, {'b', 'e'}), 'e'), ('a', ({"a"}, {"c", "e"})), (({'a'}, {'c', 'e'}), 'c'),
             (({'a'}, {'c', 'e'}), 'e'), ('b', ({'b', 'e'}, {'d'})), ('e', ({'b', 'e'}, {'d'})),
             (({'b', 'e'}, {'d'}), 'd'), ('c', ({'c', 'e'}, {'d'})), ('e', ({'c', 'e'}, {'d'})),
             (({'c', 'e'}, {'d'}), 'd')]

    # Formatted PM4PY output for L2
    L2_S1 = {'c', 'b', 'e', 'd', 'f', 'a'}
    L2_S2 = {'a'}
    L2_S3 = {'d'}
    L2_S4 = [({'a'}, {'c'}), ({'b'}, {'d'}), ({'b'}, {'e'}), ({'e'}, {'f'}), ({'f'}, {'b'}), ({'c'}, {'d'}),
             ({'a'}, {'b'}), ({'c'}, {'e'}), ({'f'}, {'c'}), ({'f', 'a'}, {'c'}), ({'b'}, {'e', 'd'}),
             ({'f', 'a'}, {'b'}), ({'c'}, {'e', 'd'})]
    L2_S5 = [({'e'}, {'f'}), ({'f', 'a'}, {'c'}), ({'b'}, {'e', 'd'}), ({'f', 'a'}, {'b'}), ({'c'}, {'e', 'd'})]
    L2_S6 = [({'b'}, {'d', 'e'}),
             ({'c'}, {'d', 'e'}),
             ({'e'}, {'f'}),
             ({'a', 'f'}, {'b'}),
             ({'a', 'f'}, {'c'}),
             'start',
             'end']
    L2_S7 = [('start', 'a'), ('d', 'end'), ('b', ({"b"}, {"d", "e"})), (({'b'}, {'d', 'e'}), 'd'),
             (({'b'}, {'d', 'e'}), 'e'), ('c', ({"c"}, {"d", "e"})), (({'c'}, {'d', 'e'}), 'd'),
             (({'c'}, {'d', 'e'}), 'e'), ('e', ({"e"}, {"f"})), (({'e'}, {'f'}), 'f'), ('a', ({"a", "f"}, {"b"})),
             ('f', ({"a", "f"}, {"b"})), (({'a', 'f'}, {'b'}), 'b'), ('a', ({"a", "f"}, {"c"})),
             ('f', ({"a", "f"}, {"c"})), (({'a', 'f'}, {'c'}), 'c')]

    # Formatted PM4PY output for L3
    L3_S1 = {'g', 'c', 'b', 'e', 'd', 'f', 'a'}
    L3_S2 = {'a'}
    L3_S3 = {'g'}
    L3_S4 = [({'a'}, {'b'}), ({'b'}, {'c'}), ({'d'}, {'e'}), ({'e'}, {'f'}), ({'f'}, {'b'}), ({'b'}, {'d'}),
             ({'c'}, {'e'}), ({'e'}, {'g'}), ({'f', 'a'}, {'b'}), ({'e'}, {'f', 'g'})]
    L3_S5 = [({'b'}, {'c'}), ({'d'}, {'e'}), ({'b'}, {'d'}), ({'c'}, {'e'}), ({'f', 'a'}, {'b'}), ({'e'}, {'f', 'g'})]
    L3_S6 = [({'b'}, {'c'}), ({'b'}, {'d'}), ({'c'}, {'e'}), ({'d'}, {'e'}), ({'e'}, {'f', 'g'}), ({'a', 'f'}, {'b'}),
             'start', 'end']
    L3_S7 = [('start', 'a'), ('g', 'end'), ('b', ({"b"}, {"c"})), (({'b'}, {'c'}), 'c'), ('b', ({"b"}, {"d"})),
             (({'b'}, {'d'}), 'd'), ('c', ({"c"}, {"e"})), (({'c'}, {'e'}), 'e'), ('d', ({"d"}, {"e"})),
             (({'d'}, {'e'}), 'e'), ('e', ({"e"}, {"f", "g"})), (({'e'}, {'f', 'g'}), 'f'), (({'e'}, {'f', 'g'}), 'g'),
             ('a', ({"a", "f"}, {"b"})), ('f', ({"a", "f"}, {"b"})), (({'a', 'f'}, {'b'}), 'b')]

    # Formatted PM4PY output for L4
    L4_S1 = {'c', 'b', 'e', 'd', 'a'}
    L4_S2 = {'a', 'b'}
    L4_S3 = {'d', 'e'}
    L4_S4 = [({'a'}, {'c'}), ({'c'}, {'d'}), ({'b'}, {'c'}), ({'c'}, {'e'}), ({'b', 'a'}, {'c'}), ({'c'}, {'e', 'd'})]
    L4_S5 = [({'b', 'a'}, {'c'}), ({'c'}, {'e', 'd'})]
    L4_S6 = [({'c'}, {'d', 'e'}), ({'a', 'b'}, {'c'}), 'start', 'end']
    L4_S7 = [('start', 'a'), ('start', 'b'), ('d', 'end'), ('e', 'end'), ('c', ({"c"}, {"d", "e"})),
             (({"c"}, {"d", "e"}), 'd'), (({"c"}, {"d", "e"}), 'e'), ('a', ({"a", "b"}, {"c"})),
             ('b', ({"a", "b"}, {"c"})), (({"a", "b"}, {"c"}), 'c')]

    # Formatted PM4PY output for L5
    L5_S1 = {'c', 'b', 'e', 'd', 'f', 'a'}
    L5_S2 = {'a'}
    L5_S3 = {'f'}
    L5_S4 = [({'a'}, {'b'}), ({'c'}, {'d'}), ({'d'}, {'b'}), ({'b'}, {'f'}), ({'a'}, {'e'}), ({'b'}, {'c'}),
             ({'e'}, {'f'}), ({'d', 'a'}, {'b'}), ({'b'}, {'f', 'c'})]
    L5_S5 = [({'c'}, {'d'}), ({'a'}, {'e'}), ({'e'}, {'f'}), ({'d', 'a'}, {'b'}), ({'b'}, {'f', 'c'})]
    L5_S6 = [({'a'}, {'e'}), ({'b'}, {'c', 'f'}), ({'c'}, {'d'}), ({'e'}, {'f'}), ({'a', 'd'}, {'b'}), 'start', 'end']
    L5_S7 = [('start', 'a'), ('f', 'end'), ('a', ({'a', 'd'}, {'b'})), ('a', ({'a'}, {'e'})), ('c', ({'c'}, {'d'})), ('e', ({'e'}, {'f'})), ('d', ({'a', 'd'}, {'b'})), ('b', ({'b'}, {'f', 'c'})), (({'b'}, {'f', 'c'}), 'c'), (({'a'}, {'e'}), 'e'), (({'c'}, {'d'}), 'd'), (({'a', 'd'}, {'b'}), 'b'), (({'b'}, {'f', 'c'}), 'f'), (({'e'}, {'f'}), 'f')]

    # Formatted PM4PY output for L6
    L6_S1 = {'g', 'c', 'b', 'e', 'd', 'f', 'a'}
    L6_S2 = {'a', 'b'}
    L6_S3 = {'g'}
    L6_S4 = [({'b'}, {'f'}), ({'d'}, {'g'}), ({'b'}, {'d'}), ({'f'}, {'g'}), ({'a'}, {'e'}), ({'c'}, {'g'}),
             ({'a'}, {'c'}), ({'e'}, {'g'}), ({'d', 'c'}, {'g'}), ({'e', 'd'}, {'g'}), ({'f', 'c'}, {'g'}),
             ({'e', 'f'}, {'g'})]
    L6_S5 = [({'b'}, {'f'}), ({'b'}, {'d'}), ({'a'}, {'e'}), ({'a'}, {'c'}), ({'d', 'c'}, {'g'}), ({'e', 'd'}, {'g'}),
             ({'f', 'c'}, {'g'}), ({'e', 'f'}, {'g'})]
    L6_S6 = [({'a'}, {'c'}), ({'a'}, {'e'}), ({'b'}, {'d'}), ({'b'}, {'f'}), ({'c', 'd'}, {'g'}), ({'d', 'e'}, {'g'}),
             ({'c', 'f'}, {'g'}), ({'e', 'f'}, {'g'}), 'start', 'end']
    L6_S7 = [('start', 'b'), ('start', 'a'), ('g', 'end'), ('d', ({'d', 'c'}, {'g'})), ('d', ({'d', 'e'}, {'g'})), ('f', ({'f', 'e'}, {'g'})), ('f', ({'f', 'c'}, {'g'})), ('e', ({'f', 'e'}, {'g'})), ('e', ({'d', 'e'}, {'g'})), ('c', ({'d', 'c'}, {'g'})), ('c', ({'f', 'c'}, {'g'})), ('b', ({'b'}, {'d'})), ('b', ({'b'}, {'f'})), ('a', ({'a'}, {'c'})), ('a', ({'a'}, {'e'})), (({'b'}, {'d'}), 'd'), (({'b'}, {'f'}), 'f'), (({'a'}, {'e'}), 'e'), (({'a'}, {'c'}), 'c'), (({'f', 'e'}, {'g'}), 'g'), (({'d', 'c'}, {'g'}), 'g'), (({'f', 'c'}, {'g'}), 'g'), (({'d', 'e'}, {'g'}), 'g')]

    # Formatted PM4PY output for L7
    L7_S1 = {'b', 'a', 'c'}
    L7_S2 = {'a'}
    L7_S3 = {'c'}
    L7_S4 = [({'a'}, {'c'})]
    L7_S5 = [({'a'}, {'c'})]
    L7_S6 = [({'a'}, {'c'}), 'start', 'end']
    L7_S7 = [('start', 'a'), ('c', 'end'), ('a', ({'a'}, {'c'})), (({'a'}, {'c'}), 'c')]

    # Formatted PM4PY output for billinstances
    billinstances_S1 = {'write bill', 'deliver bill', 'print bill'}
    billinstances_S2 = {'write bill'}
    billinstances_S3 = {'deliver bill'}
    billinstances_S4 = [({'print bill'}, {'deliver bill'}), ({'write bill'}, {'print bill'})]
    billinstances_S5 = [({'print bill'}, {'deliver bill'}), ({'write bill'}, {'print bill'})]
    billinstances_S6 = [({'print bill'}, {'deliver bill'}), ({'write bill'}, {'print bill'}), 'start', 'end']
    billinstances_S7 = [('start', 'write bill'), ('deliver bill', 'end'), ('print bill', ({'print bill'}, {'deliver bill'})), ('write bill', ({'write bill'}, {'print bill'})), (({'print bill'}, {'deliver bill'}), 'deliver bill'), (({'write bill'}, {'print bill'}), 'print bill')]

    # Formatted PM4PY output for flyerinstances
    flyerinstances_S1 = {'receive flyer order', 'design flyer', 'deliver flyer', 'send draft to customer',
                         'print flyer'}
    flyerinstances_S2 = {'receive flyer order'}
    flyerinstances_S3 = {'deliver flyer'}
    flyerinstances_S4 = [({'print flyer'}, {'deliver flyer'}), ({'send draft to customer'}, {'print flyer'}),
                         ({'receive flyer order'}, {'design flyer'})]
    flyerinstances_S5 = [({'send draft to customer'}, {'print flyer'}), ({'receive flyer order'}, {'design flyer'}),
                         ({'print flyer'}, {'deliver flyer'})]
    flyerinstances_S6 = [({'print flyer'}, {'deliver flyer'}), ({'receive flyer order'}, {'design flyer'}),
                         ({'send draft to customer'}, {'print flyer'}), 'start', 'end']

    flyerinstances_S7 = [('start', 'receive flyer order'), ('deliver flyer', 'end'), ('send draft to customer', ({'send draft to customer'}, {'print flyer'})), ('print flyer', ({'print flyer'}, {'deliver flyer'})), ('receive flyer order', ({'receive flyer order'}, {'design flyer'})), (({'send draft to customer'}, {'print flyer'}), 'print flyer'), (({'print flyer'}, {'deliver flyer'}), 'deliver flyer'), (({'receive flyer order'}, {'design flyer'}), 'design flyer')]

    # Formatted PM4PY output for posterinstance
    posterinstance_S1 = {'deliver poster', 'receive order and photo', 'design photo poster', 'print poster'}
    posterinstance_S2 = {'receive order and photo'}
    posterinstance_S3 = {'deliver poster'}
    posterinstance_S4 = [({'design photo poster'}, {'print poster'}), ({'print poster'}, {'deliver poster'}),
                         ({'receive order and photo'}, {'design photo poster'})]
    posterinstance_S5 = [({'print poster'}, {'deliver poster'}), ({'design photo poster'}, {'print poster'}),
                         ({'receive order and photo'}, {'design photo poster'})]
    posterinstance_S6 = [({'design photo poster'}, {'print poster'}), ({'print poster'}, {'deliver poster'}),
                         ({'receive order and photo'}, {'design photo poster'}), 'start', 'end']
    posterinstance_S7 = [('start', 'receive order and photo'), ('deliver poster', 'end'), ('print poster', ({'print poster'}, {'deliver poster'})), ('receive order and photo', ({'receive order and photo'}, {'design photo poster'})), ('design photo poster', ({'design photo poster'}, {'print poster'})), (({'print poster'}, {'deliver poster'}), 'deliver poster'), (({'design photo poster'}, {'print poster'}), 'print poster'), (({'receive order and photo'}, {'design photo poster'}), 'design photo poster')]

    # Formatted PM4PY output for running_example
    running_example_S1 = {'register request', 'examine thoroughly', 'examine casually', 'decide', 'reinitiate request',
                          'check ticket', 'pay compensation', 'reject request'}
    running_example_S2 = {'register request'}
    running_example_S3 = {'pay compensation', 'reject request'}
    running_example_S4 = [({'decide'}, {'pay compensation', 'reinitiate request', 'reject request'}),
                          ({'decide'}, {'reinitiate request', 'reject request'}),
                          ({'register request'}, {'examine thoroughly', 'examine casually'}),
                          ({'reinitiate request'}, {'examine thoroughly'}),
                          ({'reinitiate request', 'register request'}, {'check ticket'}),
                          ({'check ticket'}, {'decide'}), ({'decide'}, {'reinitiate request'}),
                          ({'decide'}, {'pay compensation', 'reject request'}),
                          ({'register request'}, {'check ticket'}),
                          ({'reinitiate request', 'register request'}, {'examine thoroughly'}),
                          ({'decide'}, {'pay compensation'}), ({'register request'}, {'examine thoroughly'}),
                          ({'reinitiate request'}, {'examine casually'}),
                          ({'decide'}, {'pay compensation', 'reinitiate request'}), ({'examine casually'}, {'decide'}),
                          ({'decide'}, {'reject request'}),
                          ({'reinitiate request', 'register request'}, {'examine casually'}),
                          ({'examine thoroughly', 'examine casually'}, {'decide'}),
                          ({'register request'}, {'examine casually'}),
                          ({'reinitiate request'}, {'examine thoroughly', 'examine casually'}),
                          ({'examine thoroughly'}, {'decide'}), ({'reinitiate request'}, {'check ticket'}),
                          ({'reinitiate request', 'register request'}, {'examine thoroughly', 'examine casually'})]
    running_example_S5 = [({'examine casually', 'examine thoroughly'}, {'decide'}),
                          ({'register request', 'reinitiate request'}, {'check ticket'}),
                          ({'decide'}, {'reinitiate request', 'reject request', 'pay compensation'}),
                          ({'register request', 'reinitiate request'}, {'examine casually', 'examine thoroughly'}),
                          ({'check ticket'}, {'decide'})]
    running_example_S6 = [({'check ticket'}, {'decide'}),
                          ({'decide'}, {'pay compensation', 'reinitiate request', 'reject request'}),
                          ({'examine casually', 'examine thoroughly'}, {'decide'}),
                          ({'register request', 'reinitiate request'}, {'check ticket'}),
                          ({'register request', 'reinitiate request'}, {'examine casually', 'examine thoroughly'}),
                          'start', 'end']

    running_example_S7 = [('start', 'register request'), ('pay compensation', 'end'), ('reject request', 'end'), ('examine casually', ({'examine casually', 'examine thoroughly'}, {'decide'})), ('register request', ({'reinitiate request', 'register request'}, {'check ticket'})), ('register request', ({'reinitiate request', 'register request'}, {'examine casually', 'examine thoroughly'})), ('decide', ({'decide'}, {'reject request', 'pay compensation', 'reinitiate request'})), ('check ticket', ({'check ticket'}, {'decide'})), ('examine thoroughly', ({'examine casually', 'examine thoroughly'}, {'decide'})), ('reinitiate request', ({'reinitiate request', 'register request'}, {'check ticket'})), ('reinitiate request', ({'reinitiate request', 'register request'}, {'examine casually', 'examine thoroughly'})), (({'reinitiate request', 'register request'}, {'examine casually', 'examine thoroughly'}), 'examine casually'), (({'decide'}, {'reject request', 'pay compensation', 'reinitiate request'}), 'reject request'), (({'examine casually', 'examine thoroughly'}, {'decide'}), 'decide'), (({'check ticket'}, {'decide'}), 'decide'), (({'reinitiate request', 'register request'}, {'check ticket'}), 'check ticket'), (({'reinitiate request', 'register request'}, {'examine casually', 'examine thoroughly'}), 'examine thoroughly'), (({'decide'}, {'reject request', 'pay compensation', 'reinitiate request'}), 'pay compensation'), (({'decide'}, {'reject request', 'pay compensation', 'reinitiate request'}), 'reinitiate request')]

    # set up function that runs before each test, initiates the compare values for the step you want to test
    def _setUp(self, step):

        # Step 1
        if step == 1:
            self.L1_compare = a_miner_step_1(Test.L1_activity_log)
            self.L2_compare = a_miner_step_1(Test.L2_activity_log)
            self.L3_compare = a_miner_step_1(Test.L3_activity_log)
            self.L4_compare = a_miner_step_1(Test.L4_activity_log)
            self.L5_compare = a_miner_step_1(Test.L5_activity_log)
            self.L6_compare = a_miner_step_1(Test.L6_activity_log)
            self.L7_compare = a_miner_step_1(Test.L7_activity_log)
            self.billinstances_compare = a_miner_step_1(Test.billinstances_activity_log)
            self.flyerinstances_compare = a_miner_step_1(Test.flyerinstances_activity_log)
            self.posterinstance_compare = a_miner_step_1(Test.posterinstance_activity_log)
            self.running_example_compare = a_miner_step_1(Test.running_example_activity_log)
        elif step == 2:
            self.L1_compare = a_miner_step_2(Test.L1_activity_log)
            self.L2_compare = a_miner_step_2(Test.L2_activity_log)
            self.L3_compare = a_miner_step_2(Test.L3_activity_log)
            self.L4_compare = a_miner_step_2(Test.L4_activity_log)
            self.L5_compare = a_miner_step_2(Test.L5_activity_log)
            self.L6_compare = a_miner_step_2(Test.L6_activity_log)
            self.L7_compare = a_miner_step_2(Test.L7_activity_log)
            self.billinstances_compare = a_miner_step_2(Test.billinstances_activity_log)
            self.flyerinstances_compare = a_miner_step_2(Test.flyerinstances_activity_log)
            self.posterinstance_compare = a_miner_step_2(Test.posterinstance_activity_log)
            self.running_example_compare = a_miner_step_2(Test.running_example_activity_log)
        elif step == 3:
            self.L1_compare = a_miner_step_3(Test.L1_activity_log)
            self.L2_compare = a_miner_step_3(Test.L2_activity_log)
            self.L3_compare = a_miner_step_3(Test.L3_activity_log)
            self.L4_compare = a_miner_step_3(Test.L4_activity_log)
            self.L5_compare = a_miner_step_3(Test.L5_activity_log)
            self.L6_compare = a_miner_step_3(Test.L6_activity_log)
            self.L7_compare = a_miner_step_3(Test.L7_activity_log)
            self.billinstances_compare = a_miner_step_3(Test.billinstances_activity_log)
            self.flyerinstances_compare = a_miner_step_3(Test.flyerinstances_activity_log)
            self.posterinstance_compare = a_miner_step_3(Test.posterinstance_activity_log)
            self.running_example_compare = a_miner_step_3(Test.running_example_activity_log)

        elif step == 4:
            self.L1_compare = format_to_list(
                a_miner_step_4(Test.L1_activity_log, a_miner_step_1(Test.L1_activity_log))[0])
            self.L2_compare = format_to_list(
                a_miner_step_4(Test.L2_activity_log, a_miner_step_1(Test.L2_activity_log))[0])
            self.L3_compare = format_to_list(
                a_miner_step_4(Test.L3_activity_log, a_miner_step_1(Test.L3_activity_log))[0])
            self.L4_compare = format_to_list(
                a_miner_step_4(Test.L4_activity_log, a_miner_step_1(Test.L4_activity_log))[0])
            self.L5_compare = format_to_list(
                a_miner_step_4(Test.L5_activity_log, a_miner_step_1(Test.L5_activity_log))[0])
            self.L6_compare = format_to_list(
                a_miner_step_4(Test.L6_activity_log, a_miner_step_1(Test.L6_activity_log))[0])
            self.L7_compare = format_to_list(
                a_miner_step_4(Test.L7_activity_log, a_miner_step_1(Test.L7_activity_log))[0])
            self.billinstances_compare = format_to_list(a_miner_step_4(Test.billinstances_activity_log,
                                                                       a_miner_step_1(Test.billinstances_activity_log))[
                                                            0])
            self.flyerinstances_compare = format_to_list(a_miner_step_4(Test.flyerinstances_activity_log,
                                                                        a_miner_step_1(
                                                                            Test.flyerinstances_activity_log))[0])
            self.posterinstance_compare = format_to_list(a_miner_step_4(Test.posterinstance_activity_log,
                                                                        a_miner_step_1(
                                                                            Test.posterinstance_activity_log))[0])
            self.running_example_compare = format_to_list(a_miner_step_4(Test.running_example_activity_log,
                                                                         a_miner_step_1(
                                                                             Test.running_example_activity_log))[0])
        elif step == 5:
            self.L1_compare = a_miner_step_5(
                a_miner_step_4(Test.L1_activity_log, a_miner_step_1(Test.L1_activity_log))[0])
            self.L2_compare = a_miner_step_5(
                a_miner_step_4(Test.L2_activity_log, a_miner_step_1(Test.L2_activity_log))[0])
            self.L3_compare = a_miner_step_5(
                a_miner_step_4(Test.L3_activity_log, a_miner_step_1(Test.L3_activity_log))[0])
            self.L4_compare = a_miner_step_5(
                a_miner_step_4(Test.L4_activity_log, a_miner_step_1(Test.L4_activity_log))[0])
            self.L5_compare = a_miner_step_5(
                a_miner_step_4(Test.L5_activity_log, a_miner_step_1(Test.L5_activity_log))[0])
            self.L6_compare = a_miner_step_5(
                a_miner_step_4(Test.L6_activity_log, a_miner_step_1(Test.L6_activity_log))[0])
            self.L7_compare = a_miner_step_5(
                a_miner_step_4(Test.L7_activity_log, a_miner_step_1(Test.L7_activity_log))[0])
            self.billinstances_compare = a_miner_step_5(a_miner_step_4(Test.billinstances_activity_log,
                                                                       a_miner_step_1(
                                                                           Test.billinstances_activity_log))[0])
            self.flyerinstances_compare = a_miner_step_5(a_miner_step_4(Test.flyerinstances_activity_log,
                                                                        a_miner_step_1(
                                                                            Test.flyerinstances_activity_log))[0])
            self.posterinstance_compare = a_miner_step_5(a_miner_step_4(Test.posterinstance_activity_log,
                                                                        a_miner_step_1(
                                                                            Test.posterinstance_activity_log))[0])
            self.running_example_compare = a_miner_step_5(a_miner_step_4(Test.running_example_activity_log,
                                                                         a_miner_step_1(
                                                                             Test.running_example_activity_log))[0])
        elif step == 6:
            self.L1_compare = a_miner_step_6(
                a_miner_step_5(a_miner_step_4(Test.L1_activity_log, a_miner_step_1(Test.L1_activity_log))[0]))
            self.L2_compare = a_miner_step_6(
                a_miner_step_5(a_miner_step_4(Test.L2_activity_log, a_miner_step_1(Test.L2_activity_log))[0]))
            self.L3_compare = a_miner_step_6(
                a_miner_step_5(a_miner_step_4(Test.L3_activity_log, a_miner_step_1(Test.L3_activity_log))[0]))
            self.L4_compare = a_miner_step_6(
                a_miner_step_5(a_miner_step_4(Test.L4_activity_log, a_miner_step_1(Test.L4_activity_log))[0]))
            self.L5_compare = a_miner_step_6(
                a_miner_step_5(a_miner_step_4(Test.L5_activity_log, a_miner_step_1(Test.L5_activity_log))[0]))
            self.L6_compare = a_miner_step_6(
                a_miner_step_5(a_miner_step_4(Test.L6_activity_log, a_miner_step_1(Test.L6_activity_log))[0]))
            self.L7_compare = a_miner_step_6(
                a_miner_step_5(a_miner_step_4(Test.L7_activity_log, a_miner_step_1(Test.L7_activity_log))[0]))
            self.billinstances_compare = a_miner_step_6(
                a_miner_step_5(a_miner_step_4(Test.billinstances_activity_log,
                                              a_miner_step_1(
                                                  Test.billinstances_activity_log))[0]))
            self.flyerinstances_compare = a_miner_step_6(
                a_miner_step_5(a_miner_step_4(Test.flyerinstances_activity_log,
                                              a_miner_step_1(
                                                  Test.flyerinstances_activity_log))[0]))
            self.posterinstance_compare = a_miner_step_6(
                a_miner_step_5(a_miner_step_4(Test.posterinstance_activity_log,
                                              a_miner_step_1(
                                                  Test.posterinstance_activity_log))[0]))
            self.running_example_compare = a_miner_step_6(
                a_miner_step_5(a_miner_step_4(Test.running_example_activity_log,
                                              a_miner_step_1(
                                                  Test.running_example_activity_log))[0]))
        elif step == 7:
            self.L1_compare = a_miner_step_7(
                a_miner_step_5(a_miner_step_4(Test.L1_activity_log, a_miner_step_1(Test.L1_activity_log))[0]),
                a_miner_step_1(Test.L2_activity_log), a_miner_step_2(Test.L2_activity_log),
                a_miner_step_3(Test.L2_activity_log))
            self.L2_compare = a_miner_step_7(
                a_miner_step_5(a_miner_step_4(Test.L2_activity_log, a_miner_step_1(Test.L2_activity_log))[0]),
                a_miner_step_1(Test.L2_activity_log), a_miner_step_2(Test.L2_activity_log),
                a_miner_step_3(Test.L2_activity_log))
            self.L3_compare = a_miner_step_7(
                a_miner_step_5(a_miner_step_4(Test.L3_activity_log, a_miner_step_1(Test.L3_activity_log))[0]),
                a_miner_step_1(Test.L3_activity_log), a_miner_step_2(Test.L3_activity_log),
                a_miner_step_3(Test.L3_activity_log))
            self.L4_compare = a_miner_step_7(
                a_miner_step_5(a_miner_step_4(Test.L4_activity_log, a_miner_step_1(Test.L4_activity_log))[0]),
                a_miner_step_1(Test.L4_activity_log), a_miner_step_2(Test.L4_activity_log),
                a_miner_step_3(Test.L4_activity_log))
            self.L5_compare = a_miner_step_7(
                a_miner_step_5(a_miner_step_4(Test.L5_activity_log, a_miner_step_1(Test.L5_activity_log))[0]),
                a_miner_step_1(Test.L5_activity_log), a_miner_step_2(Test.L5_activity_log),
                a_miner_step_3(Test.L5_activity_log))
            self.L6_compare = a_miner_step_7(
                a_miner_step_5(a_miner_step_4(Test.L6_activity_log, a_miner_step_1(Test.L6_activity_log))[0]),
                a_miner_step_1(Test.L6_activity_log), a_miner_step_2(Test.L6_activity_log),
                a_miner_step_3(Test.L6_activity_log))
            self.L7_compare = a_miner_step_7(
                a_miner_step_5(a_miner_step_4(Test.L7_activity_log, a_miner_step_1(Test.L7_activity_log))[0]),
                a_miner_step_1(Test.L7_activity_log), a_miner_step_2(Test.L7_activity_log),
                a_miner_step_3(Test.L7_activity_log))
            self.billinstances_compare = a_miner_step_7(
                a_miner_step_5(a_miner_step_4(Test.billinstances_activity_log,
                                              a_miner_step_1(
                                                  Test.billinstances_activity_log))[0]),
                a_miner_step_1(Test.billinstances_activity_log), a_miner_step_2(Test.billinstances_activity_log),
                a_miner_step_3(Test.billinstances_activity_log))
            self.flyerinstances_compare = a_miner_step_7(
                a_miner_step_5(a_miner_step_4(Test.flyerinstances_activity_log,
                                              a_miner_step_1(
                                                  Test.flyerinstances_activity_log))[0]),
                a_miner_step_1(Test.flyerinstances_activity_log),
                a_miner_step_2(Test.flyerinstances_activity_log), a_miner_step_3(Test.flyerinstances_activity_log))
            self.posterinstance_compare = a_miner_step_7(
                a_miner_step_5(a_miner_step_4(Test.posterinstance_activity_log,
                                              a_miner_step_1(
                                                  Test.posterinstance_activity_log))[0]),
                a_miner_step_1(Test.posterinstance_activity_log), a_miner_step_2(Test.posterinstance_activity_log),
                a_miner_step_3(Test.posterinstance_activity_log))
            self.running_example_compare = a_miner_step_7(
                a_miner_step_5(a_miner_step_4(Test.running_example_activity_log,
                                              a_miner_step_1(
                                                  Test.running_example_activity_log))[0]),
                a_miner_step_1(Test.running_example_activity_log), a_miner_step_2(Test.running_example_activity_log),
                a_miner_step_3(Test.running_example_activity_log))

    # Testing step 1 for all datasets
    def test_Step1(self):
        print("\n\033[91mTesting Step 1 for all test sets:\033[0m")
        self._setUp(1)

        # loop through L1-L7
        for i in range(1, 8):
            var_name = "L" + str(i)
            compare_var = getattr(self, var_name + "_compare")
            standard_var = getattr(Test, var_name + "_S1")

            print(f"{var_name} Step 1: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal
            assert compare_var == standard_var, f"{var_name} Step 1: failed (skipping next steps)"
            print(f"{var_name} Step 1: \033[92m Passed \033[0m")

        # loop through billinstances, flyerinstances, posterinstance, and running_example
        variables = ["billinstances", "flyerinstances", "posterinstance", "running_example"]
        for var in variables:
            compare_var = getattr(self, var + "_compare")
            standard_var = getattr(Test, var + "_S1")

            print(f"{var} Step 1: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal
            assert compare_var == standard_var, f"{var} Step 1: failed (skipping next steps)"
            print(f"{var} Step 1: \033[92m Passed \033[0m")

        print("\033[92m! Passed Step 1 !\033[0m")

    # Testing step 2 for all datasets
    def test_Step2(self):
        print("\n\033[91mTesting Step 2 for all test sets:\033[0m")
        self._setUp(2)

        # loop through L1-L7
        for i in range(1, 8):
            var_name = "L" + str(i)
            compare_var = getattr(self, var_name + "_compare")
            standard_var = getattr(Test, var_name + "_S2")

            print(f"{var_name} Step 2: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal
            assert compare_var == standard_var, f"{var_name} Step 2: failed (skipping next steps)"
            print(f"{var_name} Step 2: \033[92m Passed \033[0m")

        # loop through billinstances, flyerinstances, posterinstance, and running_example
        variables = ["billinstances", "flyerinstances", "posterinstance", "running_example"]
        for var in variables:
            compare_var = getattr(self, var + "_compare")
            standard_var = getattr(Test, var + "_S2")

            print(f"{var} Step 2: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal
            assert compare_var == standard_var, f"{var} Step 2: failed (skipping next steps)"
            print(f"{var} Step 2: \033[92m Passed \033[0m")
        print("\033[92m! Passed Step 2 ! \033[0m")

    # Testing step 3 for all datasets
    def test_Step3(self):
        print("\n\033[91mTesting Step 3 for all test sets:\033[0m")
        self._setUp(3)

        # loop through L1-L7
        for i in range(1, 8):
            var_name = "L" + str(i)
            compare_var = getattr(self, var_name + "_compare")
            standard_var = getattr(Test, var_name + "_S3")

            print(f"{var_name} Step 3: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal
            assert compare_var == standard_var, f"{var_name} Step 3: failed (skipping next steps)"
            print(f"{var_name} Step 3: \033[92m Passed \033[0m")

        # loop through billinstances, flyerinstances, posterinstance, and running_example
        variables = ["billinstances", "flyerinstances", "posterinstance", "running_example"]
        for var in variables:
            compare_var = getattr(self, var + "_compare")
            standard_var = getattr(Test, var + "_S3")

            print(f"{var} Step 3: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal
            assert compare_var == standard_var, f"{var} Step 3: failed (skipping next steps)"
            print(f"{var} Step 3: \033[92m Passed \033[0m")
        print("\033[92m! Passed Step 3 ! \033[0m")

    # Testing step 4 for all datasets
    def test_Step4(self):
        print("\n\033[91mTesting Step 4 for all test sets:\033[0m")
        self._setUp(4)

        # loop through L1-L7
        for i in range(1, 8):
            var_name = "L" + str(i)
            compare_var = getattr(self, var_name + "_compare")
            standard_var = getattr(Test, var_name + "_S4")

            print(f"{var_name} Step 4: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal

            assert all(x in standard_var for x in compare_var) and all(
                x in compare_var for x in standard_var), "Step 4: failed (skipping next steps)"
            print(f"{var_name} Step 4: \033[92m Passed \033[0m")

        # loop through billinstances, flyerinstances, posterinstance, and running_example
        variables = ["billinstances", "flyerinstances", "posterinstance", "running_example"]
        for var in variables:
            compare_var = getattr(self, var + "_compare")
            standard_var = getattr(Test, var + "_S4")

            print(f"{var} Step 4: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal
            assert all(x in standard_var for x in compare_var) and all(
                x in compare_var for x in standard_var), "Step 4: failed (skipping next steps)"
            print(f"{var} Step 4: \033[92m Passed \033[0m")
        print("\033[92m! Passed Step 4 ! \033[0m")

    # Testing step 5 for all datasets
    def test_Step5(self):
        print("\n\033[91mTesting Step 5 for all test sets:\033[0m")
        self._setUp(5)

        # loop through L1-L7
        for i in range(1, 8):
            var_name = "L" + str(i)
            compare_var = getattr(self, var_name + "_compare")
            standard_var = getattr(Test, var_name + "_S5")

            print(f"{var_name} Step 5: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal

            assert all(x in standard_var for x in compare_var) and all(
                x in compare_var for x in standard_var), "Step 5: failed (skipping next steps)"
            print(f"{var_name} Step 5: \033[92m Passed \033[0m")

        # loop through billinstances, flyerinstances, posterinstance, and running_example
        variables = ["billinstances", "flyerinstances", "posterinstance", "running_example"]
        for var in variables:
            compare_var = getattr(self, var + "_compare")
            standard_var = getattr(Test, var + "_S5")

            print(f"{var} Step 5: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal
            assert all(x in standard_var for x in compare_var) and all(
                x in compare_var for x in standard_var), "Step 5: failed (skipping next steps)"
            print(f"{var} Step 5: \033[92m Passed \033[0m")
        print("\033[92m! Passed Step 5 ! \033[0m")

    # Testing step 6 for all datasets
    def test_Step6(self):
        print("\n\033[91mTesting Step t for all test sets:\033[0m")
        self._setUp(6)

        # loop through L1-L7
        for i in range(1, 8):
            var_name = "L" + str(i)
            compare_var = getattr(self, var_name + "_compare")
            standard_var = getattr(Test, var_name + "_S6")

            print(f"{var_name} Step 6: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal

            assert all(x in standard_var for x in compare_var) and all(
                x in compare_var for x in standard_var), "Step 6: failed (skipping next steps)"
            print(f"{var_name} Step 6: \033[92m Passed \033[0m")

        # loop through billinstances, flyerinstances, posterinstance, and running_example
        variables = ["billinstances", "flyerinstances", "posterinstance", "running_example"]
        for var in variables:
            compare_var = getattr(self, var + "_compare")
            standard_var = getattr(Test, var + "_S6")

            print(f"{var} Step 6: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal
            assert all(x in standard_var for x in compare_var) and all(
                x in compare_var for x in standard_var), "Step 6: failed (skipping next steps)"
            print(f"{var} Step 6: \033[92m Passed \033[0m")
        print("\033[92m! Passed Step 6 ! \033[0m")

    # Testing step 7 for all datasets
    def test_Step7(self):
        print("\n\033[91mTesting Step t for all test sets:\033[0m")
        self._setUp(7)

        # loop through L1-L7
        for i in range(1, 8):
            var_name = "L" + str(i)
            compare_var = getattr(self, var_name + "_compare")
            standard_var = getattr(Test, var_name + "_S7")

            print(f"{var_name} Step 7: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal

            assert all(x in standard_var for x in compare_var) and all(
                x in compare_var for x in standard_var), "Step 7: failed (skipping next steps)"
            print(f"{var_name} Step 7: \033[92m Passed \033[0m")

        # loop through billinstances, flyerinstances, posterinstance, and running_example
        variables = ["billinstances", "flyerinstances", "posterinstance", "running_example"]
        for var in variables:
            compare_var = getattr(self, var + "_compare")
            standard_var = getattr(Test, var + "_S7")

            print(f"{var} Step 7: Comparing \033[93m {compare_var} \033[0m to \033[93m {standard_var} \033[0m")
            # compare the variables and print a message if they're not equal
            assert all(x in standard_var for x in compare_var) and all(
                x in compare_var for x in standard_var), "Step 7: failed (skipping next steps)"
            print(f"{var} Step 7: \033[92m Passed \033[0m")
        print("\033[92m! Passed Step 7 ! \033[0m")
