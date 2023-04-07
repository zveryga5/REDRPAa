from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTree import AbstractSyntaxTree


def translate_unit(syntax_node, result, current_condition):
    pass


class STDRSLTranslator:
    def __init__(self, syntax_tree: AbstractSyntaxTree):
        self._tree = syntax_tree

    def translate(self):
        result = []
        current_condition = None
        self._tree.traverse(translate_unit, result, current_condition)
