from typing import Any, Callable, Iterator, Match, NoReturn, Sequence, TypeVar

from parsimonious.exceptions import VisitationError as VisitationError
from parsimonious.expressions import Expression
from parsimonious.grammar import Grammar

class Node:
    expr: Expression
    full_text: str
    start: int
    end: int
    children: Sequence[Node]
    def __init__(self, expr: Expression, full_text: str, start: int, end: int, children: Sequence[Node] | None = ...) -> None: ...
    @property
    def expr_name(self) -> str: ...
    def __iter__(self) -> Iterator[Node]: ...
    @property
    def text(self) -> str: ...
    def prettily(self, error: Node | None = ...) -> str: ...

class RegexNode(Node):
    match: Match[str]

class RuleDecoratorMeta(type): ...

class NodeVisitor(metaclass=RuleDecoratorMeta):
    grammar: Grammar | Any
    unwrapped_exceptions: tuple[type[Exception], ...]
    def visit(self, node: Node) -> Any: ...
    def generic_visit(self, node: Node, visited_children: Sequence[Any]) -> NoReturn: ...
    def parse(self, text: str, pos: int = ...) -> Node: ...
    def match(self, text: str, pos: int = ...) -> Node: ...
    def lift_child(self, node: Node, children: Sequence[Any]) -> Any: ...

_CallableT = TypeVar("_CallableT", bound=Callable[..., Any])

def rule(rule_string: str) -> Callable[[_CallableT], _CallableT]: ...
