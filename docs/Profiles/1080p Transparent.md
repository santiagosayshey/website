---
title: 1080p Transparent
date: 2023-10-06
---

## Overview

The 1080p transparent profile aims to provide a balance between quality, size and compatibility.

Rather than relying on audio / video metrics to determine transparency, this profile utilises a unique metric, the [Golden Popcorn Performance Index](../Wiki/Golden%20Popcorn%20Performance%20Index.md), to identify release groups known for their consistent output of quality encodes.

### Installation

Review the guide on [Importing Profiles & Custom Formats](../Wiki/Importing%20Profiles%20&%20Custom%20Formats.md) to import the necessary custom formats and profiles inside your Radarr / Sonarr installation.

When prompted to select a profile, choose 1080p transparent.

## Score Breakdown
| Resolution | Source | Codec | Internal | Audio | Extras | Flags | Score | Upgrade |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|  |  |  | HD T1 |  |  | 1080p GP | 120 | 320 |
|  |  |  | HD T2 |  |  |  | 110 |  |
|  |  |  | HD T3 |  |  |  | 100 |  |
|  |  |  | HD T4 |  |  |  | 90 |  |
|  |  |  | HD T5 |  |  |  | 80 |  |
|  |  |  | HD T6 |  |  | HDB Internal | 70 |  |
| 1080p | Movies Anywhere |  |  |  |  |  | 60 |  |
|  | Amazon Prime |  |  |  |  |  | 50 |  |
|  | Apple TV+ |  |  |  |  |  |  |  |
|  | Disney+ | DVD Remux |  |  |  |  | 40 |  |
|  | Netflix |  |  |  |  |  |  |  |
|  | HBOMax |  |  |  |  |  |  |  |
|  | Hulu |  | SD T1 |  |  | SD GP | 30 |  |
|  | Peacock |  | HD T7 |  |  |  |  |  |
|  | Paramount+ |  |  |  |  |  |  |  |
|  | Roku |  |  |  |  |  |  |  |
|  | iTunes |  | SD T2 |  | SE |  | 20 |  |
|  | Blu-Ray | x264 |  | Atmos | IMAX |  | 10 |  |
|  | WEBRIP |  |  |  | Criterion |  |  |  |
| 480p | DVD | Xvid |  | FLAC |  |  | 0 |  |
|  |  |  |  | DD+ |  |  |  |  |
|  |  |  |  | DTS |  |  |  |  |
|  |  |  |  | DD |  |  |  |  |
| 720p |  | x265 |  | TrueHD | Features |  | -9999 |  |
| 2160p |  | BD Remux |  | DTS-HD MA |  |  |  |  |
|  |  | Disc |  | DTS-X |  |  |  |  |

A breakdown of each of the internal tiers can be found here: [Release Group Tiers](../Wiki/Release%20Group%20Tiers.md)

This profile does rely on the \*arr upgrade system, so expect files to be downloaded multiple times (examples of this are outlined in the nuances section below). If you don't want to deal with multiple upgrades, the "Upgrade Until" score can be lowered to your preference!
## Quality Profiles

- The custom format system does the heavy lifting in prioritising releases, but specific quality profiles are useful in catching some strays that make it past. Specifically, some pesky SD encodes. 99% releases are covered by Custom formats anyway, so it's not a big deal.

|Quality Profiles   |   |
|---|---|
|Transparent Capable|Bluray-1080p|
||WEBRip-1080p|
||WEBDL-1080p|
||Bluray-720p|
|Fallbacks|WEBDL-480p|
||DVD|

## The Nuances of Transparency

### 1. Application Scope

**Existing Movies**: Typically, there's a single grab. However, upgrades might occur if a more reputable group releases a 'Golden Popcorn' version later. For instance, in the case of an already available reputable Blu-ray release, this profile may bypass web releases and opt for the reputable Blu-ray rip directly.

**Unreleased Movies**: Here, the journey is more layered. With VODs being the first to hit the market, a movie might undergo several upgrades. Initially, versions with constraints, such as Korean iTunes leaks with hardcoded subtitles, might be grabbed. This is progressively upgraded as more polished VODs become available, culminating in grabbing the most transparent available VOD, which is usually "Movies Anywhere". When the Blu-ray is out, patience is key. Instead of snapping up the immediate releases (which might not be the best), the profile waits for a reputable group's encode. The cycle of upgrades continues until it hits the upgrade threshold of 320 points. This threshold can be fine tuned by the user to account for upgrade immutability.

### 2. Handling Varying Resolutions

In scenarios where a VOD or Blu-ray is unavailable in the desired resolution, the profile uses SD as a fallback. There's a clear hierarchy: DVD remuxes take precedence, followed by SD 'Golden Popcorns', and then other internal SD encodes and VODs.

In the scenario that there exists no 1080p Golden Popcorn, 720p Golden Popcorns are prioritised over 1080p web VODS, SD encodes and DVD remuxes. On first glance, this doesn't seem _transparent_ but please note that some 720p golden popcorns are more than sufficient in providing a transparent picture quality (and they save significantly more space). Once again, we place the trust in the release group the decide what is the best quality / size ratio.

### 3. The Role of Indexer Flags

Beyond relying on data, the profile also utilizes indexer flags, especially with platforms like PassThePopcorn and HDBits. These flags are instrumental in handling exceptions where a 'Golden Popcorn' exists but hasn't been accounted for or when a more reputable group has actually encoded the 'Golden Popcorn'. This mechanism ensures that genuinely transparent releases are not missed.

### 4. Quality Profiles and Their Significance

Quality isn't merely about the source. There can be instances where a 4K VOD is 'webripped' to 1080p, offering a superior source compared to a standard 1080p Blu-ray encode.

!!! info
    A 1080p 'WEBRIP' in this scenario isn't actually a WEBRIP in the traditional sense (screen captured at a high resolution and then reencoded down to 1080p or less). It's a lossless 4k WEB-DL that has been encoded in x264 down to 1080p (or something like that, I'm not an encoding guru :/). The 4k WEB-DL in these scenarios are a better source than the 1080p Blu-ray. 
    
    This is especially useful for VOD only content, where old 1080p content is quite lacking, and the 4k source was much better for encoding. 



 To ensure the best grab, various profiles like WEBRIP, BLURAY, and WEBDL are nested under a 'transparent capable' grouping, ensuring no specific source is prioritized over another.
