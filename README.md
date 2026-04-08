# target-easypost

`target-easypost` is a Singer target for [EasyPost](https://www.easypost.com/), built with the Hotglue Singer SDK.

## Overview

This target writes **shipments** to EasyPost only. For each record on the `shipments` Singer stream it creates a shipment with `POST /shipments` (relative to the v2 base URL below), then buys a label with `POST /shipments/{id}/buy` using the **first** rate returned. **Updates are not supported**

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

| Stream      | Behavior |
|-------------|----------|
| `shipments` | `POST /shipments` with the record body as JSON. If EasyPost returns no `rates`, the target raises an error. Otherwise it buys a label with the first rate (`POST /shipments/{id}/buy`). |

Only the `shipments` stream is implemented. Other stream names are not handled by this target. Payload shape must match the [EasyPost Shipment object](https://docs.easypost.com/docs/shipments) for creation.

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
