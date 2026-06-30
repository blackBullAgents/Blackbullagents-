"""
dashboard/metrics.py

Placeholder for computing the real-time market health metrics
shown on the token dashboard.
"""

def market_health(spread: float, depth: float, volatility: float) -> str:
    """Return a simple health label given basic market inputs."""
    if depth > 0 and spread / depth < 0.01 and volatility < 0.05:
        return "healthy"
    if depth > 0 and spread / depth < 0.03:
        return "watch"
    return "thin"
