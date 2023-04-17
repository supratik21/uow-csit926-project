
from typing import Dict, Type
from enum import Enum

from py2puml.domain.umlitem import UmlItem
from py2puml.domain.umlenum import UmlEnum, Member

def inspect_enum_type(
    enum_type: Type[Enum],
    enum_type_fqn: str,
    domain_items_by_fqn: Dict[str, UmlItem]
):
    domain_items_by_fqn[enum_type_fqn] = UmlEnum(
        name=enum_type.__name__,
        fqn=enum_type_fqn,
        members=[
            Member(name=enum_member.name, value=enum_member.value)
            for enum_member in enum_type
        ]
    )
