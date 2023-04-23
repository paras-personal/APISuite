import pytest
from py.xml import html


def pytest_configure(config):
    """
    pytest hook that execute before the actual execution starts
    """
    print("Start point")


def pytest_html_report_title(report):
    """
    modifying the title  of html report
    """
    report.title = "API TEST REPORT"


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.pop(3)
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    try:
        cells.insert(1, html.td(report.description))
        cells[0], cells[1] = cells[1], cells[0]
    except AttributeError:
        pass
    cells.pop(2)
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    report.description = str(item.function.__doc__)