# Chapter 4 — Supported Launchpads

## Overview

BlackBull Agent integrates with several Solana launchpads, each with different fee mechanics that the engine needs to understand in order to track and route revenue correctly.

## Meteora

Meteora pools expose fee accrual data that the engine polls to estimate available liquidity-support capacity.

## Pump.fun

Pump.fun tokens generate creator fees as trading volume accrues; the engine detects these and applies the team's configured routing percentage.

## Kickstart

Kickstart-launched tokens follow a similar model, with launchpad-specific account structures the engine adapts to automatically.

## Adding New Launchpads

Each launchpad integration is implemented as an adapter (see `code/launchpads/`) that normalizes fee data into a common format the rest of the engine consumes.
