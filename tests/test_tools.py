"""Tests for pytest_concurrency.tools module."""

from unittest.mock import Mock

import pytest
from pytest_concurrency.tools import get_workers_count


class TestGetWorkersCount:
    """Tests for get_workers_count function."""

    def test_returns_integer_value_from_config(self) -> None:
        """Should return the integer value from config.getoption."""
        config = Mock()
        config.getoption.return_value = 4

        result = get_workers_count(config, "workers")

        assert result == 4
        config.getoption.assert_called_once_with("workers")

    def test_converts_string_to_integer(self) -> None:
        """Should convert string count to integer."""
        config = Mock()
        config.getoption.return_value = "8"

        result = get_workers_count(config, "workers")

        assert result == 8
        assert isinstance(result, int)

    def test_auto_returns_cpu_count(self) -> None:
        """Should return cpu_count when config value is 'auto'."""
        config = Mock()
        config.getoption.return_value = "auto"

        result = get_workers_count(config, "workers")

        assert result >= 1
        assert isinstance(result, int)

    def test_auto_uses_default_when_cpu_count_is_none(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Should use default value when os.cpu_count returns None."""
        config = Mock()
        config.getoption.return_value = "auto"
        monkeypatch.setattr("os.cpu_count", lambda: None)

        result = get_workers_count(config, "workers", default=3)

        assert result == 3
