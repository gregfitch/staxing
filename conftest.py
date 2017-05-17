"""Check for collection issue prior to testing."""

import pytest


def pytest_addoption(parser):
    """Add branch parameter."""
    parser.addoption('--testall', action='store_true', help='Run all tests')


def pytest_collectreport(report):
    if report.failed:
        raise pytest.UsageError("Errors during collection, aborting")
