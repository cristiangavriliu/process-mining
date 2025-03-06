import itertools

import pandas as pd


def a_miner(activity_log):
    """ Applies the Alpha Miner algorithm to the activity log and returns the process model.
        Input:  activity_log (list of lists): A list of event logs, where each event log is a list of events.
        Output: Places (set): A set of the places generated by the Alpha Miner algorithm
                Transitions (set): A set of all unique events in the activity log.
                Flows (set): A set of the flows generated by the Alpha Miner algorithm
                Printer (str): A string containing outputs of each step and the footprint_matrix """
    # Extract transitions
    transitions = a_miner_step_1(activity_log)
    printer = "Step 1: Transitions = " + str(transitions) + " <br> <br>"
    print("Step 1: Final elements = ", transitions)

    # Extract initial elements
    initial_elements = a_miner_step_2(activity_log)
    printer += "Step 2: Initial elements = " + str(initial_elements) + " <br> <br>"
    print("Step 2: Final elements = ", initial_elements)

    # Extract final elements
    final_elements = a_miner_step_3(activity_log)
    printer += "Step 3: Final elements = " + str(final_elements) + " <br> <br>"
    print("Step 3: Final elements = ", final_elements)

    # Generate causal and parallel relations
    xl, dataframe = a_miner_step_4(activity_log, transitions)
    printer += "Step 4: Causal relations = " + str(xl) + '<br><br> <p class="text-sm-left font-weight-bold"> ' \
                                                         'Footprint matrix: </p>' + str(dataframe) + '<br> <p ' \
                                                                                     'class="text-sm-left"> '

    print("Step 4: Causal relations = ", xl)

    # Generate tasks
    yl = a_miner_step_5(xl)
    printer += "Step 5: Non-maximal causal relations = " + str(yl) + " <br> <br>"
    print("Step 5: Tasks = ", yl)

    # Generate sequential relations
    pl = a_miner_step_6(yl)
    printer += "Step 6: Places = " + str(pl) + " <br> <br>"
    print("Step 6: Places = ", pl)

    # Generate process model
    fl = a_miner_step_7(yl, transitions, initial_elements, final_elements)
    printer += "Step 7:  Flow relation = " + str(fl) + " <br> <br>" + '</p>'
    print("Step 7: Process model = ", fl)

    return pl, transitions, fl, printer


def a_miner_step_1(activity_log):
    """ Extracts the transitions from the activity log.
        Input:  activity_log (list of lists): A list of event logs, where each event log is a list of events.
        Output: transitions (set): A set of all unique events in the activity log."""
    transition_set = set()
    for case in activity_log:
        for trace in case:
            transition_set.add(trace)
    return transition_set


def a_miner_step_2(activity_log):
    """ Extracts the initial elements from the activity log.
        Input:  activity_log (list of lists): A list of event logs, where each event log is a list of events.
        Output: initial_elements (set): A set of the first event in each case in the activity log."""
    initial_element_set = set()
    for case in activity_log:
        initial_element_set.add(case[0])
    return initial_element_set


def a_miner_step_3(activity_log):
    """ Extracts the final elements from the activity log.
        Input:  activity_log (list of lists): A list of event logs, where each event log is a list of events.
        Output: final_elements (set): A set of the last event in each case in the activity log."""
    final_element_set = set()
    for case in activity_log:
        final_element_set.add(case[(len(case) - 1)])
    return final_element_set


