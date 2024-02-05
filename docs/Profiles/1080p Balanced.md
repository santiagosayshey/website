---
title: 1080p Balanced
date: 2024-01-26
---
## Overview

The 1080p Balanced profile provides an emphasis on space efficiency and streaming optimisation, while still retaining some audio and visual fidelity. It is available in 2 formats - Full and Single Grab. These formats affect only the immutability of the profile.

This profile prioritises high quality WEB sources i.e. Movies Anywhere, Amazon and APTV, with fallbacks to lower tier WEB sources - Netflix, Hulu, etc. After the weakest WEB sources, it uses the same release group ranking to find transparent encodes, then SD remuxes and encodes if nothing else is available.

In addition to tier 1 WEB sources, a special consideration for encodes by *BHDStudio* has been added to the scoring breakdown. While not preferred over the tier 1 WEB sources, they are ranked above any other Blu-ray encodes due to their emphasis on streaming optimised encodes. They are not ranked higher than WEB tier 1 sources due to their lack of subtitles. They're roughly equivalent to a high to mid tier WEB source in terms of fidelity. These encodes are extremely useful as many releases don't have a streaming option available. 

### Installation

Review the guide on [Importing Profiles & Custom Formats](../Wiki/Importing%20Profiles%20&%20Custom%20Formats.md) to import the necessary custom formats and profiles inside your Radarr / Sonarr installation.

When prompted to select a profile, choose 1080p Balanced in your preferred immutability. 

## Score Breakdown

| Resolution | Source | Codec | Internal | Audio | Extras | Indexer Flags | Score | Upgrade |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1080p | Movies Anywhere |  |  |  |  |  | 220 | 500 |
|  | Amazon Prime |  |  |  |  |  | 210 |  |
|  | Apple TV+ |  |  |  |  |  |  |  |
|  | Disney+ |  |  |  |  |  | 200 |  |
|  | Netflix |  |  |  |  |  |  |  |
|  | HBOMax |  |  |  |  |  |  |  |
|  | Hulu |  |  |  |  |  | 190 |  |
|  | Peacock |  |  |  |  |  |  |  |
|  | Paramount+ |  |  |  |  |  |  |  |
|  | Roku |  |  |  |  |  |  |  |
|  | iTunes |  | BHDStudio |  |  |  | 90 |  |
|  |  |  | HD Tier 1 |  |  | 1080p Golden Popcorn | 80 |  |
|  |  |  |  |  |  | Stream Optimised |  |  |
|  |  |  | HD Tier 2 |  |  |  | 70 |  |
|  |  |  | HD Tier 3 |  |  |  | 60 |  |
|  |  |  | HD Tier 4 |  |  |  | 50 |  |
|  |  | DVD Remux | HD Tier 5 |  |  |  | 40 |  |
|  |  |  | HD Tier 6 |  |  | HDB Internal | 30 |  |
|  |  |  | SD Tier 1 |  |  | SD Golden Popcorn |  |  |
|  |  |  | HD Tier 7 |  | Special Edition |  | 20 |  |
|  |  |  | SD Tier 2 |  |  |  |  |  |
|  | Blu-Ray | h264 |  | Atmos | IMAX |  | 10 |  |
|  | WEBRIP |  |  |  | Criterion |  |  |  |
| 480p | DVD | Xvid |  | FLAC |  |  | 0 |  |
|  |  |  |  | DD+ |  |  |  |  |
|  |  |  |  | DTS |  |  |  |  |
|  |  |  |  | DD |  |  |  |  |
| 720p |  | BD Remux |  | TrueHD | Special Features |  | -9999 |  |
| 2160p |  | x265 |  | DTS-HD MA |  |  |  |  |
|  |  | h265 |  | DTS-X |  |  |  |  |

A breakdown of each of the internal tiers can be found here: [Release Group Tiers](../Wiki/Release%20Group%20Tiers.md)

## Quality Profiles

| Grouping | Quality Profiles |
| ---- | ---- |
| Balanced Capable | WEBDL-1080p |
|  | Bluray-1080p |
|  | WEBRip-1080p |
| Fallbacks | HDTV-1080p |
|  | WEBDL-480p |
|  | DVD |
