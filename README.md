# Chessboard Magic Repertoire Builder – MCP Server

This repository provides the **official MCP Server** for accessing your **repertoires and games** inside AI assistants that support the **Model Context Protocol (MCP)**, such as **Claude Desktop**.

It allows you to retrieve your repertoires, games, and game details directly from your Repertoire Builder account through natural language.

## Access Requirements

This MCP is **only available to subscribers**.

You must generate a **Personal Access Token (PAT)**:

1. Open **Edit Profile** inside the Repertoire Builder
2. Go to **API Access**
3. Click **Generate Key**
4. Copy your PAT and **store it somewhere safe**

   - You can always generate a new token if needed.

## Installation

Install dependencies:

```bash
pip install aiohttp mcp
```

Clone the repository:

```bash
git clone https://github.com/<yourrepo>/chessboardmagic-mcp.git
cd chessboardmagic-mcp
```

Claude Desktop (or other Desktop AI) will run the MCP server automatically.
You do **not** launch it manually.

## Using with Claude Desktop

Requirements:

- **Claude Pro**
- **Claude Desktop installed**

Edit your `claude_desktop_config.json` and add:

```json
{
  "mcpServers": {
    "chessboard-magic": {
      "command": "python",
      "args": ["C:/Users/USERNAME/Downloads/chessboardmagic-mcp/mcp_server.py"],
      "env": {
        "CHESSBOARD_MAGIC_PAT": "REPLACE_WITH_YOUR_PAT"
      }
    }
  }
}
```

Replace `REPLACE_WITH_YOUR_PAT` with your actual PAT.

Restart Claude Desktop.

## Example Usage

`Can you give me a summary of my games?`

Based on your 110 chess games, here's a summary:

### Overall Performance

- Rating: Around 1960-2016 (fluctuating in the 1900-2000 range)
- Total Games: 110 rapid games (10 min + 0 sec)
- Win-Loss Record: Mixed results with wins, losses, and draws

### Opening Preferences

As White, you primarily play:

- English Opening (c4) - Your most common choice
- King's English Variation (c4 e5)
- Anglo-Indian Defense
- Symmetrical Variations
- Queen's Pawn formations (d4) occasionally

As Black, you face various openings and often choose:

- Caro-Kann Defense (very frequently) against e4
- King's Indian Defense structures against d4
- Dutch Defense occasionally

### Key Patterns

- You show a clear preference for flexible, positional openings rather than sharp tactical lines
- Most games reach complex middlegames with 50-100+ moves
- Many games end in endgames, suggesting you're comfortable in technical positions
- Mix of results against opponents rated 1850-2140

### Time Control

All games are Rapid (10 minutes with no increment), which suits your style of reaching long, strategic battles.

Would you like me to analyze specific aspects of your play, such as your performance with particular openings or against certain defenses?

`Yes please, what openings with white and black do I do well at`.

Looking at your games, here's your performance breakdown by opening:

### Your Best Openings as White

English Opening - King's English Variation (c4 e5)

Record: Strong performance overall
Notable wins:

- vs Dr_anas_almuhammad (1-0, mate)
- vs hruaia (1-0, 70-move endgame)
- vs Chess_king1749 (1-0)
- vs hyBvDten (1-0)

Note: This is your most successful and frequently played opening. You seem very comfortable in the positions it creates.

English Opening - Anglo-Indian Defense (c4 Nf6)

Mixed results but decent win rate
Good games against lower-rated opponents

### Openings to Avoid as White

Queen's Pawn Stonewall formations - You lost multiple games with this setup:

- Lost to Pion_Cogreg (0-1)
- Lost to Tahaa021 (0-1)

Against the Sicilian - Limited sample, but struggled:

- Lost to Ryzvelt playing e4 c5 (0-1, resigned move 32)

### Your Best Openings as Black

Caro-Kann Defense - Your most reliable weapon

Strong wins:

- vs fitilastrus (0-1) - you won
- vs agus-m (0-1, 62-move technical win)
- vs Gambit_Enjoyer1 (0-1)
- vs g8h637fG (0-1)
- vs Daniel_Barross (0-1, excellent 57-move endgame)
- vs zBamMsKu (0-1)

You have an excellent win rate with the Caro-Kann, particularly in longer games

King's Indian Defense structures

Good results:

- vs Ed_Millennium (0-1, 66-move win on time)
- vs JWuEcjDC (0-1, resigned move 25)
- Drew vs beklya (½-½, 68 moves)

### Openings to Avoid as Black

Alekhine Defense - Poor results:

- Lost to vonstolzing (1-0)
- Lost to art22890b (1-0)
- Lost to OVIS4lWT (1-0)

Against less common lines (Bird's Opening, Polish Opening)

Mixed results, but you seem less prepared

### Key Recommendation

Stick with:

White: English Opening with c4, especially after 1.c4 e5
Black: Caro-Kann Defense - this is clearly your strongest opening with excellent winning percentages and great endgame outcomes

Consider avoiding:

White: Queen's Pawn Stonewall structures (d4, e3, Bd3, f4)
Black: Alekhine Defense (you have 0% success rate with it)

Your best games tend to be long, strategic battles where you outplay opponents in the endgame - this fits perfectly with the English Opening and Caro-Kann!
