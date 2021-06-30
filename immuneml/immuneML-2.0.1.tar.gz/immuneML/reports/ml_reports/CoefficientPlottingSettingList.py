from collections.abc import MutableSequence

from immuneML.reports.ml_reports.CoefficientPlottingSetting import CoefficientPlottingSetting
from immuneML.util.ParameterValidator import ParameterValidator


class CoefficientPlottingSettingList(MutableSequence):

    def __init__(self):
        self.list = list()

    def check(self, v):
        ParameterValidator.assert_type_and_value(v, CoefficientPlottingSetting, "CoefficientPlottingSettingList", "new item")

    def __len__(self): return len(self.list)

    def __getitem__(self, i): return self.list[i]

    def __delitem__(self, i): del self.list[i]

    def __setitem__(self, i, v):
        self.check(v)
        self.list[i] = v

    def insert(self, i, v):
        self.check(v)
        self.list.insert(i, v)

    def __str__(self):
        return str(self.list)
