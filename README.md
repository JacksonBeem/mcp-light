# EC2 Light Tier MCP Runtime

This repo has been repurposed from the old custom high-workload prototype into a light-tier EC2 MCP host that matches the `light` server set defined in [`mcp-benchmark/sam/poc/template.yaml`](../../mcp-benchmark/sam/poc/template.yaml) and [`mcp-benchmark/sam/profiles/tiered.json`](../../mcp-benchmark/sam/profiles/tiered.json).

## Light Tier Servers

The runtime exposes the same 10 light-tier servers used by `mcp-benchmark`:

1. `fruityvice-mcp`
2. `math-mcp`
3. `call-for-papers-mcp`
4. `mcp-hn`
5. `hugeicons-mcp-server`
6. `movie-recommender-mcp`
7. `time-mcp`
8. `unit-converter-mcp`
9. `okx-mcp`
10. `wikipedia-mcp`

## Repo Layout

- `ec2/light-route-config.json`
  Route definition for the benchmark light tier.
- `ec2/install-light.sh`
  Clones and prepares the 10 benchmark light-tier servers on an EC2 host.
- `ec2/bootstrap-light-host.sh`
  Installs system dependencies, builds the local runtime, and starts the service with PM2.
- `ec2/ecosystem.config.cjs`
  PM2 app definition for the light runtime.
- `ec2/runtime/`
  Node/Fastify MCP runtime that bridges streamable HTTP requests to the hosted stdio MCP servers.
- `ec2_instances/server_high.py`
  Legacy heavy-workload prototype retained for reference only. It is no longer the primary runtime for this repo.

## Runtime Endpoints

- `http://127.0.0.1:3000/light/mcp`
  Light-tier MCP endpoint.
- `http://127.0.0.1:3000/light/health`
  Health check that reports the configured light-tier servers.

## EC2 Setup

Run this on the instance after cloning the repo:

```bash
bash ec2/bootstrap-light-host.sh
```

That script:

1. Installs Node.js, Git, and Python if needed.
2. Clones the 10 light-tier MCP server repositories into `./servers`.
3. Builds the local runtime in `ec2/runtime`.
4. Starts the runtime with PM2.

## Docker

`Docker/Dockerfile` now builds the light-tier runtime instead of the old Python workload server. It expects a populated `servers/` directory in the build context.

Example build from `c:\VScode`:

```bash
docker build -f Co-Work/mcp-benchmark-high/Docker/Dockerfile -t mcp-benchmark-light .
```

## Notes

- The light-tier server list here intentionally mirrors `mcp-benchmark`; that benchmark repo remains the source of truth for tier membership.
- The old heavy benchmark response samples under `high_responses/` were left untouched because they may still be useful as historical data.
