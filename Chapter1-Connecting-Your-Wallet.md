# Chapter 1 — Connecting Your Wallet

## Overview

The first step in onboarding to BlackBull Agent is connecting a Solana-compatible wallet. This establishes the identity the system uses to associate a token with its fee-routing configuration.

## Supported Wallets

The platform supports the common Solana wallet providers used by token teams and individual operators. Wallet connection is read-permission only at this stage — no transaction signing occurs until a fee redirection is explicitly authorized later in the flow.

## What Happens on Connect

1. The wallet's public key is read.
2. The system checks for any tokens already associated with that address.
3. The user is routed to token selection (see Chapter 2).

## Design Notes

Keeping wallet connection separate from fee authorization is a deliberate security boundary: a user can browse the dashboard and review their token's eligibility without granting any spending or routing permissions.
