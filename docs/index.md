---
title: Ahoy!
draft: false
date: 2023-09-17
tags: []
---

Welcome to Dictionarry! This project aims to simplify media automation via tailored custom formats & profiles via Radarr & Sonarr.

## Background

I often get questions from friends who I've introduced to torrenting about which releases to grab - is 4k better than 1080p? Should I grab SDR / HDR? Difference between x264/5, etc. The list goes on.

I wanted to create this project to try and abstract the technical nitty gritty from torrents, and turn them into quantifiable questions about the movies they want and fully automate the process of downloading those movies according to their needs. This culminated in a collection of Radarr profiles + custom formats, each of which are designed at fufilling a combination of specific needs:

1. Quality - How good do I want the movie to look?
2. Efficiency - How big should the file be?
3. Universality - Can I play it on my machine?
4. Immutability - Do I want to upgrade if a better version comes out?

## How?

I've created a [Flowchart](./Profiles/index.md) that turns the answers to these questions into a profile which automates the process in which releases are selected in Radarr.

Once you've found your desired profile, check out [Profilarr](./Wiki/Importing%20Profiles%20&%20Custom%20Formats.md) for mass importing custom formats and profiles

## What Else?

I've tried to streamline and abstract this process as much as possible, but for those of you who wish to iterate on my custom formats and profiles, I've provided the raw
json for all the custom formats I've used. These can be imported into Radarr / Sonarr and adjusted to suit your needs.
