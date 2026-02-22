"""Tests voor scripts/extract_urls.py."""

from pathlib import Path

from extract_urls import (
    classify_url,
    clean_url,
    extract_all,
    extract_urls_from_file,
    is_excluded,
    normalize_github_url,
)

# --- clean_url() ---


class TestCleanUrl:
    def test_trailing_punctuatie(self):
        assert clean_url("https://example.com/path.") == "https://example.com/path"
        assert clean_url("https://example.com/path,") == "https://example.com/path"
        assert clean_url("https://example.com/path;") == "https://example.com/path"

    def test_gebalanceerde_haakjes(self):
        assert clean_url("https://example.com/path)") == "https://example.com/path"
        assert clean_url("https://example.com/path(1)") == "https://example.com/path(1)"

    def test_trailing_slash(self):
        assert clean_url("https://example.com/path/") == "https://example.com/path"


# --- is_excluded() ---


class TestIsExcluded:
    def test_example_domains(self):
        assert is_excluded("https://example.com/test") is True
        assert is_excluded("https://api.example.com/v1") is True

    def test_localhost(self):
        assert is_excluded("http://localhost:8080") is True
        assert is_excluded("http://127.0.0.1:3000") is True

    def test_voorbeeld_domeinen(self):
        assert is_excluded("https://your-domain.nl/test") is True
        assert is_excluded("https://mijn-organisatie.nl/test") is True

    def test_echte_urls_niet_uitgesloten(self):
        assert is_excluded("https://github.com/internetstandards/Internet.nl") is False
        assert is_excluded("https://internet.nl/test-site") is False
        assert is_excluded("https://www.forumstandaardisatie.nl/open-standaarden") is False


# --- classify_url() ---


class TestClassifyUrl:
    def test_github_repo(self):
        url = "https://github.com/internetstandards/Internet.nl"
        assert classify_url(url) == "github_repo"

    def test_internet_nl(self):
        url = "https://internet.nl/test-site"
        assert classify_url(url) == "internet_nl"

    def test_forum(self):
        url = "https://www.forumstandaardisatie.nl/open-standaarden/ipv6-en-dnssec"
        assert classify_url(url) == "forum"

    def test_ncsc(self):
        url = "https://www.ncsc.nl/documenten/factsheets/2019/juni/01/factsheet"
        assert classify_url(url) == "ncsc"

    def test_onbekende_url(self):
        assert classify_url("https://www.google.com") is None


# --- normalize_github_url() ---


class TestNormalizeGithubUrl:
    def test_tags_verwijderd(self):
        assert (
            normalize_github_url("https://github.com/internetstandards/Internet.nl/tags")
            == "https://github.com/internetstandards/Internet.nl"
        )

    def test_tree_main_verwijderd(self):
        assert (
            normalize_github_url("https://github.com/internetstandards/Internet.nl/tree/main")
            == "https://github.com/internetstandards/Internet.nl"
        )

    def test_passthrough_base_url(self):
        url = "https://github.com/internetstandards/Internet.nl"
        assert normalize_github_url(url) == url

    def test_passthrough_niet_internetstandards(self):
        url = "https://github.com/other-org/some-repo/tags"
        assert normalize_github_url(url) == url


# --- extract_urls_from_file() ---


class TestExtractUrlsFromFile:
    def test_sample_skill(self):
        fixture = Path(__file__).parent / "fixtures" / "sample_skill.md"
        results = extract_urls_from_file(fixture)

        urls = [r["url"] for r in results]

        assert "https://github.com/internetstandards/Internet.nl" in urls
        assert "https://internet.nl/test-site" in urls
        assert "https://www.forumstandaardisatie.nl/open-standaarden/ipv6-en-dnssec" in urls

        excluded_urls = [u for u in urls if "example.com" in u or "your-domain" in u]
        assert excluded_urls == []

    def test_types_correct(self):
        fixture = Path(__file__).parent / "fixtures" / "sample_skill.md"
        results = extract_urls_from_file(fixture)

        type_map = {r["url"]: r["type"] for r in results}
        assert type_map["https://github.com/internetstandards/Internet.nl"] == "github_repo"
        assert type_map["https://internet.nl/test-site"] == "internet_nl"
        assert (
            type_map["https://www.forumstandaardisatie.nl/open-standaarden/ipv6-en-dnssec"]
            == "forum"
        )


# --- extract_all() deduplicatie ---


class TestExtractAll:
    def test_deduplicatie(self, tmp_path):
        skill_dir = tmp_path / "skills" / "test-skill"
        skill_dir.mkdir(parents=True)

        url = "https://github.com/internetstandards/Internet.nl"

        (skill_dir / "SKILL.md").write_text(
            f"---\nname: test\ndescription: test\nmodel: sonnet\n---\n\nRepo: {url}\n"
        )
        (skill_dir / "reference.md").write_text(f"# Ref\n\nZie ook: {url}\n")

        results = extract_all(tmp_path / "skills")
        urls = [r["url"] for r in results]

        assert urls.count(url) == 1

    def test_lege_directory(self, tmp_path):
        skill_dir = tmp_path / "skills"
        skill_dir.mkdir()
        assert extract_all(skill_dir) == []
