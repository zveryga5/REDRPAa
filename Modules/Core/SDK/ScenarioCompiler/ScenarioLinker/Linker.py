from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioLinker.Linker import AbstractScenarioLinker
from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTree import AbstractSyntaxTree
from Modules.Core.SDK.ScenarioCompiler.ScenarioTokens.Tokens import STDLinkerTokens
from Modules.Core.SDK.ScenarioExecutable.Sections.ImportsSection import STDImportsSection


def get_func_calls(func_call_node, func_calls_list, api_funcs):
    _type = func_call_node.get_type()
    if _type == STDLinkerTokens.FUNC_CALL:
        if func_call_node.get_data() in api_funcs:
            func_calls_list.append(func_call_node)
            func_call_node.set_type(STDLinkerTokens.API_FUNC_CALL)
        else:
            func_call_node.set_type(STDLinkerTokens.USER_FUNC_CALL)


class STDRSLLinker(AbstractScenarioLinker):
    def __init__(self, syntax_tree: AbstractSyntaxTree, api_funcs):
        self._tree = syntax_tree
        self._stdlib = api_funcs

    def link_names(self):
        api_imports = self._link_funcs()
        imports = STDImportsSection()
        imports.add("api", api_imports)
        return imports

    def _link_funcs(self):
        func_calls = []
        api_imports = {}
        api_functions = self._stdlib.get_all_api_methods()
        self._tree.traverse(get_func_calls, func_calls, api_functions)
        for func in func_calls:
            api_name = self._stdlib.get_api_name_by_func_name(func.get_data())
            import_string = "from " + self._stdlib.get_api_import_path(api_name) + " import " + api_name
            api_imports[api_name] = import_string
        return api_imports
