from re import search
from unittest import mock

from prowler.providers.aws.services.opensearch.opensearch_service import (
    OpenSearchDomain,
    PublishingLoggingOption,
)
from tests.providers.aws.utils import AWS_ACCOUNT_NUMBER, AWS_REGION_EU_WEST_1

domain_name = "test-domain"
domain_arn = f"arn:aws:es:us-west-2:{AWS_ACCOUNT_NUMBER}:domain/{domain_name}"


class Test_opensearch_service_domains_cloudwatch_logging_enabled:
    def test_no_domains(self):
        opensearch_client = mock.MagicMock
        opensearch_client.opensearch_domains = []

        with mock.patch(
            "prowler.providers.aws.services.opensearch.opensearch_service.OpenSearchService",
            new=opensearch_client,
        ), mock.patch(
            "prowler.providers.aws.services.opensearch.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_client",
            new=opensearch_client,
        ):
            from prowler.providers.aws.services.opensearch.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_service_domains_cloudwatch_logging_enabled import (
                opensearch_service_domains_cloudwatch_logging_enabled,
            )

            check = opensearch_service_domains_cloudwatch_logging_enabled()
            result = check.execute()
            assert len(result) == 0

    def test_no_logging_enabled(self):
        opensearch_client = mock.MagicMock
        opensearch_client.opensearch_domains = []
        opensearch_client.opensearch_domains.append(
            OpenSearchDomain(
                name=domain_name, region=AWS_REGION_EU_WEST_1, arn=domain_arn
            )
        )
        opensearch_client.opensearch_domains[0].logging = []

        with mock.patch(
            "prowler.providers.aws.services.opensearch.opensearch_service.OpenSearchService",
            new=opensearch_client,
        ), mock.patch(
            "prowler.providers.aws.services.opensearch.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_client",
            new=opensearch_client,
        ):
            from prowler.providers.aws.services.opensearch.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_service_domains_cloudwatch_logging_enabled import (
                opensearch_service_domains_cloudwatch_logging_enabled,
            )

            check = opensearch_service_domains_cloudwatch_logging_enabled()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search(
                "SEARCH_SLOW_LOGS and INDEX_SLOW_LOGS disabled",
                result[0].status_extended,
            )
            assert result[0].resource_id == domain_name
            assert result[0].resource_arn == domain_arn

    def test_logging_SEARCH_SLOW_LOGS_enabled(self):
        opensearch_client = mock.MagicMock
        opensearch_client.opensearch_domains = []
        opensearch_client.opensearch_domains.append(
            OpenSearchDomain(
                name=domain_name, region=AWS_REGION_EU_WEST_1, arn=domain_arn
            )
        )
        opensearch_client.opensearch_domains[0].logging = []
        opensearch_client.opensearch_domains[0].logging.append(
            PublishingLoggingOption(name="SEARCH_SLOW_LOGS", enabled=True)
        )

        with mock.patch(
            "prowler.providers.aws.services.opensearch.opensearch_service.OpenSearchService",
            new=opensearch_client,
        ), mock.patch(
            "prowler.providers.aws.services.opensearch.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_client",
            new=opensearch_client,
        ):
            from prowler.providers.aws.services.opensearch.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_service_domains_cloudwatch_logging_enabled import (
                opensearch_service_domains_cloudwatch_logging_enabled,
            )

            check = opensearch_service_domains_cloudwatch_logging_enabled()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search(
                "SEARCH_SLOW_LOGS enabled but INDEX_SLOW_LOGS disabled",
                result[0].status_extended,
            )
            assert result[0].resource_id == domain_name
            assert result[0].resource_arn == domain_arn

    def test_logging_INDEX_SLOW_LOGS_enabled(self):
        opensearch_client = mock.MagicMock
        opensearch_client.opensearch_domains = []
        opensearch_client.opensearch_domains.append(
            OpenSearchDomain(
                name=domain_name, region=AWS_REGION_EU_WEST_1, arn=domain_arn
            )
        )
        opensearch_client.opensearch_domains[0].logging = []
        opensearch_client.opensearch_domains[0].logging.append(
            PublishingLoggingOption(name="INDEX_SLOW_LOGS", enabled=True)
        )

        with mock.patch(
            "prowler.providers.aws.services.opensearch.opensearch_service.OpenSearchService",
            new=opensearch_client,
        ), mock.patch(
            "prowler.providers.aws.services.opensearch.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_client",
            new=opensearch_client,
        ):
            from prowler.providers.aws.services.opensearch.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_service_domains_cloudwatch_logging_enabled import (
                opensearch_service_domains_cloudwatch_logging_enabled,
            )

            check = opensearch_service_domains_cloudwatch_logging_enabled()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search(
                "INDEX_SLOW_LOGS enabled but SEARCH_SLOW_LOGS disabled",
                result[0].status_extended,
            )
            assert result[0].resource_id == domain_name
            assert result[0].resource_arn == domain_arn

    def test_logging_INDEX_SLOW_LOGS_and_SEARCH_SLOW_LOGS_enabled(self):
        opensearch_client = mock.MagicMock
        opensearch_client.opensearch_domains = []
        opensearch_client.opensearch_domains.append(
            OpenSearchDomain(
                name=domain_name, region=AWS_REGION_EU_WEST_1, arn=domain_arn
            )
        )
        opensearch_client.opensearch_domains[0].logging = []
        logging_options = [
            PublishingLoggingOption(name="INDEX_SLOW_LOGS", enabled=True),
            PublishingLoggingOption(name="SEARCH_SLOW_LOGS", enabled=True),
        ]
        opensearch_client.opensearch_domains[0].logging.extend(logging_options)

        with mock.patch(
            "prowler.providers.aws.services.opensearch.opensearch_service.OpenSearchService",
            new=opensearch_client,
        ), mock.patch(
            "prowler.providers.aws.services.opensearch.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_client",
            new=opensearch_client,
        ):
            from prowler.providers.aws.services.opensearch.opensearch_service_domains_cloudwatch_logging_enabled.opensearch_service_domains_cloudwatch_logging_enabled import (
                opensearch_service_domains_cloudwatch_logging_enabled,
            )

            check = opensearch_service_domains_cloudwatch_logging_enabled()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert search(
                "SEARCH_SLOW_LOGS and INDEX_SLOW_LOGS enabled",
                result[0].status_extended,
            )
            assert result[0].resource_id == domain_name
            assert result[0].resource_arn == domain_arn
