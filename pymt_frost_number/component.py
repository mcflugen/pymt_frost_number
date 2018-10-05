from __future__ import absolute_import

from pymt.framework.bmi_bridge import bmi_factory

from .bmi import BmiFrostnumberMethod

BmiFrostNumberMethod = bmi_factory(BmiFrostnumberMethod)

del bmi_factory
