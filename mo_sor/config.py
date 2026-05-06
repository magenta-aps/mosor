# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from fastramqpi.config import Settings as FastRAMQPISettings
from pydantic import BaseSettings
from pydantic import Field


class _Settings(BaseSettings):
    class Config:
        frozen = True
        env_nested_delimiter = "__"

    fastramqpi: FastRAMQPISettings

    httpx_timeout: int = Field(
        30, description="Timeout (seconds) for outgoing HTTP calls."
    )
