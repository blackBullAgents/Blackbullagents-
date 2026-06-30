# Chapter 5 — The Liquidity Engine

## Overview

This chapter covers how routed fees are converted into market-making activity — the "let the bull run" stage.

## Core Loop

1. Detect new fee inflow to the operating wallet
2. Evaluate current market conditions (spread, depth, recent volatility)
3. Place liquidity-supporting orders sized to the available balance
4. Log every action for later review on the dashboard

## Automated Liquidity Support

The engine continuously monitors pool depth and intervenes when conditions suggest support is needed, rather than running on a fixed schedule.

## Fee-Powered Market Making

Because the engine's capital comes directly from the token's own fee stream, its market-making capacity grows in proportion to trading activity — it does not rely on an external treasury.
