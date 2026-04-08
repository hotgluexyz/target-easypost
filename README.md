# target-easypost

`target-easypost` is a Singer target for [EasyPost](https://www.easypost.com/), built with the Hotglue Singer SDK.

## Overview

This target syncs data to EasyPost over their REST API. It uses a generic sink: each Singer stream name is sent to `POST /{stream}` for creates and `PATCH /{stream}/{id}` when a record includes an `id` (update).

## Installation

```bash
pip install target-easypost
```

Or install from source:

```bash
git clone https://github.com/hotglue/target-easypost.git
cd target-easypost
pip install .
```

## Configuration

### Required settings

| Setting   | Description |
|-----------|-------------|
| `api_key` | Your EasyPost API key (sent as the HTTP Basic auth username; password is empty) |

### Optional settings

| Setting   | Description |
|-----------|-------------|
| `sandbox` | Reserved for future use. EasyPost test vs production is determined by your API key. |

Create a `config.json` file (example—add fields your environment needs):

```json
{
  "api_key": "your-easypost-api-key",
  "sandbox": false
}
```

### API base URLs

The sink uses the EasyPost API v2 base URL:

- **`https://api.easypost.com/v2`**

Confirm paths and behavior against the [EasyPost API documentation](https://docs.easypost.com/) for your integration.

## Supported streams

There is no fixed list of streams in code: any stream name from the tap is used as the API path segment. Payload shape must match what the EasyPost API expects for that resource.

**Create:** records without an `id` (or with `id` removed before send, depending on stream) are sent with `POST /{stream_name}` as a JSON array with one element.

**Update:** records that still have an `id` after processing use `PATCH /{stream_name}/{id}` with the record body.

## Usage

### Running the target

```bash
# Display version
target-easypost --version

# Display help
target-easypost --help

# Run with a tap
tap-some-source | target-easypost --config config.json
```

## Development

### Setup

```bash
# Install poetry
pipx install poetry

# Install dependencies
poetry install
```

### Running tests

```bash
poetry run pytest
```

### CLI testing

```bash
poetry run target-easypost --help
```

## License

Apache 2.0
