---
title: 4k Remux
date: 2023-10-06
---

## Overview

The optimal profile aims to select the best possible release of a movie, regardless of file size or compatibility. Audio and video metrics are used to determine which is the best release, rather than release group. 

Update: This profile will experience a major shift to be release group focused soon. It will be a lot more consistent.

### Installation

Review the guide on [Importing Profiles & Custom Formats](../Wiki/Importing%20Profiles%20&%20Custom%20Formats.md) to import the necessary custom formats and profiles inside your Radarr installation.

When prompted to select a profile, choose optimal.

## Score Breakdown
| Resolution | Source | Codec | Tracker | Audio | HDR | Extras | Score | Upgrade |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 2160p | Blu-Ray | BD Remux |  | DTS-X |  |  | 60 | 320 |
|  | Movies Anywhere |  |  | TrueHD |  |  | 50 |  |
|  |  |  |  | DTS-HD MA |  |  |  |  |
|  | Amazon Prime |  |  |  |  |  | 40 |  |
|  | Apple TV+ |  |  |  |  |  |  |  |
|  | Disney+ |  |  | FLAC | DV |  | 30 |  |
|  | Netflix |  |  |  |  |  |  |  |
|  | HBOMax |  |  |  |  |  |  |  |
|  | Hulu |  |  |  | HDR10+ |  | 20 |  |
|  | Peacock |  |  |  |  |  |  |  |
|  | Paramount+ |  |  |  |  |  |  |  |
|  | Roku |  |  |  |  |  |  |  |
|  | iTunes |  |  | Atmos | HDR10 |  | 10 |  |
|  |  |  |  | DD+ |  | Special Edition | 0 |  |
|  |  |  |  | DTS |  |  |  |  |
|  |  |  |  | DD |  |  |  |  |
| 480p | WEBRIP | Xvid | UHDBits |  | DV w/out Fallback |  | -9999 |  |
| 720p | DVD | x264 |  |  |  |  |  |  |
| 1080p |  | x265 |  |  |  |  |  |  |
|  |  | DVD Remux |  |  |  |  |  |  |

## The Essence of Optimal

#### 1. **Indexer Priority**:

- Recognizing the limitations of parsing release notes, "Optimal" leverages indexer priority. Releases from HDB and BHD are always prioritized, given their consistent track record of hosting superior releases, notably from FRaMeSToR and 3L.

#### 2. **audio/Video Supremacy**:

- The heart of "Optimal" lies in its unwavering commitment to audio and video quality. This ensures that even if a release group isn't specified, the profile can still discern and select the best available remux based on its intrinsic quality.

#### 3. **Special Consideration for WiLDCAT**:

- Releases from WiLDCAT are almost always prioritized due to their enhanced HDR and audio tracks, setting them apart in the remux landscape.

#### 4. **Fallback Mechanism**:

- "Optimal" is not just about waiting for the perfect release. It provides a fallback to 2160p WEB VODs, ensuring that new movies are promptly grabbed. However, once the UHD Blu-ray is out, the profile will seamlessly upgrade to that superior version.
