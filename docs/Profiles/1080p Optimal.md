## Overview

The optimal profile aims to select the best possible release of a movie, regardless of file size or compatibility. Audio and video metrics are used to determine which is the best release, rather than release group. It is available in 3 formats - Full, Single Grab and Double Grab. These formats affect only the immutability of the profile.

Since this profile is considered standard compatibility, it prioritises 1080p remuxes in h264, with lossless audio and no HDR. It has fallback to DVDs, in case no 1080p Blu-ray exists. 

Try to use as little indexers as possible with this profile, as remuxes tend to be the most varying in terms of release names, for example - HDBits / UHDBits remuxes sometimes don't have audio in the release title. 

### Installation

Review the guide on [Importing Profiles & Custom Formats](../Wiki/Importing%20Profiles%20&%20Custom%20Formats.md) to import the necessary custom formats and profiles inside your Radarr installation.

When prompted to select a profile, choose 1080p optimal in your preferred immutability. 

| Resolution | Source | Codec | Internal | Tracker | Audio | HDR | Extras | Flags | Score | Upgrade |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1080p | Blu-Ray | BD Remux |  |  | DTS-X |  |  |  | 60 | 320 |
|  | Movies Anywhere |  |  |  | TrueHD |  |  |  | 50 |  |
|  |  |  |  |  | DTS-HD MA |  |  |  |  |  |
|  | Amazon Prime | DVD Remux |  |  |  |  |  |  | 40 |  |
|  | Apple TV+ |  |  |  |  |  |  |  |  |  |
|  | Disney+ |  | SD T1 |  | FLAC |  |  | SD GP | 30 |  |
|  | Netflix |  |  |  | PCM |  |  |  |  |  |
|  | HBOMax |  |  |  |  |  |  |  |  |  |
|  | Hulu |  | SD T2 |  |  |  |  |  | 20 |  |
|  | Peacock |  |  |  |  |  |  |  |  |  |
|  | Paramount+ |  |  |  |  |  |  |  |  |  |
|  | Roku |  |  |  |  |  |  |  |  |  |
|  | iTunes | x264 |  |  | Atmos |  | IMAX |  | 10 |  |
|  |  |  |  |  |  |  |  |  |  |  |
| 480p |  | Xvid |  |  | DD+ |  | Special Edition |  | 0 |  |
|  |  |  |  |  | DTS |  |  |  |  |  |
|  |  |  |  |  | DD |  |  |  |  |  |
|  | WEBRIP |  |  | UHDBits |  | HDR10 |  |  | -9999 |  |
| 720p | DVD |  |  |  |  | HDR10+ |  |  |  |  |
| 2160p |  | x265 |  |  |  | Dolby Vision |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |

A breakdown of each of the internal tiers can be found here: [Release Group Tiers](../Wiki/Release%20Group%20Tiers.md)
## Quality Profiles

| Quality Profiles |
| ---- |
| 1080p-Remux |
| 1080p WEB-DL |
| DVD |
