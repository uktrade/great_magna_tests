# -*- coding: utf-8 -*-
import logging
import os
from enum import Enum
from importlib import import_module
from pkgutil import iter_modules
from types import ModuleType
from typing import Dict, List




import browserpages

REQUIRED_PROPERTIES = ["SERVICE", "NAME", "TYPE", "URL", "SELECTORS"]


class ElementType(Enum):
    BUTTON = "button"
    CHECKBOX = "checkbox"
    IFRAME = "iframe"
    INPUT = "input"
    LABEL = "label"
    LINK = "a"
    RADIO = "radio"
    RADIO_DIV = "radiodiv"
    SELECT = "select"
    SPAN = "span"
    SUBMIT = "submit"
    TEXTAREA = "textarea"

    def __str__(self):
        return self.value


def is_page_object(module: ModuleType):
    return all([hasattr(module, prop) for prop in REQUIRED_PROPERTIES])


class PageObjects(Enum):
    """Page Objects enumeration.

    Values can only be modules with properties required for a Page Object.
    """

    def __new__(cls, value):
        logging.debug(f"is_page_object -> {is_page_object(value)}")
        if not is_page_object(value):
            raise TypeError(
                "Expected to get a Page Object module but got: {}".format(value)
            )
        member = object.__new__(cls)
        member._value_ = value
        return member

    def __str__(self):
        return "{}-{} [{} - {}]".format(
            self.value.SERVICE.value, self.value.NAME, self.value.TYPE, self.value.URL
        )

    @property
    def name(self) -> str:
        return self.value.NAME

    @property
    def service(self) -> str:
        return self.value.SERVICE.value

    @property
    def type(self) -> str:
        return self.value.TYPE.value

    @property
    def url(self) -> str:
        return self.value.URL

    @property
    def selectors(self) -> Dict:
        return self.value.SELECTORS


def get_enum_key(module: ModuleType) -> str:
    return (
        f"{module.SERVICE}_{module.TYPE}_{module.NAME}".upper()
        .replace(" ", "_")
        .replace("-", "_")
    )


def get_subpackages_names(package: ModuleType) -> List[str]:
    path = package.__path__
    logging.debug(path)
    return [name for _, name, is_pkg in iter_modules(path) if is_pkg]


def get_page_objects(package: ModuleType) -> Dict[str, ModuleType]:
    subpackages_names = get_subpackages_names(package)
    #logging.debug(f"subpackages_names -> {subpackages_names}")
    result = {}
    root_prefix = f"{package.__name__}."
    root_path = package.__path__[0]
    logging.debug(f"root_path-> {root_path}")
    for subpackage_name in subpackages_names:
        subpackage_path = os.path.join(root_path, subpackage_name)
        logging.debug(f"subpackage_path-> {subpackage_path}")
        for _, module_name, is_pkg in iter_modules([subpackage_path]):
            module_path = f"{root_prefix}{subpackage_name}.{module_name}"
            logging.debug(f"module_path-> {module_path}")
            if not is_pkg:
                logging.debug(f"importing module_path-> {module_path}")
                module = import_module(module_path)
                if is_page_object(module):
                    logging.debug(f"storing page module-> {module}")
                    enum_key = get_enum_key(module)
                    result[enum_key] = module
    return result


PAGES = PageObjects("PageObjects", names=get_page_objects(browserpages))


def get_page_object(service_and_page: str) -> ModuleType:
    #logging.debug(f"get_page_object: input '{service_and_page}'")
    assert " - " in service_and_page, f"Invalid Service & Page name: {service_and_page}"
    parts = service_and_page.split(" - ")
    sought_service = parts[0]
    sought_page = parts[1]
    sought_type = parts[2] if len(parts) == 3 else None
    result = None
    # PAGES = PageObjects("PageObjects", names=get_page_objects(browserpages))
    #logging.debug(f"PAGES.__members__.values() -> {PAGES.__members__.values()}")
    for page_object in PAGES.__members__.values():
        matched_service = False
        matched_type = False
        matched_name = False
        logging.debug(f"user entered -> {sought_service.lower()} , available -> {page_object.service.lower()}")
        if sought_service.lower() == page_object.service.lower():
            logging.debug(f"PO search: matched service '{sought_service}'")
            matched_service = True
        else:
            continue
        logging.debug(f"user entered -> {sought_page.lower()} , available -> {page_object.name.lower()}")
        # try to find a match based on the PO.NAME
        if sought_page.lower() == page_object.name.lower():
            logging.debug(f"PO search: matched name '{sought_page}'")
            matched_name = True
        else:
            # if that doesn't work, then try to do a check PO.NAMES
            if hasattr(page_object.value, "NAMES"):
                names = page_object.value.NAMES
                if sought_page.lower() in [name.lower() for name in names]:
                    logging.debug(f"PO search: matched one of names '{sought_page}'")
                    matched_name = True
                else:
                    continue
            else:
                continue

        if sought_type:
            if sought_type.lower() == page_object.type.lower():
                logging.debug(f"PO search: matched type '{sought_type}'")
                matched_type = True
            else:
                continue

        if matched_service and matched_name:
            if sought_type:
                if matched_type:
                    result = page_object.value
                    break
            else:
                result = page_object.value
                break

    if not result:
        service_key = sought_service.replace(" ", "_").upper()
        keys = [key for key in PAGES.__members__.keys() if key.startswith(service_key)]
        raise KeyError(
            f"Could not find Page Object for '{sought_page}' in "
            f"'{sought_service}' package. Here's a list of available Page "
            f"Objects: {keys}"
        )
    logging.debug(f"PO search: found 1 PO for: {service_and_page} → {result}")
    return result


