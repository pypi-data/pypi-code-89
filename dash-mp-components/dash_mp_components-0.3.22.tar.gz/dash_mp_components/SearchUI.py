# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SearchUI(Component):
    """A SearchUI component.
Component for rendering advanced search interfaces for data in an API
Renders results in a data table alongside a set of filters that map to properties in the data.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- allowViewSwitching (boolean; optional):
    Optionally enable/disable switching between SearchUI result views.

- apiKey (string; optional):
    API key (if needed) that will be used when making queries.

- autocompleteFormulaUrl (string; optional):
    Optional URL endpoint for fetching formula autocompletion results
    e.g.
    \"https://api.materialsproject.org/materials/formula_autocomplete/\".

- baseURL (string; optional):
    The base URL to the API that this search UI should query e.g.
    \"https://api.materialsproject.org/search/\".

- cardOptions (dict; optional):
    Set of options for configuring what is displayed in the result
    cards when in the cards view. Must be an object with the following
    properties:       {         imageBaseURL: '', // Base of the URL
    to use to get images for the left side of the card
    imageKey: 'material_id', // Data key to use to append value to the
    base URL (i.e. the name of the image file). The .png extension is
    added automatically.         levelOneKey: 'material_id', // Data
    key to use for the first line of text on the card
    levelTwoKey: 'formula_pretty', // Data key to use for the second
    line of text on the card         levelThreeKeys: [ // List of data
    keys and labels to display under the first and second line of text
    { key: 'energy_above_hull', label: 'Energy Above Hull' },
    { key: 'formation_energy_per_atom', label: 'Formation Energy' },
    ],       }.

- columns (list; optional):
    An array of column definitions for the results in the
    SearchUIDataTable Column properties are based on the
    react-data-table column settings
    (https://github.com/jbetancur/react-data-table-component#columns)
    The \"format\" property must match one of these pre-defined
    strings:     \"FIXED_DECIMAL\", \"SIGNIFICANT_FIGURES\",
    \"FORMULA\", \"LINK\", \"BOOLEAN\", \"SPACEGROUP_SYMBOL\",
    \"POINTGROUP\" The \"formatArg\" is a special property that is
    used to make certain formats more specific (e.g.
    SIGNIFICANT_FIGURES or FIXED_DECIMAL) The \"omit\" property lets
    you hide certain columns by default Read more about columns here:
    https://github.com/jbetancur/react-data-table-component#columns
    e.g.       [           {             name: 'Material Id',
    selector: 'task_ids',             format: 'LINK', // creates a
    link using the value in this column             formatArg:
    '/materials/' // prepends this string to the column value in the
    links href (e.g. href=\"/materials/mp-100\")           },
    {             name: 'Formula',             selector:
    'formula_pretty',             format: 'FORMULA',
    minWidth: '130px' // sets a minimum width for cells in this column
    },           {             name: 'Volume',             selector:
    'volume',             format: 'FIXED_DECIMAL',
    formatArg: 3 // number of decimals to fix to             omit:
    True // hide this column initially           },           {
    name: 'Density',             selector: 'density',
    format: 'SIGNIFICANT_FIGURES',             formatArg: 4 // number
    of significant figures to use           },           {
    name: 'Is Stable',             selector: 'is_stable',
    format: 'BOOLEAN',             formatArg: ['yes', 'no'] // sets
    display values for truthy and falsy values           },
    {             name: 'Energy Above Hull',             selector:
    'e_above_hull',             format: 'FIXED_DECIMAL',
    formatArg: 2,             units: 'meV/atom', // unit label string
    to show under column header             conversionFactor: 1000, //
    number by which to multiply result values in this columm
    },       ].

- conditionalRowStyles (list; optional):
    List of conditions for styling rows based on a property (selector)
    and a value Accepts a list of \"condition\" objects which must
    specify a...  selector: the name of the data property to use for
    the condition  value: the value that meets the condition  style:
    object of styles supplied in \"CSS-in-JS\" format Note that this
    prop currently only supports checking for  value equivalence (i.e.
    row[selector] === value) example:       [         {
    selector: \"myProperty\",           value: True,           style:
    {             backgroundColor: \"#ddd\"           }         }
    ].

- filterGroups (list; optional):
    An array of filter groups and their respective array of filters. A
    filter group is a collapsible section of the filters panel that
    contains one or more filters. A filter is a type of input element
    that filters the data based on its value. Filter \"type\" must be
    one of the all-caps strings used in the example below. Filter
    \"id\" must be a queryable field Filter \"props\" defines how that
    filter should be rendered. See example for props format based on
    filter type. e.g.       [         {           name: 'Material
    Definition',           collapsed: False,           filters: [
    {               name: 'ID',               id: 'task_ids',
    type: 'TEXT_INPUT' // a standard text input box for string values
    },             {               name: 'Elements',               id:
    'elements',               type: 'MATERIALS_INPUT', // a text input
    box and a periodic table synced together for selecting selements
    props: {                 field: 'elements' // sets which field the
    input controls ('elements' or 'formula')               }
    }           ]         },         {           name: 'General',
    collapsed: False,           filters: [             {
    name: 'Volume',               id: 'volume',               type:
    'SLIDER', // a dual range slider for setting a min and max value
    (must have two query params equal to <id>_min and <id>_max)
    units: 'kg', // (optional) unit label string to show next to
    filter label               conversionFactor: 0.001, // (optional)
    number by which to multiply filter values for api queries
    props: {                 domain: [0, 200] // sets the min and max
    values of the slider               }             },             {
    name: 'Stability',               id: 'is_stable',
    type: 'THREE_STATE_BOOLEAN_SELECT', // a dropdown with three
    values: True, False, or undefined               props: {
    options: [ // a list of options for the dropdwon (must supply only
    two options, the undefined option is added automatically)
    {                     label: 'Is stable',
    value: True                   },                   {
    label: 'Is not stable',                     value: False
    }                 ]               }             },             {
    name: 'Spacegroup Symbol',               id: 'spacegroup_symbol',
    type: 'SELECT_SPACEGROUP_SYMBOL' // a special dropdown for
    selecting a space group symbol (options are auto-generated)
    },             {               name: 'Spacegroup Number',
    id: 'spacegroup_number',               type:
    'SELECT_SPACEGROUP_NUMBER' // a special dropdown for selecting a
    space group number (options are auto-generated)             },
    {               name: 'Crystal System',               id:
    'crystal_system',               type: 'SELECT_CRYSTAL_SYSTEM' // a
    special dropdown for selecting a crystal system (options are
    auto-generated)             },             {               name:
    'Point Group',               id: 'pointgroup',               type:
    'SELECT_POINTGROUP' // a special dropdown for selecting a point
    group (options are auto-generated)             },             {
    name: 'Color',               id: 'color',               type:
    'SELECT', // a custom single select dropdown with any number of
    options               props: {                 options: [ // a
    list of options for the dropdwon                   {
    label: 'Blue',                     value: 'blue'
    },                   {                     label: 'Red',
    value: 'red'                   },                   {
    label: 'Yellow',                     value: 'yellow'
    }                 ]               }             },           ]
    }       ].

- hasSearchBar (boolean; optional):
    Optionally include/exclude the top search bar @default True.

- hasSortMenu (boolean; optional):
    Optionally include/exclude the menu for dynamically controlling
    sort options @default True.

- resultLabel (string; optional):
    A noun in singular form to describe what a result represents
    (default: \"result\") e.g. \"material\" Note that only some
    special plural mappings are handled automatically (e.g. battery ->
    batteries) In all other cases, an \"s\" is appended to
    resultLabel.

- searchBarAllowedInputTypesMap (dict; optional):
    Object with keys of allowed input types for the top-level search
    bar. Keys must be one of these supported input types:
    \"elements\", \"formula\", \"mpid\", \"smiles\", \"text\" Each key
    object must have a \"field\" property which maps the input type to
    a valid data filter field in the API. e.g.       {
    formula: {           field: 'formula'         },         elements:
    {           field: 'elements'         },         mpid: {
    field: 'material_ids'         }       }.

- searchBarErrorMessage (string; optional):
    Custom error message to display with the top-level search bar if
    the user types an invalid value.

- searchBarPeriodicTableMode (a value equal to: 'toggle', 'focus', 'none'; optional):
    Modes for showing the periodic table with the top search bar
    \"toggle\": render a button for toggling visibility of periodic
    table \"focus\": show periodic table when input is focuses, hide
    on blur \"none\": never show the periodic table for this input
    @default 'toggle'.

- searchBarPlaceholder (string; optional):
    Optionally add a string of text to show up in the top-level search
    bar.

- searchBarTooltip (string; optional):
    Optionally add a help icon with a tooltip in the search bar This
    should be used to provide instructions on how to use the search
    bar e.g.  'Type in a comma-separated list of element symbols (e.g.
    Ga, N),  a chemical formula (e.g. C3N), or a material id (e.g.
    mp-10152).  You can also click elements on the periodic table to
    add them to your search.'.

- selectableRows (boolean; optional):
    Set to True to show a checkbox next to each row.

- selectedRows (list; optional):
    Array of selected rows. This prop is dynamically updated using
    setProps and can be accessed via dash callback.

- sortAscending (boolean; optional):
    If including a sortField, set whether it should ascend by default
    True for ascending, False for descending.

- sortField (string; optional):
    Optionally include a field to sort by on initial load Must be a
    valid field and included in your list of columns.

- view (a value equal to: 'table', 'cards', 'synthesis'; optional):
    Set the initial results view to one of the preset SearchUI views:
    'table', 'cards', or 'synthesis'  To add a new view type, head to
    SearchUI/types and add the name of the type to the
    SearchUIViewType enum, then add a property in searchUIViewsMap
    using the same name you used for the type, then provide your
    custom view component as the value. The view component should
    consume the SearchUIContext state using the useSearchUIContext
    hook. See SearchUIDataTable or SearchUIDataCards for example view
    components. @default 'table'."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, columns=Component.UNDEFINED, filterGroups=Component.UNDEFINED, baseURL=Component.UNDEFINED, autocompleteFormulaUrl=Component.UNDEFINED, apiKey=Component.UNDEFINED, resultLabel=Component.UNDEFINED, hasSearchBar=Component.UNDEFINED, searchBarTooltip=Component.UNDEFINED, searchBarPlaceholder=Component.UNDEFINED, searchBarErrorMessage=Component.UNDEFINED, searchBarAllowedInputTypesMap=Component.UNDEFINED, searchBarPeriodicTableMode=Component.UNDEFINED, hasSortMenu=Component.UNDEFINED, sortField=Component.UNDEFINED, sortAscending=Component.UNDEFINED, conditionalRowStyles=Component.UNDEFINED, selectableRows=Component.UNDEFINED, selectedRows=Component.UNDEFINED, view=Component.UNDEFINED, allowViewSwitching=Component.UNDEFINED, cardOptions=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allowViewSwitching', 'apiKey', 'autocompleteFormulaUrl', 'baseURL', 'cardOptions', 'columns', 'conditionalRowStyles', 'filterGroups', 'hasSearchBar', 'hasSortMenu', 'resultLabel', 'searchBarAllowedInputTypesMap', 'searchBarErrorMessage', 'searchBarPeriodicTableMode', 'searchBarPlaceholder', 'searchBarTooltip', 'selectableRows', 'selectedRows', 'sortAscending', 'sortField', 'view']
        self._type = 'SearchUI'
        self._namespace = 'dash_mp_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'allowViewSwitching', 'apiKey', 'autocompleteFormulaUrl', 'baseURL', 'cardOptions', 'columns', 'conditionalRowStyles', 'filterGroups', 'hasSearchBar', 'hasSortMenu', 'resultLabel', 'searchBarAllowedInputTypesMap', 'searchBarErrorMessage', 'searchBarPeriodicTableMode', 'searchBarPlaceholder', 'searchBarTooltip', 'selectableRows', 'selectedRows', 'sortAscending', 'sortField', 'view']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(SearchUI, self).__init__(**args)
