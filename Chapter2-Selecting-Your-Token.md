# Chapter 2 — Selecting Your Token

## Overview

Once a wallet is connected, the team selects the token they want the engine to support. The token must be associated with a supported launchpad (see Chapter 4) so that fee streams can be detected automatically.

## Token Eligibility

A token typically needs:

- An active liquidity pool on a supported venue
- A discoverable fee-collection mechanism (creator fees, trading fees, etc.)
- A wallet with authority over that fee stream

## Selection Flow

1. Search or paste the token's mint address.
2. The system verifies the token's launchpad and current liquidity state.
3. The team reviews estimated fee volume before proceeding to fee redirection.

## Why This Matters

Token selection determines which liquidity pools the engine will monitor and which fee stream it will draw from. Getting this step right ensures the rest of the pipeline behaves predictably.
