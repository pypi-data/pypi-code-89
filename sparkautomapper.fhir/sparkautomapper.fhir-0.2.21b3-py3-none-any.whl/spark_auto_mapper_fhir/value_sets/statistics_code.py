from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class StatisticsCodeCode(FhirValueSetBase):
    """
    StatisticsCode
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/observation-statistics
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/observation-statistics"


class StatisticsCodeCodeValues:
    """
    The [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) of N measurements over the stated period.
    """

    Average = StatisticsCodeCode("average")
    """
    The [maximum](https://en.wikipedia.org/wiki/Maximal_element) value of N measurements over the stated period.
    """
    Maximum = StatisticsCodeCode("maximum")
    """
    The [minimum](https://en.wikipedia.org/wiki/Minimal_element) value of N measurements over the stated period.
    """
    Minimum = StatisticsCodeCode("minimum")
    """
    The [number] of valid measurements over the stated period that contributed to the other statistical outputs.
    """
    Count = StatisticsCodeCode("count")
    """
    The total [number] of valid measurements over the stated period, including observations that were ignored because they did not contain valid result values.
    """
    TotalCount = StatisticsCodeCode("total-count")
    """
    The [median](https://en.wikipedia.org/wiki/Median) of N measurements over the stated period.
    """
    Median = StatisticsCodeCode("median")
    """
    The [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of N measurements over the stated period.
    """
    StandardDeviation = StatisticsCodeCode("std-dev")
    """
    The [sum](https://en.wikipedia.org/wiki/Summation) of N measurements over the stated period.
    """
    Sum = StatisticsCodeCode("sum")
    """
    The [variance](https://en.wikipedia.org/wiki/Variance) of N measurements over the stated period.
    """
    Variance = StatisticsCodeCode("variance")
    """
    The 20th [Percentile](https://en.wikipedia.org/wiki/Percentile) of N measurements over the stated period.
    """
    _20thPercentile = StatisticsCodeCode("20-percent")
    """
    The 80th [Percentile](https://en.wikipedia.org/wiki/Percentile) of N measurements over the stated period.
    """
    _80thPercentile = StatisticsCodeCode("80-percent")
    """
    The lower [Quartile](https://en.wikipedia.org/wiki/Quartile) Boundary of N measurements over the stated period.
    """
    LowerQuartile = StatisticsCodeCode("4-lower")
    """
    The upper [Quartile](https://en.wikipedia.org/wiki/Quartile) Boundary of N measurements over the stated period.
    """
    UpperQuartile = StatisticsCodeCode("4-upper")
    """
    The difference between the upper and lower [Quartiles](https://en.wikipedia.org/wiki/Quartile) is called the Interquartile range. (IQR = Q3-Q1) Quartile deviation or Semi-interquartile range is one-half the difference between the first and the third quartiles.
    """
    QuartileDeviation = StatisticsCodeCode("4-dev")
    """
    The lowest of four values that divide the N measurements into a frequency distribution of five classes with each containing one fifth of the total population.
    """
    _1stQuintile = StatisticsCodeCode("5-1")
    """
    The second of four values that divide the N measurements into a frequency distribution of five classes with each containing one fifth of the total population.
    """
    _2ndQuintile = StatisticsCodeCode("5-2")
    """
    The third of four values that divide the N measurements into a frequency distribution of five classes with each containing one fifth of the total population.
    """
    _3rdQuintile = StatisticsCodeCode("5-3")
    """
    The fourth of four values that divide the N measurements into a frequency distribution of five classes with each containing one fifth of the total population.
    """
    _4thQuintile = StatisticsCodeCode("5-4")
    """
    Skewness is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean. The skewness value can be positive or negative, or even undefined.  Source: [Wikipedia](https://en.wikipedia.org/wiki/Skewness).
    """
    Skew = StatisticsCodeCode("skew")
    """
    Kurtosis  is a measure of the "tailedness" of the probability distribution of a real-valued random variable.   Source: [Wikipedia](https://en.wikipedia.org/wiki/Kurtosis).
    """
    Kurtosis = StatisticsCodeCode("kurtosis")
    """
    Linear regression is an approach for modeling two-dimensional sample points with one independent variable and one dependent variable (conventionally, the x and y coordinates in a Cartesian coordinate system) and finds a linear function (a non-vertical straight line) that, as accurately as possible, predicts the dependent variable values as a function of the independent variables. Source: [Wikipedia](https://en.wikipedia.org/wiki/Simple_linear_regression)  This Statistic code will return both a gradient and an intercept value.
    """
    Regression = StatisticsCodeCode("regression")
