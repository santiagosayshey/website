---
title: 1. Optimal
date: 2023-10-06
---

## Overview

The optimal profile aims to select the best possible release of a movie, irregardless of file size or compatability. Audio and video metrics are used to determine which is the best release.

### Installation

Review the guide on [Importing Profiles & Custom Formats](../Wiki/Importing%20Profiles%20&%20Custom%20Formats.md) to import the necessary custom formats and profiles inside your Radarr installation.

When prompted to select a profile, choose optimal.

## Score Breakdown

| Resolution                                        | Source                                                              | Codec                                                  | Internal | Audio                                                 | Extras                                           | Flags                                           | Score | Upgrade |
| ------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------ | -------- | ----------------------------------------------------- | ------------------------------------------------ | ----------------------------------------------- | ----- | ------- |
| [2160p](../Custom%20Formats/Resolutions.md#2160p) | [Blu-Ray](../Custom%20Formats/Sources.md#Blu-Ray)                   | [BD Remux](../Custom%20Formats/Codecs.md#BD%20Remux)   |          | [DTS-X](../Custom%20Formats/Audio.md#DTS-X)           |                                                  |                                                 | 60    | 320     |
|                                                   | [Movies Anywhere](../Custom%20Formats/Sources.md#Movies%20Anywhere) |                                                        |          | [TrueHD](../Custom%20Formats/Audio.md#TrueHD)         |                                                  |                                                 | 50    |         |
|                                                   | [Amazon Prime](../Custom%20Formats/Sources.md#Amazon%20Prime)       |                                                        |          | [DTS-HD MA](../Custom%20Formats/Audio.md#DTS-HD%20MA) |                                                  |                                                 |       |         |
|                                                   | [Apple TV+](../Custom%20Formats/Sources.md#Apple%20TV+)             |                                                        |          |                                                       |                                                  |                                                 |       |         |
|                                                   | [Disney+](../Custom%20Formats/Sources.md#Disney+)                   |                                                        |          | [FLAC](../Custom%20Formats/Audio.md#FLAC)             |                                                  | [DV](../Custom%20Formats/HDR.md#DV)             | 30    |         |
|                                                   | [Netflix](../Custom%20Formats/Sources.md#Netflix)                   |                                                        |          |                                                       |                                                  |                                                 |       |         |
|                                                   | [HBOMax](../Custom%20Formats/Sources.md#HBOMax)                     |                                                        |          |                                                       |                                                  |                                                 |       |         |
|                                                   | [Hulu](../Custom%20Formats/Sources.md#Hulu)                         |                                                        |          |                                                       |                                                  | [HDR10+](../Custom%20Formats/HDR.md#HDR10+)     | 20    |         |
|                                                   | [Peacock](../Custom%20Formats/Sources.md#Peacock)                   |                                                        |          |                                                       |                                                  |                                                 |       |         |
|                                                   | [Paramount+](../Custom%20Formats/Sources.md#Paramount+)             |                                                        |          |                                                       |                                                  |                                                 |       |         |
|                                                   | [Roku](../Custom%20Formats/Sources.md#Roku)                         |                                                        |          |                                                       |                                                  |                                                 |       |         |
|                                                   | [iTunes](../Custom%20Formats/Sources.md#iTunes)                     |                                                        |          | [Atmos](../Custom%20Formats/Audio.md#Atmos)           |                                                  | [HDR10](../Custom%20Formats/HDR.md#HDR10)       | 10    |         |
|                                                   |                                                                     | [Xvid](../Custom%20Formats/Codecs.md#Xvid)             |          | [DD+](../Custom%20Formats/Audio.md#DD+)               |                                                  |                                                 |       |         |
|                                                   | [WEBRIP](../Custom%20Formats/Sources.md#WEBRIP)                     | [x264](../Custom%20Formats/Codecs.md#x264)             |          | [DTS](../Custom%20Formats/Audio.md#DTS)               | [Special](../Custom%20Formats/Extras.md#Special) |                                                 |       |         |
| [SD](../Custom%20Formats/Resolutions.md#SD)       | [DVD](../Custom%20Formats/Sources.md#DVD)                           | [x265](../Custom%20Formats/Codecs.md#x265)             |          |                                                       |                                                  |                                                 | -9999 |         |
| [720p](../Custom%20Formats/Resolutions.md#720p)   |                                                                     | [DVD Remux](../Custom%20Formats/Codecs.md#DVD%20Remux) |          | [DD](../Custom%20Formats/Audio.md#DD)                 |                                                  |                                                 |       |         |
| [1080p](../Custom%20Formats/Resolutions.md#1080p) |                                                                     |                                                        |          |                                                       |                                                  |                                                 |       |         |
|                                                   |                                                                     |                                                        |          |                                                       |                                                  | [DV Only](../Custom%20Formats/HDR.md#DV%20Only) |       |         |

## The Essence of Optimal

#### 1. **Indexer Priority**:

- Recognizing the limitations of parsing release notes, "Optimal" leverages indexer priority. Releases from HDB and BHD are always prioritized, given their consistent track record of hosting superior releases, notably from FRaMeSToR and 3L.

#### 2. **Audio/Video Supremacy**:

- The heart of "Optimal" lies in its unwavering commitment to audio and video quality. This ensures that even if a release group isn't specified, the profile can still discern and select the best available remux based on its intrinsic quality.

#### 3. **Special Consideration for WiLDCAT**:

- Releases from WiLDCAT are almost always prioritized due to their enhanced HDR and Audio tracks, setting them apart in the remux landscape.

#### 4. **Fallback Mechanism**:

- "Optimal" is not just about waiting for the perfect release. It provides a fallback to 2160p WEB VODs, ensuring that new movies are promptly grabbed. However, once the UHD Blu-ray is out, the profile will seamlessly upgrade to that superior version.
