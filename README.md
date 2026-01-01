# Risk-Based AuthN Simulator

A rule based authentication risk simulator that demonstrates how modern identity platforms evaluate login attempts and decide whether to allow access, require additional verification, or block a login attempt.

This project focuses on post password decision logic and explains how authentication systems reason about risk, context, and trust after credentials have already been provided.

---

## Table of Contents

1. Overview  
2. What Problem This Project Addresses  
3. Objectives  
4. Important Scope Disclaimer  
5. How the Simulator Works  
6. Risk Signals Used  
7. Risk Priority Model  
8. Risk Scoring and Decision Logic  
9. Authentication Outcomes  
10. Core Security Concepts Explained  
11. Why Rule Based Logic Is Used  
12. What This Project Is Not  
13. Intended Audience  
14. Learning Outcomes  
15. Final Note  

---

## Overview

Modern identity platforms no longer rely solely on usernames and passwords to make access decisions.  
Instead, they evaluate the context of each login attempt and assign a risk level before deciding how much trust to grant.

The Risk Based AuthN Simulator is a simplified and transparent model of this process.

It is designed to help understand:

1. How login risk is evaluated  
2. Why multiple weak signals matter more when combined  
3. How Conditional Access decisions are made in real systems  

All logic in this project is explicit, explainable, and deterministic.

---

## What Problem This Project Addresses

Passwords alone are no longer sufficient to protect identities.

Common real world issues include:

1. Credential theft through phishing  
2. Password reuse across services  
3. Logins from unfamiliar locations or devices  
4. Automated brute force attempts  

Modern identity systems therefore ask a different question:

How confident are we that this login attempt belongs to the legitimate user?

This project models how that confidence is evaluated.

---

## Objectives

1. Demonstrate how login context affects trust decisions  
2. Show how access decisions adapt dynamically to risk  
3. Explain when and why Multi Factor Authentication is required  
4. Illustrate Zero Trust evaluation on every login attempt  
5. Highlight what happens after authentication succeeds  

---

## Important Scope Disclaimer

This project is a learning and demonstration model.

It intentionally simulates inputs instead of collecting real telemetry in order to isolate and explain decision logic clearly.

The simulator focuses on how decisions are made rather than how signals are collected.

---

## How the Simulator Works

Each login attempt is evaluated using contextual risk signals commonly used by modern identity providers.

The simulator follows this sequence:

1. Receives simulated login context  
2. Assigns risk values to each triggered signal  
3. Aggregates the values into a single risk score  
4. Maps the score to an authentication decision  

This mirrors the internal reasoning of Conditional Access engines used in enterprise identity platforms.

---

## Risk Signals Used

The simulator evaluates four contextual signals.

### Login Location
Whether the login originates from a known or new geographic location.

### Device Trust
Whether the device has been previously seen or is unknown.

### Time of Login
Whether the login occurs during expected or unusual hours.

### Failed Login Attempts
The number of failed attempts preceding a successful login.

Each signal represents a loss of confidence rather than proof of malicious intent.

---

## Risk Priority Model

Not all signals are equally dangerous.

The simulator assigns priority in the following order:

1. Failed login attempts  
2. Login location  
3. Device trust  
4. Login time  

### Why priority matters

Some behaviors strongly correlate with attacks, while others are weaker indicators on their own.

For example:

1. A new location alone may indicate travel  
2. An unknown device alone may indicate a new phone  
3. Multiple failed attempts strongly suggest misuse  

Risk emerges through correlation rather than isolation.  
This priority model reflects how real security systems weigh signals differently.

---

## Risk Scoring and Decision Logic

Each triggered signal contributes a risk value to the total score.

Key principles include:

1. Individual signals rarely indicate severe threat on their own  
2. Multiple overlapping signals increase risk significantly  
3. The score represents confidence degradation rather than guilt  

The final score determines how cautiously the system responds.

---

## Authentication Outcomes

Based on the calculated risk score, the system recommends one of three actions.

### Allow Access
Used when risk is low and login behavior aligns with expected patterns.

### Require Multi Factor Authentication
Used when risk is moderate and additional verification is required to increase confidence.

### Block or Escalate Login Attempt
Used when risk is high and strong indicators of compromise are present.

This mirrors Conditional Access behavior in enterprise environments.

---

## Core Security Concepts Explained

### Zero Trust Model

Zero Trust operates on the principle that no request should be trusted by default.

Every login attempt is evaluated independently and trust is dynamic and contextual.  
Network location alone does not provide assurance.

The simulator evaluates every login from scratch using contextual signals.

---

### Conditional Access

Conditional Access enforces Zero Trust decisions.

Instead of binary allow or deny logic, it asks what level of access is appropriate given the current risk.

The simulator adapts its response based on calculated risk rather than identity alone.

---

### Trust but Verify

Passwords verify identity claims but not legitimacy of behavior.

A correct password can still be used by an attacker.

The simulator assumes authentication succeeded and evaluates whether the surrounding context deserves trust.

---

### Purpose of Multi Factor Authentication

Multi Factor Authentication exists to increase confidence when risk is elevated.

It compensates for uncertainty in login context rather than acting as a blanket security measure.

The simulator triggers MFA only when risk crosses a defined threshold.

---

### Risk Based Authentication

Risk based authentication evaluates likelihood of misuse rather than certainty.

Signals are weak individually, risk emerges through correlation, and some signals carry more weight than others.

The simulator aggregates contextual signals into a single risk based decision.

---

### Post Password Security Thinking

Modern systems assume passwords will eventually fail.

Passwords are treated as a baseline check and real security decisions happen after authentication.

The simulator focuses entirely on post password contextual evaluation.

---

## Why Rule Based Logic Is Used

This project intentionally uses a rule based model instead of machine learning.

Reasons include:

1. Decisions remain transparent and explainable  
2. Behavior is deterministic and auditable  
3. Logic mirrors real Conditional Access policy engines  

In production systems, machine learning often generates risk signals while rule based engines enforce access decisions.

This project models the policy enforcement layer.

---

## What This Project Is Not

To maintain clarity, this project does not:

1. Collect real IP or device telemetry  
2. Use machine learning models  
3. Act as a real authentication service  
4. Enforce access on real users  

All inputs are simulated to focus purely on decision making logic.

---

## Intended Audience

1. Students learning identity and access management  
2. Beginners exploring Zero Trust concepts  
3. Security enthusiasts seeking conceptual clarity  
4. Anyone curious about how login decisions are actually made  

---

## Learning Outcomes

By building and experimenting with this simulator, you will understand:

1. Why context matters in authentication  
2. How risk accumulates across signals  
3. Why MFA is triggered selectively  
4. How modern identity platforms reason beyond passwords  

---

## Final Note

This project is not about complexity.

It is about making modern security reasoning visible.

Authentication today is not a single yes or no decision.  
It is a continuous evaluation of trust under uncertainty.

This simulator exists to make that process understandable.
