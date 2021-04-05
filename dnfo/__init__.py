"""global variables"""
ENDPOINTS: tuple = (
    "ability-scores",
    "skills",
    "proficiencies",
    "languages",
    "alignment",
    "backgrounds",
    "classes",
    "subclasses",
    "features",
    "starting-equipment",
    "races",
    "subraces",
    "traits",
    "equipment-categories",
    "equipment",
    "magic-items",
    "weapon-properties",
    "spells",
    "monsters",
    "conditions",
    "damage-types",
    "magic-schools",
    "rules",
    "rule-sections",
)
SECONDARIES: tuple = ("classes", "subclasses", "races", "subraces")
__version__: str = "1.0.0"


def remove_prefix(self: str, prefix: str) -> str:
    """remove a prefix from a string"""
    if self.startswith(prefix):
        return self[len(prefix):]
    return self


def remove_suffix(self: str, suffix: str) -> str:
    """remove a suffix from a string"""
    if self.endswith(suffix):
        return self[:-len(suffix)]
    return self
