import os
import pytest
from bot.utils.evaluate import Rating

@pytest.mark.utils
class Testratings:
    @pytest.fixture
    def ratings_instance(self):
        ratings = Rating("data", "tmp_scores.csv")
        yield ratings
        # Teardown: Remove the created file after the test
        if os.path.exists(ratings.file_path):
            os.remove(ratings.file_path)

    def test_update_and_evaluate(self, ratings_instance):
        # Perform an update
        ratings_instance.update(9999, 4, "2024-03-21")
        # Evaluate the statistics
        stats = ratings_instance.statistics
        # Check if the average ratings is correct
        assert stats["average_rating"] == 4.0