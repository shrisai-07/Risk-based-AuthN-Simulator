Risk-Based AuthN Simulator

A rule-based authentication risk simulator that demonstrates how modern identity platforms evaluate login attempts and decide whether to allow access, require additional verification, or block a login attempt.

This project focuses on post-password decision logic, showing how authentication systems reason about risk, context, and trust after credentials have already been provided.

Table of Contents

Overview

What Problem This Project Addresses

Objectives

Important Scope Disclaimer

How the Simulator Works

Risk Signals Used

Risk Priority Model

Risk Scoring and Decision Logic

Authentication Outcomes

Core Security Concepts Explained

Why Rule-Based Logic Is Used

What This Project Is Not

Intended Audience

Learning Outcomes

Final Note

Overview

Modern identity platforms no longer rely solely on usernames and passwords to make access decisions.
Instead, they evaluate the context of each login attempt and assign a risk level before deciding how much trust to grant.

The Risk-Based AuthN Simulator is a simplified, transparent model of this process.

It is designed to help understand:

how login risk is evaluated,

why multiple weak signals matter more together,

and how Conditional Access decisions are made in real systems.

All logic in this project is explicit, explainable, and deterministic.

What Problem This Project Addresses

Passwords alone are no longer sufficient to protect identities.

Common real-world issues include:

credential theft via phishing,

password reuse,

logins from unfamiliar locations or devices,

automated brute-force attempts.

Modern identity systems therefore ask a different question:

“Given this login attempt, how confident are we that this is the legitimate user?”

This project models how that confidence is evaluated.

Objectives
Objective	Description
Risk Awareness	Demonstrate how login context affects trust
Conditional Decisions	Show how access decisions adapt to risk
MFA Justification	Explain when and why MFA is required
Zero Trust Thinking	Illustrate trust evaluation per login
Post-Password Security	Highlight what happens after authentication
Important Scope Disclaimer

This project is a learning and demonstration model.

It intentionally simulates inputs instead of collecting real telemetry in order to isolate and explain decision logic clearly.

The simulator focuses on how decisions are made, not on how signals are collected.

How the Simulator Works

Each login attempt is evaluated using contextual risk signals commonly used by modern identity providers.

The simulator:

Receives simulated login context

Assigns risk values to each triggered signal

Aggregates risk into a single score

Maps the score to an authentication decision

The process mirrors the internal reasoning of Conditional Access engines.

Risk Signals Used

The simulator evaluates four contextual signals:

Login Location
Whether the login originates from a known or new geographic location.

Device Trust
Whether the device has been previously seen or is unknown.

Time of Login
Whether the login occurs during expected or unusual hours.

Failed Login Attempts
The number of failed attempts preceding a successful login.

Each signal represents a loss of confidence, not proof of malicious intent.

Risk Priority Model

Not all signals are equally dangerous.

The simulator assigns priority in the following order:

Failed Attempts > Location > Device > Time

Why priority matters

Some behaviors strongly correlate with attacks

Others are weaker indicators on their own

Risk emerges through correlation, not isolation

For example:

A new location alone may indicate travel

An unknown device alone may indicate a new phone

Multiple failed attempts strongly suggest misuse

This priority model reflects how real security systems weigh signals differently.

Risk Scoring and Decision Logic

Each triggered signal adds a risk value to the total score.

Key principles:

Individual signals rarely indicate severe threat alone

Multiple overlapping signals increase risk significantly

The score represents confidence degradation, not guilt

The final score determines how cautiously the system responds.

Authentication Outcomes

Based on the calculated risk score, the system recommends one of three actions:

Allow Access

Low risk

Login behavior aligns with expected patterns

Require Multi-Factor Authentication (MFA)

Moderate risk

Additional verification is required to increase confidence

Block or Escalate Login Attempt

High risk

Strong indicators of compromise or abuse

This mirrors real Conditional Access behavior in enterprise environments.

Core Security Concepts Explained
Zero Trust Model

Zero Trust operates on the principle:

Never trust by default. Always verify.

Even valid credentials do not automatically imply trust.

In Zero Trust:

Every login is evaluated independently

Trust is dynamic and contextual

Network location alone provides no assurance

How this project demonstrates Zero Trust
Each login attempt is evaluated from scratch using contextual signals, regardless of prior access.

Conditional Access

Conditional Access enforces Zero Trust decisions.

Instead of binary allow/deny logic, it asks:

“Given the current risk, what level of access is appropriate?”

How this project demonstrates Conditional Access
The simulator adapts its response based on calculated risk, not identity alone.

Trust but Verify

Passwords verify identity claims, not legitimacy of behavior.

A correct password may still be used by an attacker.

How this project demonstrates Trust but Verify
The simulator assumes authentication succeeded and evaluates whether the surrounding behavior deserves trust.

Purpose of Multi-Factor Authentication (MFA)

MFA is not a punishment or blanket security measure.

Its purpose is to:

increase confidence when risk is elevated,

compensate for uncertainty in login context.

How this project demonstrates MFA’s purpose
MFA is triggered only when risk crosses a threshold, showing it as a risk-response mechanism.

Risk-Based Authentication

Risk-based authentication evaluates likelihood of misuse, not certainty.

Important characteristics:

Signals are weak individually

Risk emerges through correlation

Some signals carry more weight than others

How this project demonstrates risk-based authentication
The simulator aggregates multiple contextual signals into a single risk-based decision.

Post-Password Security Thinking

Modern systems assume passwords will eventually fail.

As a result:

Passwords are treated as a baseline check

Real security decisions happen after authentication

How this project demonstrates post-password security
All logic begins after password validation and focuses entirely on contextual evaluation.

Why Rule-Based Logic Is Used

This project intentionally uses a rule-based model instead of machine learning.

Reasons:

Decisions are transparent and explainable

Behavior is deterministic and auditable

Logic mirrors real Conditional Access policy engines

In production systems:

ML often generates risk signals

Rule-based engines enforce access decisions

This project models the policy enforcement layer.

What This Project Is Not

To maintain clarity, this project does not:

Collect real IP or device telemetry

Use machine learning models

Act as a real authentication service

Enforce access on real users

All inputs are simulated to focus purely on decision-making logic.

Intended Audience

Students learning identity and access management

Beginners exploring Zero Trust concepts

Security enthusiasts seeking conceptual clarity

Anyone curious about how login decisions are actually made

Learning Outcomes

By building and experimenting with this simulator, you will understand:

why context matters in authentication,

how risk accumulates,

why MFA is triggered selectively,

how modern identity platforms reason beyond passwords.

Final Note

This project is not about complexity.

It is about making modern security reasoning visible.

Authentication today is not a single yes-or-no decision.
It is a continuous evaluation of trust under uncertainty.

This simulator exists to make that process understandable.