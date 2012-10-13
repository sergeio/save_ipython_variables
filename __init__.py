import pickle


def save_variable(name, var, auto_load=True):
    """Saves :param var: to a pickle file, named :param name:.

    :param auto_load: decides if the variable should be added to the list of
        variables that will be auto-loadable by :method load_all_variables:.
        Defaults to true.

    """
    if auto_load:
        if not _load_variable('auto_load_var_names'):
            __builtins__.setdefault('auto_load_var_names', set())
        auto_load_var_names = __builtins__.get('auto_load_var_names')
        auto_load_var_names.add(name)
        pickle.dump(auto_load_var_names, open('auto_load_var_names.pkl', 'wb'))

    pickle.dump(var, open(name + '.pkl', 'wb'))


def _load_variable(name):
    """Loads the variable :param name: from its pickled state as a builtin."""
    if not isinstance(name, basestring):
        raise TypeError('Argument should be a string.')
    cmd = '__builtins__["{name}"] = pickle.load(open("{name}.pkl", "rb"))'\
        .format(name=name)
    exec cmd


def load_all_variables(variable_names=None):
    """Loads all variables :param variable_names: into the __builtins__ scope.

    If :param variable_names: is `None`, load all variables stored in the list
    `auto_load_var_names`.

    """
    if variable_names:
        for var in variable_names:
            _load_variable(var)
        return

    try:
        _load_variable('auto_load_var_names')
    except IOError:
        raise IOError('No variables saved in `auto_load_var_names`.')

    for var in auto_load_var_names:
        _load_variable(var)

    print 'Loaded the following variables:', (
        variable_names or auto_load_var_names)
