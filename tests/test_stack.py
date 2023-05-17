"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack
import pytest

def test_node_creation():
    assert Node(5).data == 5
    assert Node(5).next_node is None
    node1 = Node(5)
    node1.data = 10
    assert node1.data == 10
    node2 = Node(10, next_node=node1)
    assert node2.data == 10
    assert node2.next_node == node1
    assert node1.next_node is None

def test_stack_push():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.top.data == 3



