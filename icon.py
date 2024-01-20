from enum import Enum
from qfluentwidgets import FluentIconBase, getIconColor, Theme


class Icon(FluentIconBase, Enum):

    PERSON = "person"

    def path(self, theme=Theme.AUTO):
        return f":/chouqian/icon/{self.value}_{getIconColor(theme)}.svg"
