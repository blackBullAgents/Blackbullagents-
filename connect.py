"""
wallet/connect.py

Minimal example of reading a connected wallet's public key and checking
for associated tokens. This is illustrative scaffolding, not production code.
"""

def get_wallet_tokens(public_key: str) -> list:
    """Return tokens already associated with this wallet (placeholder)."""
    raise NotImplementedError("Implement wallet -> token lookup here")


def connect_wallet(public_key: str) -> dict:
    """Validate and register a wallet connection (placeholder)."""
    return {"public_key": public_key, "connected": True}
