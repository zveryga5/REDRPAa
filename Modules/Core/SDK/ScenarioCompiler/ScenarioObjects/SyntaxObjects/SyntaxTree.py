from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxNode import AbstractSyntaxNode
from Modules.Core.Abstract.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTree import AbstractSyntaxTree
from Modules.Core.SDK.ScenarioCompiler.ScenarioObjects.SyntaxObjects.SyntaxTreeIterator import STDRSLPreOrderSyntaxTreeIterator


class STDRSLSyntaxTree(AbstractSyntaxTree):

    def __init__(self, header_node: AbstractSyntaxNode):
        self._header_node = header_node
        self._iterator = STDRSLPreOrderSyntaxTreeIterator(self)

    def deserialize(self):
        self._header_node.deserialize()

    def traverse(self, func, *func_args):
        self._iterator.traverse(self._header_node, func, *func_args)

    def get_head(self):
        return self._header_node
