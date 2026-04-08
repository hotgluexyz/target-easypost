"""easypost target class."""

from typing import Type
from hotglue_singer_sdk import typing as th
from hotglue_singer_sdk.sinks import Sink
from hotglue_singer_sdk.target_sdk.target import TargetHotglue

from target_easypost.sinks import ShipmentSink


class TargetEasypost(TargetHotglue):
    """Sample target for easypost."""

    name = "target-easypost"

    config_jsonschema = th.PropertiesList(
        th.Property("api_key", th.StringType, required=True),
    ).to_dict()

    SINK_TYPES = [ShipmentSink]

if __name__ == "__main__":
    TargetEasypost.cli()