def a_miner_step_4(activity_log, transitions):
    """ Generates causal and parallel relations from the activity log.
        Input:  activity_log (list of lists): A list of event logs, where each event log is a list of events.
                transitions (set): A set of all unique events in the activity log.
        Output: xl (list): List of causal relations
                dataframe (DataFrame): footprint matrix
        """
    # Create a set of direct succession sequences from activity_log
    succession_set = set()
    for trace in activity_log:
        # Iterate over task sequences
        for x, y in zip(trace, trace[1:]):
            succession_set.add((x, y))

    # see which nodes are looping with itself
    looping_node = set()
    for x in succession_set:
        if x == x[::-1]:
            looping_node.add(x[0])

    # Generate set of causal relations
    causal_set = set()
    for sequence in succession_set:
        # If sequence is in succession_set and reverse sequence is not, add to causal_set
        if sequence[::-1] not in succession_set:
            causal_set.add(sequence)

    # Generate set of parallel relations
    parallel_set = set()
    for sequence in succession_set:
        # If sequence is in succession_set and reverse sequence is in succession_set, add to parallel_set
        if sequence[::-1] in succession_set:
            parallel_set.add(sequence)

    # Generate set of independent relations
    independent_set = set()
    all_permutations = itertools.permutations(transitions, 2)
    for pair in all_permutations:
        # If the pair is not in causal_set, parallel_set and reverse pair is not in causal_set, add to independent_set
        if pair not in causal_set and pair[::-1] not in causal_set and pair not in parallel_set:
            independent_set.add(pair)

    # helper function to check for independency
    def is_ind_set(sub_set, ind_set):
        """
        Given a set of activities, this function checks if all pairs of activities in the set are independent of each other.
        """
        if len(sub_set) == 1:
            return True
        else:
            # Get all possible combinations of pairs of activities from the set
            combinations = itertools.combinations(sub_set, 2)
            for combi in combinations:
                # check if each pair of activities is in the independent set
                if combi not in ind_set:
                    return False
            return True

    # helper function to check for causal relations
    def is_cs_set(sub_set, causi_set):
        """
        Given a set of activities, this function checks if all pairs of activities in the set are causally related to each other.
        """
        set_a, set_b = sub_set[0], sub_set[1]
        # Get all possible combinations of activities from set_a and set_b
        s_all = itertools.product(set_a, set_b)
        for combi in s_all:
            # check if each pair of activities is in the causal set
            if combi not in causi_set:
                return False
        return True

    xl = set()
    # Get all subsets of size 1 to n of the set of transitions
    subsets = itertools.chain.from_iterable(
        itertools.combinations(transitions, r) for r in range(1, len(transitions) + 1))

    # Get all subsets that are independent, according to the ind relation
    independent_a_or_b = [subset for subset in subsets if is_ind_set(subset, independent_set)]

    # Generate all combinations of independent subsets
    for a, b in itertools.product(independent_a_or_b, independent_a_or_b):
        # Check if the current combination of subsets is a valid Xl relation
        if is_cs_set((a, b), causal_set):
            xl.add((a, b))

    # eliminate all traces from xl that contain a looping element
    xl = {x for x in xl if not any(z == tuple(y) for y in looping_node for z in x)}

    return xl, create_footprint_matrix(transitions, causal_set, parallel_set, independent_set)


def a_miner_step_5(xl):
    """ Generates tasks from the causal relations.
        Input:  xl (list): List of causal relations
        Output: yl (list): List of non-maximal causal relations"""
    # Create a copy of xl
    yl = xl.copy()
    for x in xl:
        # Convert tuples x[0] and x[1] to sets
        a = set(x[0])
        b = set(x[1])
        for y in xl:
            # If a is a subset of y[0] and b is a subset of y[1], discard x from yl
            if a.issubset(y[0]) and b.issubset(y[1]):
                if x != y:
                    yl.discard(x)
                    break

    # format yl into a list
    yl_list = []
    for relation in yl:
        yl_list.append((set(relation[0]), set(relation[1])))
    return yl_list


def a_miner_step_6(yl):
    """ Generates sequential relations from the tasks.
        Input:  yl (list): List of non-maximal causal relations
        Output: pl (set): Set of places"""
    pl = []
    for relation in yl:
        pl.append((set(relation[0]), set(relation[1])))
    pl.append('start')
    pl.append('end')

    return pl


def a_miner_step_7(xl, transition_set, initial_element_set, final_element_set):
    """ Generates the process model from the sequential relations, transitions, initial elements, and final elements.
        Input:  yl (list): List of non-maximal causal relations
                transitions (set): A set of all unique events in the activity log.
                initial_elements (set): A set of the first event in each case in the activity log.
                final_elements (set): A set of the last event in each case in the activity log.
        Output: fl (set): Set of the flows generated by the Alpha Miner algorithm
    """

    # create list of flow relations and append initial elements
    fl = [("start", a) for a in initial_element_set]

    # append final elements
    fl += [(a, "end") for a in final_element_set]

    # append transition -> (a, b) for all transition in a
    fl += [(transition, (a, b)) for transition in transition_set for a, b in xl if transition in a]

    # append (a, b) -> transition for all transition in b
    fl += [((a, b), transition) for transition in transition_set for a, b in xl if transition in b]

    return fl


def create_footprint_matrix(transitions, causal_set, parallel_set, independent_set):
    """Creates a footprint matrix from the activity log and transitions.
        Input:  activity_log (list of lists): A list of event logs, where each event log is a list of events.
                transitions (set): A set of all unique events in the activity log.
        Output: dataframe (DataFrame): footprint matrix
        """

    # Initialize a dataframe with all elements as NaN
    footprint_matrix = pd.DataFrame(index=list(transitions), columns=list(transitions))
    # fill the matrix with "# L"
    footprint_matrix.fillna("# L", inplace=True)

    for sequence in causal_set:
        # set the cell of matrix with "-> L"
        footprint_matrix[sequence[0]][sequence[1]] = "-> L"
    for sequence in causal_set:
        # set the cell of matrix with "<- L"
        footprint_matrix[sequence[1]][sequence[0]] = "<- L"

    for sequence in parallel_set:
        # set the cell of matrix with "|| L"
        footprint_matrix[sequence[0]][sequence[1]] = '|| L'

    for sequence in independent_set:
        # set the cell of matrix with "# L"
        footprint_matrix[sequence[0]][sequence[1]] = '# L'

    # returns the matrix in a html table format
    return footprint_matrix.to_html(classes='table table-dark table-bordered')
