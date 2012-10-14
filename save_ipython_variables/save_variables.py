import pickle


def save_variable(name, var, auto_load=True):
    """Saves :param var: to a pickle file, named :param name:.

    :param auto_load: decides if the variable should be added to the list of
        variables that will be auto-loadable by :method load_all_variables:.
        Defaults to true.

    """
    if auto_load:
        if not _load_variable('saved_var_names'):
            __builtins__.setdefault('saved_var_names', set())
        saved_var_names = __builtins__.get('saved_var_names')
        saved_var_names.add(name)
        pickle.dump(saved_var_names, open('saved_var_names.pkl', 'wb'))

    pickle.dump(var, open(name + '.pkl', 'wb'))


def _load_variable(name):
    """Loads the variable :param name: from its pickled state as a builtin.

    Returns whether loading variable went successfully.

    """
    cmd = '__builtins__["{name}"] = pickle.load(open("{name}.pkl", "rb"))'\
        .format(name=name)

    try:
        exec cmd
    except IOError:
        return False
    return True


def load_all_variables(variable_names=None):
    """Loads all variables :param variable_names: into the __builtins__ scope.

    If :param variable_names: is `None`, load all variables stored in the list
    `saved_var_names`.

    """
    def load_all_and_print(variables):
        names_loaded_successfully = filter(_load_variable, variables)
        print 'Loaded the following variables:', names_loaded_successfully

    if variable_names:
        return load_all_and_print(variable_names)

    if not _load_variable('saved_var_names'):
        raise IOError('No variables saved in `saved_var_names`.')

    return load_all_and_print(saved_var_names)
