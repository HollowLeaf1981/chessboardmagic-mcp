import asyncio
import os
import aiohttp
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, CallToolResult

API_BASE = "https://api.chessboardmagic.com"

server = Server("chessboard-magic")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="get_repertoires",
            description="Fetch your chess repertoires from the Chessboard Magic Repertoire Builder",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_games",
            description="Fetch your chess games from the Chessboard Magic Repertoire Builder",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_game_details",
            description="Fetch a single game's metadata, moves, tags, variations and comment links",
            inputSchema={
                "type": "object",
                "properties": {
                    "gameId": {"type": "string"}
                },
                "required": ["gameId"]
            }
        ),
        Tool(
            name="get_repertoire_details",
            description="Fetch a single repertoire's metadata, moves, variations and comment links",
            inputSchema={
                "type": "object",
                "properties": {
                    "repertoireId": {"type": "string"}
                },
                "required": ["repertoireId"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name not in ["get_repertoires", "get_games", "get_game_details", "get_repertoire_details"]:
        return CallToolResult(
            content=[TextContent(type="text", text=f"Unknown tool: {name}")]
        )

    pat = os.environ.get("CHESSBOARD_MAGIC_PAT")
    if not pat:
        return CallToolResult(
            content=[TextContent(type="text", text="Missing Personal Access Token (PAT)")]
        )

    # Determine endpoint
    if name == "get_game_details":
        game_id = arguments.get("gameId")
        if not game_id:
            return CallToolResult(
                content=[TextContent(type="text", text="Missing required argument: gameId")]
            )
        url = f"{API_BASE}/mcp/games/{game_id}"
    elif name == "get_repertoire_details":
        repertoire_id = arguments.get("repertoireId")
        if not repertoire_id:
            return CallToolResult(
                content=[TextContent(type="text", text="Missing required argument: repertoireId")]
            )
        url = f"{API_BASE}/mcp/repertoires/{repertoire_id}"
    else:
        endpoint = "repertoires" if name == "get_repertoires" else "games"
        url = f"{API_BASE}/mcp/{endpoint}"

    async with aiohttp.ClientSession() as session:
        async def do_request():
            async with session.get(url, headers={"Authorization": f"Bearer {pat}"}) as resp:
                try:
                    data = await resp.json()
                except Exception:
                    return CallToolResult(
                        content=[TextContent(type="text", text=f"Invalid JSON response (status {resp.status})")]
                    )

                if resp.status != 200:
                    return CallToolResult(
                        content=[TextContent(type="text", text=f"API error: {data}")]
                    )

                return CallToolResult(
                    content=[TextContent(type="text", text=str(data))]
                )

        return await do_request()

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())