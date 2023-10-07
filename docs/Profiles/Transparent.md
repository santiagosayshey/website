---
title: 2. Transparent
date: 2023-10-06
---

## Overview

The transparent profile aims to provide a balance between quality, size and compatability.

Rather than relying on audio / video metrics to determine transparency, this profile utilises a unique metric, the [Golden Popcorn Performance Index](../Wiki/Golden%20Popcorn%20Performance%20Index.md), to identify release groups known for their consistent output of quality encodes.

### Examples
Coming soon
### Installation

Review the guide on [Importing Profiles & Custom Formats](../Wiki/Importing%20Profiles%20&%20Custom%20Formats.md) to import the necessary custom formats and profiles inside your Radarr installation.

When prompted to select a profile, choose transparent.

## Score Breakdown

A breakdown of each of the internal tiers can be found here: [Release Group Tiers](../Wiki/Release%20Group%20Tiers.md)

### 1080p Only

This version of transparent prioritises 1080p encodes and allows SD remuxes and encodes as fallback. 720p, 2160p and x265 encodes are not allowed. Choose this version if you are not on PTP.

| Resolution                                      | Source                                                          | Codec                                              | Internal | Audio                                     | Extras                                             | Flags                                                   | Score | Upgrade |
| ----------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------- | -------- | ----------------------------------------- | -------------------------------------------------- | ------------------------------------------------------- | ----- | ------- |
|                                                 |                                                                 |                                                    | HD T1    |                                           |                                                    | [1080p GP](../Custom Formats/Flags.md#1080p GP)         | 120   | 320     |
|                                                 |                                                                 |                                                    | HD T2    |                                           |                                                    |                                                         | 110   |         |
|                                                 |                                                                 |                                                    | HD T3    |                                           |                                                    |                                                         | 100   |         |
|                                                 |                                                                 |                                                    | HD T4    |                                           |                                                    |                                                         | 90    |         |
|                                                 |                                                                 |                                                    | HD T5    |                                           |                                                    |                                                         | 80    |         |
|                                                 |                                                                 |                                                    | HD T6    |                                           |                                                    | [HDB Internal](../Custom Formats/Flags.md#HDB Internal) | 70    |         |
| [1080p](../Custom Formats/Resolutions.md#1080p) | [Movies Anywhere](../Custom Formats/Sources.md#Movies Anywhere) |                                                    |          |                                           |                                                    |                                                         | 60    |         |
|                                                 | [Amazon Prime](../Custom Formats/Sources.md#Amazon Prime)       |                                                    |          |                                           |                                                    |                                                         | 50    |         |
|                                                 | [Apple TV+](../Custom Formats/Sources.md#Apple TV+)             |                                                    |          |                                           |                                                    |                                                         |       |         |
|                                                 | [Disney+](../Custom Formats/Sources.md#Disney+)                 | [DVD Remux](../Custom Formats/Codecs.md#DVD Remux) |          |                                           |                                                    |                                                         | 40    |         |
|                                                 | [Netflix](../Custom Formats/Sources.md#Netflix)                 |                                                    |          |                                           |                                                    |                                                         |       |         |
|                                                 | [HBOMax](../Custom Formats/Sources.md#HBOMax)                   |                                                    |          |                                           |                                                    |                                                         |       |         |
|                                                 | [Hulu](../Custom Formats/Sources.md#Hulu)                       |                                                    | SD T1    |                                           |                                                    | [SD GP](../Custom Formats/Flags.md#SD GP)               | 30    |         |
|                                                 | [Peacock](../Custom Formats/Sources.md#Peacock TV)              |                                                    | HD T7    |                                           |                                                    |                                                         |       |         |
|                                                 | [Paramount+](../Custom Formats/Sources.md#Paramount+)           |                                                    |          |                                           |                                                    |                                                         |       |         |
|                                                 | [Roku](../Custom Formats/Sources.md#Roku)                       |                                                    |          |                                           |                                                    |                                                         |       |         |
|                                                 | [iTunes](../Custom Formats/Sources.md#iTunes)                   |                                                    | SD T2    | [SE](../Custom Formats/Audio.md#SE)       |                                                    |                                                         | 20    |         |
|                                                 | [Blu-Ray](../Custom Formats/Sources.md#Blu-Ray)                 | [x264](../Custom Formats/Codecs.md#x264)           |          | [Atmos](../Custom Formats/Audio.md#Atmos) | [IMAX](../Custom Formats/Extras.md#IMAX)           |                                                         | 10    |         |
|                                                 | [WEBRIP](../Custom Formats/Sources.md#WEBRIP)                   |                                                    |          |                                           | [Criterion](../Custom Formats/Extras.md#Criterion) |                                                         |       |         |
| [480p](../Custom Formats/Resolutions.md#480p)   | [DVD](../Custom Formats/Sources.md#DVD)                         | [Xvid](../Custom Formats/Codecs.md#Xvid)           |          | [FLAC](../Custom Formats/Audio.md#FLAC)   |                                                    |                                                         | 0     |         |
| [720p](../Custom Formats/Resolutions.md#720p)   |                                                                 |                                                    |          | [DD+](../Custom Formats/Audio.md#DD+)     |                                                    |                                                         | -9999 |         |
| [2160p](../Custom Formats/Resolutions.md#2160p) |                                                                 |                                                    |          | [DTS](../Custom Formats/Audio.md#DTS)     |                                                    |                                                         |       |         |
|                                                 |                                                                 |                                                    |          | [DD](../Custom Formats/Audio.md#DD)       |                                                    |                                                         |       |         |

### 720p Fallback

In addition to the previous fallbacks, this version allows grabbing 720p golden popcorns when no reputable 1080p encode of WEB VOD is available. In the case that a 1080p encode from a reputable group is available, it is still prioritised over the 720p golden popcorn.

| Resolution                                      | Source                                                          | Codec                                              | Internal | Audio                                             | Extras                                             | Flags                                                   | Score | Upgrade |
| ----------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------- | -------- | ------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------- | ----- | ------- |
|                                                 |                                                                 |                                                    | HD T1    |                                                   |                                                    | [HD GP](../Custom Formats/Flags.md#HD GP)               | 120   | 320     |
|                                                 |                                                                 |                                                    | HD T2    |                                                   |                                                    |                                                         | 110   |         |
|                                                 |                                                                 |                                                    | HD T3    |                                                   |                                                    |                                                         | 100   |         |
|                                                 |                                                                 |                                                    | HD T4    |                                                   |                                                    |                                                         | 90    |         |
|                                                 |                                                                 |                                                    | HD T5    |                                                   |                                                    |                                                         | 80    |         |
|                                                 |                                                                 |                                                    | HD T6    |                                                   |                                                    | [HDB Internal](../Custom Formats/Flags.md#HDB Internal) | 70    |         |
| [1080p](../Custom Formats/Resolutions.md#1080p) | [Movies Anywhere](../Custom Formats/Sources.md#Movies Anywhere) |                                                    |          |                                                   |                                                    |                                                         | 60    |         |
|                                                 | [Amazon Prime](../Custom Formats/Sources.md#Amazon Prime)       |                                                    |          |                                                   |                                                    |                                                         | 50    |         |
|                                                 | [Apple TV+](../Custom Formats/Sources.md#Apple TV+)             |                                                    |          |                                                   |                                                    |                                                         |       |         |
|                                                 | [Disney+](../Custom Formats/Sources.md#Disney+)                 | [DVD Remux](../Custom Formats/Codecs.md#DVD Remux) |          |                                                   |                                                    |                                                         | 40    |         |
|                                                 | [Netflix](../Custom Formats/Sources.md#Netflix)                 |                                                    |          |                                                   |                                                    |                                                         |       |         |
|                                                 | [HBOMax](../Custom Formats/Sources.md#HBOMax)                   |                                                    |          |                                                   |                                                    |                                                         |       |         |
|                                                 | [Hulu](../Custom Formats/Sources.md#Hulu)                       |                                                    | SD T1    |                                                   |                                                    | [SD GP](../Custom Formats/Flags.md#SD GP)               | 30    |         |
|                                                 | [Peacock](../Custom Formats/Sources.md#Peacock)                 |                                                    | HD T7    |                                                   |                                                    |                                                         |       |         |
|                                                 | [Paramount+](../Custom Formats/Sources.md#Paramount+)           |                                                    |          |                                                   |                                                    |                                                         |       |         |
|                                                 | [Roku](../Custom Formats/Sources.md#Roku)                       |                                                    |          |                                                   |                                                    |                                                         |       |         |
|                                                 | [iTunes](../Custom Formats/Sources.md#iTunes)                   |                                                    | SD T2    | [SE](../Custom Formats/Audio.md#SE)               |                                                    |                                                         | 20    |         |
|                                                 | [Blu-Ray](../Custom Formats/Sources.md#Blu-Ray)                 | [x264](../Custom Formats/Codecs.md#x264)           |          | [Atmos](../Custom Formats/Audio.md#Atmos)         | [IMAX](../Custom Formats/Extras.md#IMAX)           |                                                         | 10    |         |
|                                                 | [WEBRIP](../Custom Formats/Sources.md#WEBRIP)                   |                                                    |          |                                                   | [Criterion](../Custom Formats/Extras.md#Criterion) |                                                         |       |         |
| [480p](../Custom Formats/Resolutions.md#480p)   | [DVD](../Custom Formats/Sources.md#DVD)                         | [Xvid](../Custom Formats/Codecs.md#Xvid)           |          | [FLAC](../Custom Formats/Audio.md#FLAC)           |                                                    |                                                         | 0     |         |
|                                                 |                                                                 |                                                    |          | [DD+](../Custom Formats/Audio.md#DD+)             |                                                    |                                                         |       |         |
|                                                 |                                                                 |                                                    |          | [DTS](../Custom Formats/Audio.md#DTS)             |                                                    |                                                         |       |         |
|                                                 |                                                                 |                                                    |          | [DD](../Custom Formats/Audio.md#DD)               |                                                    |                                                         |       |         |
| [720p](../Custom Formats/Resolutions.md#720p)   |                                                                 |                                                    |          |                                                   |                                                    |                                                         | -120  |         |
| [2160p](../Custom Formats/Resolutions.md#2160p) |                                                                 | [x265](../Custom Formats/Codecs.md#x265)           |          | [TrueHD](../Custom Formats/Audio.md#TrueHD)       | [Features](../Custom Formats/Extras.md#Features)   |                                                         | -9999 |         |
|                                                 |                                                                 | [BD Remux](../Custom Formats/Codecs.md#BD Remux)   |          | [DTS-HD MA](../Custom Formats/Audio.md#DTS-HD MA) |                                                    |                                                         |       |         |
|                                                 |                                                                 | [Disc](../Custom Formats/Codecs.md#Disc)           |          | [DTS-X](../Custom Formats/Audio.md#DTS-X)         |

### Remux Fallback

Coming Soon!

### Quality Profiles

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

Quality isn't merely about the source. There can be instances where a 4K VOD is 'webripped' to 1080p, offering a superior source compared to a standard 1080p Blu-ray encode. To ensure the best grab, various profiles like WEBRIP, BLURAY, and WEBDL are nested under a 'transparent capable' grouping, ensuring no specific source is prioritized over another.
