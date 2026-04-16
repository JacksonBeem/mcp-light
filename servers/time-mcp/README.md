# MCP Time Server

This is the MCP (Model Context Protocol) Time Server, extracted from the official [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) repository.

## Source

This server was originally located at:
- Repository: https://github.com/modelcontextprotocol/servers
- Path: `/src/time`
- Original commit: Extracted from the main branch

## Description

A Model Context Protocol server that provides time and timezone functionality. This server enables LLMs to get current time information across different timezones.

## Features

- Get current time in any timezone
- List available timezones
- Convert times between timezones

## Installation

```bash
# Using pip
pip install -e .

# Using uv
uv pip install -e .
```

## Usage

The server can be used with any MCP-compatible client.

## License

This project maintains the same license as the original modelcontextprotocol/servers repository.

## Acknowledgments

All credit goes to the original authors at Anthropic and contributors to the modelcontextprotocol/servers project.