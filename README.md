# Skill Discovery

This little project is a "hack" developed as part of [MetaFest](https://metafest.metagame.wtf) 2021.

### Objective

Create a graphical representation of people skills and interests.

### Why?

To facilitate social bonding and skills exchange:

 * Find someone that has skill S, which you are looking for
 * Find what skills/interests you have in common with person P
 * Get a general feel of the interests within a community
 * ...

## Project structure

At the moment, this project consists of a single script that ingests data in CSV format and produces a .dot file (a.k.a. GraphViz format).

The idea is to start from here and incrementally make this better and more useful.

 * Slurp data from Discord (where people can self-report their skills in a special channel)
 * Calculate edges with different heuristics to highlight different aspects of the network
 * Allow filtering of people and skills
 * Create interactive web-based visualizations
 * ...
