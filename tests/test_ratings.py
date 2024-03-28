import pytest


@pytest.mark.utils
class Testratings:
    """Tests for ratings"""

    def test_update_and_evaluate(self, rating_instance):
        """test_update_and_evaluate tests average rating

        Parameters
        ----------
        rating_instance : uses fixture rating_instance
        """
        # Perform an update
        rating_instance.update(9999, 4, "2024-03-21")
        rating_instance.update(9999, 5, "2024-03-21")
        rating_instance.update(8888, 4, "2024-03-21")
        stats = rating_instance.statistics
        assert stats["average_rating"] == 4.0
