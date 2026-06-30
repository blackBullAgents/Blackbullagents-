"""
fees/router.py

Scaffolding for the fee-routing configuration described in
docs/part2/Chapter3-Redirecting-Fees.md.
"""

class FeeRouter:
    def __init__(self, token_mint: str, routing_pct: float):
        self.token_mint = token_mint
        self.routing_pct = routing_pct
        self.enabled = True

    def update_routing(self, new_pct: float):
        self.routing_pct = new_pct

    def disable(self):
        """Acts as the kill switch for this token's routing."""
        self.enabled = False
