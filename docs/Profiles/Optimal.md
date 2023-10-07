---
title: 1. Optimal
date: 2023-10-06
---

## Overview

The optimal profile aims to select the best possible release of a movie, irregardless of file size or compatability. audio and video metrics are used to determine which is the best release.

### Installation

Review the guide on [Importing Profiles & Custom Formats](../Wiki/Importing%20Profiles%20&%20Custom%20Formats.md) to import the necessary custom formats and profiles inside your Radarr installation.

When prompted to select a profile, choose optimal.

## Score Breakdown

| Resolution                                      | Source                                                            | Codec                                                | Internal | audio                                             | Extras                                         | Flags                                         | Score | Upgrade |
| ----------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------- | -------- | ------------------------------------------------- | ---------------------------------------------- | --------------------------------------------- | ----- | ------- |
| [2160p](../Custom Formats/Resolutions.md#2160p) | [Blu-Ray](../Custom Formats/Sources.md#blu-ray)                   | [BD Remux](../Custom Formats/Codecs.md#bd%20remux)   |          | [DTS-X](../Custom Formats/Audio.md#dts-x)         |                                                |                                               | 60    | 320     |
|                                                 | [Movies Anywhere](../Custom Formats/Sources.md#movies%20anywhere) |                                                      |          | [TrueHD](../Custom Formats/Audio.md#truehd)       |                                                |                                               | 50    |         |
|                                                 | [Amazon Prime](../Custom Formats/Sources.md#amazon%20prime)       |                                                      |          | [DTS-HD MA](../Custom Formats/Audio.md#dts-hd-ma) |                                                |                                               |       |         |
|                                                 | [Apple TV+](../Custom Formats/Sources.md#apple%20tv+)             |                                                      |          |                                                   |                                                |                                               |       |         |
|                                                 | [Disney+](../Custom Formats/Sources.md#disney+)                   |                                                      |          | [FLAC](../Custom Formats/Audio.md#flac)           |                                                | [DV](../Custom Formats/HDR.md#dv)             | 30    |         |
|                                                 | [Netflix](../Custom Formats/Sources.md#netflix)                   |                                                      |          |                                                   |                                                |                                               |       |         |
|                                                 | [HBOMax](../Custom Formats/Sources.md#hbomax)                     |                                                      |          |                                                   |                                                |                                               |       |         |
|                                                 | [Hulu](../Custom Formats/Sources.md#hulu)                         |                                                      |          |                                                   |                                                | [HDR10+](../Custom Formats/HDR.md#hdr10+)     | 20    |         |
|                                                 | [Peacock](../Custom Formats/Sources.md#peacock)                   |                                                      |          |                                                   |                                                |                                               |       |         |
|                                                 | [Paramount+](../Custom Formats/Sources.md#paramount+)             |                                                      |          |                                                   |                                                |                                               |       |         |
|                                                 | [Roku](../Custom Formats/Sources.md#roku)                         |                                                      |          |                                                   |                                                |                                               |       |         |
|                                                 | [iTunes](../Custom Formats/Sources.md#itunes)                     |                                                      |          | [Atmos](../Custom Formats/Audio.md#atmos)         |                                                | [HDR10](../Custom Formats/HDR.md#hdr10)       | 10    |         |
|                                                 |                                                                   | [Xvid](../Custom Formats/Codecs.md#xvid)             |          | [DD+](../Custom Formats/Audio.md#dd+)             |                                                |                                               |       |         |
|                                                 | [WEBRIP](../Custom Formats/Sources.md#webrip)                     | [x264](../Custom Formats/Codecs.md#x264)             |          | [DTS](../Custom Formats/Audio.md#dts)             | [Special](../Custom Formats/Extras.md#special) |                                               |       |         |
| [SD](../Custom Formats/Resolutions.md#sd)       | [DVD](../Custom Formats/Sources.md#dvd)                           | [x265](../Custom Formats/Codecs.md#x265)             |          |                                                   |                                                |                                               | -9999 |         |
| [720p](../Custom Formats/Resolutions.md#720p)   |                                                                   | [DVD Remux](../Custom Formats/Codecs.md#dvd%20remux) |          | [DD](../Custom Formats/Audio.md#dd)               |                                                |                                               |       |         |
| [1080p](../Custom Formats/Resolutions.md#1080p) |                                                                   |                                                      |          |                                                   |                                                |                                               |       |         |
|                                                 |                                                                   |                                                      |          |                                                   |                                                | [DV Only](../Custom Formats/HDR.md#dv%20only) |       |         |

## The Essence of Optimal

#### 1. **Indexer Priority**:

- Recognizing the limitations of parsing release notes, "Optimal" leverages indexer priority. Releases from HDB and BHD are always prioritized, given their consistent track record of hosting superior releases, notably from FRaMeSToR and 3L.

#### 2. **audio/Video Supremacy**:

- The heart of "Optimal" lies in its unwavering commitment to audio and video quality. This ensures that even if a release group isn't specified, the profile can still discern and select the best available remux based on its intrinsic quality.

#### 3. **Special Consideration for WiLDCAT**:

- Releases from WiLDCAT are almost always prioritized due to their enhanced HDR and audio tracks, setting them apart in the remux landscape.

#### 4. **Fallback Mechanism**:

- "Optimal" is not just about waiting for the perfect release. It provides a fallback to 2160p WEB VODs, ensuring that new movies are promptly grabbed. However, once the UHD Blu-ray is out, the profile will seamlessly upgrade to that superior version.
