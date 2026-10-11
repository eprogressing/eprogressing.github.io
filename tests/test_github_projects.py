import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError, URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import refresh_github_projects as cards


class ProjectDataTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.config = self.root / "selection.json"
        self.output = self.root / "projects.json"
        self.item = {"repository": "eprogressing/triangle-light-maze-solver", "title": "Maze"}
        self.config.write_text(json.dumps([self.item]))
        self.payload = {"full_name": self.item["repository"], "private": False,
                        "stargazers_count": 44, "forks_count": 5, "language": None,
                        "description": "<script>not markup</script>", "license": None}

    def write_success(self):
        with patch.object(cards, "fetch_repository", return_value=self.payload):
            self.assertTrue(cards.refresh(self.config, self.output))

    def test_successful_snapshot_contains_no_token_or_foreign_url(self):
        payload = dict(self.payload, html_url="https://untrusted.example")
        with patch.dict(cards.os.environ, {"GH_TOKEN": "test-token-never-published"}), \
                patch.object(cards, "fetch_repository", return_value=payload):
            cards.refresh(self.config, self.output)
        text = self.output.read_text()
        result = json.loads(text)["projects"][0]
        self.assertNotIn("test-token-never-published", text)
        self.assertEqual(result["url"], "https://github.com/" + self.item["repository"])
        self.assertIsNone(result["license"])
        self.assertIsNone(result["language"])

    def test_private_payload_is_not_published_and_does_not_replace_snapshot(self):
        self.write_success()
        original = self.output.read_bytes()
        with patch.object(cards, "fetch_repository", return_value=dict(self.payload, private=True)):
            with self.assertRaises(ValueError):
                cards.refresh(self.config, self.output)
        self.assertEqual(self.output.read_bytes(), original)

    def test_transient_failure_keeps_original_bytes_and_timestamp(self):
        self.write_success()
        original = self.output.read_bytes()
        with patch.object(cards, "fetch_repository", side_effect=URLError("offline")):
            self.assertFalse(cards.refresh(self.config, self.output))
        self.assertEqual(self.output.read_bytes(), original)

    def test_changed_selection_cannot_fall_back_to_removed_project(self):
        self.write_success()
        self.config.write_text(json.dumps([{"repository": "other/selected", "title": "Other"}]))
        with patch.object(cards, "fetch_repository", side_effect=URLError("offline")):
            with self.assertRaises(URLError):
                cards.refresh(self.config, self.output)

    def test_not_found_is_not_treated_as_transient(self):
        self.write_success()
        error = HTTPError("https://api.github.com", 404, "not found", {}, None)
        with patch.object(cards, "fetch_repository", side_effect=error):
            with self.assertRaises(HTTPError):
                cards.refresh(self.config, self.output)

    def test_invalid_identity_or_counts_cannot_create_snapshot(self):
        for updates in [{"full_name": "someone/else"}, {"stargazers_count": -1},
                        {"stargazers_count": True}, {"private": None}]:
            with self.subTest(updates=updates):
                with patch.object(cards, "fetch_repository", return_value=dict(self.payload, **updates)):
                    with self.assertRaises(ValueError):
                        cards.refresh(self.config, self.output)
                self.assertFalse(self.output.exists())

    def test_duplicate_or_path_like_selection_is_rejected(self):
        for items in [[self.item, self.item], [{"repository": "../../secret", "title": "No"}]]:
            self.config.write_text(json.dumps(items))
            with self.assertRaises(ValueError):
                cards.selection(self.config)


if __name__ == "__main__":
    unittest.main()
