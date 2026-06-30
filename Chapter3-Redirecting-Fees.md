# Chapter 3 — Redirecting Fees

## Overview

Fee redirection is the core authorization step: the team grants the engine permission to route a defined share of trading or creator fees into the liquidity engine's operating wallet.

## Routing Model

Fee routing is configurable, not all-or-nothing. Teams can choose:

- What percentage of incoming fees is redirected
- Whether routing can be paused or revoked at any time
- Which destination wallet receives the routed share

## Revocable by Design

Every redirection grant is revocable from the dashboard. There is no on-chain lock-in that prevents a team from turning routing off if priorities change.

## Common Pitfalls

- Redirecting 100% of fees with no operating buffer for the project itself
- Forgetting that routing changes can take one settlement cycle to propagate
